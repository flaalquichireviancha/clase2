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
cielo = (10,10,40)
blanco = (255,255,255)
rojo = (220, 60, 60)

# --- cargar imagenes desde la carpeta "imagenes"---
robot_img = pygame.image.load(os.path.join("imagenes", "robot.png"))
meteorito_img = pygame.image.load(os.path.join("imagenes", "meteorito.png"))

# ---cambiar eltamaño de las imagenes---
robot_img = pygame.transform.scale(robot_img, (60, 60))
meteorito_img = pygame.transform.scale(meteorito_img, (40, 40))