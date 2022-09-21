import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# sampling information
sr = 44100 # sample rate
freq = 200
lenght =1.0

t = np.arange(0,lenght,1.0/sr)
signal = np.sin(np.pi * 2 *freq * t)
N = sr*t # total points in signal

plt.plot(t,signal)
plt.show()

signal*= 32767
signal = np.int16(signal)
wavfile.write("file.wav",sr,signal)
