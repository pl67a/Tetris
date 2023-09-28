import pygame
from const import *
from pygame.locals import *


class Block(pygame.sprite.Sprite):
    def __init__(self, block_type, pos):
        super().__init__()
        self.image = pygame.image.load(BLOCK_RES[block_type])
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT]:
            self.rect.move_ip(-1, 0)
        elif pressed[K_RIGHT]:
            self.rect.move_ip(1, 0)
        elif pressed[K_UP]:
            self.rect.move_ip(0, -1)
        elif pressed[K_DOWN]:
            self.rect.move_ip(0, 1)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
