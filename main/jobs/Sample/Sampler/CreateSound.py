from cmath import sin
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
from Sampler import *
from SamplerEffect import *

# sampling information
sr = 44100 # sample rate
freq = 20
lenght =1.0
t = np.arange(0,lenght,1.0/sr)
x = np.pi * 2 *freq * t

signalNoise = soundOcsNoise(lenght=lenght,sr=sr,case=2)
writeSample(sr=sr,signal=signalNoise,path="signalNoise.wav")

Osc = np.zeros(shape=44100)
Osc2 = np.where(Osc == 0,1,1)



signalFilter = soundFilterApply(Osc=Osc2,sr=sr,cutoff=150.00,filterType = "lowpass")
writeSample(sr=sr,signal=signalFilter,path="signalFilter.wav")




#A mettre dans un nouveau fichier "SamplerGetParameters"
def findEnvelopParameters(time_duration):
    print('TO DO')

