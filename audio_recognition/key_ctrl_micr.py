import keyboard
import sounddevice
from scipy.io.wavfile import write, read
from audio_recognition.cut_1sec import segment as s
from preprocessing_and_training.predict import make_single_prediction
import keras


def control_mic(game):
    """wave-file parameters"""
    sample_rate = 16000
    duration = 3
    frames = sample_rate * duration
    path = './/recorded_order.wav'
    model = keras.models.load_model('./model')
    print("Bitte die Leertaste drücken, um die Aufzeichnung zu starten.")
    while game:
        if keyboard.is_pressed("space") and game == 1:

            """Recording with specified parameters"""
            print("Aufzeichnung beginnt.")
            record = sounddevice.rec(frames, sample_rate, channels=1)
            sounddevice.wait()  # wait for exit recording
            write(path, sample_rate, record)
            print("Aufzeichnung beendet.")
            s(path)
            print("Zuschneiden beendet.")
            a = make_single_prediction(path, model)
            print("Ergebnis der Prediction: ")
            print(a)

