from turtle import Screen
import matplotlib
matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import pygame
import pylab
import numpy as np
from pygame_widgets.sliderKnobman import SliderKnobman
from pygame_widgets.slider import Slider
from pygame_widgets.dropdown import Dropdown 
from pygame_widgets.button import Button 
from pygame_widgets.textbox import TextBox 

from CreatePiano import *
from Sampler import *



#------------------Draw Osc Curve 
def draw_env(sr = 44100, # sample rate
            lenght =1.0,
            screen=pygame.display.get_surface,
            screen_location = (0,0),
            attack = 0.10,
            hold = 0.15,
            decay = 0.30,
            substain =0.50,
            release = 0.90):
    


    #Create Graph
    fig = pylab.figure(figsize=[4, 2], # Inches
                    dpi=100)

    Osc = np.zeros(shape=sr)
    Osc2 = np.where(Osc == 0,1,1)
    try:
        envelop = soundEnvelopApply(Osc2,sr,attack = attack,hold=hold,decay=decay,substain=substain,release=release)
        t = np.arange(0,lenght,1.0/sr)
        ax = fig.gca()
        ax.yaxis.set_visible(False)
        ax.xaxis.set_visible(True)
        ax.plot(t,envelop,lw=2, color='red',)
    except:
        envelop = soundEnvelopApply(Osc2,sr,attack = attack,hold=hold,decay=decay,substain=substain,release=release)
        t = np.arange(0,lenght+(1/sr),1.0/sr)
        ax = fig.gca()
        ax.plot(t,envelop)
        ax = fig.gca()
        ax.yaxis.set_visible(False)
        ax.xaxis.set_visible(False)
        ax.plot(t,envelop,lw=2, color='red',)





    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    size = canvas.get_width_height()

    surf = pygame.image.fromstring(raw_data, size, "RGB")
    screen.blit(surf, screen_location)
    pygame.display.flip()


#--------------------Input Osc Sub Parameters
def draw_envelopParameters(screen):
    sliderAttack = SliderKnobman(screen, 800, 40, 50, 40,initial = 10,min=0, max=99, step=1)
    outputAttack = TextBox(screen, 810, 50, 30, 30, fontSize=12)
    
    sliderHold = SliderKnobman(screen, 870, 40, 50, 40,initial = 20,min=0, max=99, step=1)
    outputHold = TextBox(screen, 880, 50, 30, 30, fontSize=12)
    sliderHold.set(sliderAttack,value =0)

    sliderSubstain = SliderKnobman(screen, 960, 40, 50, 40,initial = 50,min=0, max=99, step=1)
    outputSubstain = TextBox(screen, 970, 50, 30, 30, fontSize=12)

    sliderDecay = SliderKnobman(screen, 1030, 40, 50, 40,initial = 50 ,min=0, max=99, step=1)
    outputDecay = TextBox(screen, 1040, 50, 30, 30, fontSize=12)

    sliderRelease = SliderKnobman(screen, 1130, 40, 50, 40,initial = 99,min=0, max=99, step=1)
    outputRelease = TextBox(screen, 1140, 50, 30, 30, fontSize=12)

    return sliderAttack,outputAttack,sliderHold,outputHold,sliderDecay,outputDecay,sliderSubstain,outputSubstain,sliderRelease,outputRelease


