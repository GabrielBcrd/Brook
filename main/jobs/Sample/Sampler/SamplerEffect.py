import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import math
import librosa
import pyaudio
import matplotlib.pyplot as plt

def soundFilterApply(Osc,sr,t,cutoff,filterType):
    print("FILTER")

    b, a = signal.butter(4, cutoff, filterType, analog=True)
    w, h = signal.freqs(b, a)
     #Response of filter
    plt.semilogx(w, 20 * np.log10(abs(h)))
    plt.title('filter frequency response')
    plt.xlabel('Frequency [radians / second]')
    plt.ylabel('Amplitude [dB]')
    plt.margins(0, 0.1)
    plt.grid(which='both', axis='both')
    plt.axvline(cutoff, color='green') # cutoff frequency
    plt.show()

    sig = Osc * 1/sr
    t = t
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    ax1.plot(t, sig)
    ax1.set_title('SignalBefore')


    #btype{‘lowpass’, ‘highpass’, ‘bandpass’, ‘bandstop’}, optional The type of filter. Default is ‘lowpass’.
    sos = signal.butter(4, cutoff, filterType, fs=sr, output='sos')
    filtered = signal.sosfilt(sos, sig)
    ax2.plot(t, filtered)
    ax2.set_title('After filter')
    ax2.set_xlabel('Time [seconds]')
    plt.tight_layout()
    plt.show()
    return filtered

def soundPitchApply(signal,sr):
    
    y = signal * 1/sr# y is a numpy array of the wav file, sr = sample rate
    y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=7) # shifted by 4 half steps
    return y_shifted

def distortionApply():
    print("distortion")

def delayApply():
    print("ddelay")

def ReverbApply():
        print("reveerb")