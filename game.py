import pygame
import random
from os import path
from classes import *
from config import *
from win_screen_red import*
from win_screen_blue import*
from SETTINGS import*
from CREDITS import*

def load_assets(snd_dir):
    assets = {}
    assets["Fireball+3"] = pygame.mixer.Sound(path.join(snd_dir, 'Fireball+3.wav'))
    assets["Fireball+3"].set_volume(0.2)
    return assets


def game(game_status):
    screen = game_status.screen
    
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    
    inicio = pygame.time.get_ticks()
    fonte = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)
    
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

    pygame.mixer.music.load(path.join(snd_dir, 'Fire_Emblem_Theme_-_8Bit-he7HEV86ozc.wav'))
    pygame.mixer.music.set_volume(0.4)
    
    pygame.mixer.music.play(loops=-1)
    assets = load_assets(snd_dir)
    pew_sound = assets["Fireball+3"]

    running = True
    while running:
        
        timer = pygame.time.get_ticks()
        milis = timer - inicio
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
                state = QUIT
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player1.dir = LEFT
                    player1.speedx = -2
                if event.key == pygame.K_RIGHT:
                    player1.dir = RIGHT
                    player1.speedx = 2
                if event.key == pygame.K_DOWN:
                    player1.dir = DOWN
                    player1.speedy = 2
                if event.key == pygame.K_UP:
                    player1.dir = UP
                    player1.speedy = -2   
                if event.key == pygame.K_SPACE:
                    pew_sound.play()
                    if player1.dir == LEFT:
                        bullet = Bullet(player1.rect.centerx, player1.rect.bottom -5, 1)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedx = -4
                        
                    elif player1.dir == RIGHT:
                        bullet = Bullet(player1.rect.centerx, player1.rect.bottom -5, 1)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedx = 4
                    elif player1.dir == DOWN:
                        bullet = Bullet(player1.rect.centerx, player1.rect.top + 20, 1)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedy = 4
                    elif player1.dir == UP:
                        bullet = Bullet(player1.rect.centerx, player1.rect.top + 10, 1)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedy = -4
                if event.key == pygame.K_a:
                    player3.dir = LEFT
                    player3.speedx = -2
                if event.key == pygame.K_d:
                    player3.dir = RIGHT
                    player3.speedx = 2
                if event.key == pygame.K_s:
                    player3.dir = DOWN
                    player3.speedy = 2
                if event.key == pygame.K_w:
                    player3.dir = UP
                    player3.speedy = -2   
                if event.key == pygame.K_q:
                    pew_sound.play()
                    if player3.dir == LEFT:
                        bullet = Bullet(player3.rect.centerx, player3.rect.bottom -5, 3)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedx = -4
                    elif player3.dir == RIGHT:
                        bullet = Bullet(player3.rect.centerx, player3.rect.bottom -5, 3)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedx = 4
                    elif player3.dir == DOWN:
                        bullet = Bullet(player3.rect.centerx, player3.rect.top + 20, 3)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedy = 4
                    elif player3.dir == UP:
                        bullet = Bullet(player3.rect.centerx, player3.rect.top +10, 3)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedy = -4  
                if event.key == pygame.K_KP4:
                    player4.dir = LEFT
                    player4.speedx = -2
                if event.key == pygame.K_KP6:
                    player4.dir = RIGHT
                    player4.speedx = 2
                if event.key == pygame.K_KP5:
                    player4.dir = DOWN
                    player4.speedy = 2
                if event.key == pygame.K_KP8:
                    player4.dir = UP
                    player4.speedy = -2   
                if event.key == pygame.K_RETURN:
                    pew_sound.play()
                    if player4.dir == LEFT:
                        bullet = Bullet(player4.rect.centerx, player4.rect.bottom -5, 4)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedx = -4
                    elif player4.dir == RIGHT:
                        bullet = Bullet(player4.rect.centerx, player4.rect.bottom -5, 4)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedx = 4
                    elif player4.dir == DOWN:
                        bullet = Bullet(player4.rect.centerx, player4.rect.top + 20, 4)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedy = 4
                    elif player4.dir == UP:
                        bullet = Bullet(player4.rect.centerx, player4.rect.top + 10, 4)
                        bullet.speedy = -4
                if event.key == pygame.K_g:
                    player2.dir = LEFT
                    player2.speedx = -2
                if event.key == pygame.K_j:
                    player2.dir = RIGHT
                    player2.speedx = 2
                if event.key == pygame.K_h:
                    player2.dir = DOWN
                    player2.speedy = 2
                if event.key == pygame.K_y:
                    player2.dir = UP
                    player2.speedy = -2   
                if event.key == pygame.K_x:
                    pew_sound.play()
                    if player2.dir == LEFT:
                        bullet = Bullet(player2.rect.centerx, player2.rect.bottom -5, 2)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedx = -4
                    elif player2.dir == RIGHT:
                        bullet = Bullet(player2.rect.centerx, player2.rect.bottom -5, 2)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedx = 4
                    elif player2.dir == DOWN:
                        bullet = Bullet(player2.rect.centerx, player2.rect.top + 20, 2)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedy = 4
                    elif player2.dir == UP:
                        bullet = Bullet(player2.rect.centerx, player2.rect.top + 10, 2)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        bullet.speedy = -4
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player1.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player1.speedx = 0
                if event.key == pygame.K_UP:
                    player1.speedy = 0
                if event.key == pygame.K_DOWN:
                    player1.speedy = 0
                if event.key == pygame.K_a:
                    player3.speedx = 0
                if event.key == pygame.K_d:
                    player3.speedx = 0
                if event.key == pygame.K_w:
                    player3.speedy = 0
                if event.key == pygame.K_s:
                    player3.speedy = 0
                if event.key == pygame.K_KP4:
                    player4.speedx = 0
                if event.key == pygame.K_KP6:
                    player4.speedx = 0
                if event.key == pygame.K_KP8:
                    player4.speedy = 0
                if event.key == pygame.K_KP5:
                    player4.speedy = 0
                if event.key == pygame.K_g:
                    player2.speedx = 0
                if event.key == pygame.K_j:
                    player2.speedx = 0
                if event.key == pygame.K_y:
                    player2.speedy = 0
                if event.key == pygame.K_h:
                    player2.speedy = 0
                                      
        all_sprites.update()


        hitsp1 = pygame.sprite.spritecollide(player1, bullets, False, pygame.sprite.collide_circle)
        for b in hitsp1:
            if b.dono != 1 and b.dono != 2:
                player1.vida -= 1
                if player1.vida == 0:
                    player1.deixa_ovo()
                    player1.rect.centerx = 40
                    player1.rect.bottom = HEIGHT - 40
                    player1.vida = 2
        
        hitsp2 = pygame.sprite.spritecollide(player2, bullets, False, pygame.sprite.collide_circle)
        for b in hitsp2:
            if b.dono != 2 and b.dono != 1:
                player2.vida -= 1
                if player2.vida == 0:
                    player2.deixa_ovo()
                    player2.rect.centerx = 40
                    player2.rect.bottom = HEIGHT - 80
                    player2.vida = 2
        
        hitsp3 = pygame.sprite.spritecollide(player3, bullets, False, pygame.sprite.collide_circle)
        for b in hitsp3:
            if b.dono != 3 and b.dono != 4:
                player3.vida -= 1
                if player3.vida == 0:
                    player3.deixa_ovo()
                    player3.rect.centerx = WIDTH - 40
                    player3.rect.bottom = 50
                    player3.vida = 2
        
        hitsp4 = pygame.sprite.spritecollide(player4, bullets, False, pygame.sprite.collide_circle)
        for b in hitsp4:
            if b.dono != 4 and b.dono != 3:
                player4.vida -= 1
                if player4.vida == 0:
                    player4.deixa_ovo()
                    player4.rect.centerx = WIDTH - 40
                    player4.rect.bottom = 80
                    player4.vida = 2


        hits = pygame.sprite.spritecollide(player1, paredes, False, pygame.sprite.collide_circle)
        if hits:
            player1.volta()
            
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
            
        hitovo4 = pygame.sprite.collide_rect(player4, ovo_vermelho)
        if hitovo4:
            player4.toma_ovo(ovo_vermelho)
        
        hitovo2 = pygame.sprite.collide_rect(player2, ovo_azul)
        if hitovo2:
            player2.toma_ovo(ovo_azul)
        
        hits = pygame.sprite.groupcollide(paredes, bullets, False, True)

        hits = pygame.sprite.groupcollide(grama, bullets, True, True)
        
        hit_win_vermelho = pygame.sprite.spritecollide(ninho_vermelho, ovo_sprites, False, pygame.sprite.collide_circle)
        if hit_win_vermelho:
            for ovo in hit_win_vermelho:
                if ovo.cor == 2:
                    state = WINV
                    running  = False
                        
        
        hit_win_azul = pygame.sprite.spritecollide(ninho_azul, ovo_sprites, False, pygame.sprite.collide_circle)
        if hit_win_azul:
            for ovo in hit_win_azul:
                if ovo.cor == 1:
                    state = WINA
                    running  = False
                    
        


        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        ovo_sprites.draw(screen)
        paredes.draw(screen)
        grama.draw(screen)
        
        
        # Desenha o score
        mi = milis % 1000
        s = milis//1000
        
        text_surface = fonte.render("{0}.{1:03d}".format(s, mi), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        screen.blit(text_surface, text_rect)

        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
        
    game_status.milis = milis
    
    return state