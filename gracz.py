import pygame
import stale


class Player(pygame.sprite.Sprite):
    """ Klasa gracza """
 

    walking_frames_l = []
    walking_frames_r = []
    direction = "R"

    # -- Methods
    def __init__(self,color):
        super().__init__()

        if color == 0:
            image_r = pygame.image.load("mage1.png").convert()
        elif color == 1:
            image_r = pygame.image.load("mage3.png").convert()
        else:
            image_r = pygame.image.load("mage2.png").convert()
 
        image_r.set_colorkey(stale.RED)
        self.walking_frames_r.append(image_r)
        image_l = pygame.transform.flip(image_r, True, False)
        self.walking_frames_l.append(image_l)

        self.image = player_image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()
 
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
 
        # List of sprites we can bump against
        self.level = None
 
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.change_x
        #pos = self.rect.x        


        if self.direction == "R":
            self.image = self.walking_frames_r[0]
        else:
            self.image = self.walking_frames_l[0]
 
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Co robic jak natrafimy na platforme
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                self.change_y = 0
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            #Stop our vertical movement
#            self.change_y = 0
 
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
 
    def jump(self):
        """ Called when user hits 'jump' button. """
 
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
 
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= stale.SCREEN_HEIGHT:
            self.change_y = -10
 
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -4
        self.direction = "L"
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 4
        self.direction = "R"
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0

    #def odpalpocisk(self):
     #   self.fire = True
