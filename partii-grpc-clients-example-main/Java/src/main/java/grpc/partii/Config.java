package grpc.partii;

import io.grpc.Metadata;
import partii.grpc.PartiiService;

import static partii.grpc.PartiiService.*;

public class Config {
    static String input_file = "";
    static String output_file = "";
    static String server_ip = "partii.aiforthai.in.th";
    static String server_port = "27016";
    static String apikey_key = "xxxxxxx";
    static String model_key = "default";
    static String clientid = "java-client";
    static String codec_key = AudioCodec.LINEAR16.toString();
    static String protocol = "partii";
    static String vad_threshold = "0.5";
    static String sampling_rate = "16000";
    static String num_channels = "1";
    static String decode_channels = "0";
    static String enable_textnorm = "true";
    static String enable_partial = "true";
    static String enable_vad = "true";
    static String enable_delay = "false";
    static String enable_endpoint = "true";
    static String enable_phone_result = "false";
    static String number_target = "english";
    static double chunk_length_secs = 0.032;
    static int package_size = (int) (16000 * chunk_length_secs * (16 / 8));//1024;
    static boolean use_mic = false;
}
