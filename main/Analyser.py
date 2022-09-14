from configparser import ConfigParser
from logging import config
import wave

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

def AnalyserRowNumDbMax(SampleArray):
    a = pd.DataFrame(SampleArray)
    RowNumMaxDb = a[a['0']==AnalyserDbMax(SampleArray)].index
    return RowNumMaxDb
    
    
def analyser(conf,instruName):
   
    
    pathSample = conf.get('InstrumentPath',instruName) + ""
    print(pathSample)

    audio_files = glob(pathSample + '\*.wav')
    print (audio_files)
    #ipd.Audio(audio_files[0])

    y, sr = librosa.load(audio_files[12])
    print(AnalyserDbMax(y))
    #print(AnalyserRowNumDbMax(y))
    #print(sr)
    print(librosa.get_duration(y=y, sr=sr))
    df=pd.DataFrame(y)
    a = AnalyserDbMax(y)
    #print(df)
    #print(a)
    #print(df.loc[df['0']==a])
    
    
    
    
    y_trimmed, _ = librosa.effects.trim(y,top_db=15)

    pd.Series(y_trimmed).plot(figsize=(10,5),
                      lw = 1,
                      title = "yoyo")

    #plt.show()
    
    


# Appel Fonction pour test
analyser(fileConfig,'rim')

