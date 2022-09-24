from asyncore import write
import numpy as np
import matplotlib.pyplot as plt
from Sampler import *
import IPython.display as ipd
import librosa 
import librosa.display
import scipy as sci
from pydub import AudioSegment
from pydub.playback import play
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv

# sampling information
sr = 44100 # sample rate
freq = 20
lenght =1.0
t = np.arange(0,lenght,1.0/sr)
x = np.pi * 2 *freq * t

signalNoise = soundOcsNoise(lenght=lenght,sr=sr,case=2)
signalSub = soundOcsSub(x=x,case='triangle')*1/sr
signalSub2 = soundOcsSub(x=x,case='triangle')

#plt.plot(t,signalNoise)
#plt.show()
#plt.plot(t,signalSub)
#plt.show()

writeSample(sr=sr,signal=signalNoise,path="signalNoise.wav")
writeSample(sr=sr,signal=signalSub2,path="signalSub2.wav")

#,attack=0.23,hold=0.56,decay=0.75,substain=-20,release=1
signalEnvelop = soundEnvelopApply(signalSub,sr,t,attack = 0.30,hold=0.50,decay=0.80,substain=0.15,release=0.90)

"""D = np.abs(librosa.stft(signalSub2))**2 #Utiliser un spectre d'énergie (magnitude) au lieu d'un spectrogramme de puissance
S = librosa.feature.melspectrogram(S=D, sr=sr, n_mels=128,fmax=50000)
fig, ax = plt.subplots(figsize=(15,5))
S_dB = librosa.power_to_db(S, ref=np.max)
G = librosa.fft_frequencies(sr=22050, n_fft=16)

D = np.abs(librosa.stft(signalSub2))**2
 
X1 = np.abs(D[..., f, t]) #is the magnitude of frequency bin f at frame t, and

X2 = np.angle(D[..., f, t]) #is the phase of frequency bin f at frame t.    

print(X1)    
print(X2)       
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(signalSub2, t, D)
plt.xlabel('x')
plt.ylabel('y')
plt.show()"""
                                 
                                   
                                   
                                   
#signalFilter = soundFilter(signalSub2,sr,t,cutoff=10000,res=1000,drive=10)
writeSample(sr=sr,signal=signalEnvelop,path="signal.wav")


#plt.plot(t,signalEnvelop)
#plt.show()

#A mettre dans un nouveau fichier "SamplerGetParameters"
def findEnvelopParameters(time_duration):
    print('TO DO')

   