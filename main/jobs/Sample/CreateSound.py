import numpy as np
import matplotlib.pyplot as plt
from Sampler import *

# sampling information
sr = 44100 # sample rate
freq = 20
lenght =1.0
t = np.arange(0,lenght,1.0/sr)
x = np.pi * 2 *freq * t

signalNoise = soundOcsNoise(lenght=lenght,sr=sr,case=2)
signalSub = soundOcsSub(x=x,case='square')

plt.plot(t,signalNoise)
plt.show()
plt.plot(t,signalSub)
plt.show()

writeSample(sr=sr,signal=signalNoise,path="signalNoise.wav")
writeSample(sr=sr,signal=signalSub,path="signalSub.wav")

#,attack=0.23,hold=0.56,decay=0.75,substain=-20,release=1
signalEnvelop = soundEnvelopApply(signalSub,sr,t,attack = 0.10,hold=0.30,decay=0.53,substain=0.00,release=0.83)

plt.plot(t,signalEnvelop)
plt.show()

c = np.pi
print(c) 

#A mettre dans un nouveau fichier "SamplerGetParameters"
def findEnvelopParameters(time_duration):
    print('TO DO')

   