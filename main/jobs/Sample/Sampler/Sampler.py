from multiprocessing.dummy import Array
from platform import release
import numpy as np
from scipy.io import wavfile
import wave as wave
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

def soundOcsSub(sr,lenght,freq,case):
    t = np.arange(0,lenght,1.0/sr)
    x = np.pi * 2 *freq * t
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

#,attack,hold,decay,substain,release
def soundEnvelopApply(Osc,sr,attack:float, hold:float,decay:float,substain:float,release:float):

    t_attack = np.arange(0,attack,1.00/sr)
    begin_to_attack = Osc[np.arange(0,len(t_attack),1)]
    
    t_hold = np.arange(attack,hold,1.00/sr)
    attack_to_hold = Osc[np.arange(len(t_attack),
                                    len(t_attack)+len(t_hold),1)]

    t_decay = np.arange(hold,decay,1.00/sr)
    hold_to_decay = Osc[np.arange(len(t_attack)+len(t_hold), 
                                        len(t_decay)+ len(t_hold)+len(t_attack),1)]


    t_release = np.arange(decay,release,1.00/sr)
    decay_to_release = Osc[np.arange(len(t_attack)+len(t_hold)+len(t_decay), 
                                    len(t_release)+len(t_decay)+ len(t_hold)+len(t_attack),1)]

    release_to_end = Osc[np.arange(len(t_attack)+len(t_hold)+len(t_decay)+len(t_release), 
                                    len(Osc),1)]


    envelopNumMatrix = np.concatenate((np.arange(0,1,1/len(begin_to_attack)),
                                            attack_to_hold,
                                            np.arange(1,substain,-(1-substain)/(len(t_decay))),
                                            np.arange(substain,0,-(substain)/(len(t_release))),
                                            release_to_end*0))

    return envelopNumMatrix



def writeSample(sr,signal,path):
    signal*= 32767
    signal = np.int16(signal)
    wav_file = wave.open(path,'w')
    wav_file.setnchannels(1)
    wav_file.setsampwidth(1)
    wav_file.setframerate(sr)
    wav_file.writeframesraw(signal)
    wav_file.close
    #wavfile.write(path,sr,signal)

