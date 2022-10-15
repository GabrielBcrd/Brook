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

import numpy as np
from pygame_widgets.dropdown import Dropdown 
from pygame_widgets.button import Button 
from pygame_widgets.textbox import TextBox 
from pygame_widgets.sliderKnobman import SliderKnobman
# sampling information

class Envelop(object):
    
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
        self.handleColour = kwargs.get('handleColour',(210,0,0))

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

    def draw_env(self,sr = 44100,lenght =1.0,):
    
        #Create Graph
        fig = pylab.figure(figsize=[3.975, 2], # Inches
                        dpi=100)

        Osc = np.zeros(shape=sr)
        Osc2 = np.where(Osc == 0,1,1)
        try:
            envelop = soundEnvelopApply(Osc2,sr,self.attack,hold=self.hold,decay=self.decay,substain=self.substain,release=self.release)
            t = np.arange(0,lenght,1.0/sr)
            ax = fig.gca()
            ax.yaxis.set_visible(False)
            ax.xaxis.set_visible(True)
            ax.plot(t,envelop,lw=2, color='red',)
        except:
            envelop = soundEnvelopApply(Osc2,sr,attack = self.attack,hold=self.hold,decay=self.decay,substain=self.substain,release=self.release)
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
        self.screen.blit(surf, (self._x+3.5,self._y+100))
        pygame.display.flip()
            

    def draw_envelopParameters(self):
        self.sliderAttack = SliderKnobman(self.screen, self._x + 30, self._y + 30, 50, 40,initial = 10,min=1, max=99, step=1)
        self.outputAttack = TextBox(self.screen, self._x + 60, self._y + 60, 20, 20, fontSize=12)
        
        self.sliderHold = SliderKnobman(self.screen, self._x + 100, self._y + 30, 50, 40,initial = 20,min=0, max=99, step=1)
        self.outputHold = TextBox(self.screen, self._x + 130, self._y + 60, 20, 20,  fontSize=12)

        self.sliderSubstain = SliderKnobman(self.screen, self._x + 180, self._y + 30,50, 40,initial = 50,min=1, max=99, step=1)
        self.outputSubstain = TextBox(self.screen,self._x + 210, self._y + 60,20, 20,  fontSize=12)

        self.sliderDecay = SliderKnobman(self.screen, self._x + 250, self._y + 30, 50, 40,initial = 50 ,min=0, max=99, step=1)
        self.outputDecay = TextBox(self.screen, self._x + 280, self._y + 60, 20, 20,  fontSize=12)

        self.sliderRelease = SliderKnobman(self.screen, self._x + 330, self._y + 30, 50, 40,initial = 99,min=0, max=100, step=1)
        self.outputRelease = TextBox(self.screen,  self._x + 360, self._y + 60, 20, 20,  fontSize=12)


    def draw_EnvBackground(self):
        pygame.draw.rect(self.screen,"white",(self._x,self._y,400,100),0)
        pygame.draw.rect(self.screen,self.handleColour,(self._x,self._y,3,300),0)
        pygame.draw.rect(self.screen,self.handleColour,(self._x,self._y,400,3),0)


    def getArguments_Envelop(self):
        self.attack=self.sliderAttack.getValue()/100
        self.hold=self.sliderHold.getValue()/100
        self.substain=self.sliderSubstain.getValue()/100
        self.decay=self.sliderDecay.getValue()/100
        self.release=self.sliderRelease.getValue()/100

        self.outputAttack.setText(self.sliderAttack.getValue())
        self.outputHold.setText(self.sliderHold.getValue())
        self.outputSubstain.setText(self.sliderSubstain.getValue())
        self.outputDecay.setText(self.sliderDecay.getValue())
        self.outputRelease.setText(self.sliderRelease.getValue())





if __name__ == '__main__':

    pygame.init()

    win = pygame.display.set_mode((1000, 600))

    signalOcs = Envelop(screen=win,x=100,y=100)
    signalOcs.draw_envelopParameters()
    signalOcs.getArguments_Envelop()
    signalOcs.draw_env(lenght =1.0)


    run = True
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()

        
        signalOcs.getArguments_Envelop()
        signalOcs.draw_env()
        signalOcs.draw_EnvBackground()


        pygame_widgets.update(events)
        pygame.display.update()