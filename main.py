from numpy import indices
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


iteracion = 1

with open('E:/Fish-weights.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
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
        
        
        fishx = int(random.randint(10,650))#320
        fishy = int(fishx * (9/16))
        
        #Tomar un pez aleatorio
        ranFish = random.randint(1,FishImageAmount)
        fs = pygame.image.load(f"./fish/{ranFish}.png")
        fs = pygame.transform.scale(fs, (fishx,fishy))
        
        #colocar el pez en una posicion aleatoria
        ranx = random.randint(0,xlenght-fishx)
        rany = random.randint(0,ylenght-fishy)
        screen.blit(fs,(ranx,rany))
        #pygame.draw.rect(screen, color, pygame.Rect(ranx, rany, fishx, fishy),2)

        #escribir los datos de la imagen en el archivo
        filewriter.writerow([f"E:/generated/{iteracion}.jpg", ranx,rany,ranx + fishx, int(rany + fishy), 'Fish'])
        
        #Guardar captura de la ventana como imagen
        rect = pygame.Rect(0, 0, xlenght, ylenght)
        sub = screen.subsurface(rect)
        pygame.image.save(sub, f"E:/generated/{iteracion}.jpg")

        iteracion += 1 
        pygame.display.update()