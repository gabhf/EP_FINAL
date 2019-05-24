import pygame
import random
from os import path
from config import*

from config import img_dir, BLACK, FPS, GAME, QUIT, INIT

def win_screen_blue(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(img_dir, 'time azul.png')).convert()
    background_rect = background.get_rect()

    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            elif event.type == pygame.KEYDOWN:
                state = INIT
                running = False

        screen.fill(BLACK)
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state