from re import sub
import matplotlib
matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import pygame
from pygame.locals import *
import pylab
import pygame_widgets
from pygame import gfxdraw 
from pygame_widgets.mouse import Mouse, MouseState
 
from Sampler import *
import matplotlib.pyplot as plt
from scipy import signal

import numpy as np
from pygame_widgets.dropdown import Dropdown 
from pygame_widgets.button import Button 
from pygame_widgets.textbox import TextBox 
from pygame_widgets.sliderKnobman import SliderKnobman
# sampling information

class Filter(object):
    
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
        self.handleColour = kwargs.get('handleColour',(0,210,210))

        self.borderThickness = kwargs.get('borderThickness', 3)
        self.borderColour = kwargs.get('borderColour', (0, 0, 0))
    
  

    def draw_filter(self):
    
        
        b, a = signal.butter(4, self.CutOff, 'highpass', analog=True)
        w, h = signal.freqs(b, a)
        #Response of filter

        fig = pylab.figure(figsize=[2, 2], # Inches
                        dpi=100)

        plt.semilogx(w, 20 * np.log10(abs(h)))
        plt.title('filter frequency response')
        plt.xlabel('Frequency [radians / second]')
        plt.ylabel('Amplitude [dB]')
        plt.margins(0, 0.1)
        plt.grid(which='both', axis='both')
        plt.axvline(self.CutOff, color='cyan') # cutoff frequency


        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()

        surf = pygame.image.fromstring(raw_data, size, "RGB")
        self.screen.blit(surf, (self._x+3.5,self._y+100))
        pygame.display.flip()


    def getArguments_filter(self):
        self.CutOff = self.sliderCutOff.getValue()
        self.outputCutOff.setText(self.sliderCutOff.getValue())

        self.Drive = self.sliderDrive.getValue()/100
        self.outputDrive.setText(self.sliderDrive.getValue())

        self.Res = self.sliderRes.getValue()/100
        self.outputRes.setText(self.sliderRes.getValue())

        self.typeFilter = self.dropdownTypeFilter.getSelected()
    

    def draw_filter_parameters(self):
        self.sliderCutOff = SliderKnobman(self.screen, self._x + 15, self._y + 30, 50, 40,initial = 10,min=0, max=99, step=1,handleColour = (0,210,210))
        self.outputCutOff = TextBox(self.screen, self._x + 45, self._y + 60, 20, 20, fontSize=12)
        
        self.sliderDrive = SliderKnobman(self.screen,  self._x + 80, self._y + 30, 50, 40,initial = 20,min=0, max=99, step=1,handleColour = (0,210,210))
        self.outputDrive = TextBox(self.screen,self._x + 110, self._y + 60, 20, 20, fontSize=12)

        self.sliderRes = SliderKnobman(self.screen, self._x + 145, self._y + 30,50, 40,initial = 50,min=0, max=99, step=1,handleColour = (0,210,210))
        self.outputRes = TextBox(self.screen, self._x + 175, self._y + 60, 20, 20, fontSize=12)

        self.dropdownTypeFilter = Dropdown(
            self.screen, self._x + 220 , self._y + 40, 50, 30, name='filter',
            choices=[
                'lowpass',
                'highpass',
                '2',
            ],
            borderRadius=100, colour=pygame.Color('white'), values=['lowpass', 'highpass', '2'], direction='down', textHAlign='left'
        )


    def draw_SubBackground(self):
        pygame.draw.rect(self.screen,"white",(self._x,self._y,200,100),0)
        pygame.draw.rect(self.screen,"white",(self._x + 200,self._y,100,300),0)
        pygame.draw.rect(self.screen,self.handleColour,(self._x,self._y,3,300),0)
        pygame.draw.rect(self.screen,self.handleColour,(self._x,self._y,300,3),0)







if __name__ == '__main__':

    pygame.init()

    win = pygame.display.set_mode((1000, 600))

    filter = Filter(screen=win,x=100,y=100)
    filter.draw_filter_parameters()
    filter.getArguments_filter()
    filter.draw_filter()

    run = True
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()

        
        filter.getArguments_filter()
        filter.draw_filter()
        filter.draw_SubBackground()


        pygame_widgets.update(events)
        pygame.display.update()