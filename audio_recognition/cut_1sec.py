from pydub import AudioSegment
import os

'''  'segment' cuts the loudest, 1-second-long part
out of an audio file with unknown length
file path gets passed as an argument
'''


def segment(file):
    sound = AudioSegment.from_file(file, format="wav")  # read wave-file
    # print(len(sound))
    output = file
    i = 0  # start window at 0 ms
    j = 999  # end window at 999 ms
    k = 0
    m = 999
    dB = -1000  # set loudness -1000dB
    while len(sound) >= j:  # window of 1 sec runs over whole audio
        zwischenspeicher = ".//zwischen.wav"
        split = sound[i:j]  # split sound in parts of 1 sec
        split.export(zwischenspeicher, format="wav")  # export the new wave-file
        part = AudioSegment.from_file(zwischenspeicher, format="wav")
        loudness = part.dBFS  # calculate loudness of current part
        if loudness > dB:  # if the new segment is louder than the last-loudest segment, replace with new segment
            dB = loudness
            # print("\nNeuer maximaler Wert ist: ")
            # print(dB)
            k = i
            m = j  # save time stamp of loudest section
        i += 10  # shift window 10ms
        j += 10
    sound[k:m].export(output, format="wav")  # replace output with loudest segment
    os.remove(".//zwischen.wav")  # remove unnecessary file

# input = './/input//audio//test.wav'
# segment(input)