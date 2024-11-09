#!/bin/bash

# python3 -m grpc_tools.protoc -I./v2.1/ --python_out=../Python3/ --grpc_python_out=../Python3/ v2.1/PartiiService.proto
python -m grpc_tools.protoc -I./v2.1/ --python_out=../Python3/ --grpc_python_out=../Python3/ v2.1/PartiiService.proto