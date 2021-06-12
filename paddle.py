import pygame
from pygame.locals import *


black = (0, 0, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    # Rectangle move script
    def moveUp(self, pixels):
        self.rect.y -= pixels

        if self.rect.y + self.height < 0:
            self.rect.y = 640

    def moveDown(self, pixels):
        self.rect.y += pixels

        if self.rect.y > 640:
            self.rect.y = 0
