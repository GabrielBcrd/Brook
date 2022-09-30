import pygame_widgets
import pygame
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

pygame.init()
win = pygame.display.set_mode((1000, 600))


def create_slideBar_Parameters():
    slider = Slider(win, 100, 100, 800, 40, min=0, max=99, step=1)
    output = TextBox(win, 475, 200, 50, 50, fontSize=30)

    output.disable()  # Act as label instead of textbox
    return slider,output

slider, output = create_slideBar_Parameters()

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    output.setText(slider.getValue())

    pygame_widgets.update(events)
    pygame.display.update()