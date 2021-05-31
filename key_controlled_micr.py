import pyaudio
import wave
import keyboard

"""Variables for wave-file specification"""
audio = pyaudio.PyAudio()
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RESOLUTION = 1024
RECORD_SECONDS = 1
# Path
WAVE_OUTPUT_FILENAME = ".//input//audio//recorded_order.wav"


"""Possible variable connection to game parameters / status"""
game = 1

while game:
    if keyboard.is_pressed("space") and game == 1:

        """start Recording"""

        print("recording...")
        stream = audio.open(format=pyaudio.paInt16, channels=2,
                            rate=44100, input=True,
                            frames_per_buffer=1024)
        
        # creating array of single frames with specified resolution in specified time period
        frames = []

        for i in range(0, int(RATE / RESOLUTION * RECORD_SECONDS)):
            data = stream.read(RESOLUTION)
            frames.append(data)
        print("finished recording")

        """stop Recording"""

        stream.stop_stream()
        stream.close()
        audio.terminate()

        """extracting wave file"""

        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
        break









