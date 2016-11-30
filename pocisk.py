import pygame
import stale
from sprajtszit import SpriteSheet


class Bullet(pygame.sprite.Sprite):

    fire_frames_r = []
    fire_frames_l = []
    
    def __init__(self,kierunek):
        super().__init__()
        
        self.direction = kierunek

        sprite_sheet = SpriteSheet("Fiyah.png")

        pocisk = sprite_sheet.get_image(0,0,72,58)
        self.fire_frames_r.append(pocisk)
        pocisk = pygame.transform.flip(pocisk, True, False)
        self.fire_frames_l.append(pocisk)

        pocisk = sprite_sheet.get_image(72,0, 72,58)
        self.fire_frames_r.append(pocisk)
        pocisk = pygame.transform.flip(pocisk, True, False)
        self.fire_frames_l.append(pocisk)

        pocisk = sprite_sheet.get_image(0,58, 72,58)
        self.fire_frames_r.append(pocisk)
        pocisk = pygame.transform.flip(pocisk, True, False)
        self.fire_frames_l.append(pocisk)

        pocisk = sprite_sheet.get_image(72,58, 72,58)
        self.fire_frames_r.append(pocisk)
        pocisk = pygame.transform.flip(pocisk, True, False)
        self.fire_frames_l.append(pocisk)

        pocisk = sprite_sheet.get_image(0,116, 72,58)
        self.fire_frames_r.append(pocisk)
        pocisk = pygame.transform.flip(pocisk, True, False)
        self.fire_frames_l.append(pocisk)

        pocisk = sprite_sheet.get_image(72,116, 72,58)
        self.fire_frames_r.append(pocisk)
        pocisk = pygame.transform.flip(pocisk, True, False)
        self.fire_frames_l.append(pocisk)


        if self.direction == "R":
            self.image = self.fire_frames_r[0]
        else:
            self.image = self.fire_frames_l[0]

        self.rect = self.image.get_rect()

    def update(self):
        if self.direction == "R":
            self.rect.x += 6
            frame = (self.rect.x // 30) % 6
            self.image = self.fire_frames_r[frame]
        else:
            self.rect.x -= 6
            frame = (self.rect.x // 30) % 6
            self.image = self.fire_frames_l[frame]
