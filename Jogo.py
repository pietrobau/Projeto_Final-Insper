import pygame
import random
import os
import sys

pygame.init()
surf= pygame.display.set_mode([1360,720])
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
surf.blit(personagem, movimento)
#____________________________
pygame.display.update()
clock= pygame.time.Clock()
while True:
    time=clock.tick(60)
    evento=pygame.event.get()
    if evento:
        print(evento)
    for e in evento:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                movimento[0]+= -1
            elif e.key == pygame.K_RIGHT:
                movimento[0]+=1
            elif e.key == pygame.K_UP:
                movimento[1]+=1
            elif e.key == pygame.K_DOWN:
                movimento[1]+= -1

