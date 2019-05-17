import pygame
import random
from os import path
from classes import *
from config import *


def game(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    
    ninho_azul = ninhoA()
    ninho_vermelho = ninhoV()
    ovo_azul = OvoAzul()
    ovo_vermelho = OvoVermelho()
    player1= Player ()
    player2= Player2()
    player3= Player3()
    player4= Player4()
    
    ovo_sprites = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    
    all_sprites.add(ninho_azul)
    all_sprites.add(ninho_vermelho)
    all_sprites.add(player1)
    all_sprites.add(player2)
    all_sprites.add(player3)
    all_sprites.add(player4)
    ovo_sprites.add(ovo_azul)
    ovo_sprites.add(ovo_vermelho)
    bullets = pygame.sprite.Group()
    #cria a lista de paredes
    paredes = []
    grama = []
    
    #cria o mapa
    mapa = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "WGGGGGGG        GGGGG           W",
    "WGGWWGGG        GGGGG           W",
    "WGGWWGGG        GWWGG           W",
    "WGGWWGGG        GGGGG  WW       W",
    "W                      WW       W",
    "W                 WW   WW       W",
    "W        WW       WW            W",
    "W        WWW                 WWWW",
    "W                 GGGGG      WWWW",
    "W                 GWWWG         W",
    "W        W   G    GGGGG         W",
    "W        W                  W   W",
    "W  WWW   W          WWWWW   W   W",
    "W  WWW              WGGGG       W",
    "W      GGG          WG    W     W",
    "W      GWG                      W",
    "W      GWG                      W",
    "W      GWGG         WWW         W",
    "W   W   GWG                     W",
    "W        GG      W              W",
    "W                W              W",
    "W                W              W",
    "W                W              W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ]
    paredes = pygame.sprite.Group()
    grama = pygame.sprite.Group()
    x = y = -10
    for linha in mapa:
        for coluna in linha:
            if coluna == "W":
                paredes.add(Parede((x, y)))
            elif coluna == "G":
                grama.add(Grama((x,y)))
            x += 25
        y += 25
        x = 0

    background = pygame.image.load(path.join(img_dir, 'Ultimocenario(espero).png')).convert()
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
                    player1.esquerda = True
                    bullets.cima = False
                    bullets.baixo = False
                    bullets.esquerda= True
                    bullets.direita = False
                    player1.speedx = -2
                if event.key == pygame.K_RIGHT:
                    player1.direita = True
                    bullets.cima = False
                    bullets.baixo = False
                    bullets.esquerda= False
                    bullets.direita = True
                    player1.speedx = 2
                if event.key == pygame.K_DOWN:
                    player1.baixo = True
                    bullets.cima = False
                    bullets.baixo = True
                    bullets.esquerda= False
                    bullets.direita = False
                    player1.speedy = 2
                if event.key == pygame.K_UP:
                    player1.cima = True
                    bullets.cima = True
                    bullets.baixo = False
                    bullets.esquerda= False
                    bullets.direita = False
                    player1.speedy = -2   
                if event.key == pygame.K_SPACE:
                    if bullets.esquerda == True:
                        bullet = Bullet(player1.rect.centerx, player1.rect.bottom -5, 1)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedx = -4
                    elif bullets.direita == True:
                        bullet = Bullet(player1.rect.centerx, player1.rect.bottom -5, 1)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedx = 4
                    elif bullets.baixo == True:
                        bullet = Bullet(player1.rect.centerx, player1.rect.top + 20, 1)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedy = 4
                    elif bullets.cima == True:
                        bullet = Bullet(player1.rect.centerx, player1.rect.top + 10, 1)
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
                        bullet = Bullet(player3.rect.centerx, player3.rect.bottom -5, 3)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedx = -4
                    elif bullets.direita == True:
                        bullet = Bullet(player3.rect.centerx, player3.rect.bottom -5, 3)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedx = 4
                    elif bullets.baixo == True:
                        bullet = Bullet(player3.rect.centerx, player3.rect.top + 20, 3)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedy = 4
                    elif bullets.cima == True:
                        bullet = Bullet(player3.rect.centerx, player3.rect.top +10, 3)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedy = -4               
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player1.esquerda = False
                    player1.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player1.direita = False
                    player1.speedx = 0
                if event.key == pygame.K_UP:
                    player1.cima = False
                    player1.speedy = 0
                if event.key == pygame.K_DOWN:
                    player1.baixo = False
                    player1.speedy = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player3.esquerda = False
                    player3.speedx = 0
                if event.key == pygame.K_d:
                    player3.direita = False
                    player3.speedx = 0
                if event.key == pygame.K_w:
                    player3.cima = False
                    player3.speedy = 0
                if event.key == pygame.K_s:
                    player3.baixo = False
                    player3.speedy = 0
                                      
        all_sprites.update()


        hitsp1 = pygame.sprite.spritecollide(player1, bullets, False, pygame.sprite.collide_circle)
        for b in hitsp1:
            if b.dono != 1:
                player1.vida -= 1
                if player1.vida == 0:
                    player1.deixa_ovo()
                    player1.rect.centerx = 40
                    player1.rect.bottom = HEIGHT - 40
                    player1.vida = 2
        
        hitsp2 = pygame.sprite.spritecollide(player2, bullets, False, pygame.sprite.collide_circle)
        for b in hitsp2:
            if b.dono != 2:
                player2.vida -= 1
                if player2.vida == 0:
                    player2.deixa_ovo()
                    player2.rect.centerx = 40
                    player2.rect.bottom = HEIGHT - 80
                    player2.vida = 2
        
        hitsp3 = pygame.sprite.spritecollide(player3, bullets, False, pygame.sprite.collide_circle)
        for b in hitsp3:
            if b.dono != 3:
                player3.vida -= 1
                if player3.vida == 0:
                    player3.deixa_ovo()
                    player3.rect.centerx = WIDTH - 40
                    player3.rect.bottom = 50
                    player3.vida = 2
        
        hitsp4 = pygame.sprite.spritecollide(player4, bullets, False, pygame.sprite.collide_circle)
        for b in hitsp4:
            if b.dono != 4:
                player4.vida -= 1
                if player4.vida == 0:
                    player4.deixa_ovo()
                    player4.rect.centerx = WIDTH - 40
                    player4.rect.bottom = 80
                    player4.vida = 2


        hits = pygame.sprite.spritecollide(player1, paredes, False, pygame.sprite.collide_circle)
        if hits:
            player1.volta()
#            for parede in hits:
#                if player1.speedx > 0 :
#                    player1.speedx = 0
#                    player1.rect.right = parede.rect.left
#                if player1.speedx < 0 :
#                    player1.speedx = 0
#                    player1.rect.left = parede.rect.right
#                if player1.speedy > 0 :
#                    player1.speedy = 0
#                    player1.rect.top = parede.rect.bottom
#                if player1.speedy < 0 :
#                    player1.speedy = 0
#                    player1.rect.bottom = parede.rect.top
            
        hits = pygame.sprite.spritecollide(player2, paredes, False, pygame.sprite.collide_circle)
        if hits:
            player2.volta()

        hits = pygame.sprite.spritecollide(player3, paredes, False, pygame.sprite.collide_circle)
        if hits:
            player3.volta()
        
        hits = pygame.sprite.spritecollide(player4, paredes, False, pygame.sprite.collide_circle)
        if hits:
            player4.volta()

        hitovo = pygame.sprite.collide_rect(player1, ovo_azul)
        if hitovo:
            player1.toma_ovo(ovo_azul)
        
        
        hitovo3 = pygame.sprite.collide_rect(player3, ovo_vermelho)
        if hitovo3:
            player3.toma_ovo(ovo_vermelho)
        
        hits = pygame.sprite.groupcollide(paredes, bullets, False, True)

        hits = pygame.sprite.groupcollide(grama, bullets, True, True)
        
        hit_win_vermelho = pygame.sprite.spritecollide(ninho_vermelho, ovo_sprites, False, pygame.sprite.collide_circle)
        if hit_win_vermelho:
            for ovo in hit_win_vermelho:
                if ovo.cor == 2:
                    print("time vermelho ganhou")
        
        hit_win_azul = pygame.sprite.spritecollide(ninho_azul, ovo_sprites, False, pygame.sprite.collide_circle)
        if hit_win_azul:
            for ovo in hit_win_azul:
                if ovo.cor == 1:
                    print("time azul ganhou")
        


        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        ovo_sprites.draw(screen)
        paredes.draw(screen)
        grama.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
    return QUIT