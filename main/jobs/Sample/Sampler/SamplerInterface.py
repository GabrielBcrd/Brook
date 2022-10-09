from re import sub
from turtle import Screen
import numpy as np
import pygame
import pygame_widgets 

# sampling information
from Sampler import *
from CreatePiano import *
from CreateOscNoise import draw_ocs_noise, draw_OscNoiseParameters
from CreateOcs import draw_ocs
from CreateEnvInterface import *
from CreateOscSub import *
from pygame import mixer
from CreateWidget import *
from CreateFilterInteface import *



#-----------------variables------------------
sr = 44100 # sample rate
freq = 1
lenght =1.0
t = np.arange(0,lenght,1.0/sr)
x = np.pi * 2 *freq * t
data = 20


#------------------init pygame -------------------------------
pygame.init()
mixer.init()

white_notes,black_notes = transform_notes_to_list(nbOctave=8)
width = len(white_notes) * len(black_notes)
height = 900
screen=pygame.display.set_mode([width,height])

#------------------Filter sliders
sliderCutOff,outputCutOff,sliderDrive,outputDrive,sliderRes,outputRes,dropdownTypeFilter = draw_filter_parameters(screen=screen)
draw_filter(sr=sr,lenght=lenght,screen=screen,screen_location=(450,400),cutoff=150.00,filterType="lowpass")

#------------------Osc Sub sliders ------------------------
sliderMixerVolume,outputMixerVolume,dropdownTypeOsc = draw_OscSubParameters(screen)

#------------------Osc Noise sliders ------------------------
sliderMixerVolumeNoise,outputNoiseMixerVolume,dropdownTypeOscNoise = draw_OscNoiseParameters(screen)
draw_ocs_noise(sr=sr,lenght=1,screen=screen,screen_location=(0,400))



#------------------Envelop sliders ------------------------

Attack,outputAttack,Hold,outputHold,Decay,outputDecay,Substain,outputSubstain,Release,outputRelease = draw_envelopParameters(screen)

#------------------ Piano keys ------------------------------

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
    
    
    

textboxFrequency = TextBox(screen, 1300, 500, 400, 80, fontSize=50,
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
            
       
    outputMixerVolume.setText(sliderMixerVolume.getValue()/100)
    outputAttack.setText(Attack.getValue()/100)
    outputHold.setText(Hold.getValue()/100)
    outputDecay.setText(Decay.getValue()/100)
    outputSubstain.setText(Substain.getValue()/100)
    outputRelease.setText(Release.getValue()/100)


     # ------------- Get Sub parameters to draw Ocs Sub Box -----------------------------------
    typeOsc=(dropdownTypeOsc.getSelected())
    signalOcs = soundOcsSub(sr=sr,lenght=1,freq = 1,case=typeOsc)

    draw_ocs_sub(sr=sr,screen=screen,screen_location=(0,100),signal=signalOcs)

    # ------------- Get Noise parameters to draw Ocs Noise Box -----------------------------------
   
    
    # ------------- Get Envelop parameters to draw Envelop  ----------------------------------------
    attack = int(Attack.getValue())/100 
    hold = int(Hold.getValue())/100
    decay = int(Decay.getValue())/100
    substain = int(Substain.getValue())/100
    releas = int(Release.getValue())/100

    draw_env(sr=sr,lenght=lenght,screen=screen,screen_location=(850,100),attack=attack,hold=hold,decay=decay,substain=substain,release=releas)
    
    pygame.draw.rect(screen,"white",(0,0,200,100),0)
    pygame.draw.rect(screen,"white",(200,0,100,300),0)
    pygame.draw.rect(screen,"blue",(0,0,300,2),0)


    pygame.draw.rect(screen,"white",(0,300,200,100),0)
    pygame.draw.rect(screen,"white",(200,300,100,300),0)
    pygame.draw.rect(screen,"purple",(0,300,300,2),0)

    pygame.draw.rect(screen,"white",(750,0,500,100),0)
    pygame.draw.rect(screen,"red",(750,0,500,2),0)

    pygame.draw.rect(screen,"white",(301,300,399,100),0)
    pygame.draw.rect(screen,"white",(301,300,150,300),0)
    pygame.draw.rect(screen,"cyan",(301,300,399,2),0)

    pygame.draw.rect(screen,"white",(1250,0,500,500),0)
    



    pygame_widgets.update(events)
    pygame.display.update()