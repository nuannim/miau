
# -*- coding: utf-8 -*-


import configparser
import time
import grpc
import PartiiService_pb2_grpc
import PartiiService_pb2
import wave
import numpy as np
import sys

_SERVER_IP = "partii.aiforthai.in.th"
_SERVER_PORT = 27018
_AUDIO_INPUT = "audio.wav"
_AUDIO_SAMPLE_RATE = 16000
_AUDIO_CODEC = "LINEAR16"
_PACKAGE_SIZE = 1024
_CHUNK_LEN_SECONE = 0.2
_VERBOSE = 0

_API_KEY = "0niRHCX9q2pEknt3HHKiuWowW6k264Su"
_CLIENT_ID = ""

_VAD_THRESHOLD = 0.5
_NUM_CHANNELS = 1
_DECODE_CHANEL = 0
_MODEL_KEY = "default"
_PROTOCOL = "partii"
_ENABLE_TEXTNORM = "true"
_ENABLE_PARTIAL = "true"
_ENABLE_VAD = "true"
_ENABLE_ENDPOINT = "true"
_NUMBER_TARGET = "thai"
_VIEW = "sentent"

def convMilliFormat(millis):
	time = (float(millis) * 1000);
	mil = time % 1000;
	sec = (time / 1000) % 60;
	minute = (time / (1000 * 60)) % 60;
	hour = (time / (1000 * 60 * 60)) % 24;
	return "{:02d}:{:02d}:{:02d},{:03d}".format(int(hour), int(minute), int(sec), int(mil));


def readwave(fname):
    obj = wave.open(fname,'r')
    if _VERBOSE != "0" : 
        print( "Number of channels",obj.getnchannels())
        print ( "Sample width",obj.getsampwidth())
        print ( "Frame rate.",obj.getframerate())
        print ( "Number of frames",obj.getnframes())
        print ( "parameters:",obj.getparams())
        
    for i in range(0, obj.getnframes(), int(_PACKAGE_SIZE)):
        waveData = obj.readframes(int(_PACKAGE_SIZE))
        yield PartiiService_pb2.AudioData(ByteChunk=waveData, Bytelen=len(waveData), Datatype=PartiiService_pb2.AudioDataType.SPEECH)
    obj.close()


def GetAvailable():
    available = 0
    channel = grpc.insecure_channel('{}:{}'.format(_SERVER_IP, _SERVER_PORT))
    stub = PartiiService_pb2_grpc.TranscriptionStub(channel)
    metadata = (
                    ('apikey', str(_API_KEY)),
                    ('client-id', str(_CLIENT_ID)),
                    ('modelkey', str(_MODEL_KEY)),
                    ('protocol', str(_PROTOCOL))
                   )
    response = stub.GetAvailable(PartiiService_pb2.EmptyMsg(), metadata=metadata)
    available = response.Available
    return available

def run():

    retries = 1
    timeout = 3

    while retries > 0:
        
        if GetAvailable() > 0 :
            if _VERBOSE != "0" : 
                print("Start : ",_AUDIO_INPUT )
                print('{}:{}'.format(_SERVER_IP, _SERVER_PORT))
            
            with grpc.insecure_channel('{}:{}'.format(_SERVER_IP, _SERVER_PORT)) as channel:
                stub = PartiiService_pb2_grpc.TranscriptionStub(channel)

                metadata = (
                            ('apikey', str(_API_KEY)),
                            ('sampling-rate', str(_AUDIO_SAMPLING_RATE)),
                            ('client-id', str(_CLIENT_ID)),
                            ('vad-threshold', str(_VAD_THRESHOLD)),
                            ('num-channels', str(_NUM_CHANNELS)),
                            ('decode-channels', str(_DECODE_CHANEL)),
                            ('modelkey', str(_MODEL_KEY)),
                            ('audio-codec', str(_AUDIO_CODEC)),
                            ('protocol', str(_PROTOCOL)),
                            ('enable-textnorm', str(_ENABLE_TEXTNORM)),
                            ('enable-partial', str(_ENABLE_PARTIAL)),
                            ('enable-vad', str(_ENABLE_VAD)),
                            ('enable-endpoint', str(_ENABLE_ENDPOINT)),
                            ('number-target', str(_NUMBER_TARGET))
                        )
                
                if _VERBOSE != "0" : 
                    print(metadata)
                
                rawbyte_list = readwave(_AUDIO_INPUT)
                
                responses = stub.LiveTranscribe(rawbyte_list, metadata=metadata)
                
                try:
                    # print("สวัสดีครับ")
                    for response in responses:
                        if(response.Status == PartiiService_pb2.StatusCode.Ok):
                            if(response.sentenceType == PartiiService_pb2.ResultType.PARTIAL):
                                if _VERBOSE != "0" : 
                                    print("sentenceNumber %s " %(response.sentenceNumber))
                                    print("transcript %s " %(response.transcript))
                                    print("confidence %s " %(response.confidence))
                                    print("startTime %s, %s " %(response.startTime, convMilliFormat(response.startTime)))
                                    print("endTime %s, %s " %(response.endTime, convMilliFormat(response.endTime)))
                        
                            elif(response.sentenceType == PartiiService_pb2.ResultType.RESULT):
                                if _VIEW == "sentent" :
                                    print("sentenceNumber %s " %(response.sentenceNumber))
                                    print("transcript %s " %(response.transcript))
                                    print("confidence %s " %(response.confidence))
                                    print("startTime %s " %(response.startTime))
                                    print("endTime %s " %(response.endTime))
                            
                                if _VIEW == "word" :
                                    for w in response.words:
                                        print("\twordNumber %s " %(w.wordNumber))
                                        print("\tword %s " %(w.word))
                                        print("\tconfidence %s " %(w.confidence))
                                        print("\tstartTime %s " %(w.startTime))
                                        print("\tendTime %s " %(w.endTime))
                                        
                                if _VIEW == "phone" :
                                    for w in response.words:
                                        for p in w.phones:
                                            print("\t\tphoneNumber %s " %(p.phoneNumber))
                                            print("\t\tphone %s " %(p.phone))
                                            print("\t\tconfidence %s " %(p.confidence))
                                            print("\t\tstartTime %s " %(p.startTime))
                                            print("\t\tendTime %s " %(p.endTime))
                                            
                            elif(response.sentenceType == PartiiService_pb2.ResultType.FINISHED):
                                
                                if _VERBOSE != "0" :
                                    print("Last respond from server [%s] " %(response.transcript))
                                    print("Stop : ", _AUDIO_INPUT)

                                retries = 0
                                break

                        elif(response.Status == PartiiService_pb2.StatusCode.Failed):
                            print("ERROR [%s] " %(response.transcript))
                            print('Waiting for %s seconds'%(timeout))
                            time.sleep(timeout)
                            retries -= 1
                    
                except:
                    print("An exception occurred")
                    print('Waiting for %s seconds'%(timeout))
                    time.sleep(timeout)
                    retries -= 1
                
        else:
            
            print('Waiting for %s seconds'%(timeout))
            time.sleep(timeout)
            retries -= 1
                    
