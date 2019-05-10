import pygame
import random
from os import path

from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    
        player_img = pygame.image.load(path.join(img_dir, "dragaovermelhor.png")).convert()

        self.image = player_img
        
        self.image = pygame.transform.scale(player_img,(30,30))
        
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = 20
        self.rect.bottom = HEIGHT - 40
        
        self.speedx = 0
        self.speedy = 0

        self.radius = 10
        
        self.direita = False
        self.esquerda = False
        self.baixo = False
        self.cima = False
        
    def update(self):
        if self.direita:
            player_img = pygame.image.load(path.join(img_dir, "dragaovermelhor.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(WHITE)
            
        elif self.esquerda:
            player_img = pygame.image.load(path.join(img_dir, "dragaovermelhol.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
            
            self.image.set_colorkey(WHITE)
        
        elif self.baixo:
            player_img = pygame.image.load(path.join(img_dir, "dragaovermelhod.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(WHITE)
        elif self.cima:
            player_img = pygame.image.load(path.join(img_dir, "dragaovermelhou.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(WHITE)
        
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
        
        player_img = pygame.image.load(path.join(img_dir, "dragaoroxor.png")).convert()

        self.image = player_img
        
        self.image = pygame.transform.scale(player_img,(30,30))
        
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = 20
        self.rect.bottom = HEIGHT - 90
        
        self.speedx = 0
        self.speedy = 0

        self.radius = 10
    
        self.direita = False
        self.esquerda = False
        self.baixo = False
        self.cima = False
        
    def update(self):
        if self.direita:
            player_img = pygame.image.load(path.join(img_dir, "dragaoroxor.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(WHITE)
            
        elif self.esquerda:
            player_img = pygame.image.load(path.join(img_dir, "dragaoroxol.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
            
            self.image.set_colorkey(WHITE)
        
        elif self.baixo:
            player_img = pygame.image.load(path.join(img_dir, "dragaoroxod.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(WHITE)
        elif self.cima:
            player_img = pygame.image.load(path.join(img_dir, "dragaoroxou.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(WHITE)
            
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
        
        player_img = pygame.image.load(path.join(img_dir, "dragaoazull.png")).convert()
        self.image = player_img
        
        self.image = pygame.transform.scale(player_img,(30,30))
        
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = WIDTH - 20
        self.rect.bottom = 40
        
        self.speedx = 0
        self.speedy = 0

        self.radius = 10

        self.direita = False
        self.esquerda = False
        self.baixo = False
        self.cima = False
    
    def update(self):
        if self.direita:
            player_img = pygame.image.load(path.join(img_dir, "dragaoazulr.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(WHITE)
            
        elif self.esquerda:
            player_img = pygame.image.load(path.join(img_dir, "dragaoazull.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
            
            self.image.set_colorkey(WHITE)
        
        elif self.baixo:
            player_img = pygame.image.load(path.join(img_dir, "dragaoazuld.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(WHITE)
        elif self.cima:
            player_img = pygame.image.load(path.join(img_dir, "dragaoazulu.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(WHITE)

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
        
        player_img = pygame.image.load(path.join(img_dir, "dragaoverdel.png")).convert()

        self.image = player_img
        
        self.image = pygame.transform.scale(player_img,(30,30))
        
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = WIDTH - 20
        self.rect.bottom = 100
        
        self.speedx = 0
        self.speedy = 0

        self.radius = 10

        self.direita = False
        self.esquerda = False
        self.baixo = False
        self.cima = False
    
    def update(self):
        if self.direita:
            player_img = pygame.image.load(path.join(img_dir, "dragaoverder.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(WHITE)
            
        elif self.esquerda:
            player_img = pygame.image.load(path.join(img_dir, "dragaoverdel.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
            
            self.image.set_colorkey(WHITE)
        
        elif self.baixo:
            player_img = pygame.image.load(path.join(img_dir, "dragaoverded.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(WHITE)
        elif self.cima:
            player_img = pygame.image.load(path.join(img_dir, "dragaoverdeu.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(WHITE)

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
#cria classe de parede
class Parede(object):
    def __init__(self, pos):
        paredes.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 25,25 )
#cria o projétil do dragão
class Bullet(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, x, y):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        bullet_img = pygame.image.load(path.join(img_dir, "sol.png")).convert()
        self.image = bullet_img
        self.image = pygame.transform.scale(bullet_img,(30, 20))
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 0
        self.speedx = 0

        self.direita = False
        self.esquerda = False
        self.baixo = False
        self.cima = False
    # Metodo que atualiza a posição da bullet
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()
        elif self.rect.top > HEIGHT:
            self.kill()
        elif self.rect.left < 0:
            self.kill()
        elif self.rect.right > WIDTH:
            self.kill()

# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()



player = Player ()
player2= Player2()
player3= Player3()
player4= Player4()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(player2)
all_sprites.add(player3)
all_sprites.add(player4)

bullets = pygame.sprite.Group()
#cria a lista de paredes
paredes = []

#cria o mapa
mapa = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WGGGGGG                     W   W",
"WGWWWGG           W         W   W",
"WGWWWGG           W         WW  W",
"WGWWWGG           W    WWW   W  W",
"WGGGGGG                WWW      W",
"W        WWW      WWW  WWW      W",
"W        WWW      WWW        WWWW",
"W        WWW      WWW        WWWW",
"W                            WWWW",
"W                               W",
"W      WWW          WW  W       W",
"W      WWW              W   WWW W",
"WWWW   WWW           WWWW   WWW W",
"WWWW                            W",
"WWWW                            W",
"W       W               W  W    W",
"W       W       WWWWWWWW        W",
"W       W                       W",
"W  W    W                       W",
"W  WWWWWW                       W",
"W  WWWWWW                       W",
"W  WWWWWW                       W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

x = y = 0
for linha in mapa:
    for coluna in linha:
        if coluna == "W":
            Parede((x, y))
        x += 24.5
    y += 25
    x = 0

def game(screen):
    background = pygame.image.load(path.join(img_dir, 'Cenario top.png')).convert()
    background_rect = background.get_rect()
    
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
                    player.esquerda = True
                    bullets.cima = False
                    bullets.baixo = False
                    bullets.esquerda= True
                    bullets.direita = False
                    player.speedx = -2
                if event.key == pygame.K_RIGHT:
                    player.direita = True
                    bullets.cima = False
                    bullets.baixo = False
                    bullets.esquerda= False
                    bullets.direita = True
                    player.speedx = 2
                if event.key == pygame.K_DOWN:
                    player.baixo = True
                    bullets.cima = False
                    bullets.baixo = True
                    bullets.esquerda= False
                    bullets.direita = False
                    player.speedy = 2
                if event.key == pygame.K_UP:
                    player.cima = True
                    bullets.cima = True
                    bullets.baixo = False
                    bullets.esquerda= False
                    bullets.direita = False
                    player.speedy = -2   
                if event.key == pygame.K_SPACE:
                    if bullets.esquerda == True:
                        bullet = Bullet(player.rect.centerx, player.rect.bottom -5)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedx = -4
                    elif bullets.direita == True:
                        bullet = Bullet(player.rect.centerx, player.rect.bottom -5)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedx = 4
                    elif bullets.baixo == True:
                        bullet = Bullet(player.rect.centerx, player.rect.top + 20)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedy = 4
                    elif bullets.cima == True:
                        bullet = Bullet(player.rect.centerx, player.rect.top +10)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedy = -4               
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.esquerda = False
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.direita = False
                    player.speedx = 0
                if event.key == pygame.K_UP:
                    player.cima = False
                    player.speedy = 0
                if event.key == pygame.K_DOWN:
                    player.baixo = False
                    player.speedy = 0
                                      
        all_sprites.update()
            
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        for parede in paredes:
            pygame.draw.rect(screen, (WHITE), parede.rect)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        


