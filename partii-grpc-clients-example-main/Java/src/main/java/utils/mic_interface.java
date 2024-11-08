package utils;

public interface mic_interface {
    void onMicSpeech(byte[] speech);

    void onMicError(String err);

    void onMicStop();
}
