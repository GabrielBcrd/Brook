import wave
import numpy as np
#Open the files.
import librosa
import matplotlib.pyplot as plt
from Sampler import *

sr = 44100 # sample rate
freq = 20
shift = 300//freq # shifting 100 Hz
    
lenght =1.0
t = np.arange(0,lenght,1.0/sr)


signalOcs = wave.open('signalSub.wav', 'r')
# Set the parameters for the output file.
par = list(signalOcs.getparams())
par[3] = 0  # The number of samples will be set by writeframes.
par = tuple(par)
print(par)

signalOutput = wave.open('pitch1.wav', 'w')
signalOutput.setparams(par)

#The sound should be processed in small fractions of a second. This cuts down on reverb. Try setting fr to 1; you'll hear annoying echos.

sz = sr  # Read and process 1/fr second at a time.
print (sz)
# A larger number for fr means less reverb.
c = int(signalOcs.getnframes()/sz)  # count of the whole file
print(c)
#Read the data.
da = np.fromstring(signalOcs.readframes(sz), dtype=np.int16)
print(da)

for num in range(c):
#Extract the frequencies using the Fast Fourier Transform built into numpy.
    FastFourierFrequency = np.fft.rfft(da)
#Roll the array to increase the pitch.
    FastFourierFrequencyPitch = np.roll(FastFourierFrequency,shift)
    
#The highest frequencies roll over to the lowest ones. That's not what we want, so zero them.
    FastFourierFrequencyPitch[0:shift] = 0

#Now use the inverse Fourier transform to convert the signal back into amplitude.
    signalOutputTmp = np.fft.irfft(FastFourierFrequencyPitch)
    signalOuput = signalOutputTmp.ravel().astype(np.int16)
    plt.plot(t,(signalOuput))
    plt.show()
#Write the output data.
    signalOutput.writeframes(signalOuput.tobytes())
    print(signalOutputTmp)
signalOcs.close()
signalOutput.close()









