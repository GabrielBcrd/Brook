from re import sub
from turtle import Screen
import numpy as np
import pygame
import pygame_widgets 

# sampling information
from Sampler import *
from CreatePiano import *
from CreateOscNoise import draw_ocs_noise
from CreateOcs import draw_ocs
from CreateEnvInterface import *
from CreateOscSub import *
from pygame import mixer



#-----------------variables------------------
sr = 44100 # sample rate
freq = 1
lenght =1.0
t = np.arange(0,lenght,1.0/sr)
x = np.pi * 2 *freq * t



#------------------init pygame -------------------------------
pygame.init()
mixer.init()

white_notes,black_notes = transform_notes_to_list(nbOctave=8)
width = len(white_notes) * len(black_notes)
height = 900
screen=pygame.display.set_mode([width,height])

#------------------Osc Sub parameters ------------------------
sliderMixerVolume,outputMixerVolume,dropdownTypeOsc = draw_OscSubParameters(screen)

Attack,outputAttack,Hold,outputHold,Decay,outputDecay,Substain,outputSubstain,Release,outputRelease = draw_envelopParameters(screen)

#------------------ Piano

active_whites = []
active_blacks = []

white_keys, black_keys, active_whites, active_blacks = draw_piano(active_whites, active_blacks,
                                                                screen=screen,width=width,height=height,
                                                                white_notes=white_notes, black_notes=black_notes,
                                                                nb_float_black = 23
                                                                ) 

#------------------- Submit TextBox (to play the song)
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
    
    
    

textboxFrequency = TextBox(screen, 700, 100, 800, 80, fontSize=50,
                  borderColour=(255, 0, 0), textColour=(0, 200, 0),
                  onSubmit=outputTxt, radius=10, borderThickness=5)


#---------------- Events (while run) ---------------


run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    outputMixerVolume.setText(sliderMixerVolume.getValue())


    
    #draw_ocs_noise(sr=sr, freq=freq,screen=screen,screen_location=(0,0))
    #draw_ocs(sr=sr, freq=freq,screen=screen,screen_location=(300,300))
    #draw_ocs(sr=sr, freq=freq,screen=screen,screen_location=(300,0))#


     # ------------- Get Signal 1 to draw Ocs Sub Box
    typeOsc=(dropdownTypeOsc.getSelected())
    signalOcs = soundOcsSub(sr=sr,lenght=1,freq = 1,case=typeOsc)

    draw_ocs_sub(sr=sr,screen=screen,screen_location=(0,300),signal=signalOcs)

    pygame.draw.rect(screen,"grey",(0,0,300,300),0)

    attack = Attack.getValue()
    hold = Hold.getValue()
    decay = Decay.getValue()
    substain = Substain.getValue()
    releas = Release.getValue()

    draw_env(sr=sr,lenght=lenght,screen=screen,screen_location=(300,300),attack=attack,hold=hold,decay=decay,substain=substain,release=releas)

    pygame.draw.rect(screen,"grey",(310,0,300,300),0)

    pygame_widgets.update(events)
    pygame.display.update()
