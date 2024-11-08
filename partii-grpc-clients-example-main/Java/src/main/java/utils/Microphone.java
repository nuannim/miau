package utils;

import javax.sound.sampled.*;

public class Microphone implements Runnable {

    mic_interface callback;
    Boolean stopCapture = false;
    AudioFormat audioFormat;
    TargetDataLine microphone;
    private Thread rec_thread = null;

    public Microphone(mic_interface p) {
        callback = p;
    }

    private AudioFormat getAudioFormat() {
        float sampleRate = 16000;
        // 8000,11025,16000,22050,44100
        int sampleSizeInBits = 16;
        // 8,16
        int channels = 1;
        // 1,2
        boolean signed = true;
        // true,false
        boolean bigEndian = false;
        // true,false
        return new AudioFormat(sampleRate, sampleSizeInBits, channels, signed, bigEndian);
    }

    public void stop_rec() {
        stopCapture = true;
    }

    @Override
    public void run() {

        if (rec_thread != null) {
            if (rec_thread.isAlive()) {
                rec_thread.stop();
            }
        }

        rec_thread = new Thread(() -> {
            System.out.println("record thread start...");
            do {
                try {

                    // Get everything set up for capture
                    audioFormat = getAudioFormat();
                    DataLine.Info info = new DataLine.Info(TargetDataLine.class, audioFormat);

                    // checks if system supports the data line
                    if (!AudioSystem.isLineSupported(info)) {
                        callback.onMicError("Line not supported");
                    }
                    microphone = (TargetDataLine) AudioSystem.getLine(info);
                    microphone.open(audioFormat);
                    microphone.start();   // start capturing

                    byte[] tempBuffer = new byte[microphone.getBufferSize() / 4];

                    //byteArrayOutputStream = new ByteArrayOutputStream();
                    stopCapture = false;
                    try {// Loop until stopCapture is set by
                        // another thread that services the Stop
                        // button.
                        while (!stopCapture) {
                            // Read data from the internal buffer of
                            // the data line.

                            int cnt = microphone.read(tempBuffer, 0, tempBuffer.length);
                            if (cnt > 0) {
                                // Save data in output stream object.
                                //byteArrayOutputStream.write(tempBuffer, 0, cnt);
                                callback.onMicSpeech(tempBuffer);

                            } // end if
                        } // end while
                        System.out.println("Stop record!!");
                        microphone.stop();
                        microphone.close();


                        //byteArrayOutputStream.close();
                    } catch (Exception e) {
                        callback.onMicError(e.getMessage());
                    } // end catch

                } catch (Exception e) {
                    callback.onMicError(e.getMessage());
                } // end catch


            } while (!stopCapture);
            callback.onMicStop();
            System.out.println("Exit record thread");
        });
        rec_thread.start();

    }

}