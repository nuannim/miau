package grpc.partii;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import utils.Microphone;

import java.text.DecimalFormat;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;


public class Main {

    private static double startAsrTime = 0;
    private static double stopAsrTime = 0;
    private static Microphone mic_ = null;
    private static Boolean rec_stage = false;
    private static DecimalFormat df2 = new DecimalFormat("###.##");

    private static boolean getOpts(String[] args) {
        int i = 0;
        String arg;
        while (i < args.length && args[i].startsWith("-")) {
            arg = args[i];
            if (arg.equals("-i")) {
                Config.input_file = (args[i + 1] != null) ? args[i + 1].trim() : "";
                i += 2;
            }else if (arg.equals("-o")) {
                Config.output_file = (args[i + 1] != null) ? args[i + 1].trim() : "";
                i += 2;
            } else if (arg.equals("-apikey")) {
                Config.apikey_key = (args[i + 1] != null) ? args[i + 1].trim() : "";
                i += 2;
            } else if (arg.equals("-chunk-len")) {
                double tmp = Double.parseDouble((args[i + 1] != null) ? args[i + 1].trim() : "");
                Config.chunk_length_secs = (tmp > 0) ? tmp : Config.chunk_length_secs;
                i += 2;
            } else if (arg.equals("-server-ip")) {
                Config.server_ip = (args[i + 1] != null) ? args[i + 1].trim() : "";
                i += 2;
            } else if (arg.equals("-server-port")) {
                Config.server_port = (args[i + 1] != null) ? args[i + 1].trim() : "";
                i += 2;
            } else if (arg.equals("-model-key")) {
                Config.model_key = (args[i + 1] != null) ? args[i + 1].trim() : "";
                i += 2;
            } else if (arg.equals("-clientid")) {
                Config.clientid = (args[i + 1] != null) ? args[i + 1].trim() : "";
                i += 2;
            } else if (arg.equals("-codec-key")) {
                Config.codec_key = (args[i + 1] != null) ? args[i + 1].trim() : "";
                i += 2;
            } else if (arg.equals("-protocol")) {
                Config.protocol = (args[i + 1] != null) ? args[i + 1].trim() : "";
                i += 2;
            } else if (arg.equals("-vad-threshold")) {
                Config.vad_threshold = (args[i + 1] != null) ? args[i + 1].trim() : "";
                i += 2;
            } else if (arg.equals("-sampling-rate")) {
                Config.sampling_rate = (args[i + 1] != null) ? args[i + 1].trim() : "";
                i += 2;
            } else if (arg.equals("-num-channels")) {
                Config.num_channels = (args[i + 1] != null) ? args[i + 1].trim() : "";
                i += 2;
            } else if (arg.equals("-decode-channels")) {
                Config.decode_channels = (args[i + 1] != null) ? args[i + 1].trim() : "";
                i += 2;
            } else if (arg.equals("-enable-textnorm")) {
                Config.enable_textnorm = (args[i + 1] != null) ? args[i + 1].trim() : "";
                i += 2;
            } else if (arg.equals("-enable-partial")) {
                Config.enable_partial = (args[i + 1] != null) ? args[i + 1].trim() : "";
                i += 2;
            } else if (arg.equals("-enable-vad")) {
                Config.enable_vad = (args[i + 1] != null) ? args[i + 1].trim() : "";
                i += 2;
            } else if (arg.equals("-enable-endpoint")) {
                Config.enable_endpoint = (args[i + 1] != null) ? args[i + 1].trim() : "";
                i += 2;
            } else if (arg.equals("-enable-phone-result")) {
                Config.enable_phone_result = (args[i + 1] != null) ? args[i + 1].trim() : "";
                i += 2;
            } else if (arg.equals("-number-target")) {
                Config.number_target = (args[i + 1] != null) ? args[i + 1].trim() : "";
                i += 2;
            } else if (arg.equals("-enable-delay")) {
                Config.enable_delay = (args[i + 1] != null) ? args[i + 1].trim() : "";
                i += 2;
            } else if (arg.equals("-use-mic")) {
                Config.use_mic = Boolean.parseBoolean(args[i + 1]);
                i += 2;
            } else {
                i++;
            }
        }

        if (Config.input_file == "" && !Config.use_mic) {
            System.out.println("Usage: program \n"
                    + "\t-i speech.wav \n"
                    + "\t-o save.wav \n"
                    + "\t[-apikey KEY] \n"
                    + "\t[-chunk-len second (default 0.032)] \n"
                    + "\t[-server-ip 0.0.0.0] \n"
                    + "\t[-server-port 27015] \n"
                    + "\t[-model-key default] \n"
                    + "\t[-clientid java-client] \n"
                    + "\t[-codec-key LINEAR16] \n"
                    + "\t[-protocol partii] \n"
                    + "\t[-vad-threshold 0.5] \n"
                    + "\t[-sampling-rate 16000] \n"
                    + "\t[-num-channels 1] \n"
                    + "\t[-decode-channels true|false] \n"
                    + "\t[-enable-textnorm true|false] \n"
                    + "\t[-enable-partial true|false] \n"
                    + "\t[-enable-vad true|false] \n"
                    + "\t[-enable-endpoint true|false] \n"
                    + "\t[-enable-phone-result true|false] \n"
                    + "\t[-number-target english|thai] \n"
                    + "\t[-enable-delay true|false] \n"
                    + "\t[-use-mic true|false] \n"
            );
            return false;
        } else {
            return true;
        }
    }

