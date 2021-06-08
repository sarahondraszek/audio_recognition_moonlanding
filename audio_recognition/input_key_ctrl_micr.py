from pynput.keyboard import Key, Controller
import keyboard
import sounddevice
from scipy.io.wavfile import write
from audio_recognition.cut_1sec import segment as s
from preprocessing_and_training.predict import make_single_prediction as msp

kb = Controller()

"""wave-file parameters"""
sample_rate = 16000
duration = 3
frames = sample_rate * duration
path = './recorded_order.wav'

"""Possible variable connection to game parameters / status"""
"""
game = 1

while game:
    if keyboard.is_pressed("space") and game == 1:

        Recording with specified parameters

        print('°')
        record = sounddevice.rec(frames, sample_rate, channels=1)
        sounddevice.wait()  # wait for exit recording
        write(path, sample_rate, record)

        Cutting recorded wav to 1s, depending on volume level

        # amplitudes = signal_data[:1 * sample_rate]
        s(path)
        nn_model = keras.models.load_model('./preprocessing_and_training/model')
        print(msp(path, nn_model))
"""


def record_order():

    """Recording with specified parameters"""

    print('°')
    record = sounddevice.rec(frames, sample_rate, channels=1)
    sounddevice.wait()  # wait for exit recording
    write(path, sample_rate, record)

    """Cutting recorded wav to 1s, depending on volume level"""

    # amplitudes = signal_data[:1 * sample_rate]
    s(path)
    nn_model = gm()
    order = msp(path, nn_model)
    print(order)
    return order


def simulate_key_press(key):
    if key == "right":
        kb.press(Key.right)
    if key == "left":
        kb.press(Key.left)
    if key == "up":
        kb.press(Key.up)
    if key == "down":
        kb.press(Key.down)
    if key == "escape":
        kb.press(Key.esc)
    if key == "r":
        kb.press("r")


def release_key(key):
    if key == "right":
        kb.release(Key.right)
    if key == "left":
        kb.release(Key.left)
    if key == "up":
        kb.release(Key.up)
    if key == "down":
        kb.release(Key.down)
    if key == "escape":
        kb.release(Key.esc)
    if key == "r":
        kb.release("r")


simulate_key_press("escape")


