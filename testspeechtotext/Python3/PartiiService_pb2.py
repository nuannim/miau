# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: PartiiService.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'PartiiService.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13PartiiService.proto\x12\x06partii\"\x17\n\x04Word\x12\x0f\n\x07wordstr\x18\x01 \x01(\t\"-\n\nWordResult\x12\x0e\n\x06wordid\x18\x01 \x01(\x03\x12\x0f\n\x07wordstr\x18\x02 \x01(\t\"\n\n\x08\x45mptyMsg\"(\n\x13\x41vailableConnection\x12\x11\n\tAvailable\x18\x01 \x01(\x03\" \n\x0b\x42uildNumber\x12\x11\n\tBuildDate\x18\x01 \x01(\t\"Q\n\x08\x41uthData\x12\x0e\n\x06\x41piKey\x18\x01 \x01(\t\x12\x14\n\x0cSamplingRate\x18\x02 \x01(\x03\x12\x10\n\x08\x43lientID\x18\x03 \x01(\t\x12\r\n\x05\x43odec\x18\x04 \x01(\x03\"E\n\nAuthStatus\x12\x0f\n\x07Message\x18\x01 \x01(\t\x12&\n\nAuthStatus\x18\x02 \x01(\x0e\x32\x12.partii.StatusCode\"X\n\tAudioData\x12\x11\n\tByteChunk\x18\x01 \x01(\x0c\x12\x0f\n\x07\x42ytelen\x18\x02 \x01(\x03\x12\'\n\x08\x44\x61tatype\x18\x03 \x01(\x0e\x32\x15.partii.AudioDataType\"\x8b\x01\n\nWordsLevel\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\x11\n\tstartTime\x18\x03 \x01(\x02\x12\x0f\n\x07\x65ndTime\x18\x04 \x01(\x02\x12\x12\n\nwordNumber\x18\x05 \x01(\x03\x12#\n\x06phones\x18\x06 \x03(\x0b\x32\x13.partii.PhonesLevel\"i\n\x0bPhonesLevel\x12\r\n\x05phone\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\x11\n\tstartTime\x18\x03 \x01(\x02\x12\x0f\n\x07\x65ndTime\x18\x04 \x01(\x02\x12\x13\n\x0bphoneNumber\x18\x05 \x01(\x03\"\xba\x02\n\x13TranscriptionResult\x12\x12\n\ntranscript\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\x11\n\tstartTime\x18\x03 \x01(\x02\x12\x0f\n\x07\x65ndTime\x18\x04 \x01(\x02\x12\x16\n\x0esentenceNumber\x18\x05 \x01(\x03\x12(\n\x0csentenceType\x18\x06 \x01(\x0e\x32\x12.partii.ResultType\x12!\n\x05words\x18\x07 \x03(\x0b\x32\x12.partii.WordsLevel\x12&\n\x07\x65motion\x18\x08 \x01(\x0b\x32\x15.partii.EmotionResult\x12&\n\x07speaker\x18\t \x01(\x0b\x32\x15.partii.SpeakerResult\x12\"\n\x06Status\x18\n \x01(\x0e\x32\x12.partii.StatusCode\"\xaa\x01\n\rSpeakerResult\x12\x11\n\tspeakerID\x18\x01 \x01(\x03\x12\x11\n\tstartTime\x18\x02 \x01(\x02\x12\x0f\n\x07\x65ndTime\x18\x03 \x01(\x02\x12\x15\n\rspeakerNumber\x18\x04 \x01(\x03\x12\'\n\x0bspeakerType\x18\x05 \x01(\x0e\x32\x12.partii.ResultType\x12\"\n\x06Status\x18\x06 \x01(\x0e\x32\x12.partii.StatusCode\"\xe5\x01\n\rEmotionResult\x12\x0f\n\x07\x65motion\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\x11\n\tstartTime\x18\x03 \x01(\x02\x12\x0f\n\x07\x65ndTime\x18\x04 \x01(\x02\x12\x15\n\remotionNumber\x18\x05 \x01(\x03\x12\'\n\x0bsegmentType\x18\x06 \x01(\x0e\x32\x12.partii.ResultType\x12\'\n\x0bsubemotions\x18\x07 \x03(\x0b\x32\x12.partii.SubEmotion\x12\"\n\x06Status\x18\x08 \x01(\x0e\x32\x12.partii.StatusCode\"l\n\nSubEmotion\x12\x0f\n\x07\x65motion\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\x11\n\tstartTime\x18\x03 \x01(\x02\x12\x0f\n\x07\x65ndTime\x18\x04 \x01(\x02\x12\x15\n\remotionNumber\x18\x05 \x01(\x03\"X\n\x07VADProb\x12\x0f\n\x07\x66rameid\x18\x01 \x01(\x03\x12\x13\n\x0bprobability\x18\x02 \x01(\x02\x12\'\n\x08\x64\x61tatype\x18\x03 \x01(\x0e\x32\x15.partii.AudioDataType\"n\n\x12\x43\x61librateVadResult\x12\x14\n\x0cvadthreshold\x18\x01 \x01(\x02\x12\x1e\n\x05probs\x18\x02 \x03(\x0b\x32\x0f.partii.VADProb\x12\"\n\x06Status\x18\x03 \x01(\x0e\x32\x12.partii.StatusCode\"\xbc\x01\n\x0eWakeWordResult\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\x11\n\tstartTime\x18\x03 \x01(\x02\x12\x0f\n\x07\x65ndTime\x18\x04 \x01(\x02\x12\x16\n\x0ewakewordNumber\x18\x05 \x01(\x03\x12(\n\x0csentenceType\x18\x06 \x01(\x0e\x32\x12.partii.ResultType\x12\"\n\x06Status\x18\x07 \x01(\x0e\x32\x12.partii.StatusCode\"\xda\x01\n\x1eWakeWordAndTranscriptionResult\x12/\n\ntranscript\x18\x01 \x01(\x0b\x32\x1b.partii.TranscriptionResult\x12(\n\x08wakeword\x18\x02 \x01(\x0b\x32\x16.partii.WakeWordResult\x12&\n\nresulttype\x18\x03 \x01(\x0e\x32\x12.partii.ResultType\x12\"\n\x06Status\x18\x04 \x01(\x0e\x32\x12.partii.StatusCode\x12\x11\n\tstatusmsg\x18\x05 \x01(\t*f\n\nAudioCodec\x12\x0c\n\x08LINEAR16\x10\x00\x12\t\n\x05SPEEX\x10\x01\x12\x08\n\x04\x46LAC\x10\x02\x12\x07\n\x03MP3\x10\x03\x12\t\n\x05MULAW\x10\x04\x12\x07\n\x03\x41MR\x10\x05\x12\n\n\x06\x41MR_WB\x10\x06\x12\x0c\n\x08OGG_OPUS\x10\x07*Q\n\nResultType\x12\x0b\n\x07PARTIAL\x10\x00\x12\n\n\x06RESULT\x10\x01\x12\x0c\n\x08\x46INISHED\x10\x02\x12\x0c\n\x08WAKEWORD\x10\x03\x12\x0e\n\nTRANSCRIPT\x10\x04*8\n\rAudioDataType\x12\n\n\x06SPEECH\x10\x00\x12\r\n\tNONSPEECH\x10\x01\x12\x0c\n\x08\x45NDPOINT\x10\x02*-\n\nStatusCode\x12\x0b\n\x07Unknown\x10\x00\x12\x06\n\x02Ok\x10\x01\x12\n\n\x06\x46\x61iled\x10\x02\x32\x9d\x02\n\rTranscription\x12H\n\x10SingleTranscribe\x12\x11.partii.AudioData\x1a\x1b.partii.TranscriptionResult\"\x00(\x01\x30\x01\x12\x46\n\x0eLiveTranscribe\x12\x11.partii.AudioData\x1a\x1b.partii.TranscriptionResult\"\x00(\x01\x30\x01\x12?\n\x0cGetAvailable\x12\x10.partii.EmptyMsg\x1a\x1b.partii.AvailableConnection\"\x00\x12\x39\n\x0eGetBuildNumber\x12\x10.partii.EmptyMsg\x1a\x13.partii.BuildNumber\"\x00\x42\r\n\x0bpartii.grpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PartiiService_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\013partii.grpc'
  _globals['_AUDIOCODEC']._serialized_start=2130
  _globals['_AUDIOCODEC']._serialized_end=2232
  _globals['_RESULTTYPE']._serialized_start=2234
  _globals['_RESULTTYPE']._serialized_end=2315
  _globals['_AUDIODATATYPE']._serialized_start=2317
  _globals['_AUDIODATATYPE']._serialized_end=2373
  _globals['_STATUSCODE']._serialized_start=2375
  _globals['_STATUSCODE']._serialized_end=2420
  _globals['_WORD']._serialized_start=31
  _globals['_WORD']._serialized_end=54
  _globals['_WORDRESULT']._serialized_start=56
  _globals['_WORDRESULT']._serialized_end=101
  _globals['_EMPTYMSG']._serialized_start=103
  _globals['_EMPTYMSG']._serialized_end=113
  _globals['_AVAILABLECONNECTION']._serialized_start=115
  _globals['_AVAILABLECONNECTION']._serialized_end=155
  _globals['_BUILDNUMBER']._serialized_start=157
  _globals['_BUILDNUMBER']._serialized_end=189
  _globals['_AUTHDATA']._serialized_start=191
  _globals['_AUTHDATA']._serialized_end=272
  _globals['_AUTHSTATUS']._serialized_start=274
  _globals['_AUTHSTATUS']._serialized_end=343
  _globals['_AUDIODATA']._serialized_start=345
  _globals['_AUDIODATA']._serialized_end=433
  _globals['_WORDSLEVEL']._serialized_start=436
  _globals['_WORDSLEVEL']._serialized_end=575
  _globals['_PHONESLEVEL']._serialized_start=577
  _globals['_PHONESLEVEL']._serialized_end=682
  _globals['_TRANSCRIPTIONRESULT']._serialized_start=685
  _globals['_TRANSCRIPTIONRESULT']._serialized_end=999
  _globals['_SPEAKERRESULT']._serialized_start=1002
  _globals['_SPEAKERRESULT']._serialized_end=1172
  _globals['_EMOTIONRESULT']._serialized_start=1175
  _globals['_EMOTIONRESULT']._serialized_end=1404
  _globals['_SUBEMOTION']._serialized_start=1406
  _globals['_SUBEMOTION']._serialized_end=1514
  _globals['_VADPROB']._serialized_start=1516
  _globals['_VADPROB']._serialized_end=1604
  _globals['_CALIBRATEVADRESULT']._serialized_start=1606
  _globals['_CALIBRATEVADRESULT']._serialized_end=1716
  _globals['_WAKEWORDRESULT']._serialized_start=1719
  _globals['_WAKEWORDRESULT']._serialized_end=1907
  _globals['_WAKEWORDANDTRANSCRIPTIONRESULT']._serialized_start=1910
  _globals['_WAKEWORDANDTRANSCRIPTIONRESULT']._serialized_end=2128
  _globals['_TRANSCRIPTION']._serialized_start=2423
  _globals['_TRANSCRIPTION']._serialized_end=2708
# @@protoc_insertion_point(module_scope)
