import pygame
from player import Player
from pygame.locals import (
        QUIT,
        KEYDOWN,
        K_ESCAPE,
)

running = True

# def process_events(events):
# todo check why setting running flag not works here

HEIGH = 500
WIDTH = 500

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([WIDTH, HEIGH])
player = Player();

while running:
#    clock.tick(30)

    events = pygame.event.get()

    for event in events:
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                print(' escape clicked')
                running = False
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    pressed_keys =  pygame.key.get_pressed()

    player.update(pressed_keys)


    screen.blit(player.surf,player.rect)

    pygame.display.flip()


pygame.quit()
