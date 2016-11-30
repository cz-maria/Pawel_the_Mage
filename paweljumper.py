#!/usr/bin/env python

import pygame
import random
import os
from gracz import Player
from pocisk import Bullet
from platforma import Platform
import stale
from poziomy import Level, Level_01, Level_02, Level_03, Level_04, Level_05, Koniec
from wrogowie import Enemy

pygame.init()

# -------------------- teksty ------------------------------------

font = pygame.font.SysFont(".kenpixel_blocks.ttf", 45, True, False)

tekst1 = font.render("The great mage Paweł returns from the Mages", False, stale.YELLOW)
rect1 = tekst1.get_rect()

tekst2 = font.render("Conference. He'd like to have a cup of water. During ", False, stale.YELLOW)
rect2 = [0,45]

tekst3 = font.render("his absence, the evil Lord and his knights have", False, stale.YELLOW)
rect3 = [0,90]

tekst4 = font.render("invaded his 5-floor tower. The kitchen is on the last", False, stale.YELLOW)
rect4 = [0,135]

tekst5 = font.render("floor. Help Pawel the Mage get rid of the intruders", False, stale.YELLOW)
rect5 = [0,180]

tekst6 = font.render("and make it to the kitchen for the longed cup of water.", False, stale.YELLOW)
rect6 = [0,225]

tekst7 = font.render("Move left - K_LEFT, move right - K_RIGHT, skok - K_UP", False, stale.YELLOW)
rect7 = [0,315]

tekst8 = font.render("fire blast - K_SPACE", False, stale.YELLOW)
rect8 = [0,360]

tekst9 = font.render("Press ENTER to start or press ESC to leave.", False, stale.YELLOW)
rect9 = [0,450]



gameover2 = font.render("Press ESC to exit or ENTER, to start over.", False, stale.YELLOW)
rectg2 = [0,45]

 

tekst10 = font.render("Congratulation, You won! Pawel will not attend any ", False, stale.YELLOW)
rect10 = [0,0]


tekst12 = font.render("Press ENTER, to start over or ESC to quit.", False, stale.YELLOW)
rect12 = [0,90]
# -------------------------------------------------------------------------- 
os.environ["SDL_VIDEO_CENTERED"] = "1"

 
def main():
    
 
    # Okienko
    size = [stale.SCREEN_WIDTH, stale.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

 
    pygame.display.set_caption("Pawel the Mage")

    options_txt = open("options.txt", "r")
    opcja = options_txt.read()
    options_txt.close()

# ------- Dzwieki ---------------------------------------------

    firesound = pygame.mixer.Sound("Pickup_04.wav")
    death = pygame.mixer.Sound("Explosion_04.wav")
    skok = pygame.mixer.Sound("Jump_03.wav")
    eksplozja = pygame.mixer.Sound("Explosion_02.wav")
    nowypoziom = pygame.mixer.Sound("Collect_Point_01.wav")
    
# ----------------------------------------------------------------------------- 
   
 
    # Petle gry
    started = False
    done = False
    clock = pygame.time.Clock()

# ---------------------- Petla poczatkowa - instrukcje i inne ---------------    
    while not started:
        screen.fill(stale.BLACK)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:

                opcja = open("options.txt","r")
                color = int(opcja.read())               
                started = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                started = True
                done = True

        screen.blit(tekst1,rect1)
        screen.blit(tekst2,rect2)
        screen.blit(tekst3,rect3)
        screen.blit(tekst4,rect4)
        screen.blit(tekst5,rect5)
        screen.blit(tekst6,rect6)
        screen.blit(tekst7,rect7)
        screen.blit(tekst8,rect8)
        screen.blit(tekst9,rect9)

        pygame.display.flip()

# ---------------------------------------------------------------------------
 # Gracz

    player = Player(color)
 
    # Poziomy
    level_list = []
    level_list.append(Level_01())
    level_list.append(Level_02())
    level_list.append(Level_03())
    level_list.append(Level_04())
    level_list.append(Level_05())
    level_list.append(Koniec())
 
    # Ustawienie obecnego poziomu
    current_level_no = 0
    current_level = level_list[current_level_no]
    score = 0

    # pociski
    bullet_list = pygame.sprite.Group()
    # wrogowie
    knight_list = pygame.sprite.Group()
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    # znowu gracz 
    player.rect.x = 10
    player.rect.y = stale.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
 
    # Dodaj rycerzy do listy wrogow i sprajtow
    knight_list = current_level.enemy_list
    for rycerz in knight_list:
        active_sprite_list.add(rycerz)

# ------------------- Main Program Loop -------------------------------------

    while not done:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: done = True
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                    skok.play()
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player.direction)
                    bullet.rect.x = player.rect.x
                    bullet.rect.y = player.rect.y + 20
                    active_sprite_list.add(bullet)
                    bullet_list.add(bullet)
                    firesound.play()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

