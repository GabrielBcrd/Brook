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

signalEnvelop = soundEnvelopApply(Osc2,sr,t=t,attack = 0.30,hold=0.50,decay=0.80,substain=0.15,release=0.90)
writeSample(sr=sr,signal=signalEnvelop,path="signalEnvelop.wav")


signalFilter = soundFilterApply(Osc=signalEnvelop,sr=sr,t=t,cutoff=150.00,filterType = "lowpass")
writeSample(sr=sr,signal=signalFilter,path="signalFilter.wav")

plt.plot(t,signalEnvelop)
plt.show()


#A mettre dans un nouveau fichier "SamplerGetParameters"
def findEnvelopParameters(time_duration):
    print('TO DO')

