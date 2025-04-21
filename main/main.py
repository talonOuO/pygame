import pygame
from pexpect.screen import screen

pygame.init()

screenHigh = 760
screenWidth = 1000
playground = [screenWidth,screenHigh]
screen = pygame.display.set_mode((screenWidth,screenHigh))

running = True
fps = 120
clock =pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type ==   pygame.QUIT:
            running=False
    pygame.display.update()
    dt =clock.tick(fps)
pygame.quit()