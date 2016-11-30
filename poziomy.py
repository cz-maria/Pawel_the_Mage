import pygame
import stale
import random
from gracz import Player
from platforma import Platform
from wrogowie import Enemy


class Level(object):
    """ Ogolna klasa poziomow gry """
 
    def __init__(self):

        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        #self.player = player
        self.background = None
 
    def update(self):
        """ Odswieza stan poziomu """
        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
        """ Rysuj poziom """
 
        # Draw the background
        screen.fill(stale.BLUE)
        screen.blit(self.background, [0,0])

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
 
 
# Create platforms for the level
class Level_01(Level):
    """ Poziom pierwszy - ogrod """
 
    def __init__(self):

        Level.__init__(self)
        self.background = pygame.image.load("kwiaty.png").convert()
 
        # Array with width, height, x, and y of platform
        level = [[300, 50, 300, 150],
                     [400,50,400,300],
                     [500,50,200,450],
                     [500,50, 400,600]]

        color = stale.PINK

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1],color)
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            #block.player = self.player
            self.platform_list.add(block)

            rycerz = Enemy()
            rycerz.level = self
 
        # Ulokowianie rycerzy; obecnie randomowe
            rycerz.rect.x = block.rect.x + random.randrange(platform[0]-101)
            rycerz.rect.y = block.rect.y - 85
 
        # Dodaj rycerzy do listy wrogow i sprajtow
            self.enemy_list.add(rycerz)


class Level_02(Level):
    """ Poziom 2 - klatka schodowa """
    
    def __init__(self):
        Level.__init__(self)

        self.background = pygame.image.load("schody.png").convert()

        level = [[500, 50, 0, 150],
                 [600, 50, 300, 300],
                 [400, 50, 100, 450],
                 [500, 50, 500, 600]]

        color = stale.SELEDYN

        for platform in level:
            block = Platform(platform[0], platform[1],color)
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            #block.player = self.player
            self.platform_list.add(block)

        #self.enemy_list.append(rycerz)
            rycerz = Enemy()
            rycerz.level = self
 
        # Ulokowianie rycerzy; obecnie randomowe
            rycerz.rect.x = block.rect.x + random.randrange(platform[0]-101)
            rycerz.rect.y = block.rect.y - 85
 
        # Dodaj rycerzy do listy wrogow i sprajtow
            self.enemy_list.add(rycerz)

class Level_03(Level):
    """ Poziom 3 - lazienka """
    
    def __init__(self):
        Level.__init__(self)

        self.background = pygame.image.load("prysznic.png").convert()

        level = [[800, 50, 200, 600],
                 [300, 50, 0, 450],
                 [400, 50, 10, 300],
                 [300, 50, 0, 150],
                 [300, 50, 700, 150],
                 [200, 50, 500, 300],
                 [500, 50, 500, 450]]

        color = stale.ORANGE

        for platform in level:
            block = Platform(platform[0], platform[1],color)
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            #block.player = self.player
            self.platform_list.add(block)

        #self.enemy_list.append(rycerz)
            rycerz = Enemy()
            rycerz.level = self
 
        # Ulokowianie rycerzy; obecnie randomowe
            rycerz.rect.x = block.rect.x + random.randrange(platform[0]-101)
            rycerz.rect.y = block.rect.y - 85
 
        # Dodaj rycerzy do listy wrogow i sprajtow
            self.enemy_list.add(rycerz)


class Level_04(Level):
    """ Poziom 4 - biblioteka """
    
    def __init__(self):
        Level.__init__(self)

        self.background = pygame.image.load("library.png").convert()

        level = [[300, 50, 300, 150],
                 [150, 50, 200, 300],
                 [200, 50, 700, 300],
                 [500, 50, 200, 600],
                 [300, 50, 500, 450]]

        color = stale.BLUE

        for platform in level:
            block = Platform(platform[0], platform[1],color)
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            #block.player = self.player
            self.platform_list.add(block)

        #self.enemy_list.append(rycerz)
            rycerz = Enemy()
            rycerz.level = self
 
        # Ulokowianie rycerzy; obecnie randomowe
            rycerz.rect.x = block.rect.x + random.randrange(platform[0]-101)
            rycerz.rect.y = block.rect.y - 85
 
        # Dodaj rycerzy do listy wrogow i sprajtow
            self.enemy_list.add(rycerz)

class Level_05(Level):
    """ Poziom 5 - magiczne studio czy cos """
    
    def __init__(self):
        Level.__init__(self)

        self.background = pygame.image.load("level5.png").convert()

        level = [[300, 50, 0, 300],
                 [500, 50, 200, 450],
                 [400, 50, 400, 600],
                 [500, 50, 400, 150]]

        color = stale.GREEN

        for platform in level:
            block = Platform(platform[0], platform[1],color)
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            #block.player = self.player
            self.platform_list.add(block)

        #self.enemy_list.append(rycerz)
            rycerz = Enemy()
            rycerz.level = self
 
        # Ulokowianie rycerzy; obecnie randomowe
            rycerz.rect.x = block.rect.x + random.randrange(platform[0]-101)
            rycerz.rect.y = block.rect.y - 85
 
            self.enemy_list.add(rycerz)

class Koniec(Level):
    """ Koniec gry """
    
    def __init__(self):
        Level.__init__(self)
        self.background = pygame.Surface([1000,700])
        self.background.fill(stale.BLACK)

