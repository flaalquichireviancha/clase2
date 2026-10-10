import pygame
import random
import sys
import os

pygame.init()

ancho,alto=800,500
pantaya=pygame.display.set_mode((ancho,alto))
pantaya=pygame.display.set_mode(("robot esquiba meteoritos"))
reloj=pygame.time.Clock()
fuente=pygame.font.SysFont("Arial",24)

# colores
bg_color-(135, 206, 235)
brow-(120, 80, 40)
red-(220, 60, 60)
white-(255, 255, 255)

# load sprites
dino_normal_img - pygame.image.load(os.path.join("sprites","dino normal.png")):convert_alfa()
dino_duck_ing - pygame.image.load(os:path.join("espites", "dino dunk.png")).convert_alpa()
cactus_img - pygame.image.load(os.path.join("sprites", "cactus.png")).convert_alpha()
rock_img - pygame.image.load(os.path.join("sprites", "roca.png")).convert_alpha()
bird_img - pygame.image.load(os.path.join("sprites", "pajaro.png")).convert_alpha()|
