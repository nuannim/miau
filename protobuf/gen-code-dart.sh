#!/bin/bash
protoc --dart_out=grpc:./v2.1/ -I./v2.1/ v2.1/PartiiService.proto
