import keyboard
import sounddevice
from scipy.io.wavfile import write, read

"""wave-file parameters"""
sample_rate = 44100
duration = 5
frames = sample_rate * duration
path = './/input//audio//recorded_order.wav'

"""Possible variable connection to game parameters / status"""
game = 1

while game:
    if keyboard.is_pressed("space") and game == 1:

        """Recording with specified parameters"""

        print('°')
        record = sounddevice.rec(frames, sample_rate, channels=2)
        sounddevice.wait()  # wait for exit recording
        write(path, sample_rate, record)

        """Extracting amplitudinal data from audio signal"""

        file = path
        sample_rate, signal_data = read(file)
        amplitudes = signal_data[:3 * sample_rate]  # cutting wave file to needed duration (if necessary)
        # print(sample_rate)
        print(amplitudes)


