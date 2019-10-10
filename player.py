import pygame

from pygame.locals import (
        K_w,
        K_s,
        K_a,
        K_d
)

class Player(pygame.sprite.Sprite):
    speed = 10

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 75))
        self.surf.fill((0, 255,0))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0,-self.speed)
        if pressed_keys[K_s]:
            self.rect.move_ip(0,self.speed)
        if pressed_keys[K_a]:
            self.rect.move_ip(-self.speed,0)
        if pressed_keys[K_d]:
            self.rect.move_ip(self.speed,0)

