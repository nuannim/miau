This is example for using Partii with Python languages.
Quick start for gRPC python can go to https://grpc.io/docs/languages/python/quickstart/

Before use this example you need to prepare partii library from protobuf file first.
- By go to protobuf/ then run "./gen-code-python.sh" the output will save at Python3/PartiiService_pb2.py and Python3/PartiiService_pb2_grpc.py

In this example contain two Partii clients example such as :
- Process record wav fiel : partii-client-process-wav-file.py
    - This file will show the idea for process wav file into chunk and stream to Partii service.
    - You can start with "python3 partii-client-process-wav-file.js test.wav apikey"

- Record audio from microphone and stream to Partii : partii-client-record-microphone.py
    - Before use this example you need to install pyaudio for recorder tool (https://pypi.org/project/PyAudio/)
    - You can start with "python3 partii-client-record-microphone.py apikey" then press 'q' for stop record and exit.