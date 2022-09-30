import pygame
import pandas as pd


#-----------------Retrieve lists of white and black notes
def transform_notes_to_list(nbOctave):
    df = pd.read_csv('array_notes_frequency.csv')  
    white_notesdf = df[(df['color_notes'].str.contains("white_note")) & (df['octave']<nbOctave)]
    black_notesdf = df[(df['color_notes'].str.contains("black_note")) & (df['octave']<nbOctave)]

    white_notes = white_notesdf['Note'].values.tolist()
    black_notes = black_notesdf['Note'].values.tolist()
    return white_notes,black_notes



def draw_piano(whites, blacks,screen,height,width,white_notes,black_notes,nb_float_black=0):


    #------------------import font ---------------------------------
    font = pygame.font.Font('main/resources/made_okine_sans/MADEOkineSansPERSONALUSE-Black.otf',30)
    medium_font = pygame.font.Font('main/resources/made_okine_sans/MADEOkineSansPERSONALUSE-Black.otf',11)
    small_font = pygame.font.Font('main/resources/made_okine_sans/MADEOkineSansPERSONALUSE-Black.otf',8)
    small_small_font = pygame.font.Font('main/resources/made_okine_sans/MADEOkineSansPERSONALUSE-Black.otf',6)

    #------------------draw piano ---------------------------------
    white_rects = []

    for i in range(len(white_notes)):
        rect = pygame.draw.rect(screen, 'white', [i * len(black_notes), height - 300, len(black_notes), 300], 0, 2)
        white_rects.append(rect)
        pygame.draw.rect(screen, 'black', [i * len(black_notes), height - 300, len(black_notes)+len(white_notes), 300], 1, 2)
        key_label = medium_font.render(white_notes[i], True, 'black')
        screen.blit(key_label, (i * len(black_notes) + 4, height - 20))
    skip_count = 0
    last_skip = 2
    skip_track = 2
    
    black_rects = []

    for i in range(len(black_notes)):
        rect = pygame.draw.rect(screen, 'black', [nb_float_black + (i * len(black_notes)) + (skip_count * len(black_notes)), height - 300, width/len(white_notes)*0.8, 200], 0, 2)
        for q in range(len(blacks)):
            if blacks[q][0] == i:
                if blacks[q][1] > 0:
                    pygame.draw.rect(screen, 'green', [height/20 + (i * len(black_notes)) + (skip_count * len(black_notes)), height - 300, width/len(white_notes)*0.8, 200], 2, 2)
                    blacks[q][1] -= 1

        key_label = small_font.render(black_notes[i], True, 'white')
        screen.blit(key_label, (nb_float_black + 4 + (i * len(black_notes)) + (skip_count * len(black_notes)), height - 120))
        black_rects.append(rect)
        skip_track += 1
        if last_skip == 2 and skip_track == 3:
            last_skip = 3
            skip_track = 0
            skip_count += 1
        elif last_skip == 3 and skip_track == 2:
            last_skip = 2
            skip_track = 0
            skip_count += 1

    for i in range(len(whites)):
        if whites[i][1] > 0:
            j = whites[i][0]
            pygame.draw.rect(screen, 'green', [j * len(black_notes), height - 100, len(black_notes), 100], 2, 4)
            whites[i][1] -= 1

    return white_rects, black_rects, whites, blacks