# ----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
        # zderzenie z rycerzem, znaczy koniec gry

        hit = pygame.sprite.spritecollideany(player,knight_list)
        if hit != None:
            death.play()
            bleble = False

            gameover1 = font.render("You got killed. Game over. You killed %d enemies." % score, False, (255, 255, 51))
            rectg1 = [0,0]

            while not bleble:

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        done = True
                        bleble = True
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        
                        # Poziomy
                        level_list = []
                        level_list.append(Level_01())
                        level_list.append(Level_02())
                        level_list.append(Level_03())
                        level_list.append(Level_04())
                        level_list.append(Level_05())
                        level_list.append(Koniec())
 
                        # Ustawienie obecnego poziomu
                        current_level_no = 0
                        current_level = level_list[current_level_no]
                        score = 0

                        # pociski
                        bullet_list = pygame.sprite.Group()
                        # wrogowie
                        knight_list = pygame.sprite.Group()
 
                        active_sprite_list = pygame.sprite.Group()
                        player.level = current_level
                        player.rect.x = 0
                        player.rect.y = stale.SCREEN_HEIGHT - player.rect.height
                        player.change_x = 0
                        player.change_y = 0
                        active_sprite_list.add(player)

                        # Dodaj rycerzy do listy wrogow i sprajtow
                        knight_list = current_level.enemy_list
                        for rycerz in knight_list:
                            active_sprite_list.add(rycerz)

                        bleble = True

                screen.fill(stale.BLACK)
                screen.blit(gameover1, rectg1)
                screen.blit(gameover2, rectg2)
                pygame.display.flip()
# -----------------------------------------------------------------------------

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right > stale.SCREEN_WIDTH:
            player.rect.right = stale.SCREEN_WIDTH
 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left < 0:
            player.rect.left = 0

        # co sie dzieje z pociskiem
        for bullet in bullet_list:
            knight_hit_list = pygame.sprite.spritecollide(bullet, knight_list, True)
            if bullet.rect.x > stale.SCREEN_WIDTH or bullet.rect.x < 0:
                bullet_list.remove(bullet)
                active_sprite_list.remove(bullet)

            # For each block hit, remove the bullet and add to the score
            for knight in knight_hit_list:
                bullet_list.remove(bullet)
                active_sprite_list.remove(bullet)
                eksplozja.play()
                score += 1

        if player.rect.y < 0:
            current_level_no += 1
            nowypoziom.play()

# ---------------------------KONIEC GRY ------------------------------------

            if current_level_no == 5:
                bleble = False

                tekst11 = font.render("mage conference in next few months. %d enemies killed ." % score, False, stale.YELLOW)
                rect11 = [0,45]

                while not bleble:
        
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:

                        # Poziomy
                            level_list = []
                            level_list.append(Level_01())
                            level_list.append(Level_02())
                            level_list.append(Level_03())
                            level_list.append(Level_04())
                            level_list.append(Level_05())
                            level_list.append(Koniec())
 
                            # Ustawienie obecnego poziomu
                            current_level_no = 0
                            current_level = level_list[current_level_no]
                            score = 0

                            # pociski
                            bullet_list = pygame.sprite.Group()
                            # wrogowie
                            knight_list = pygame.sprite.Group()
 
                            active_sprite_list = pygame.sprite.Group()
                            player.level = current_level
                            player.rect.x = 0
                            player.rect.y = stale.SCREEN_HEIGHT - player.rect.height
                            player.change_x = 0
                            player.change_y = 0
                            active_sprite_list.add(player)

                            # Dodaj rycerzy do listy wrogow i sprajtow
                            knight_list = current_level.enemy_list
                            for rycerz in knight_list:
                                active_sprite_list.add(rycerz)

                            bleble = True

                        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            done = True

                            bleble = True

                    screen.fill(stale.BLACK)
                    screen.blit(tekst10, rect10)
                    screen.blit(tekst11, rect11)
                    screen.blit(tekst12, rect12)
                    pygame.display.flip()


# ------------------------------------------------------------------------------
            current_level = level_list[current_level_no]
            for rycerz in knight_list:
                active_sprite_list.remove(rycerz)


            knight_list = current_level.enemy_list
            for rycerz in knight_list:
                active_sprite_list.add(rycerz)

            
            player.rect.x = 0
            player.rect.y = stale.SCREEN_HEIGHT - player.rect.height

        # Update
        player.level = current_level
        active_sprite_list.update()
        current_level.update()

 
        # \begin{kod do rysowania}
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        punkty = font.render("%d" % score, False, stale.YELLOW)
        screen.blit(punkty,[950,10])
 
        # \end{kod fo rysowania}
 
        # 60 klatek na sekunde max
        clock.tick(60)
 
        # Narysuj obecny stan rzeczy
        pygame.display.flip()
 

    pygame.quit()
 
if __name__ == "__main__":
    main()
