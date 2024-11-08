
protoc ./v2.1/PartiiService.proto --grpc_out=./v2.1 --plugin=protoc-gen-grpc=/usr/local/bin/grpc_cpp_plugin --proto_path=./v2.1\

protoc ./v2.1/PartiiService.proto --cpp_out=./v2.1 --proto_path=./v2.1