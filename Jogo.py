import pygame

pygame.init()
surf= pygame.display.set_mode([400,400])
surf.fill([0,0,0])
pygame.display.update()

while True:
    evento=pygame.event.get()
    if eventos:
        print(eventos)