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

fileConfig = ConfigParser()
fileConfig.read('dev.application.conf')

def AnalyserDbMax(SampleArray):
    MaxDb = max(abs(SampleArray))
    return MaxDb

def analyser(conf,instruName):
   
    Fs = 44100 # sample rate
    
    pathSample = conf.get('InstrumentPath',instruName) + ""
    audio_files = glob(pathSample + '\*.wav')

    y, sr = librosa.load(audio_files[1])
    print(AnalyserDbMax(y))
    
    a = ((librosa.get_duration(y=y, sr=Fs)))
    print((a))
    
    #Séparation des sources harmoniques-percussives¶
    y_harmonic, y_percussive = librosa.effects.hpss(y)

    #Amplitude / Time
    pd.Series(y_percussive).plot(figsize=(10,5),
                      lw = 1,
                      title = "yoyo")
    pd.Series(y_harmonic).plot(figsize=(10,5),
                      lw = 1,
                      title = "yoyo")
                      
    plt.ylabel('Amplitude')
    plt.xlabel('Time [Sec]')
    plt.show()


    #Mel Spectrogram -- Amplitude    / Frequency / Time
    D = np.abs(librosa.stft(y))**2 #Utiliser un spectre d'énergie (magnitude) au lieu d'un spectrogramme de puissance
    S = librosa.feature.melspectrogram(S=D, sr=Fs, n_mels=128,
                                        fmax=50000)
    plt.show()
    # Passing through arguments to the Mel filters
    fig, ax = plt.subplots(figsize=(15,5))
    S_dB = librosa.power_to_db(S, ref=np.max)
    
    img = librosa.display.specshow(S_dB, x_axis='time',
                                y_axis='mel', sr=Fs,
                                fmax=50000, ax=ax)
    fig.colorbar(img, ax=ax, format='%+2.0f dB')
    ax.set(title='Mel-frequency spectrogram')
    plt.show()

    print(pathSample)
    print(S)
    
    

    

    import csv

    print("Un programme qui utilise csv.writer() pour écrire dans un fichier")
    print("\n")
    # Les données que nous allons écrire
    dataDb = S_dB
    dataAmp = D
    # Ouvrir le fichier en mode écriture
    fichier = open(conf.get('DSADataPath',instruName),'w')
    print("Nous avons ouvert le fichier" +instruName+ ", s'il n'existe pas il sera créé ")
    # Créer l'objet fichier
    obj = csv.writer(fichier)
    # Chaque élément de data correspond à une ligne
    for element in dataDb, dataAmp:
        obj.writerow(element)
    fichier.close()



# Appel Fonction pour test
analyser(fileConfig,'closedHiHat')
analyser(fileConfig,'rim')