# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import random
import pygame
from os import path

# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')
# Dados gerais do jogo.
WIDTH = 550 # Largura da tela
HEIGHT = 340 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREN = (0, 255, 0)
BLU = (0, 0, 255)
YELLO = (255, 255, 0)
PORPLE = (200,0,255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        player_img = pygame.image.load(path.join(img_dir, "spritedragao.png")).convert()
        self.image = player_img
        
        self.image = pygame.transform.scale(player_img,(30,18))
        
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = 20
        self.rect.bottom = HEIGHT - 40
        
        self.speedx = 0
        self.speedy = 0

        self.radius = 25
    
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        if self.rect.top < 0:
            self.rect.top = 0

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        player_img = pygame.image.load(path.join(img_dir, "dragaoroxo.png")).convert()
        self.image = player_img
        
        self.image = pygame.transform.scale(player_img,(30, 18))
        
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = 20
        self.rect.bottom = HEIGHT - 90
        
        self.speedx = 0
        self.speedy = 0

        self.radius = 25
    
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        if self.rect.top < 0:
            self.rect.top = 0

class Player3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        player_img = pygame.image.load(path.join(img_dir, "dragaoazul.png")).convert()
        self.image = player_img
        
        self.image = pygame.transform.scale(player_img,(30,18))
        
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = WIDTH - 20
        self.rect.bottom = 40
        
        self.speedx = 0
        self.speedy = 0

        self.radius = 25
    
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        if self.rect.top < 0:
            self.rect.top = 0            

class Player4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        player_img = pygame.image.load(path.join(img_dir, "dragaoverde.png")).convert()
        self.image = player_img
        
        self.image = pygame.transform.scale(player_img,(30,18))
        
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = WIDTH - 20
        self.rect.bottom = 100
        
        self.speedx = 0
        self.speedy = 0

        self.radius = 25
    
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        if self.rect.top < 0:
            self.rect.top = 0
# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Dragao")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

background = pygame.image.load(path.join(img_dir, '14-shading.png')).convert()
background_rect = background.get_rect()
backgorund_rect = pygame.transform.scale(background,(WIDTH,HEIGHT))


player = Player ()
player2= Player2()
player3= Player3()
player4= Player4()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(player2)
all_sprites.add(player3)
all_sprites.add(player4)



try:
    
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.speedx = -2
                if event.key == pygame.K_RIGHT:
                    player.speedx = 2
                if event.key == pygame.K_DOWN:
                    player.speedy = 2
                if event.key == pygame.K_UP:
                    player.speedy = -2    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                if event.key == pygame.K_UP:
                    player.speedy = 0
                if event.key == pygame.K_DOWN:
                    player.speedy = 0
                                      
        all_sprites.update()
            
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()