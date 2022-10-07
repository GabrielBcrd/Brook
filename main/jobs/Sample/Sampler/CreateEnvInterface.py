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
            release = 0.99):
    

    t = np.arange(0,lenght,1.0/sr)

    #Create Graph
    fig = pylab.figure(figsize=[5, 3], # Inches
                    dpi=100,        # 100 dots per inch, resulting buffer is 400x400 pixels
                    )

    #Create 
    Osc = np.zeros(shape=sr)
    Osc2 = np.where(Osc == 0,1,1)
    envelop = soundEnvelopApply(Osc2,sr,t=t,attack = attack,hold=hold,decay=decay,substain=substain,release=release)

    ax = fig.gca()
    ax.plot(t,envelop)

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
    sliderAttack = SliderKnobman(screen, 380, 40, 200, 40,initial = 0,min=0, max=99, step=1)
    outputAttack = TextBox(screen, 580, 0, 30, 30, fontSize=12)
    
    sliderHold = SliderKnobman(screen, 380, 120, 200, 40,initial = 20,min=0, max=99, step=1)
    outputHold = TextBox(screen, 580, 50, 30, 30, fontSize=12)
    sliderHold.set(sliderAttack,value =0)

    sliderSubstain = SliderKnobman(screen, 380, 200, 200, 40,initial = 50,min=0, max=99, step=1)
    outputSubstain = TextBox(screen, 580, 150, 30, 30, fontSize=12)

    sliderDecay = SliderKnobman(screen, 380, 280, 200, 40,initial = 50 ,min=0, max=99, step=1)
    outputDecay = TextBox(screen, 580, 100, 30, 30, fontSize=12)

    sliderRelease = SliderKnobman(screen, 380, 360, 200, 40,initial = 0.99,min=0, max=99, step=1)
    outputRelease = TextBox(screen, 580, 250, 30, 30, fontSize=12)
    sliderHold.set(sliderAttack,value =99)


    return sliderAttack,outputAttack,sliderHold,outputHold,sliderDecay,outputDecay,sliderSubstain,outputSubstain,sliderRelease,outputRelease


