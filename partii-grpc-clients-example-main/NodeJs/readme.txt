This is example for using Partii with NodeJS languages.
Quick start for gRPC node-js can go to https://grpc.io/docs/languages/node/quickstart/

In this example contain two Partii clients example such as :
- Process record wav fiel : partii-client-process-wav-file.js
    - This file will show the idea for process wav file into chunk and stream to Partii service.
    - You can start with "node partii-client-process-wav-file.js -i test.wav -apikey XXXXXXX"

- Record audio from microphone and stream to Partii : partii-client-record-microphone.js
    - Before use this example you need to install sox comand for recorder tool (https://sox.sourceforge.net/)
    - You can start with "node partii-client-record-microphone.js -apikey XXXXXXX"