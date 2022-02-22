import pygame, sys, time, random, csv
from pygame.locals import *

# configurar pygame
pygame.init()
relojPrincipal = pygame.time.Clock()

#Variables para el funcionamiendo del algoritmo
BackgroundImageAmount = 13
FishImageAmount = 9

xlenght = 1080
ylenght = 720

fishx = 320
fishy = fishx * (9/16)
color = (255,0,0)

# configurar la ventana
screen = pygame.display.set_mode((xlenght, ylenght), 0, 32)
pygame.display.set_caption('Generador de imagenes para entrenamiento de IA')



while True:
    # comprobar si se ha disparado el evento QUIT (salir)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
            
    #Tomar un background aleatorio
    ranBG = random.randint(1,BackgroundImageAmount)
    bg = pygame.image.load(f"./background/{ranBG}.jpeg")
    bg = pygame.transform.scale(bg, (xlenght, ylenght))
    screen.blit(bg,(0,0))
    
    #Tomar un pez aleatorio
    ranFish = random.randint(1,FishImageAmount)
    fs = pygame.image.load(f"./fish/{ranFish}.png")
    fs = pygame.transform.scale(fs, (fishx,fishy))
    #screen.blit(fs,(0,0))
    ranx = random.randint(0,xlenght-fishx)
    rany = random.randint(0,ylenght-fishy)
    screen.blit(fs,(ranx,rany))
    fishRect = fs.get_rect()
    print(fishRect.left)
    print(fishRect.top)
    print(fishRect.width)
    print(fishRect.height)
    pygame.draw.rect(screen, color, pygame.Rect(ranx, rany, fishx, fishy),2)
    
    
    
    

    time.sleep(.5)
    pygame.display.update()