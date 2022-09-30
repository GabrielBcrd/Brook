import matplotlib
matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import pygame
from pygame.locals import *
import pylab


from CreatePiano import *
from Sampler import *
import matplotlib.pyplot as plt

# sampling information


def draw_ocs(sr = 44100, # sample rate
            freq = 20,
            lenght =1.0,
            screen=pygame.display.get_surface,
            screen_location =  (0,0)):
    
    t = np.arange(0,lenght,1.0/sr)
    x = np.pi * 2 *freq * t

    # ------------- Get signals 
    signalOcs = soundOcsSub(x=x,case='square')

    #------------- Create Graph
    fig = pylab.figure(figsize=[4, 3], # Inches
                    dpi=100,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                    )
    ax = fig.gca()
    ax.plot(t,signalOcs)

    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()


    size = canvas.get_width_height()

    surf = pygame.image.fromstring(raw_data, size, "RGB")
    screen.blit(surf, screen_location)
    pygame.display.flip()

    # ------------Add parameters input


