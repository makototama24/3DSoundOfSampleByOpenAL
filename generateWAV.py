import numpy as np
import wave
import struct

sec = 1
note_hz = 440
sample_hz = 44100
t = np.arange(0, sample_hz * sec)
wv = np.sin(2 * np.pi * note_hz * t / sample_hz)

max_num = 32767.0 / max(wv)
wv16 = [int(x * max_num) for x in wv]
bi_wv = struct.pack("h" * len(wv16), *wv16)

file = wave.open('Music/wav_Sound/create.wav', mode='wb')
param = (1, 2, sample_hz, len(bi_wv), 'NONE', 'not compressed')
file.setparams(param)
file.writeframes(bi_wv)
file.close()