if __name__ == '__main__':
    start_time = time.time()
    config = configparser.ConfigParser()
    # config.read('config.ini')

    # print(config.sections())  # This will print the sections found in the config file
    # print(config['DEFAULT'])   # This will print all the default values



# Add default values
    config['DEFAULT'] = {
        '_SERVER_IP': 'partii.aiforthai.in.th',
        '_SERVER_PORT': '27018',
        '_AUDIO_SAMPLING_RATE': '16000',
        '_AUDIO_CODEC': 'LINEAR16',
        '_CLIENT_ID': 'Python-Mac',
        '_VERBOSE': '1',
        '_VAD_THRESHOLD': '0.5',
        '_NUM_CHANNELS': '1',
        '_DECODE_CHANEL': '0',
        '_MODEL_KEY': 'default',
        '_PROTOCOL': 'partii',
        '_ENABLE_TEXTNORM': 'true',
        '_ENABLE_PARTIAL': 'true',
        '_ENABLE_VAD': 'true',
        '_ENABLE_ENDPOINT': 'true',
        '_NUMBER_TARGET': 'thai',
        '_VIEW': 'sentent'
    }

    config.read('config.ini')

    print(config.sections())  # This will print the sections found in the config file
    print(config['DEFAULT']['_SERVER_IP'])   # This will print all the default values



    _SERVER_IP = config['DEFAULT']['_SERVER_IP']
    _SERVER_PORT = int(config['DEFAULT']['_SERVER_PORT'])
    _AUDIO_INPUT = sys.argv[1]
    _AUDIO_SAMPLING_RATE = int(config['DEFAULT']['_AUDIO_SAMPLING_RATE'])
    _AUDIO_CODEC = config['DEFAULT']['_AUDIO_CODEC']
    _CHUNK_LEN_SECONE = config['DEFAULT']['_CHUNK_LEN_SECOND']
    _VERBOSE = config['DEFAULT']['_VERBOSE']
    
    _PACKAGE_SIZE = float(_CHUNK_LEN_SECONE) * float(_AUDIO_SAMPLE_RATE) * 2
    _API_KEY = sys.argv[2]
    _CLIENT_ID = config['DEFAULT']['_CLIENT_ID']
    
    _VAD_THRESHOLD = config['DEFAULT']['_VAD_THRESHOLD']
    _NUM_CHANNELS = config['DEFAULT']['_NUM_CHANNELS']
    _DECODE_CHANEL = config['DEFAULT']['_DECODE_CHANEL']
    _MODEL_KEY = config['DEFAULT']['_MODEL_KEY']
    _PROTOCOL = config['DEFAULT']['_PROTOCOL']
    _ENABLE_TEXTNORM = config['DEFAULT']['_ENABLE_TEXTNORM']
    _ENABLE_PARTIAL = config['DEFAULT']['_ENABLE_PARTIAL']
    _ENABLE_VAD = config['DEFAULT']['_ENABLE_VAD']
    _ENABLE_ENDPOINT = config['DEFAULT']['_ENABLE_ENDPOINT']
    _NUMBER_TARGET = config['DEFAULT']['_NUMBER_TARGET']
    _VIEW = config['DEFAULT']['_VIEW']
     
    run()
    
    end_time = time.time()
    print("Runtime of the program is ", (end_time - start_time))
