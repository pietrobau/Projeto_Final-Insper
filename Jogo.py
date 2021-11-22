import pygame
import random
import os
import sys

pygame.init()
WIDTH=1360
HEIGHT= 720

surf= pygame.display.set_mode([WIDTH,HEIGHT])
surf.fill([0,150,0])

#colocar paredes
a = []
b = []
pos = []
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
        paredes = pygame.image.load("parede.png")
        surf.blit(paredes, [f,j])
        pos.append([f,j])
#_____________________________
#colocar blocos
c = []
d = []
pos_bloco = []
i = 80
while i < 1360: #lista das posicoes
    c.append(i)
    i = i + 80
i = 80
while i < 720:
    d.append(i)
    i = i + 80
i = 0
level = 30
while i < level:    #pegar posicoes aleatorias
    aleatorioc = random.choice(c)
    aleatoriod = random.choice(d)
    pos2 = [aleatorioc,aleatoriod]
    if pos2 not in pos: #colocar o bloco se a posiçao não for igual a parede
        pos_bloco.append([aleatorioc,aleatoriod])
        blocos = pygame.image.load("bloco.png")
        surf.blit(blocos, [aleatorioc,aleatoriod])
        i = i + 1
#___________________________
#posicionar porta da vitoria
posicao_porta = random.choice(pos_bloco)
porta = pygame.image.load("porta.png")
surf.blit(porta, posicao_porta)
#____________________________
#Movimento do personagem
movimento=[0,0]
personagem=pygame.image.load("Raposa_frente.gif")
#surf.blit(personagem, movimento)
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

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

#____________________________
pygame.display.update()
clock= pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player= Raposa(personagem)
all_sprites.add(player)
#delta = {"esquerda":0, "direita":0, "acima":0, "abaixo":0}

while True:
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
    all_sprites.update()

    # ----- Gera saídas
    surf.fill((0,150,0))  # Preenche com a cor branca
    #surf.blit(background, (0, 0))
    # Desenhando meteoros
    for f in a: #colocar as paredes nas posicoes
        for j in b:
            paredes = pygame.image.load("parede.png")
            surf.blit(paredes, [f,j])
    #for posicao in pos2:
        #surf.blit(blocos, [posicao[0],posicao[1]])
    all_sprites.draw(surf)

    pygame.display.update()



# O bloca esta na tela porem nao esta sendo mostrado
# all.sprites sera usado para adicionar inimigos


