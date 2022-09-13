from configparser import ConfigParser
from logging import config
import wave

import pygame
import configparser
import librosa
from librosa import display
import matplotlib.pyplot as plt


fileConfig = ConfigParser()
fileConfig.read('dev.application.conf')

pygame.init()
pygame.display.set_caption("tes pygame")


def analyser(conf,instruName):
   

    pathSample = conf.get('InstrumentPath',instruName) + "\RimRag.wav"
    print(pathSample)

#pygame package test
    window_resolution = (640,480)
    window_surface = pygame.display.set_mode(window_resolution)
    song = pygame.mixer.Sound(pathSample)
    song.play(loops=10) 
    
    pygame.display.flip()
    launched = True
    while launched:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                launched = False

#librosa package test
    x , sr = librosa.load(pathSample, sr=44100)
    print(type(x), type(sr))


    plt.figure(figsize=(14, 5))

    chromagram = librosa.feature.chroma_stft(x, sr=sr, hop_length=hop_length)
    plt.figure(figsize=(15, 5))
    librosa.display.specshow(chromagram, x_axis='time', y_axis='chroma', hop_length='hop_length', cmap='coolwarm')





# Appel Fonction pour test
analyser(fileConfig,'rim')




