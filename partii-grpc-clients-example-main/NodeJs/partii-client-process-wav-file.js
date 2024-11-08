const WaveFile = require('wavefile').WaveFile;
const fs = require('fs');
var grpc = require('@grpc/grpc-js');
var protoLoader = require('@grpc/proto-loader');

var wave_path =  __dirname + '/test.wav';
var PROTO_PATH = __dirname + '/../protobuf/v2.1/PartiiService.proto';

const debug = 1;

var packageDefinition = protoLoader.loadSync(
  PROTO_PATH,
  {keepCase: true,
   longs: String,
   enums: String,
   defaults: true,
   oneofs: true
  });

var partii_proto = grpc.loadPackageDefinition(packageDefinition).partii;
var client_partii = null;
var call_partii = null;

let setting = JSON.parse(
  '{'+
  '"server_ip": "partii.aiforthai.in.th",'+
  '"server_port": "27016",'+
  '"sampling-rate": "16000",'+
  '"vad-threshold": "0.5",'+
  '"num-channels": "1",'+
  '"decode-channels": "0",'+
  '"apikey": "xxxxxx",'+
  '"client-id": "partii-client-nodejs",'+
  '"modelkey": "default",'+
  '"audio-codec": "LINEAR16",'+
  '"protocol": "partii",'+
  '"enable-textnorm": "true",'+
  '"enable-partial": "true",'+
  '"enable-vad": "true",'+
  '"enable-endpoint": "true",'+
  '"number-target": "english"'+
  '}'
);

function connect_grpc(metadata){
    try {
      if(debug == 1){
        console.log("connect to grpc "+setting['server_ip']+":"+setting['server_port'])
      }
      
        client_partii = new partii_proto.Transcription(setting['server_ip']+":"+setting['server_port'],grpc.credentials.createInsecure());
        call_partii = client_partii.LiveTranscribe(metadata);
        
        call_partii.on('data', function(TranscriptionResult) {
                
                if( TranscriptionResult.sentenceType == "PARTIAL" || TranscriptionResult.sentenceType == "RESULT"){

                  if(debug == 1){  
                    console.log("\t sentenceNumber:" + TranscriptionResult.sentenceNumber);
                    console.log("\t Status:" + TranscriptionResult.Status);
                    console.log("\t sentenceType:" + TranscriptionResult.sentenceType);
                    console.log("\t transcript:" + TranscriptionResult.transcript);
                    console.log("\t confidence:" + TranscriptionResult.confidence);
                    console.log("\t startTime:" + TranscriptionResult.startTime+", "+convMilliFormat(TranscriptionResult.startTime));
                    console.log("\t endTime:" + TranscriptionResult.endTime+", "+convMilliFormat(TranscriptionResult.endTime));
                  }
                } 
                
                if(TranscriptionResult.sentenceType == "RESULT"){
                  
		                var words = TranscriptionResult.words;
                    for (var i = 0; i < words.length; i++) {

                        if(debug == 1){  
                          console.log("\t\t wordNumber:" + words[i].wordNumber);
                          console.log("\t\t word:" + words[i].word);
                          console.log("\t\t confidence:" + words[i].confidence);
                          console.log("\t\t startTime:" + words[i].startTime+", "+convMilliFormat(words[i].startTime));
                          console.log("\t\t endTime:" + words[i].endTime+", "+convMilliFormat(words[i].endTime));
                        }
						
                        var phones = words[i].phones;
                        for (var j = 0; j < phones.length; j++) {

                          if(debug == 1){  
                            console.log("\t\t\t phoneNumber:" + phones[j].phoneNumber);
                            console.log("\t\t\t phone:" + phones[j].phone);
                            console.log("\t\t\t confidence:" + phones[j].confidence);
                            console.log("\t\t\t startTime:" + phones[j].startTime+", "+convMilliFormat(phones[j].startTime));
                            console.log("\t\t\t endTime:" + phones[j].endTime+", "+convMilliFormat(phones[j].endTime));
                          }
  						  
                        }


                    }
                }else if(TranscriptionResult.sentenceType == "FINISHED"){
                  if(debug == 1){  
                    console.log("\t Status:" + TranscriptionResult.Status);
                    console.log("\t sentenceType:" + TranscriptionResult.sentenceType);
                    console.log("\t transcript:" + TranscriptionResult.transcript);
                  }

                }
            
        });
        
        call_partii.on('end', function() {
          if(debug == 1){  
            console.log('end grpc');
          }
        
        });

        call_partii.on('error', function(e) {
          // An error has occurred and the stream has been closed.
          if(debug == 1){
            console.log('error grpc:'+e);
          }

          return false
        });

    } catch (ex) {
      if(debug == 1){
        console.log("grpc error:"+ex);
      }
        return false
    }
    return true
}

