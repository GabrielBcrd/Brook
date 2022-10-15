import matplotlib
matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import pygame
from pygame.locals import *
import pylab
import pygame_widgets
from pygame import gfxdraw 
from pygame_widgets.mouse import Mouse, MouseState

from CreatePiano import *
from Sampler import *
import matplotlib.pyplot as plt

from pygame_widgets.dropdown import Dropdown 
from pygame_widgets.button import Button 
from pygame_widgets.textbox import TextBox 
from pygame_widgets.sliderKnobman import SliderKnobman
# sampling information

class OcsNoise(object):
    
    def __init__(self, screen, x, y, **kwargs):

        self.selected = False
        self.screen = screen
        self._x = x
        self._y = y

        self._height = kwargs.get('height', 0)
        self._width = kwargs.get('width', 99)

        self.min = kwargs.get('min', 0)
        self.max = kwargs.get('max', 99)
        self.step = kwargs.get('step', 1)

        self.colour = kwargs.get('colour', (200, 200, 200))
        self.handleColour = kwargs.get('handleColour',(186,85,211))

        self.borderThickness = kwargs.get('borderThickness', 3)
        self.borderColour = kwargs.get('borderColour', (0, 0, 0))
    
    def contains(self, x, y):
        return (self._x < x - self.screen.get_abs_offset()[0] < self._x + self._width) and \
               (self._y < y - self.screen.get_abs_offset()[1] < self._y + self._height)

    def listen(self, events):
        mouseState = Mouse.getMouseState()
        x, y = Mouse.getMousePos()
        if self.contains(x, y):
            if mouseState == MouseState.CLICK:
                self.selected = True
            if mouseState == MouseState.RELEASE:
                self.selected = False

    def draw_ocs_noise(self, sr = 44100, # sample rate
                lenght =1.0,
                screen=pygame.display.get_surface,
                ):

            screen_location = (self._x,self._y + 100)

            t = np.arange(0,lenght,1.0/sr)

            # ------------- Get signals 
            signalNoise = soundOcsNoise(lenght=lenght,sr=sr,case=2)

            fig = pylab.figure(figsize=[2, 2], # Inches
                            dpi=100)        # 100 dots per inch, resulting buffer is 400x400 pixel
            ax = fig.gca()
            ax.yaxis.set_visible(False)
            ax.xaxis.set_visible(False)
            ax.plot(t,signalNoise,lw=2, color='purple')

            canvas = agg.FigureCanvasAgg(fig)
            canvas.draw()
            renderer = canvas.get_renderer()
            raw_data = renderer.tostring_rgb()
            size = canvas.get_width_height()

            surf = pygame.image.fromstring(raw_data, size, "RGB")
            self.screen.blit(surf, screen_location)
            pygame.display.flip()
            

        # ------------Add parameters input

    def draw_OscNoiseParameters(self, screen):
        self.sliderMixerVolume = SliderKnobman(self.screen, self._x + 30 , self._y+30, 40, 40, 
                                            min=0, max=99, step=1,handleColour = (186,85,211))
        self.outputMixerVolume = TextBox(self.screen, self._x + 65 , self._y +65, 20, 20, fontSize=12)

        self.dropdownTypeOsc = Dropdown(
            screen, self._x + 220 , self._y + 40, 60, 20, name='noise',
            choices=[
                '1',
                '2',
                'nope',
            ],
            borderRadius=100, colour=pygame.Color('white'), values=['1', '2', 'nope'], 
            direction='down', textHAlign='left'
        )

    def draw_OscNoiseBackground(self):
        pygame.draw.rect(self.screen,"white",(self._x,self._y,200,100),0)
        pygame.draw.rect(self.screen,"white",(self._x + 200,self._y,100,300),0)
        pygame.draw.rect(self.screen,self.handleColour,(self._x,self._y,3,300),0)
        pygame.draw.rect(self.screen,self.handleColour,(self._x,self._y,300,3),0)

     

    def getArguments_OscNoise(self):
        self.typeOsc=(self.dropdownTypeOsc.getSelected())

        self.outputMixerVolume.setText(self.sliderMixerVolume.getValue())


if __name__ == '__main__':

    pygame.init()
    win = pygame.display.set_mode((1000, 600))
    signalOcs = OcsNoise(screen=win,x=100,y=100)
    signalOcs.draw_OscNoiseParameters(win)
    signalOcs.draw_ocs_noise()

    run = True
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()

        typeOcsNoise = signalOcs.getArguments_OscNoise()
        signalOcs.draw_OscNoiseBackground()
        
        


        pygame_widgets.update(events)
        pygame.display.update()