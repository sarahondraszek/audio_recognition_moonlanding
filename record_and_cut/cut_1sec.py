from pydub import AudioSegment, silence, effects

'''  
'segment' cuts the loudest, 1-second-long part
out of an audio file with unknown length
file path gets passed as an argument
'''


def segment(file):
    raw = AudioSegment.from_file(file, format="wav")  # read raw wave-file
    normalized_sound = effects.normalize(raw)  # normalize raw file
    nonsilent_parts = silence.detect_nonsilent(normalized_sound, silence_thresh=-65)  # save array of all nonsilent parts of file
    nonsilent_start = 0
    nonsilent_end = 999
    dB = -1000
    for i in nonsilent_parts:
        split = normalized_sound[i[0]:i[1]]
        loudness = split.dBFS
        if loudness > dB:  # find loudest one of the nonsilent parts
            dB = loudness
            nonsilent_start = i[0]
            nonsilent_end = i[1]
    if nonsilent_end-nonsilent_start > 999:  # if loudest nonsilent part is longer than 1s, cut it short
        a = silence.detect_leading_silence(normalized_sound, silence_threshold=-40)  # increase silence threshold
        b = a+999
        normalized_sound[a:b].export(file, format="wav")
    else:  # increase length of audio clip for better accuracy
        len_of_additional_audio = (1000-(nonsilent_end-nonsilent_start))/2
        start_of_audio = nonsilent_start-len_of_additional_audio
        end_of_audio = nonsilent_end + len_of_additional_audio
        if start_of_audio < 0:
            start_of_audio = 0
            end_of_audio = 999
        normalized_sound[start_of_audio:end_of_audio].export(file, format="wav")

