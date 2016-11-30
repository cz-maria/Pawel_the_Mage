import pygame
import stale

class Enemy(pygame.sprite.Sprite):
 

    walking_frames_l = []
    walking_frames_r = []

    def __init__(self):
        super().__init__()
 
        image = pygame.image.load("knight.png").convert()
        image.set_colorkey(stale.WHITE)
        self.walking_frames_l.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = pygame.image.load("knight2.png").convert()
        image.set_colorkey(stale.WHITE)
        self.walking_frames_l.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)

        self.image = knight_image = self.walking_frames_l[0]
        self.rect = self.image.get_rect()

        # Szybkosc rycerza
        self.change_x = -1
        self.change_y = 0
 
        # List of sprites we can bump against
        self.level = None

    def update(self):
        """ Ruch rycerza """
        # Gravity
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x        

        if self.change_x < 0:
            frame = (pos // 20) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        else:
            frame = (pos // 20) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
                self.change_x = - self.change_x
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
                self.change_x = -self.change_x
                self.direction = "R"
        if self.rect.x > stale.SCREEN_WIDTH - self.rect.width or self.rect.x < 0:
            self.change_x = - self.change_x
            

# Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                if self.change_x > 0 and self.rect.x > block.rect.right - 85:
                    self.change_x = -1
                elif self.change_x < 0 and self.rect.x < block.rect.left:
                    self.change_x = 1
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
 
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        # See if we are on the ground.
        if self.rect.y >= stale.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = stale.SCREEN_HEIGHT - self.rect.height

class Boss(Enemy):
    def __init__(self, player):
        super().__init__()
        
