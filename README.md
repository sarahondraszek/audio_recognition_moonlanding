
# Simple Audio Recognition of Speech Commands for Moonlanding Game

Im Rahmen des Projektseminar-Moduls des Studiengangs Computerlinguistik an der Universität Trier haben wir uns ein Semester lang mit der Programmierung einer per Sprachsteuerung spielbaren Variante des Moonlanding-Spieles beschäftigt. Ziel des Spiels ist es hierbei, eine Rakete sicher auf der Mondoberfläche landen zu lassen.

## Requirements
Python 3.8
### Verwendete Bibliotheken:
* keras 2.4.3
* librosa 0.8.0
* numpy 1.19.5
* pandas 1.4.2
* pyAutoGui 0.9.52
* pydub 0.25.1
* pygame 2.0.1
* pyYAML 5.4.1
* sklearn 0.0
* sounddevice 0.4.1
* tensorflow 2.5.0
* tqdm 4.61.0

Die Dokumentation kann [hier](https://github.com/sarahondraszek/audio_recognition_moonlanding/tree/master/_Anderes/schriftliche_Ausarbeitungen/Dokumentation.pdf) eingesehen werden.

## How-to train (your drago-... model?)
Das Sprachmodell für die Spracherkennung wird über die sequentielle Ausführung verschiedener Skripte vollzogen. Zunächst müssen aus den WAVE-Dateien numpy-Arrays via ```create_arrays.py``` erstellt werden. Daraufhin kann mit ```run_train.py``` das Modell dann trainiert und abgespeichert werden. Gegebenenfalls muss für die Ausführung dieser Skripte das Projekt zur Systemvariable hinzugefügt werden, damit die Packages richtig erkannt werden.

## How-to play
Das Spiel wird durch Ausführen der ```MAIN.py``` gestartet.
Weitere Informationen zu den Spielregeln können dem [Benutzerhandbuch](https://github.com/sarahondraszek/audio_recognition_moonlanding/tree/master/_Anderes/schriftliche_Ausarbeitungen/Benutzerhandbuch.pdf) entnommen werden.

## Mitwirkende

Dennis Binz, Nathalie Elsässer, Julia Karst, Sarah Ondraszek, Till Preidt

Mit freundlicher Unterstützung von: Kai Kugler, Sven Naumann