Number.prototype.pad = function(size) {
    var s = String(this);
    while (s.length < (size || 2)) {s = "0" + s;}
    return s;
}

function convMilliFormat(millis) {
    var alltime = (parseFloat(millis) * 1000);
    
    var mil = Number(alltime % 1000);
    var sec = Number((alltime / 1000) % 60);
    var min = Number((alltime / (1000 * 60)) % 60);
    var hour = Number((alltime / (1000 * 60 * 60)) % 24);
    
    return (parseInt(hour)).pad(2)+":"+(parseInt(min)).pad(2)+":"+(parseInt(sec)).pad(2)+","+(parseInt(mil)).pad(3);
}

function chunkArray(myArray, chunk_size){
    var index = 0;
    var arrayLength = myArray.length;
    var tempArray = [];
    
    for (index = 0; index < arrayLength; index += chunk_size) {
        var myChunk = myArray.slice(index, index+chunk_size);
        // Do something if you want with the group
        tempArray.push({
            ByteChunk: myChunk,
            Bytelen: myChunk.length,
            Datatype: 0
        });
    }
    if(debug == 1){
      console.log("chunkArray length:"+tempArray.length)
    }
    return tempArray;
}

function readWave(wavpath) {
  if(debug == 1){
    console.log("readWave from : "+wavpath);
  }
   
      let wav = new WaveFile(fs.readFileSync(wavpath));
      let wavBuffer = wav.toBuffer();
      if(debug == 1){
        console.log("wavBuffer length:"+wavBuffer.length)
      }
      var chunk_size = 1024;
      var chunks = chunkArray(wavBuffer, chunk_size);
      return chunks;

}

function processstream( chunk, msg_type) { 
  if(msg_type == "EOS"){
    if(debug == 1){
      console.log('EOS');
    }
    try{
      call_partii.end();
    }catch(err){
      if(debug == 1){
        console.log('EOS error');
      }
    }
    
  }else{
    try{
      call_partii.write(chunk);
    }catch(err){
      if(debug == 1){
        console.log('EOS error');
      }
    }
  }
}

// main process.....
var Options = process.argv.slice(2);

for (var i =0; i < Options.length; i++){
	switch (Options[i]) {
	case '-i':
		wave_path = Options[i+1];
		i++;
	  continue;
  case '-apikey':
    setting['apikey'] = Options[i+1];
    i++;
    continue;
  case '-server_ip':
    setting['server_ip'] = Options[i+1];
    i++;
    continue;
  case '-server_port':
    setting['server_port'] = Options[i+1];
    i++;
    continue;
	default:
	    console.log('Sorry, that is not something I know how to do.');
	}
}

try {

  if (fs.existsSync(wave_path)) {
	  var metadata = new grpc.Metadata();
  
	  for ( var key in setting ) {
	  	if(debug == 1){
	      console.log(key+":"+setting[key])
	  	}
	  	metadata.add(key, setting[key]);
	  }
  
	  if(debug == 1){
	  	console.log("metadata:"+metadata)
	  }
	  connect_grpc(metadata);
	  let chunks = readWave(wave_path)
  
	  if(debug == 1){
	  	console.log("chunks:"+chunks.length);
	  }
	  for (var i = 0; i < chunks.length; i++) {
	  	processstream( chunks[i], "data");
	  }
	  processstream( [], "EOS");
	  
  }else{
  	console.log('Sorry, file not found!');
  }
} catch(err) {
  console.error(err)
}
