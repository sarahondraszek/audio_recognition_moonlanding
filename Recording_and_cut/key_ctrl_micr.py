import keyboard
import sounddevice
from scipy.io.wavfile import write, read
from cut_1sec import segment as s

"""wave-file parameters"""
sample_rate = 16000
duration = 3
frames = sample_rate * duration
path = './/recorded_order.wav'

"""Possible variable connection to game parameters / status"""
game = 1

while game:
    if keyboard.is_pressed("space") and game == 1:

        """Recording with specified parameters"""

        print('°')
        record = sounddevice.rec(frames, sample_rate, channels=1)
        sounddevice.wait()  # wait for exit recording
        write(path, sample_rate, record)

        s(path)

        """Extracting amplitudinal data from audio signal"""
        """
        file = path
        sample_rate, signal_data = read(file)
        amplitudes = signal_data[:3 * sample_rate]  # cutting wave file to needed duration (if necessary)
        # print(sample_rate)
        print(amplitudes)
        """

