import matplotlib
matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import pygame
from pygame.locals import *
import pylab


from CreatePiano import *
from Sampler import *
import matplotlib.pyplot as plt

from pygame_widgets.dropdown import Dropdown 
from pygame_widgets.button import Button 
from pygame_widgets.textbox import TextBox 
from pygame_widgets.sliderKnobman import SliderKnobman

# sampling information


def draw_ocs_noise(sr = 44100, # sample rate
            lenght =1.0,
            screen=pygame.display.get_surface,
            screen_location = (0,0)):
    
    t = np.arange(0,lenght,1.0/sr)

    # ------------- Get signals 
    signalNoise = soundOcsNoise(lenght=lenght,sr=sr,case=2)

    fig = pylab.figure(figsize=[2, 2], # Inches
                    dpi=100)        # 100 dots per inch, resulting buffer is 400x400 pixel
    ax = fig.gca()
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.plot(t,signalNoise,lw=2, color='purple',)

    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    size = canvas.get_width_height()

    surf = pygame.image.fromstring(raw_data, size, "RGB")
    screen.blit(surf, screen_location)
    pygame.display.flip()

    # ------------Add parameters input

def draw_OscNoiseParameters(screen):
    sliderMixerVolume = SliderKnobman(screen, 40, 340, 200, 40, min=0, max=99, step=1,handleColour = (186,85,211))
    outputMixerVolume = TextBox(screen, 50, 350, 30, 30, fontSize=12)


    dropdownTypeOsc = Dropdown(
        screen, 200, 330, 100, 30, name='wave type',
        choices=[
            'sin',
            'square',
            'triangle',
        ],
        borderRadius=100, colour=pygame.Color('white'), values=['sin', 'square', 'triangle'], direction='down', textHAlign='left'
    )
    return sliderMixerVolume,outputMixerVolume,dropdownTypeOsc
