import pygame
import random
import os
import sys

from pygame import rect

pygame.init()
WIDTH=1360
HEIGHT= 720
game = True
pygame.display.set_caption('BomberFox')
surf= pygame.display.set_mode([WIDTH,HEIGHT])
surf.fill([0,110,110])

paredes = pygame.image.load("parede.png")
blocos = pygame.image.load("bloco.png")
personagem = pygame.image.load('Raposa_frente.gif').convert_alpha()
jacare = pygame.image.load('jacaré.gif').convert_alpha()

all_sprites_blocos = pygame.sprite.Group()
all_sprites_paredes = pygame.sprite.Group()
all_player = pygame.sprite.Group()
all_jacare = pygame.sprite.Group()

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
i = 80
while i < 720:
    y.append(i)
    i = i + 80
i = 0
level = 30
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
posicao_porta = random.choice(pos_bloco)
porta = pygame.image.load("porta.png")
surf.blit(porta, posicao_porta)
#____________________________
#Movimento do personagem

class Raposa(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.top = 0
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


player= Raposa(personagem)
all_player.add(player)
#____________________________

#Inimigo

level2 = 6
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

    class Ini(pygame.sprite.Sprite):
        def __init__(self, img):
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = ale[0] +40
            self.rect.bottom = ale[1] -9
            self.speedx = 3

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

            self.rect.x += self.speedx
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
                self.speedx = -3
            if self.rect.left < 0:
                self.rect.left = 0
                self.speedx = 3

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
                #delta["esquerda"] = 1
            elif evento.key == pygame.K_RIGHT:
                player.speedx+=10
                #delta["direita"] = 1
            elif evento.key == pygame.K_UP:
                player.speedy -= 10
                
                #delta["acima"] = 1
            elif evento.key == pygame.K_DOWN:
                player.speedy += 10
                
                #delta["abaixo"] = 1
            ''' elif evento.key == pygame.K_SPACE:
                clique = True'''

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                player.speedx += 10
                #delta["esquerda"] = 0
            if evento.key == pygame.K_RIGHT:
                player.speedx -= 10
                #delta["direita"] = 0
            elif evento.key == pygame.K_UP:
                player.speedy += 10
                #delta["acima"] = 0
            elif evento.key == pygame.K_DOWN:
                player.speedy -= 10
                
                #delta["abaixo"] = 0
            '''elif evento.key == pygame.K_SPACE:
                clique = False'''
    all_sprites_paredes.update()
    all_sprites_blocos.update()
    all_player.update()
    all_jacare.update()

    hits = pygame.sprite.spritecollide(player, all_jacare, True)
    if len(hits) > 0:
        game = False

    # ----- Gera saídas
    surf.fill((0,110,110))  # Preenche com a cor branca
    #surf.blit(background, (0, 0))
    # Desenhando meteoros
    for v in posicao_porta:
        porta = pygame.image.load("porta.png")
        surf.blit(porta, posicao_porta)

    all_sprites_paredes.draw(surf)
    all_sprites_blocos.draw(surf)
    all_player.draw(surf)
    all_jacare.draw(surf)

    pygame.display.update()



# O bloca esta na tela porem nao esta sendo mostrado
# all.sprites sera usado para adicionar inimigos
# estou tentando fazer o personagem não atravessar paredes e blocos