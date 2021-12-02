import pygame
import random
import os
import sys

from config import IMG_DIR, BLACK, FPS, GAME, QUIT

from pygame import rect
from pygame import image
pygame.init()

def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(os.path.join(IMG_DIR, 'Inicio.png')).convert()
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

            if event.type == pygame.KEYUP:
                state = GAME
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return True
oi = True
while oi:
    WIDTH=1360
    HEIGHT= 720
    game = True
    vitoria = True
    level = 30
    level2 = 6
    pygame.display.set_caption('BomberFox')
    surf= pygame.display.set_mode([WIDTH,HEIGHT])
    surf.fill([0,110,110])

    paredes = pygame.image.load("parede.png")
    blocos = pygame.image.load("bloco.png")
    personagem = pygame.image.load('Raposa_frente.gif').convert_alpha()
    jacare = pygame.image.load('jacaré.gif').convert_alpha()
    bomba = pygame.image.load('Bomba.png').convert_alpha()
    porta = pygame.image.load('porta.png').convert_alpha()
    explosao = pygame.image.load('Explosao.png').convert_alpha()
    fake = pygame.image.load('Fake.png').convert_alpha()
    ex_cima = pygame.image.load('Ex_cima.png').convert_alpha()
    ex_baixo = pygame.image.load('Ex_baixo.png').convert_alpha()
    ex_direita = pygame.image.load('Ex_direita.png').convert_alpha()
    ex_esquerda = pygame.image.load('Ex_esquerda.png').convert_alpha()

    Passos = pygame.mixer.Sound(os.path.join("Passos.wav"))
    Explo = pygame.mixer.Sound(os.path.join("assets", "img", "expl3.wav"))
    musica = os.path.join("musica.ogg")
    pygame.mixer.music.load(musica)
    pygame.mixer.music.set_volume(0)
    pygame.mixer.music.play(-1)


    game = init_screen(surf)

    all_sprites_ex = pygame.sprite.Group()
    all_sprites_blocos = pygame.sprite.Group()
    all_sprites_bombas = pygame.sprite.Group()
    all_sprites_paredes = pygame.sprite.Group()
    all_porta = pygame.sprite.Group()
    all_player = pygame.sprite.Group()
    all_jacare = pygame.sprite.Group()
    all_sprites_ex_c = pygame.sprite.Group()
    all_sprites_ex_b = pygame.sprite.Group()
    all_sprites_ex_d = pygame.sprite.Group()
    all_sprites_ex_e = pygame.sprite.Group()

    #colocar paredes
    a = []
    b = []
    pos_parede = []
    i = 80
    while i < 1280: #lista das posicoes especificas
        a.append(i)
        i = i + 160
    i = 80
    while i < 600:
        b.append(i)
        i = i + 160
    for f in a: #colocar as paredes nas posicoes
        for j in b:
            pos_parede.append([f,j])
    for x in a:
        for y in b:
            class Parede(pygame.sprite.Sprite):
                def __init__(self, img):
                    pygame.sprite.Sprite.__init__(self)

                    self.image = img
                    self.rect = self.image.get_rect()
                    self.rect.centerx = x + 40
                    self.rect.centery = y + 40
                    self.speedx = 0
                    self.speedy= 0


            pygame.display.update()
            clock= pygame.time.Clock()
            Paredes= Parede(paredes)
            all_sprites_paredes.add(Paredes)
    #_____________________________
    #colocar blocos

    x = []
    y = []
    pos_bloco = []
    i = 80
    while i < 1360: #lista das posicoes
        x.append(i)
        i = i + 80
    i = 0
    while i < 720:
        y.append(i)
        i = i + 80
    i = 0
    while i < level:    #pegar posicoes aleatorias
        aleatorioc = random.choice(x)
        aleatoriod = random.choice(y)
        pos2 = [aleatorioc,aleatoriod]
        if pos2 not in pos_parede: #colocar o bloco se a posiçao não for igual a parede
            pos_bloco.append(pos2)
            i = i + 1

    for p in pos_bloco:
        class Bloco(pygame.sprite.Sprite):
            def __init__(self, img):
                pygame.sprite.Sprite.__init__(self)

                self.image = img
                self.rect = self.image.get_rect()
                self.rect.centerx = p[0] + 40
                self.rect.centery = p[1] + 40
                self.speedx = 0
                self.speedy= 0


        Blocos = Bloco(blocos)
        all_sprites_blocos.add(Blocos)
    #___________________________
    #posicionar porta da vitoria
    class Porta(pygame.sprite.Sprite):
        def __init__(self, img, pos):
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.center = random.choice(pos)
            self.rect.centerx += 40
            self.rect.centery += 40
    #____________________________
    #Movimento do personagem

    class Raposa(pygame.sprite.Sprite):
        def __init__(self, img):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = 40
            self.rect.centerx= 40
            #self.rect.top = 0
            self.speedx = 0
            self.speedy= 0

        def update(self):
            # Atualização da posição da nave
            self.rect.x += self.speedx
            self.rect.y += self.speedy

    
            for s in all_sprites_paredes:
                if self.rect.right > s.rect.left and self.rect.left < s.rect.right and self.rect.bottom > s.rect.top and self.rect.top < s.rect.bottom:
                    if self.rect.centerx-20 > s.rect.centerx+20:
                        self.rect.left = s.rect.right
                    elif self.rect.centerx+20 < s.rect.centerx-20:
                        self.rect.right = s.rect.left
                    elif self.rect.centery-20 < s.rect.centery+20:
                        self.rect.bottom = s.rect.top
                    elif self.rect.centery+20 > s.rect.centery-20:
                        self.rect.top = s.rect.bottom
            for s in all_sprites_blocos:
                if self.rect.right > s.rect.left and self.rect.left < s.rect.right and self.rect.bottom > s.rect.top and self.rect.top < s.rect.bottom:
                    if self.rect.centerx-20 > s.rect.centerx+20:
                        self.rect.left = s.rect.right
                    elif self.rect.centerx+20 < s.rect.centerx-20:
                        self.rect.right = s.rect.left
                    elif self.rect.centery-20 < s.rect.centery+20:
                        self.rect.bottom = s.rect.top
                    elif self.rect.centery+20 > s.rect.centery-20:
                        self.rect.top = s.rect.bottom
                
            # Mantem dentro da tela
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT

    class Ini(pygame.sprite.Sprite):
        def __init__(self, img):
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = ale[0] +40
            self.rect.bottom = ale[1] -9
            self.speedx = -3

        def update(self):

            for s in all_sprites_paredes:
                if self.rect.right > s.rect.left and self.rect.left < s.rect.right and self.rect.bottom > s.rect.top and self.rect.top < s.rect.bottom:
                    if self.rect.centerx-20 > s.rect.centerx+20:
                        self.rect.left = s.rect.right
                    elif self.rect.centerx+20 < s.rect.centerx-20:
                        self.rect.right = s.rect.left
                    elif self.rect.centery-20 < s.rect.centery+20:
                        self.rect.bottom = s.rect.top
                    elif self.rect.centery+20 > s.rect.centery-20:
                        self.rect.top = s.rect.bottom
                    self.speedx = -(self.speedx)
            for s in all_sprites_blocos:
                if self.rect.right > s.rect.left and self.rect.left < s.rect.right and self.rect.bottom > s.rect.top and self.rect.top < s.rect.bottom:
                    if self.rect.centerx-20 > s.rect.centerx+20:
                        self.rect.left = s.rect.right
                    elif self.rect.centerx+20 < s.rect.centerx-20:
                        self.rect.right = s.rect.left
                    elif self.rect.centery-20 < s.rect.centery+20:
                        self.rect.bottom = s.rect.top
                    elif self.rect.centery+20 > s.rect.centery-20:
                        self.rect.top = s.rect.bottom
                    self.speedx = -(self.speedx)       
            for s in all_sprites_bombas:
                if self.rect.right > s.rect.left and self.rect.left < s.rect.right and self.rect.bottom > s.rect.top and self.rect.top < s.rect.bottom:
                    if self.rect.centerx-20 > s.rect.centerx+20:
                        self.rect.left = s.rect.right
                    elif self.rect.centerx+20 < s.rect.centerx-20:
                        self.rect.right = s.rect.left
                    elif self.rect.centery-20 < s.rect.centery+20:
                        self.rect.bottom = s.rect.top
                    elif self.rect.centery+20 > s.rect.centery-20:
                        self.rect.top = s.rect.bottom
                    self.speedx = -(self.speedx)

            self.rect.x += self.speedx
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
                self.speedx = -3
            if self.rect.left < 0:
                self.rect.left = 0
                self.speedx = 3


    class Bomba(pygame.sprite.Sprite):
        def __init__(self, img, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = x 
            self.rect.centery = y 
            self.tempo = 90
        def update(self):
            self.tempo -= 1
        def contagem (self):
            if self.tempo == 32:
                self.image= explosao
                self.add(all_sprites_ex)
                Explo.play()
            if self.tempo <= 0:
                self.kill()

    class Explosao_cima(pygame.sprite.Sprite):
        def __init__(self, img, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = x 
            self.rect.centery = y -80
            self.tempo = 90
        def update(self):
            self.tempo -= 1
        def contagem (self):
            if self.tempo == 30:
                self.image= ex_cima
                self.add(all_sprites_ex)
            if self.tempo <= 0:
                self.kill() 

    class Explosao_baixo(pygame.sprite.Sprite):
        def __init__(self, img, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = x 
            self.rect.centery = y +80
            self.tempo = 90
        def update(self):
            self.tempo -= 1
        def contagem (self):
            if self.tempo == 30:
                self.image= ex_baixo
                self.add(all_sprites_ex)
            if self.tempo <= 0:
                self.kill()

    class Explosao_direita(pygame.sprite.Sprite):
        def __init__(self, img, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = x +80
            self.rect.centery = y 
            self.tempo = 90
        def update(self):
            self.tempo -= 1
        def contagem (self):
            if self.tempo == 30:
                self.image= ex_direita
                self.add(all_sprites_ex)
            if self.tempo <= 0:
                self.kill()

    class Explosao_esquerda(pygame.sprite.Sprite):
        def __init__(self, img, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = x -80
            self.rect.centery = y 
            self.tempo = 90
        def update(self):
            self.tempo -= 1
        def contagem (self):
            if self.tempo == 30:
                self.image= ex_esquerda
                self.add(all_sprites_ex)
            if self.tempo <= 0:
                self.kill()



    player= Raposa(personagem)
    all_player.add(player)
    porta2= Porta(porta,pos_bloco)
    all_porta.add(porta2)
    #____________________________

    #Inimigo

    mob = 0
    pos_jacare = []
    espaço_vazio = []
    todas_pos = []
    for x in x:
        for yy in y:
            todas_pos.append([x,yy])
    for t in todas_pos:
        if t not in pos_parede and t not in pos_parede:
            espaço_vazio.append(t)

    while mob < level2:
        spal_jacare = []
        ale = random.choice(espaço_vazio)
        spal_jacare.append(ale)

        

        pos_jacare.append(ale)
        inimigo= Ini(jacare)
        all_jacare.add(inimigo)
        mob += 1

    while game:

        clock.tick(30)
        eventos = pygame.event.get()
        for evento in eventos:

            if evento.type == pygame.QUIT: #or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                pygame.quit() # terminado a aplicação pygame
                sys.exit()    # sai pela rotina do sistema

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    player.speedx -= 10
                    Passos.play()
                elif evento.key == pygame.K_RIGHT:
                    player.speedx+=10
                    Passos.play()
                elif evento.key == pygame.K_UP:
                    player.speedy -= 10
                    Passos.play()
                elif evento.key == pygame.K_DOWN:
                    player.speedy += 10
                    Passos.play()
                elif evento.key == pygame.K_SPACE:
                    
                    ex_c = Explosao_cima(fake, (int(player.rect.centerx / 80) * 80) + 40, (int(player.rect.centery / 80) * 80) + 40)
                    ex_b = Explosao_baixo(fake, (int(player.rect.centerx / 80) * 80) + 40, (int(player.rect.centery / 80) * 80) + 40)
                    ex_d = Explosao_direita(fake, (int(player.rect.centerx / 80) * 80) + 40, (int(player.rect.centery / 80) * 80) + 40)
                    ex_e = Explosao_esquerda(fake, (int(player.rect.centerx / 80) * 80) + 40, (int(player.rect.centery / 80) * 80) + 40)
                    bomba2 = Bomba(bomba, (int(player.rect.centerx / 80) * 80) + 40, (int(player.rect.centery / 80) * 80) + 40)
                    all_sprites_ex_c.add(ex_c)
                    all_sprites_ex_b.add(ex_b)
                    all_sprites_ex_d.add(ex_d)
                    all_sprites_ex_e.add(ex_e)
                    all_sprites_bombas.add(bomba2)

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT:
                    player.speedx += 10
                elif evento.key == pygame.K_RIGHT:
                    player.speedx -= 10            
                elif evento.key == pygame.K_UP:
                    player.speedy += 10              
                elif evento.key == pygame.K_DOWN:
                    player.speedy -= 10
                Passos.stop()

        all_porta.update()
        all_player.update()
        all_jacare.update()
        all_sprites_paredes.update()
        all_sprites_blocos.update()
        all_sprites_bombas.update()
        all_sprites_ex_c.update()
        all_sprites_ex_b.update()
        all_sprites_ex_d.update()
        all_sprites_ex_e.update()

        for b in all_sprites_bombas.sprites():
            b.contagem()
        for b in all_sprites_ex_e.sprites():
            b.contagem()
        for b in all_sprites_ex_d.sprites():
            b.contagem()
        for b in all_sprites_ex_c.sprites():
            b.contagem()
        for b in all_sprites_ex_b.sprites():
            b.contagem()

        hits_e = pygame.sprite.groupcollide(all_sprites_ex, all_sprites_blocos, False, False)
        for b, blocos  in hits_e.items():
            for bloco in blocos:
                bloco.kill()
            b.kill()
        
        hits_bj = pygame.sprite.groupcollide(all_sprites_ex, all_jacare, False, False)
        for b, blocos  in hits_bj.items(): 
            for bloco in blocos:
                bloco.kill()

        hits_cp = pygame.sprite.groupcollide(all_sprites_ex, all_sprites_paredes, True, False)
        hits_bp = pygame.sprite.groupcollide(all_sprites_ex, all_player, False, False, pygame.sprite.collide_rect_ratio(0.85))
        if len(hits_bp) > 0:
            game = False

        hits = pygame.sprite.spritecollide(player, all_jacare, True)
        if len(hits) > 0:
            level = 30
            level2 = 6
            game = False
        hits2 = pygame.sprite.spritecollide(player, all_porta, False)
        if len(hits2) > 0:
            level += 10
            level2 += 10
            game = False


        surf.fill((0,110,110))
        
        all_sprites_ex.draw(surf)
        all_porta.draw(surf)
        all_sprites_paredes.draw(surf)
        all_sprites_bombas.draw(surf)
        all_sprites_blocos.draw(surf)
        all_player.draw(surf)
        all_jacare.draw(surf)
        all_sprites_ex_c.draw(surf)
        all_sprites_ex_b.draw(surf)
        all_sprites_ex_d.draw(surf)
        all_sprites_ex_e.draw(surf)

        pygame.display.update()



# O bloca esta na tela porem nao esta sendo mostrado
# all.sprites sera usado para adicionar inimigos
# estou tentando fazer o personagem não atravessar paredes e blocos