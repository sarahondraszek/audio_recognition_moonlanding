from pydub import AudioSegment

def segment(file):
    sound = AudioSegment.from_file(file, format="wav")
    # print(len(sound))
    i = 0
    j = 999
    dB = -1000
    while len(sound) >= j:
        zwischenspeicher = ".//input//audio//zwischen.wav"
        output = ".//input//audio//max.wav"
        split = sound[i:j]
        split.export(zwischenspeicher, format="wav")
        part = AudioSegment.from_file(zwischenspeicher, format="wav")
        loudness = part.dBFS
        if loudness > dB:
            dB = loudness
            # print("\nNeuer maximaler Wert ist: ")
            # print(dB)
            split.export(output, format="wav")
        i += 23
        j += 23


input = './/input//audio//test.wav'
segment(input)