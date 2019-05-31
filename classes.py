import pygame
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        
        vida = 1
        self.vida = vida
        pygame.sprite.Sprite.__init__(self)
    
        player_img = pygame.image.load(path.join(img_dir, "dragaovermelhor.png")).convert()

        self.image = player_img
        
        self.image = pygame.transform.scale(player_img,(30,30))
        
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = 40
        self.rect.bottom = HEIGHT - 40
        
        self.x_prev = self.rect.x
        self.y_prev = self.rect.y
                
        self.speedx = 0
        self.speedy = 0

        self.radius = 10
        
        self.dir = RIGHT
        
        self.ovo = None
        
    def update(self):
        if self.dir == RIGHT:
            player_img = pygame.image.load(path.join(img_dir, "dragaovermelhor.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(WHITE)
            
        elif self.dir == LEFT:
            player_img = pygame.image.load(path.join(img_dir, "dragaovermelhol.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
            
            self.image.set_colorkey(WHITE)
        
        elif self.dir == DOWN:
            player_img = pygame.image.load(path.join(img_dir, "dragaovermelhod.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(WHITE)
        elif self.dir == UP:
            player_img = pygame.image.load(path.join(img_dir, "dragaovermelhou.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(WHITE)
        
        self.x_prev = self.rect.x
        self.y_prev = self.rect.y
        
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
            
        if self.ovo:
            self.ovo.rect.x = self.rect.x
            self.ovo.rect.y = self.rect.y

    def volta(self):        
        self.rect.x = self.x_prev
        self.rect.y = self.y_prev

    def toma_ovo(self, ovo):
        self.ovo = ovo
        
    def deixa_ovo(self):
        self.ovo = None
            
            
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        
        vida = 1
        self.vida = vida
        
        pygame.sprite.Sprite.__init__(self)
        
        player_img = pygame.image.load(path.join(img_dir, "dragaoroxor.png")).convert()

        self.image = player_img
        
        self.image = pygame.transform.scale(player_img,(30,30))
        
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = 40
        self.rect.bottom = HEIGHT - 80

        self.x_prev = self.rect.x
        self.y_prev = self.rect.y
        
        self.speedx = 0
        self.speedy = 0

        self.radius = 10
    
        self.dir = RIGHT
        
        self.ovo = None
        
    def update(self):
        if self.dir == RIGHT:
            player_img = pygame.image.load(path.join(img_dir, "dragaoroxor.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(WHITE)
            
        elif self.dir==LEFT:
            player_img = pygame.image.load(path.join(img_dir, "dragaoroxol.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
            
            self.image.set_colorkey(WHITE)
        
        elif self.dir == DOWN:
            player_img = pygame.image.load(path.join(img_dir, "dragaoroxod.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(WHITE)
        elif self.dir==UP:
            player_img = pygame.image.load(path.join(img_dir, "dragaoroxou.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(WHITE)

        self.x_prev = self.rect.x
        self.y_prev = self.rect.y
            
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
            
        if self.ovo:
            self.ovo.rect.x = self.rect.x
            self.ovo.rect.y = self.rect.y

   
    def volta(self):        
        self.rect.x = self.x_prev
        self.rect.y = self.y_prev

    def toma_ovo(self, ovo):
        self.ovo = ovo
        
    def deixa_ovo(self):
        self.ovo = None

class Player3(pygame.sprite.Sprite):
    def __init__(self):
        
        vida = 1
        self.vida = vida
        pygame.sprite.Sprite.__init__(self)
        
        player_img = pygame.image.load(path.join(img_dir, "dragaoazull2.png")).convert()
        self.image = player_img
        
        self.image = pygame.transform.scale(player_img,(30,30))
        
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = WIDTH - 40
        self.rect.bottom = 50

        self.x_prev = self.rect.x
        self.y_prev = self.rect.y
        
        self.speedx = 0
        self.speedy = 0

        self.radius = 10

        self.dir = LEFT
        
        self.ovo = None        
    
    def update(self):
        if self.dir == RIGHT:
            player_img = pygame.image.load(path.join(img_dir, "dragaoazulr2.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(BLACK)
            
        elif self.dir == LEFT:
            player_img = pygame.image.load(path.join(img_dir, "dragaoazull2.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
            
            self.image.set_colorkey(BLACK)
        
        elif self.dir == DOWN:
            player_img = pygame.image.load(path.join(img_dir, "dragaoazuld2.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(BLACK)
        elif self.dir == UP:
            player_img = pygame.image.load(path.join(img_dir, "dragaoazulu2.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(BLACK)

        self.x_prev = self.rect.x
        self.y_prev = self.rect.y

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
            
        if self.ovo:
            self.ovo.rect.x = self.rect.x
            self.ovo.rect.y = self.rect.y
            
        
    def volta(self):        
        self.rect.x = self.x_prev
        self.rect.y = self.y_prev

    def toma_ovo(self, ovo):
        self.ovo = ovo
        
    def deixa_ovo(self):
        self.ovo = None

class Player4(pygame.sprite.Sprite):
    def __init__(self):
        
        vida = 1
        self.vida = vida
        
        pygame.sprite.Sprite.__init__(self)
        
        player_img = pygame.image.load(path.join(img_dir, "dragaoverdel.png")).convert()

        self.image = player_img
        
        self.image = pygame.transform.scale(player_img,(30,30))
        
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = WIDTH - 40
        self.rect.bottom = 80

        self.x_prev = self.rect.x
        self.y_prev = self.rect.y
        
        self.speedx = 0
        self.speedy = 0

        self.radius = 10

        self.dir = LEFT
        
        self.ovo = None
        
    
    def update(self):
        if self.dir == RIGHT:
            player_img = pygame.image.load(path.join(img_dir, "dragaoverder.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(WHITE)
            
        elif self.dir == LEFT:
            player_img = pygame.image.load(path.join(img_dir, "dragaoverdel.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
            
            self.image.set_colorkey(WHITE)
        
        elif self.dir == DOWN:
            player_img = pygame.image.load(path.join(img_dir, "dragaoverded.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(WHITE)
        elif self.dir == UP:
            player_img = pygame.image.load(path.join(img_dir, "dragaoverdeu.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img,(30,30))
        
            self.image.set_colorkey(WHITE)

        self.x_prev = self.rect.x
        self.y_prev = self.rect.y

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
            
        if self.ovo:
            self.ovo.rect.x = self.rect.x
            self.ovo.rect.y = self.rect.y
            

    def volta(self):        
        self.rect.x = self.x_prev
        self.rect.y = self.y_prev

    def toma_ovo(self, ovo):
        self.ovo = ovo
        
    def deixa_ovo(self):
        self.ovo = None

class ninhoV(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    
        ninho_img = pygame.image.load(path.join(img_dir, "ninho.png")).convert()

        self.image = ninho_img
        
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = 85
        self.rect.bottom = HEIGHT - 30
        
class ninhoA(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    
        ninho_img = pygame.image.load(path.join(img_dir, "ninhoA.png")).convert()

        self.image = ninho_img
        
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = WIDTH - 85
        self.rect.bottom = 130

class OvoVermelho(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    
        OVO_img = pygame.image.load(path.join(img_dir, "OVOV.png")).convert()

        self.image = OVO_img
        
        self.image = pygame.transform.scale(OVO_img,(35,40))
        
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = 80
        self.rect.bottom = HEIGHT - 60

        self.speedx = 0
        self.speedy = 0
        
        self.speedx = 0
        self.speedy = 0
        
        self.cor = 1 
        
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
         

class OvoAzul(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    
        OVOA_img = pygame.image.load(path.join(img_dir, "OVOA.png")).convert()

        self.image = OVOA_img
        
        self.image = pygame.transform.scale(OVOA_img,(25,35))
        
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = WIDTH - 100
        self.rect.bottom = 90
        
        self.speedx = 0
        self.speedy = 0
        
        self.cor = 2
        
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
    
   
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
        self.image = pygame.transform.scale(grama_img,(25, 26))
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

#cria o projétil do dragão
class Bullet(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, x, y, dono):
        
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
        
        self.dono = dono
        
    # Metodo que atualiza a posição da bullet
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o tiro passar da tela, morre.
        if self.rect.bottom < 0:
            self.kill()
        elif self.rect.top > HEIGHT:
            self.kill()
        elif self.rect.left < 0:
            self.kill()
        elif self.rect.right > WIDTH:
            self.kill()

