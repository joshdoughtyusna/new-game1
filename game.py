import pygame
import time
pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("this is my cool game")
screen.fill((0,255,0))

while True:
    print(pygame.event.get())
    pygame.display.flip()
    time.sleep(1)
