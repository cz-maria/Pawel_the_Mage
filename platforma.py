import pygame
import stale

class Platform(pygame.sprite.Sprite):
    """ Platforma """
 
    def __init__(self, width, height, color):
        
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