    public static void main(String[] args) throws InterruptedException {
        startAsrTime = System.currentTimeMillis();
        if (!getOpts(args)) {
            System.exit(0);
        }
        Config.package_size = (int) (16000 * Config.chunk_length_secs * (16 / 8));//1024;

        // Create a communication channel to the server, known as a Channel. Channels are thread-safe
        // and reusable. It is common to create channels at the beginning of your application and reuse
        // them until the application shuts down.
        System.out.println("target -> " + Config.server_ip + ":" + Config.server_port);
        //ManagedChannel channel = ManagedChannelBuilder.forTarget(target).usePlaintext().build();
        ManagedChannel channel = ManagedChannelBuilder.forAddress(
                Config.server_ip, Integer.parseInt(Config.server_port)).usePlaintext().build();

        if (Config.use_mic) {
            try {
                Partii_Client_Java_Mic client = new Partii_Client_Java_Mic(channel);

                if (mic_ == null) {
                    mic_ = new Microphone(client);

                    if (mic_ != null) {
                        mic_.run();
                        rec_stage = true;
                        System.out.println("Start record...");
                    }
                } else if (rec_stage == false) {
                    mic_.run();
                    rec_stage = true;
                    System.out.println("Stop record...");
                }

                // Send and receive some notes.
                CountDownLatch finishLatch = client.LiveTranscribe();

                if (!finishLatch.await(5, TimeUnit.MINUTES)) {
                    System.out.println("SendAudioStream_ can not finish within 1 minutes");
                }

            } catch (InterruptedException e) {
                e.printStackTrace();
            } finally {
                // ManagedChannels use resources like threads and TCP connections. To prevent leaking these
                // resources the channel should be shut down when it will no longer be used. If it may be used
                // again leave it running.
                channel.shutdownNow().awaitTermination(60, TimeUnit.SECONDS);
            }
        } else {
            if (Config.input_file != "") {
                try {
                    Partii_Client_Java_File client = new Partii_Client_Java_File(channel);

                    // Send and receive some notes.
                    CountDownLatch finishLatch = client.FileTranscribe(Config.input_file);

                    if (!finishLatch.await(3, TimeUnit.HOURS)) {
                        System.out.println("FileTranscribe can not finish within 3 hours");
                    }

                } finally {
                    // ManagedChannels use resources like threads and TCP connections. To prevent leaking these
                    // resources the channel should be shut down when it will no longer be used. If it may be used
                    // again leave it running.
                    channel.shutdownNow().awaitTermination(60, TimeUnit.SECONDS);
                }
            }
        }


        stopAsrTime = System.currentTimeMillis();
        double pt = (stopAsrTime - startAsrTime) / 1000;
        System.out.println("Processing time = " + Double.valueOf(df2.format(pt)));

    }
}
