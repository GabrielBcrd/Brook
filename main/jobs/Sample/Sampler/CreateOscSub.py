from turtle import Screen, color
import matplotlib
matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import pygame
import pylab
import numpy as np
from pygame_widgets.slider import Slider 
from pygame_widgets.dropdown import Dropdown 
from pygame_widgets.button import Button 
from pygame_widgets.textbox import TextBox 
from pygame_widgets.sliderKnobman import SliderKnobman
from CreatePiano import *



#------------------Draw Osc Curve 
def draw_ocs_sub(sr = 44100, # sample rate
            lenght =1.0,
            screen=pygame.display.get_surface,
            screen_location =  (0,0),
            signal = np.sin(1)):
    
    t = np.arange(0,lenght,1.0/sr)

    #Create Graph
    fig = pylab.figure(figsize=[2, 2], # Inches
                    dpi=100)        # 100 dots per inch, resulting buffer is 400x400 pixel
    ax = fig.gca()
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.plot(t,signal,lw=2, color='navy',)

    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    size = canvas.get_width_height()

    surf = pygame.image.fromstring(raw_data, size, "RGB")
    screen.blit(surf, screen_location)
    pygame.display.flip()


#--------------------Input Osc Sub Parameters
def draw_OscSubParameters(screen):
    sliderMixerVolume = SliderKnobman(screen, 40, 40, 200, 40, min=0, max=99, step=1,handleColour = (0,0,210))
    outputMixerVolume = TextBox(screen, 50, 50, 30, 30, fontSize=12)


    dropdownTypeOsc = Dropdown(
        screen, 200, 30, 100, 30, name='wave type',
        choices=[
            'sin',
            'square',
            'triangle',
        ],
        borderRadius=100, colour=pygame.Color('white'), values=['sin', 'square', 'triangle'], direction='down', textHAlign='left'
    )
    return sliderMixerVolume,outputMixerVolume,dropdownTypeOsc


