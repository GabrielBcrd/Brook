from configparser import ConfigParser
from logging import config
from sqlite3 import TimeFromTicks
from time import time_ns
from timeit import timeit
import wave
from xmlrpc.client import DateTime

import pygame
import pandas as pd 
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns 
from glob import glob
import librosa 
import librosa.display
import IPython.display as ipd

from datetime import datetime, time
import time
from datetime import datetime, date, time, timedelta

fileConfig = ConfigParser()
fileConfig.read('dev.application.conf')

def AnalyserDbMax(SampleArray):
    MaxDb = max(abs(SampleArray))
    return MaxDb

def analyser(conf,instruName):
   
    
    pathSample = conf.get('InstrumentPath',instruName) + ""
    audio_files = glob(pathSample + '\*.wav')

    y, sr = librosa.load(audio_files[0])
    print(AnalyserDbMax(y))
    
    a = ((librosa.get_duration(y=y, sr=sr)))
    print((a))
    
    #Séparation des sources harmoniques-percussives¶
    y_harmonic, y_percussive = librosa.effects.hpss(y)

    pd.Series(y_percussive).plot(figsize=(10,5),
                      lw = 1,
                      title = "yoyo")


    pd.Series(y_harmonic).plot(figsize=(10,5),
                      lw = 1,
                      title = "yoyo")

    plt.show()

    librosa.feature.melspectrogram(y=y, sr=sr)

    D = np.abs(librosa.stft(y))
    S = librosa.feature.melspectrogram(S=D)
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128,fmax=8000)
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(librosa.power_to_db(S,ref=np.max),y_axis='mel', fmax=8000,x_axis='time')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel spectrogram')
    plt.tight_layout()
    plt.show()


    pitches, magnitudes = librosa.piptrack(y=y, sr=sr, threshold=0.2)
    print(pitches)
    print('///')
    print(magnitudes)
    plt.subplot(212)
    plt.plot(pitches)
    plt.show()
    plt.plot(magnitudes)
    plt.show()
    plt.imshow(pitches[:100, :], aspect="auto", interpolation="nearest")
    plt.show()

# Appel Fonction pour test
analyser(fileConfig,'rim')