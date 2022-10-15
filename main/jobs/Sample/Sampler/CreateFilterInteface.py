import matplotlib
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
from SamplerEffect import *



#------------------Draw Osc Curve 
def draw_filter(sr = 44100, # sample rate
            lenght =1.0,
            screen=pygame.display.get_surface,
            screen_location = (0,0),
            cutoff = 50,
            filterType = 'lowpass'):
    


    #Create Graph

    """ b, a = signal.butter(4, cutoff, filterType, analog=True)
    w, h = signal.freqs(b, a)

    fig = pylab.figure(figsize=[3, 3], # Inches
                    dpi=100)
    

    ax = fig.gca()
    ax.semilogx((w, 20 * np.log10(abs(h))))
    ax.set_ylabel('Amplitude [dB]')
    ax.set_xlabel('Frequency [radians / second]')
    ax.grid(which='both',axis='both')
    ax.axvline(cutoff, color='green') """
    
    b, a = signal.butter(4, cutoff, filterType, analog=True)
    w, h = signal.freqs(b, a)
     #Response of filter

    fig = pylab.figure(figsize=[2.5, 2], # Inches
                    dpi=100)

    plt.semilogx(w, 20 * np.log10(abs(h)))
    plt.title('filter frequency response')
    plt.xlabel('Frequency [radians / second]')
    plt.ylabel('Amplitude [dB]')
    plt.margins(0, 0.1)
    plt.grid(which='both', axis='both')
    plt.axvline(cutoff, color='green') # cutoff frequency




    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    size = canvas.get_width_height()

    surf = pygame.image.fromstring(raw_data, size, "RGB")
    screen.blit(surf, screen_location)
    pygame.display.flip()


#--------------------Input Osc Sub Parameters
def draw_filter_parameters(screen):
    sliderCutOff = SliderKnobman(screen, 500, 340, 50, 40,initial = 10,min=0, max=99, step=1,handleColour = (0,210,210))
    outputCutOff = TextBox(screen, 510, 350, 30, 30, fontSize=12)
    
    sliderDrive = SliderKnobman(screen, 570, 340, 50, 40,initial = 20,min=0, max=99, step=1,handleColour = (0,210,210))
    outputDrive = TextBox(screen, 580, 350, 30, 30, fontSize=12)

    sliderRes = SliderKnobman(screen, 650, 340, 50, 40,initial = 50,min=0, max=99, step=1,handleColour = (0,210,210))
    outputRes = TextBox(screen, 650, 350, 30, 30, fontSize=12)

    dropdownTypeFilter = Dropdown(
        screen, 330, 330, 100, 30, name='filter type',
        choices=[
            'lowpass',
            'highpass',
            '2',
        ],
        borderRadius=100, colour=pygame.Color('white'), values=['lowpass', 'highpass', '2'], direction='down', textHAlign='left'
    )

    return sliderCutOff,outputCutOff,sliderDrive,outputDrive,sliderRes,outputRes,dropdownTypeFilter


