import pygame
import random
import time

from os import path

from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from init_screen import init_screen
from game import *

# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Capture The Flegg")

# Comando para evitar travamentos.
try:
    state = INIT
    while state != QUIT:
        if state == INIT:
            state = init_screen(screen)
        elif state == GAME:
            state = game(screen)
        else:
            state = QUIT
finally:
    pygame.quit()