package utils;

public class SpeechObject {
    private int size = 0;
    private byte[] raw = null;
    private boolean eos = false;

    public boolean isEos() {
        return eos;
    }

    public void setEos(boolean eos) {
        this.eos = eos;
    }

    public SpeechObject(byte[] rawdata, boolean eos) {
        if (rawdata != null) {
            this.raw = rawdata;
            this.size = rawdata.length;
        }
        this.eos = eos;
    }

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public byte[] getRaw() {
        return raw;
    }

    public void setRaw(byte[] raw) {
        this.raw = raw;
    }


}
