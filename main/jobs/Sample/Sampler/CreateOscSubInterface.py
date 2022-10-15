from re import sub
import matplotlib
matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import pygame
from pygame.locals import *
import pylab
import pygame_widgets
from pygame_widgets.mouse import Mouse, MouseState
 
from Sampler import *

import numpy as np
from pygame_widgets.dropdown import Dropdown 
from pygame_widgets.textbox import TextBox 
from pygame_widgets.sliderKnobman import SliderKnobman

# sampling information

class Sub(object):
    
    def __init__(self, screen, x, y, **kwargs):

        self.selected = False
        self.screen = screen
        self._x = x
        self._y = y

        self._height = kwargs.get('height', 0)
        self._width = kwargs.get('width', 99)

        self.signal = soundOcsSub(sr=44100,lenght=1,freq = 1,case='sin')


        self.min = kwargs.get('min', 0)
        self.max = kwargs.get('max', 99)
        self.step = kwargs.get('step', 1)

        self.colour = kwargs.get('colour', (200, 200, 200))
        self.handleColour = kwargs.get('handleColour',(0,0,210))

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

    def draw_ocs_sub(self, sr = 44100, # sample rate
            lenght =1.0):
            
    
        t = np.arange(0,lenght,1.0/sr)

        #Create Graph
        fig = pylab.figure(figsize=[2, 2], # Inches
                        dpi=100)        # 100 dots per inch, resulting buffer is 400x400 pixel
        ax = fig.gca()
        ax.yaxis.set_visible(False)
        ax.xaxis.set_visible(False)

        ax.plot(t,self.signal,lw=2, color='navy',)

        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()

        surf = pygame.image.fromstring(raw_data, size, "RGB")
        self.screen.blit(surf, (self._x+3.5,self._y+100))
        pygame.display.flip()


    def getArguments_Sub(self):
        self.SubMixerVolume = self.sliderMixerVolume.getValue()/100
        self.outputMixerVolume.setText(self.sliderMixerVolume.getValue())

        self.typeOsc = self.dropdownTypeOsc.getSelected()
        self.signal = soundOcsSub(sr=44100,lenght=1,freq = 1,case=self.typeOsc)
    

    def draw_OscSubParameters(self):
        self.sliderMixerVolume = SliderKnobman(self.screen, self._x + 30 , self._y+30, 40, 40, 
                                            min=0, max=99, step=1,handleColour = self.handleColour)
        self.outputMixerVolume = TextBox(self.screen, self._x + 65 , self._y +65, 20, 20, fontSize=12)


        self.dropdownTypeOsc = Dropdown(
            self.screen, self._x + 220 , self._y + 40, 60, 20, name='sub',
            choices=[
                'sin',
                'square',
                'triangle',
            ],
            borderRadius=100, colour=pygame.Color('white'), values=['sin', 'square', 'triangle'], direction='down', textHAlign='left'
        )


    def draw_SubBackground(self):
        pygame.draw.rect(self.screen,"white",(self._x,self._y,200,100),0)
        pygame.draw.rect(self.screen,"white",(self._x + 200,self._y,100,300),0)
        pygame.draw.rect(self.screen,self.handleColour,(self._x,self._y,3,300),0)
        pygame.draw.rect(self.screen,self.handleColour,(self._x,self._y,300,3),0)







if __name__ == '__main__':

    pygame.init()

    win = pygame.display.set_mode((1000, 600))

    signalOcsSub = Sub(screen=win,x=100,y=100)
    signalOcsSub.draw_OscSubParameters()
    signalOcsSub.draw_ocs_sub()
    signalOcsSub.getArguments_Sub()
    signalOcsSub.draw_ocs_sub()

    run = True
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()

        
        signalOcsSub.getArguments_Sub()
        signalOcsSub.draw_ocs_sub()
        signalOcsSub.draw_SubBackground()


        pygame_widgets.update(events)
        pygame.display.update()