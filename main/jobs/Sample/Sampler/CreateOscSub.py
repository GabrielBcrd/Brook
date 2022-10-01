from turtle import Screen
import matplotlib
matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import pygame
from pygame.locals import *
import pylab
import numpy as np
from pygame_widgets.slider import Slider 
from pygame_widgets.dropdown import Dropdown 
from pygame_widgets.button import Button 
from pygame_widgets.textbox import TextBox 

from CreatePiano import *



#------------------Draw Osc Curve 
def draw_ocs_sub(sr = 44100, # sample rate
            lenght =1.0,
            screen=pygame.display.get_surface,
            screen_location =  (0,0),
            signal = np.sin(1)):
    
    t = np.arange(0,lenght,1.0/sr)

    #------------- Create Graph
    fig = pylab.figure(figsize=[3, 3], # Inches
                    dpi=100,        # 100 dots per inch, resulting buffer is 400x400 pixels
                    )
    ax = fig.gca()
    ax.plot(t,signal)

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
    sliderMixerVolume = Slider(screen, 20, 250, 200, 20, min=0, max=1, step=0.01)
    outputMixerVolume = TextBox(screen, 250, 250, 30, 30, fontSize=12)


    dropdownTypeOsc = Dropdown(
        screen, 20, 200, 200, 30, name='Select wave type',
        choices=[
            'sin',
            'square',
            'triangle',
        ],
        borderRadius=100, colour=pygame.Color('white'), values=['sin', 'square', 'triangle'], direction='down', textHAlign='left'
    )
    return sliderMixerVolume,outputMixerVolume,dropdownTypeOsc


