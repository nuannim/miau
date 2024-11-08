package grpc.partii;

import com.google.protobuf.ByteString;
import io.grpc.*;
import io.grpc.stub.MetadataUtils;
import io.grpc.stub.StreamObserver;
import partii.grpc.PartiiService.*;
import partii.grpc.TranscriptionGrpc;
import partii.grpc.TranscriptionGrpc.TranscriptionStub;

import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CountDownLatch;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Partii_Client_Java_File {
    private static final Logger logger = Logger.getLogger(Partii_Client_Java_File.class.getName());

    private TranscriptionStub asyncStub;


    private String convMilliFormat(double millis) {
        double time = (millis * 1000);
        long mil = (long) (time % 1000);
        long sec = (long) (time / 1000) % 60;
        long minute = (long) (time / (1000 * 60)) % 60;
        long hour = (long) (time / (1000 * 60 * 60)) % 24;
        return String.format("%02d:%02d:%02d,%03d", (hour), (minute), (sec), (mil));
    }

    /**
     * Construct client for accessing HelloWorld server using the existing channel.
     */
    public Partii_Client_Java_File(Channel channel) {
        // 'channel' here is a Channel, not a ManagedChannel, so it is not this code's responsibility to
        // shut it down.

        // Passing Channels to code makes code easier to test and makes it easier to reuse Channels.
        asyncStub = TranscriptionGrpc.newStub(channel);

    }

    public List<AudioData> read_wav(String file_name) {
        List<AudioData> audio_packages = new ArrayList<AudioData>();

        int totalFramesRead = 0;
        File fileIn = new File(file_name);
        // somePathName is a pre-existing string whose value was
        // based on a user selection.
        try {
            AudioInputStream audioInputStream = AudioSystem.getAudioInputStream(fileIn);
            int bytesPerFrame = audioInputStream.getFormat().getFrameSize();
            if (bytesPerFrame == AudioSystem.NOT_SPECIFIED) {
                // some audio formats may have unspecified frame size
                // in that case we may read any amount of bytes
                bytesPerFrame = 1;
            }
            // Set an arbitrary buffer size of 1024 frames.
            //int numBytes = 1024 * bytesPerFrame;
            byte[] audioBytes = new byte[Config.package_size];
            try {
                int numBytesRead = 0;
                int numFramesRead = 0;
                // Try to read numBytes bytes from the file.
                while ((numBytesRead = audioInputStream.read(audioBytes)) != -1) {
                    //System.out.println(numBytesRead);
                    // Calculate the number of frames actually read.
                    numFramesRead = numBytesRead / bytesPerFrame;
                    totalFramesRead += numFramesRead;
                    // Here, do something useful with the audio data that's
                    // now in the audioBytes array...


                    ByteString bytes_str = ByteString.copyFrom(audioBytes);
                    AudioData ad = AudioData.newBuilder()
                            .setByteChunk(bytes_str)
                            .setBytelen(bytes_str.size())
                            .setDatatype(AudioDataType.SPEECH).build();
                    audio_packages.add(ad);


                }
            } catch (Exception ex) {
                // Handle the error...
            }
        } catch (Exception e) {
            // Handle the error...
        }

        return audio_packages;
    }

    /**
     * FileTranscribe to server.
     */
    public CountDownLatch FileTranscribe(String name) {
        logger.info("Will sent " + name + " to partii server");

        Metadata header = new Metadata();
        Metadata.Key<String> apikey_key = Metadata.Key.of("apikey", Metadata.ASCII_STRING_MARSHALLER);
        header.put(apikey_key, Config.apikey_key);
        Metadata.Key<String> model_key = Metadata.Key.of("modelkey", Metadata.ASCII_STRING_MARSHALLER);
        header.put(model_key, Config.model_key);
        Metadata.Key<String> clientid_key = Metadata.Key.of("client-id", Metadata.ASCII_STRING_MARSHALLER);
        header.put(clientid_key, Config.clientid);
        Metadata.Key<String> codec_key = Metadata.Key.of("audio-codec", Metadata.ASCII_STRING_MARSHALLER);
        header.put(codec_key, Config.codec_key);
        Metadata.Key<String> protocol = Metadata.Key.of("protocol", Metadata.ASCII_STRING_MARSHALLER);
        header.put(protocol, Config.protocol);

        Metadata.Key<String> vad_threshold = Metadata.Key.of("vad-threshold", Metadata.ASCII_STRING_MARSHALLER);
        header.put(vad_threshold, Config.vad_threshold);
        Metadata.Key<String> sampling_rate = Metadata.Key.of("sampling-rate", Metadata.ASCII_STRING_MARSHALLER);
        header.put(sampling_rate, Config.sampling_rate);
        Metadata.Key<String> num_channels = Metadata.Key.of("num-channels", Metadata.ASCII_STRING_MARSHALLER);
        header.put(num_channels, Config.num_channels);
        Metadata.Key<String> decode_channels = Metadata.Key.of("decode-channels", Metadata.ASCII_STRING_MARSHALLER);
        header.put(decode_channels, Config.decode_channels);
        Metadata.Key<String> enable_textnorm = Metadata.Key.of("enable-textnorm", Metadata.ASCII_STRING_MARSHALLER);
        header.put(enable_textnorm, Config.enable_textnorm);
        Metadata.Key<String> enable_partial = Metadata.Key.of("enable-partial", Metadata.ASCII_STRING_MARSHALLER);
        header.put(enable_partial, Config.enable_partial);
        Metadata.Key<String> enable_vad = Metadata.Key.of("enable-vad", Metadata.ASCII_STRING_MARSHALLER);
        header.put(enable_vad, Config.enable_vad);
        Metadata.Key<String> enable_endpoint = Metadata.Key.of("enable-endpoint", Metadata.ASCII_STRING_MARSHALLER);
        header.put(enable_endpoint, Config.enable_endpoint);
        Metadata.Key<String> enable_phone_result = Metadata.Key.of("enable-phone-result", Metadata.ASCII_STRING_MARSHALLER);
        header.put(enable_phone_result, Config.enable_phone_result);
        Metadata.Key<String> number_target = Metadata.Key.of("number-target", Metadata.ASCII_STRING_MARSHALLER);
        header.put(number_target, Config.number_target);

        asyncStub = MetadataUtils.attachHeaders(asyncStub, header);

        final CountDownLatch finishLatch = new CountDownLatch(1);
        StreamObserver<AudioData> requestObserver = asyncStub.liveTranscribe(
                new StreamObserver<TranscriptionResult>() {
                    @Override
                    public void onNext(TranscriptionResult value) {

                        if (value.getStatus() == StatusCode.Ok) {
                            if (value.getSentenceType() == ResultType.PARTIAL) {
                                System.out.println("Partial....");
                                System.out.println("sentenceNumber : " + value.getSentenceNumber());
                                System.out.println("transcript : " + (value.getTranscript()));
                                System.out.println("confidence : " + (value.getConfidence()));
                                System.out.println("startTime " + (value.getStartTime() + ", " + convMilliFormat(value.getStartTime())));
                                System.out.println("endTime " + (value.getEndTime() + ", " + convMilliFormat(value.getEndTime())));

                            } else if (value.getSentenceType() == ResultType.RESULT) {


                                System.out.println("Sentence....");
                                System.out.println("sentenceNumber : " + value.getSentenceNumber());
                                System.out.println("transcript : " + (value.getTranscript()));
                                System.out.println("confidence : " + (value.getConfidence()));
                                System.out.println("startTime " + (value.getStartTime() + ", " + convMilliFormat(value.getStartTime())));
                                System.out.println("endTime " + (value.getEndTime() + ", " + convMilliFormat(value.getEndTime())));


                                for (WordsLevel w : value.getWordsList()) {
                                    System.out.println("\twordNumber " + (w.getWordNumber()));
                                    System.out.println("\tword " + (w.getWord()));
                                    System.out.println("\tconfidence " + (w.getConfidence()));
                                    System.out.println("\tstartTime " + (w.getStartTime()));
                                    System.out.println("\tendTime " + (w.getEndTime()));

                                    for (PhonesLevel p : w.getPhonesList()) {
                                        System.out.println("\t\tphoneNumber " + (p.getPhoneNumber()));
                                        System.out.println("\t\tphone " + (p.getPhone()));
                                        System.out.println("\t\tconfidence " + (p.getConfidence()));
                                        System.out.println("\t\tstartTime " + (p.getStartTime()));
                                        System.out.println("\t\tendTime " + (p.getEndTime()));
                                    }
                                }

                            } else if (value.getSentenceType() == ResultType.FINISHED) {
                                System.out.println("Last respond from server");
                                System.out.println(value.getTranscript());


                            }

                        }

                    }

                    @Override
                    public void onError(Throwable t) {
                        Status status = Status.fromThrowable(t);
                        logger.log(Level.WARNING, "Failed: {0}", status);
                        finishLatch.countDown();
                    }

                    @Override
                    public void onCompleted() {
                        logger.info("Finished sendAudioStream");
                        finishLatch.countDown();
                    }

                });

        try {
            System.out.println("create audio pack");
            List<AudioData> audio_packages = read_wav(name);

            for (AudioData pack : audio_packages) {
                //System.out.println(pack.getBytelen());
                requestObserver.onNext(pack);

                if (Config.enable_delay.equals("true")) {
                    //add delay
                    double len_per_sec = 16000 * (16 / 8);
                    double delay_time = 1000 / (len_per_sec / Config.package_size);
                    try {
                        Thread.sleep((long) delay_time);
                        //Thread.sleep((long)(chunk_length_secs*1000));
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }

                if (finishLatch.getCount() == 0) {
                    // RPC completed or errored before we finished sending.
                    // Sending further requests won't error, but they will just be thrown away.
                    System.out.println("RPC completed or errored before we finished sending.");
                }
            }

        } catch (RuntimeException e) {
            // Cancel RPC
            requestObserver.onError(e);
            throw e;
        }
        // Mark the end of requests
        requestObserver.onCompleted();

        return finishLatch;
    }

}