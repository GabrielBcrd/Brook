import numpy as np
from scipy.io import wavfile
from numpy import where

def normalizeSound(data):
    min_v = min(data)
    max_v = max(data)
    offset = min_v + max_v
    data = data+(offset/2)
    data = np.array ([((x-min_v) / (max_v - min_v)) for x in data])*2.0-1
    return data * ((max_v/min_v)*-1)

def soundOcsNoise(lenght,sr,case):
    print("NOISE")
    match case:
        case 1:
            signal = normalizeSound(np.random.random(int(lenght*sr))*2.0-1.0) #Random Noise
        case 2:
            signal = normalizeSound(np.random.randn(int(lenght*sr))) #Normal Noise
        case _:
            signal = normalizeSound(np.random.randn(int(lenght*sr)))*0 #Normal Noise *0
            print("thing is not 1 or 2, There is no Noise")
    return signal 

def soundOcsSub(x,case):
    print("SUB")
    match case:
        case 'sin':
            signal = np.sin(x)
        case 'triangle':
            signal = np.abs((x/np.pi-2.5)%2-1)*2-1
        case 'square':
            signal = np.where(x/np.pi % 2 > 1, -1,1)
        case 'sawtooth':
            signal = -((x/np.pi)%2)+1
        case _:
            signal = np.sin(x)*0
            print("no sub")
    return signal 

def soundOcs():
    print("OSC")


def soundEnvelopApply(Osc,attack,hold,decay,substain,release):
    print("ENV")
    print(Osc)
    attackApply = Osc #en sec ou ms
    return attackApply
    


def soundLFO ():
    print("LFO")

def soundFilter():
    print("FILTER")

def writeSample(sr,signal,path):
    signal*= 32767
    signal = np.int16(signal)
    wavfile.write(path,sr,signal)

