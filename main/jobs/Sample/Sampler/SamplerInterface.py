from re import sub
from turtle import Screen
import numpy as np
import pygame
import pygame_widgets 

# sampling information
from Sampler import *
from CreatePiano import *
from pygame import mixer
from CreateFilterInterface import Filter

from CreateOscNoiseInterface import OcsNoise
from CreateEnvInterface import Envelop
from CreateOscSubInterface import Sub

#-----------------variables------------------
sr = 44100 # sample rate
freq = 1
lenght =1.0
t = np.arange(0,lenght,1.0/sr)
x = np.pi * 2 *freq * t
data = 20


#------------------init pygame -------------------------------

pygame.init()

white_notes,black_notes = transform_notes_to_list(nbOctave=8)
width = len(white_notes) * len(black_notes)
height = 900
screen=pygame.display.set_mode([width,height])

#----------------Noise -------------------------------
signalOcs = OcsNoise(screen=screen,x=0,y=0)
signalOcs.draw_OscNoiseParameters(screen=screen)
signalOcs.draw_ocs_noise()


#----------------Envelop -------------------------------
env = Envelop(screen=screen,x=0,y=300)
env.draw_envelopParameters()

#---------------Sub -----------------------------------
signalOcsSub = Sub(screen=screen,x=300,y=0)
signalOcsSub.draw_OscSubParameters()
signalOcsSub.draw_ocs_sub()

#------------------Filter -----------------------------
filter = Filter(screen=screen,x=950,y=300)
filter.draw_filter_parameters()


#------------------ Piano keys ------------------------------
active_whites = []
active_blacks = []
white_keys, black_keys, active_whites, active_blacks = draw_piano(active_whites, active_blacks,
                                                                screen=screen,width=width,height=height,
                                                                white_notes=white_notes, black_notes=black_notes,
                                                                nb_float_black = 23
                                                             ) 
"""#------------------- Submit TextBox (to play the song)
def outputTxt():
    #Unload the last song :)
    mixer.music.unload()
    # Get text in the textbox
    freq = int(textboxFrequency.getText())
    #Loading the song.
    lenght =1.0
    signal = soundOcsSub(sr=sr,lenght=lenght, freq=freq,case=dropdownTypeOsc.getSelected())
    writeSample(sr=44100,signal = signal, path = 'signalSub.wav')
    signal = soundEnvelopApply(signal,sr=sr,t=t,
                                attack=Attack.getValue(),
                                hold=Hold.getValue(),
                                decay=Decay.getValue(),
                                substain=Substain.getValue(),
                                release=Release.getValue())
mixer.music.load("signalSub.wav")
#Setting the volume.
mixer.music.set_volume(sliderMixerVolume.getValue())
#Start playing the song.
mixer.music.play()



textboxFrequency = TextBox(screen, 1300, 500, 400, 80, fontSize=50,
                    borderColour=(255, 0, 0), textColour=(0, 200, 0),
                    onSubmit=outputTxt, radius=10, borderThickness=5) """


#---------------- Events (while run) ---------------

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()
            
        signalOcsSub.getArguments_Sub()
        signalOcsSub.draw_ocs_sub()
        signalOcsSub.draw_SubBackground()

        env.getArguments_Envelop()
        env.draw_env()
        env.draw_EnvBackground()

        filter.getArguments_filter()
        filter.draw_filter()
        filter.draw_SubBackground()

        typeOcsNoise = signalOcs.getArguments_OscNoise()
        signalOcs.draw_OscNoiseBackground()


        pygame.draw.rect(screen,"white",(1250,0,500,500),0)
        


        pygame_widgets.update(events)
        pygame.display.update()