import pygame
import random
import time
from os import path

from config import WIDTH, HEIGHT, INIT, GAME, QUIT, WINV, WINA, SETTINGS, CREDITS

from init_screen import init_screen
from win_screen_red import win_screen_red
from game import *

class GameStatus:
    def __init__(self, screen):
        self.milis = 0
        self.screen = screen

# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Capture The Flegg")

game_status = GameStatus(screen)

# Comando para evitar travamentos.
try:
    state = INIT
    while state != QUIT:
        if state == INIT:
            state = init_screen(game_status)
        elif state == GAME:
            state = game(game_status)
        elif state == WINV:
            state = win_screen_red(game_status)
        elif state == WINA:
            state = win_screen_blue(game_status)
        elif state == SETTINGS:
            state = settings(game_status)
        elif state == CREDITS:
            state = creditss(game_status)
        else:
            state = QUIT
finally:
    pygame.quit()

