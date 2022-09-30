from turtle import Screen
import numpy as np
import pygame
import pygame_widgets

# sampling information
from CreatePiano import *
from CreateOscNoise import draw_ocs_noise
from CreateOcs import draw_ocs
from CreateOscSub import draw_ocs_sub
from pygame_widgets.slider import Slider 
from pygame_widgets.dropdown import Dropdown 
from pygame_widgets.button import Button 
from pygame_widgets.textbox import TextBox 


#-----------------variables------------------
sr = 44100 # sample rate
freq = 20
lenght =1.0
t = np.arange(0,lenght,1.0/sr)
x = np.pi * 2 *freq * t



#------------------init pygame -------------------------------
pygame.init()

white_notes,black_notes = transform_notes_to_list(nbOctave=8)
width = len(white_notes) * len(black_notes)
height = 900
screen=pygame.display.set_mode([width,height])

active_whites = []
active_blacks = []


slider = Slider(screen, 20, 250, 200, 20, min=0, max=99, step=1)
output = TextBox(screen, 250, 250, 30, 30, fontSize=24)

output.disable()  # Act as label instead of textbox

dropdown = Dropdown(
    screen, 20, 200, 200, 30, name='Select Octave',
    choices=[
        'Red',
        'Blue',
        'Yellow',
    ],
    borderRadius=100, colour=pygame.Color('white'), values=[1, 2, 'true'], direction='down', textHAlign='left'
)
output2 = TextBox(screen, 250, 200, 30, 30, fontSize=24)
output2.disable()  # Act as label instead of textbox

def print_value():
    print(dropdown.getSelected())








run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()


    screen.fill('gray')
    
    #draw_ocs_noise(sr=sr, freq=freq,screen=screen,screen_location=(0,0))
    #draw_ocs(sr=sr, freq=freq,screen=screen,screen_location=(300,300))
    #draw_ocs(sr=sr, freq=freq,screen=screen,screen_location=(300,0))#
    draw_ocs_sub(sr=sr, freq=freq,screen=screen,screen_location=(0,300))

    white_keys, black_keys, active_whites, active_blacks = draw_piano(active_whites, active_blacks,
                                                                screen=screen,width=width,height=height,
                                                                white_notes=white_notes, black_notes=black_notes,
                                                                nb_float_black = 23
                                                                ) 

    output.setText(slider.getValue())
    output2.setText(dropdown.getSelected())




    pygame_widgets.update(events)
    pygame.display.update()
