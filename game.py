import pygame
import random
from os import path

from config import *

class OvoVermelho(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    
        OVO_img = pygame.image.load(path.join(img_dir, "OVOA.png")).convert()

        self.image = OVO_img
        
        self.image = pygame.transform.scale(OVO_img,(25,30))
        
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = 60
        self.rect.bottom = HEIGHT - 50
        
        

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    
        player_img = pygame.image.load(path.join(img_dir, "dragaovermelhor.png")).convert()

        self.image = player_img
        
        self.image = pygame.transform.scale(player_img,(30,30))
        
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = 40
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
        
        self.rect.centerx = 30
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
        
        self.rect.centerx = WIDTH - 30
        self.rect.bottom = 60
        
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
        
        self.rect.centerx = WIDTH - 30
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

class OvoVermelho(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    
        OVO_img = pygame.image.load(path.join(img_dir, "OVOV.png")).convert()

        self.image = OVO_img
        
        self.image = pygame.transform.scale(OVO_img,(25,30))
        
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = 60
        self.rect.bottom = HEIGHT - 50

class OvoAzul(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    
        OVOA_img = pygame.image.load(path.join(img_dir, "OVOA.png")).convert()

        self.image = OVOA_img
        
        self.image = pygame.transform.scale(OVOA_img,(25,30))
        
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = WIDTH - 60
        self.rect.bottom = 70
        
#cria classe de parede
class Parede(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, pos):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        parede_img = pygame.image.load(path.join(img_dir, "bloco.jpg")).convert()
        self.image = parede_img
        self.image = pygame.transform.scale(parede_img,(25, 25))
        # Deixando transparente.
        self.image.set_colorkey(WHITE)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
# criando graminha
class Grama(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, pos):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        grama_img = pygame.image.load(path.join(img_dir, "grama.png")).convert()
        self.image = grama_img
        self.image = pygame.transform.scale(grama_img,(25, 25))
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

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

ovo_azul = OvoAzul()
ovo_vermelho = OvoVermelho()
player = Player ()
player2= Player2()
player3= Player3()
player4= Player4()


all_sprites = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(player2)
all_sprites.add(player3)
all_sprites.add(player4)
all_sprites.add(ovo_azul)
all_sprites.add(ovo_vermelho)
bullets = pygame.sprite.Group()
#cria a lista de paredes
paredes = []
grama = []

#cria o mapa
mapa = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WGGGGGG                         W",
"WGWW  G                         W",
"WGWW  G          WW             W",
"WGWW  G                WW       W",
"WG G G G               WW       W",
"W                 WW   WW       W",
"W        WW       WW            W",
"W        WWW                 WWWW",
"W                            WWWW",
"W                  WWW          W",
"W        W                      W",
"W        W                  W   W",
"W  WWW   W          WWWWW   W   W",
"W  WWW              W           W",
"W                   W     W     W",
"W       W                       W",
"W       W                       W",
"W       W           WWW         W",
"W   W    W                      W",
"W                W              W",
"W                W              W",
"W                W              W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]
paredes = pygame.sprite.Group()
grama = pygame.sprite.Group()
x = y = 0
for linha in mapa:
    for coluna in linha:
        if coluna == "W":
            paredes.add(Parede((x, y)))
        elif coluna == "G":
            grama.add(Grama((x,y)))
        x += 25
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
                if event.key == pygame.K_a:
                    player3.esquerda = True
                    bullets.cima = False
                    bullets.baixo = False
                    bullets.esquerda= True
                    bullets.direita = False
                    player3.speedx = -2
                if event.key == pygame.K_d:
                    player3.direita = True
                    bullets.cima = False
                    bullets.baixo = False
                    bullets.esquerda= False
                    bullets.direita = True
                    player3.speedx = 2
                if event.key == pygame.K_s:
                    player3.baixo = True
                    bullets.cima = False
                    bullets.baixo = True
                    bullets.esquerda= False
                    bullets.direita = False
                    player3.speedy = 2
                if event.key == pygame.K_w:
                    player3.cima = True
                    bullets.cima = True
                    bullets.baixo = False
                    bullets.esquerda= False
                    bullets.direita = False
                    player3.speedy = -2   
                if event.key == pygame.K_q:
                    if bullets.esquerda == True:
                        bullet = Bullet(player3.rect.centerx, player3.rect.bottom -5)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedx = -4
                    elif bullets.direita == True:
                        bullet = Bullet(player3.rect.centerx, player3.rect.bottom -5)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedx = 4
                    elif bullets.baixo == True:
                        bullet = Bullet(player3.rect.centerx, player3.rect.top + 20)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedy = 4
                    elif bullets.cima == True:
                        bullet = Bullet(player3.rect.centerx, player3.rect.top +10)
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
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player3.esquerda = False
                    player3.speedx = 0
                if event.key == pygame.K_d:
                    player3.direita = False
                    player3.speedx = 0
                if event.key == pygame.K_w:
                    player3.cima = False
                    player.speedy = 0
                if event.key == pygame.K_s:
                    player3.baixo = False
                    player3.speedy = 0
                                      
        all_sprites.update()

        hits = pygame.sprite.spritecollide(player, paredes, False, pygame.sprite.collide_circle)
        if hits:
            player.speedx = 0
            player.speedy = 0
        hits = pygame.sprite.groupcollide(paredes, bullets, False, True)
        hits = pygame.sprite.groupcollide(grama, bullets, True, True)

        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        paredes.draw(screen)
        grama.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        


