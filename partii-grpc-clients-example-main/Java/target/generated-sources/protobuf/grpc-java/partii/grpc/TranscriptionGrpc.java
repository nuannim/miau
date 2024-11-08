package partii.grpc;

import static io.grpc.MethodDescriptor.generateFullMethodName;
import static io.grpc.stub.ClientCalls.asyncBidiStreamingCall;
import static io.grpc.stub.ClientCalls.asyncClientStreamingCall;
import static io.grpc.stub.ClientCalls.asyncServerStreamingCall;
import static io.grpc.stub.ClientCalls.asyncUnaryCall;
import static io.grpc.stub.ClientCalls.blockingServerStreamingCall;
import static io.grpc.stub.ClientCalls.blockingUnaryCall;
import static io.grpc.stub.ClientCalls.futureUnaryCall;
import static io.grpc.stub.ServerCalls.asyncBidiStreamingCall;
import static io.grpc.stub.ServerCalls.asyncClientStreamingCall;
import static io.grpc.stub.ServerCalls.asyncServerStreamingCall;
import static io.grpc.stub.ServerCalls.asyncUnaryCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedStreamingCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall;

/**
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.30.2)",
    comments = "Source: PartiiService.proto")
public final class TranscriptionGrpc {

  private TranscriptionGrpc() {}

  public static final String SERVICE_NAME = "partii.Transcription";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<partii.grpc.PartiiService.AudioData,
      partii.grpc.PartiiService.TranscriptionResult> getSingleTranscribeMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "SingleTranscribe",
      requestType = partii.grpc.PartiiService.AudioData.class,
      responseType = partii.grpc.PartiiService.TranscriptionResult.class,
      methodType = io.grpc.MethodDescriptor.MethodType.BIDI_STREAMING)
  public static io.grpc.MethodDescriptor<partii.grpc.PartiiService.AudioData,
      partii.grpc.PartiiService.TranscriptionResult> getSingleTranscribeMethod() {
    io.grpc.MethodDescriptor<partii.grpc.PartiiService.AudioData, partii.grpc.PartiiService.TranscriptionResult> getSingleTranscribeMethod;
    if ((getSingleTranscribeMethod = TranscriptionGrpc.getSingleTranscribeMethod) == null) {
      synchronized (TranscriptionGrpc.class) {
        if ((getSingleTranscribeMethod = TranscriptionGrpc.getSingleTranscribeMethod) == null) {
          TranscriptionGrpc.getSingleTranscribeMethod = getSingleTranscribeMethod =
              io.grpc.MethodDescriptor.<partii.grpc.PartiiService.AudioData, partii.grpc.PartiiService.TranscriptionResult>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.BIDI_STREAMING)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "SingleTranscribe"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  partii.grpc.PartiiService.AudioData.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  partii.grpc.PartiiService.TranscriptionResult.getDefaultInstance()))
              .setSchemaDescriptor(new TranscriptionMethodDescriptorSupplier("SingleTranscribe"))
              .build();
        }
      }
    }
    return getSingleTranscribeMethod;
  }

  private static volatile io.grpc.MethodDescriptor<partii.grpc.PartiiService.AudioData,
      partii.grpc.PartiiService.TranscriptionResult> getLiveTranscribeMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "LiveTranscribe",
      requestType = partii.grpc.PartiiService.AudioData.class,
      responseType = partii.grpc.PartiiService.TranscriptionResult.class,
      methodType = io.grpc.MethodDescriptor.MethodType.BIDI_STREAMING)
  public static io.grpc.MethodDescriptor<partii.grpc.PartiiService.AudioData,
      partii.grpc.PartiiService.TranscriptionResult> getLiveTranscribeMethod() {
    io.grpc.MethodDescriptor<partii.grpc.PartiiService.AudioData, partii.grpc.PartiiService.TranscriptionResult> getLiveTranscribeMethod;
    if ((getLiveTranscribeMethod = TranscriptionGrpc.getLiveTranscribeMethod) == null) {
      synchronized (TranscriptionGrpc.class) {
        if ((getLiveTranscribeMethod = TranscriptionGrpc.getLiveTranscribeMethod) == null) {
          TranscriptionGrpc.getLiveTranscribeMethod = getLiveTranscribeMethod =
              io.grpc.MethodDescriptor.<partii.grpc.PartiiService.AudioData, partii.grpc.PartiiService.TranscriptionResult>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.BIDI_STREAMING)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "LiveTranscribe"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  partii.grpc.PartiiService.AudioData.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  partii.grpc.PartiiService.TranscriptionResult.getDefaultInstance()))
              .setSchemaDescriptor(new TranscriptionMethodDescriptorSupplier("LiveTranscribe"))
              .build();
        }
      }
    }
    return getLiveTranscribeMethod;
  }

  private static volatile io.grpc.MethodDescriptor<partii.grpc.PartiiService.EmptyMsg,
      partii.grpc.PartiiService.AvailableConnection> getGetAvailableMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "GetAvailable",
      requestType = partii.grpc.PartiiService.EmptyMsg.class,
      responseType = partii.grpc.PartiiService.AvailableConnection.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<partii.grpc.PartiiService.EmptyMsg,
      partii.grpc.PartiiService.AvailableConnection> getGetAvailableMethod() {
    io.grpc.MethodDescriptor<partii.grpc.PartiiService.EmptyMsg, partii.grpc.PartiiService.AvailableConnection> getGetAvailableMethod;
    if ((getGetAvailableMethod = TranscriptionGrpc.getGetAvailableMethod) == null) {
      synchronized (TranscriptionGrpc.class) {
        if ((getGetAvailableMethod = TranscriptionGrpc.getGetAvailableMethod) == null) {
          TranscriptionGrpc.getGetAvailableMethod = getGetAvailableMethod =
              io.grpc.MethodDescriptor.<partii.grpc.PartiiService.EmptyMsg, partii.grpc.PartiiService.AvailableConnection>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "GetAvailable"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  partii.grpc.PartiiService.EmptyMsg.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  partii.grpc.PartiiService.AvailableConnection.getDefaultInstance()))
              .setSchemaDescriptor(new TranscriptionMethodDescriptorSupplier("GetAvailable"))
              .build();
        }
      }
    }
    return getGetAvailableMethod;
  }

  private static volatile io.grpc.MethodDescriptor<partii.grpc.PartiiService.EmptyMsg,
      partii.grpc.PartiiService.BuildNumber> getGetBuildNumberMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "GetBuildNumber",
      requestType = partii.grpc.PartiiService.EmptyMsg.class,
      responseType = partii.grpc.PartiiService.BuildNumber.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<partii.grpc.PartiiService.EmptyMsg,
      partii.grpc.PartiiService.BuildNumber> getGetBuildNumberMethod() {
    io.grpc.MethodDescriptor<partii.grpc.PartiiService.EmptyMsg, partii.grpc.PartiiService.BuildNumber> getGetBuildNumberMethod;
    if ((getGetBuildNumberMethod = TranscriptionGrpc.getGetBuildNumberMethod) == null) {
      synchronized (TranscriptionGrpc.class) {
        if ((getGetBuildNumberMethod = TranscriptionGrpc.getGetBuildNumberMethod) == null) {
          TranscriptionGrpc.getGetBuildNumberMethod = getGetBuildNumberMethod =
              io.grpc.MethodDescriptor.<partii.grpc.PartiiService.EmptyMsg, partii.grpc.PartiiService.BuildNumber>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "GetBuildNumber"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  partii.grpc.PartiiService.EmptyMsg.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  partii.grpc.PartiiService.BuildNumber.getDefaultInstance()))
              .setSchemaDescriptor(new TranscriptionMethodDescriptorSupplier("GetBuildNumber"))
              .build();
        }
      }
    }
    return getGetBuildNumberMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static TranscriptionStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<TranscriptionStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<TranscriptionStub>() {
        @java.lang.Override
        public TranscriptionStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new TranscriptionStub(channel, callOptions);
        }
      };
    return TranscriptionStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static TranscriptionBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<TranscriptionBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<TranscriptionBlockingStub>() {
        @java.lang.Override
        public TranscriptionBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new TranscriptionBlockingStub(channel, callOptions);
        }
      };
    return TranscriptionBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static TranscriptionFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<TranscriptionFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<TranscriptionFutureStub>() {
        @java.lang.Override
        public TranscriptionFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new TranscriptionFutureStub(channel, callOptions);
        }
      };
    return TranscriptionFutureStub.newStub(factory, channel);
  }

  /**
   */
  public static abstract class TranscriptionImplBase implements io.grpc.BindableService {

    /**
     */
    public io.grpc.stub.StreamObserver<partii.grpc.PartiiService.AudioData> singleTranscribe(
        io.grpc.stub.StreamObserver<partii.grpc.PartiiService.TranscriptionResult> responseObserver) {
      return asyncUnimplementedStreamingCall(getSingleTranscribeMethod(), responseObserver);
    }

    /**
     */
    public io.grpc.stub.StreamObserver<partii.grpc.PartiiService.AudioData> liveTranscribe(
        io.grpc.stub.StreamObserver<partii.grpc.PartiiService.TranscriptionResult> responseObserver) {
      return asyncUnimplementedStreamingCall(getLiveTranscribeMethod(), responseObserver);
    }

    /**
     */
    public void getAvailable(partii.grpc.PartiiService.EmptyMsg request,
        io.grpc.stub.StreamObserver<partii.grpc.PartiiService.AvailableConnection> responseObserver) {
      asyncUnimplementedUnaryCall(getGetAvailableMethod(), responseObserver);
    }

    /**
     */
    public void getBuildNumber(partii.grpc.PartiiService.EmptyMsg request,
        io.grpc.stub.StreamObserver<partii.grpc.PartiiService.BuildNumber> responseObserver) {
      asyncUnimplementedUnaryCall(getGetBuildNumberMethod(), responseObserver);
    }

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
          .addMethod(
            getSingleTranscribeMethod(),
            asyncBidiStreamingCall(
              new MethodHandlers<
                partii.grpc.PartiiService.AudioData,
                partii.grpc.PartiiService.TranscriptionResult>(
                  this, METHODID_SINGLE_TRANSCRIBE)))
          .addMethod(
            getLiveTranscribeMethod(),
            asyncBidiStreamingCall(
              new MethodHandlers<
                partii.grpc.PartiiService.AudioData,
                partii.grpc.PartiiService.TranscriptionResult>(
                  this, METHODID_LIVE_TRANSCRIBE)))
          .addMethod(
            getGetAvailableMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                partii.grpc.PartiiService.EmptyMsg,
                partii.grpc.PartiiService.AvailableConnection>(
                  this, METHODID_GET_AVAILABLE)))
          .addMethod(
            getGetBuildNumberMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                partii.grpc.PartiiService.EmptyMsg,
                partii.grpc.PartiiService.BuildNumber>(
                  this, METHODID_GET_BUILD_NUMBER)))
          .build();
    }
  }

  /**
   */
  public static final class TranscriptionStub extends io.grpc.stub.AbstractAsyncStub<TranscriptionStub> {
    private TranscriptionStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected TranscriptionStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new TranscriptionStub(channel, callOptions);
    }

    /**
     */
    public io.grpc.stub.StreamObserver<partii.grpc.PartiiService.AudioData> singleTranscribe(
        io.grpc.stub.StreamObserver<partii.grpc.PartiiService.TranscriptionResult> responseObserver) {
      return asyncBidiStreamingCall(
          getChannel().newCall(getSingleTranscribeMethod(), getCallOptions()), responseObserver);
    }

    /**
     */
    public io.grpc.stub.StreamObserver<partii.grpc.PartiiService.AudioData> liveTranscribe(
        io.grpc.stub.StreamObserver<partii.grpc.PartiiService.TranscriptionResult> responseObserver) {
      return asyncBidiStreamingCall(
          getChannel().newCall(getLiveTranscribeMethod(), getCallOptions()), responseObserver);
    }

    /**
     */
    public void getAvailable(partii.grpc.PartiiService.EmptyMsg request,
        io.grpc.stub.StreamObserver<partii.grpc.PartiiService.AvailableConnection> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getGetAvailableMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void getBuildNumber(partii.grpc.PartiiService.EmptyMsg request,
        io.grpc.stub.StreamObserver<partii.grpc.PartiiService.BuildNumber> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getGetBuildNumberMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   */
  public static final class TranscriptionBlockingStub extends io.grpc.stub.AbstractBlockingStub<TranscriptionBlockingStub> {
    private TranscriptionBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected TranscriptionBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new TranscriptionBlockingStub(channel, callOptions);
    }

    /**
     */
    public partii.grpc.PartiiService.AvailableConnection getAvailable(partii.grpc.PartiiService.EmptyMsg request) {
      return blockingUnaryCall(
          getChannel(), getGetAvailableMethod(), getCallOptions(), request);
    }

    /**
     */
    public partii.grpc.PartiiService.BuildNumber getBuildNumber(partii.grpc.PartiiService.EmptyMsg request) {
      return blockingUnaryCall(
          getChannel(), getGetBuildNumberMethod(), getCallOptions(), request);
    }
  }

  /**
   */
  public static final class TranscriptionFutureStub extends io.grpc.stub.AbstractFutureStub<TranscriptionFutureStub> {
    private TranscriptionFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected TranscriptionFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new TranscriptionFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<partii.grpc.PartiiService.AvailableConnection> getAvailable(
        partii.grpc.PartiiService.EmptyMsg request) {
      return futureUnaryCall(
          getChannel().newCall(getGetAvailableMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<partii.grpc.PartiiService.BuildNumber> getBuildNumber(
        partii.grpc.PartiiService.EmptyMsg request) {
      return futureUnaryCall(
          getChannel().newCall(getGetBuildNumberMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_GET_AVAILABLE = 0;
  private static final int METHODID_GET_BUILD_NUMBER = 1;
  private static final int METHODID_SINGLE_TRANSCRIBE = 2;
  private static final int METHODID_LIVE_TRANSCRIBE = 3;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final TranscriptionImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(TranscriptionImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_GET_AVAILABLE:
          serviceImpl.getAvailable((partii.grpc.PartiiService.EmptyMsg) request,
              (io.grpc.stub.StreamObserver<partii.grpc.PartiiService.AvailableConnection>) responseObserver);
          break;
        case METHODID_GET_BUILD_NUMBER:
          serviceImpl.getBuildNumber((partii.grpc.PartiiService.EmptyMsg) request,
              (io.grpc.stub.StreamObserver<partii.grpc.PartiiService.BuildNumber>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_SINGLE_TRANSCRIBE:
          return (io.grpc.stub.StreamObserver<Req>) serviceImpl.singleTranscribe(
              (io.grpc.stub.StreamObserver<partii.grpc.PartiiService.TranscriptionResult>) responseObserver);
        case METHODID_LIVE_TRANSCRIBE:
          return (io.grpc.stub.StreamObserver<Req>) serviceImpl.liveTranscribe(
              (io.grpc.stub.StreamObserver<partii.grpc.PartiiService.TranscriptionResult>) responseObserver);
        default:
          throw new AssertionError();
      }
    }
  }

  private static abstract class TranscriptionBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    TranscriptionBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return partii.grpc.PartiiService.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("Transcription");
    }
  }

  private static final class TranscriptionFileDescriptorSupplier
      extends TranscriptionBaseDescriptorSupplier {
    TranscriptionFileDescriptorSupplier() {}
  }

  private static final class TranscriptionMethodDescriptorSupplier
      extends TranscriptionBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    TranscriptionMethodDescriptorSupplier(String methodName) {
      this.methodName = methodName;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.MethodDescriptor getMethodDescriptor() {
      return getServiceDescriptor().findMethodByName(methodName);
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (TranscriptionGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new TranscriptionFileDescriptorSupplier())
              .addMethod(getSingleTranscribeMethod())
              .addMethod(getLiveTranscribeMethod())
              .addMethod(getGetAvailableMethod())
              .addMethod(getGetBuildNumberMethod())
              .build();
        }
      }
    }
    return result;
  }
}
