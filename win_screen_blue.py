import pygame
import random
from os import path
from config import*

from config import img_dir, BLACK, FPS, GAME, QUIT, INIT



def win_screen_blue(game_status):
    screen = game_status.screen
    
    fonte = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)
    

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
                if event.key == pygame.K_BACKSPACE:
                    state = INIT
                    running = False
                

        screen.fill(BLACK)
        screen.blit(background, background_rect)
        
        text_surface = fonte.render("Tempo: {0}s".format(game_status.milis/1000), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        screen.blit(text_surface, text_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state