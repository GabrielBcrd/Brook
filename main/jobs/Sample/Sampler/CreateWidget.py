import pygame

def draw_knobman(screen,x,y,data,color):
    match color:
        case "red":
            img  = pygame.image.load("BDD\Image\KNB_metal_red_L.png")
            img2 = pygame.transform.rotate(img,data)
            screen.blit(img2,(x,y))
        case "blue":
            img = pygame.image.load("BDD\Image\KNB_metal_blue_L.png")
            img2= pygame.transform.rotate(img,data)
            screen.blit(img2,(x,y))
    
    return img
