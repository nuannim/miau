const fs = require('fs')
var grpc = require('@grpc/grpc-js');
var protoLoader = require('@grpc/proto-loader');
const recorder = require('node-record-lpcm16');
var FileWriter = require('wav').FileWriter;
const readline = require('readline');

var PROTO_PATH = __dirname + '/../protobuf/v2.1/PartiiService.proto';

const debug = 0;
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

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

var temp_rec_name = "temp.wav";
var bit_per_sample = 16;
var record_duration = 0;
const skip_rec = 0.5; //milisec

function connect_grpc(metadata){
    try {
      if(debug == 1){
        console.log("connect to grpc "+setting['server_ip']+":"+setting['server_port'])
      }
      
        client_partii = new partii_proto.Transcription(setting['server_ip']+":"+setting['server_port'],grpc.credentials.createInsecure());
        call_partii = client_partii.LiveTranscribe(metadata);

         
        call_partii.on('data', function(TranscriptionResult) {
                
                if( TranscriptionResult.sentenceType == "PARTIAL"){
                  process.stdout.write('\r'+TranscriptionResult.transcript.padEnd(128)); //format output string "abc       "

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
                    if(TranscriptionResult.transcript != ""){
                      process.stdout.write('\r'+TranscriptionResult.transcript.padEnd(128) + '\n'); //format output string "abc       "
                    }
                    
                    /*
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
                    */
                }else if(TranscriptionResult.sentenceType == "FINISHED"){
                  console.log(TranscriptionResult.transcript);

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

function main() {
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

    var outputFileStream = new FileWriter(temp_rec_name, {
      sampleRate: parseInt(setting['sampling-rate']),
      channels: parseInt(setting['num-channels'])
    });
  
    recording = recorder.record({
      recorder: 'sox',
      sampleRate: parseInt(setting['sampling-rate']),
      channels: parseInt(setting['num-channels'])
    })
  
    recording.stream().on('data', function(chunk){ 
      const duration = (chunk.length) / ( parseInt(setting['sampling-rate']) * parseInt(setting['num-channels']) * (bit_per_sample / 8));
      record_duration += duration
      if( record_duration >= skip_rec ){ //skip fist 500 milisecond first
        processstream( {
          ByteChunk: chunk,
          Bytelen: chunk.length,
          Datatype: 0
        }, "data");
  
        outputFileStream.write(chunk)
      }
      
    })
  
    recording.stream().on('error', function(){
      if(debug == 1){  
        console.log('recording stream().on error')
      }
      recording.stop()
    })

    recording.stream().on('end', function(){
      if(debug == 1){  
        console.log('recording stream().on end')
      }
      processstream( [], "EOS");
    })

    //setup metadata
    var metadata = new grpc.Metadata();
    for ( var key in setting ) {
      metadata.add(key, setting[key]);
    
      if(key == "server_ip"){ 
        grpc_server = setting[key];
      }else if(key == "server_port"){
        grpc_port = setting[key];
      }
    }

    console.log("Connect to Partii service...");
    connect_grpc(metadata);
    console.log("Start recording and transcribe...");

  } catch(err) {
    console.error(err)
  }
}

if (require.main === module) {
  main();

  rl.question('Do you want to stop record (y/n)? \n', function (answer) {
    if(answer == 'y'){
      recording.stop();
      rl.close();
    }
  });

  rl.on('close', function () {
    console.log('\nStop recording!!!');
  });

}
  





 



