from configparser import ConfigParser
from logging import config
import wave

import pygame



fileConfig = ConfigParser()
fileConfig.read('dev.application.conf')

pygame.init()
pygame.display.set_caption("tes pygame")


def analyser(conf,instruName):
   

    pathSample = conf.get('InstrumentPath',instruName) + ""
    print(pathSample)

#pygame package test
    """  window_resolution = (640,480)
    window_surface = pygame.display.set_mode(window_resolution)
    song = pygame.mixer.Sound(pathSample)
    song.play(loops=10) 
    
    pygame.display.flip()
    launched = True
    while launched:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                launched = False
    """
#librosa package test

    import pandas as pd 
    import numpy as np
    import matplotlib.pylab as plt
    import seaborn as sns 
    from glob import glob
    import librosa 
    import librosa.display
    import IPython.display as ipd


    audio_files = glob(pathSample + '\*.wav')
  
    ipd.Audio(audio_files[0])

    y, sr = librosa.load(audio_files[0])
    print(y)
    print(sr)

    y_trimmed, _ = librosa.effects.trim(y,top_db=10)

    pd.Series(y).plot(figsize=(10,5),
                      lw = 1,
                      title = "yo")

    plt.show()


# Appel Fonction pour test
analyser(fileConfig,'rim')

