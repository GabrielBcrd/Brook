import numpy as np
import matplotlib.pyplot as plt
from main.jobs.Sample.Sampler import writeSample, soundOcsNoise, soundOcsSub

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
""" signalEnvelop = soundEnvelopApply(signalSub)
plt.plot(t,signalEnvelop)
plt.show() """

#A mettre dans un nouveau fichier "SamplerGetParameters"
def findEnvelopParameters(time_duration):
    print('TO DO')