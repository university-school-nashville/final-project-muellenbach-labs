# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:42:21 2021

@author: joshu
"""
# needed libraries
import pygame
import sys
import math
import random

pygame.init()       #add pygame, sys, 

display_width = 1600    
display_height = 1000       #display screen

display = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()


#player walking images


player_walk_images_right = [pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test Character sprite.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test Character sprite.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test Character sprite.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test Character sprite.png")]

player_idle_images = [pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test Character sprite.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test Character sprite.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test Character sprite.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test Character sprite.png")]

#weapon image
player_weapon = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/test gun.png")

a = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/test cursor 3.png")

cursor_image = pygame.transform.scale(a, (100, 100))

pygame.mouse.set_visible(False)

b = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/test projectile.png")

projectile_image = pygame.transform.scale(b, (100, 100))

class Player:           #player for game
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.moving_right = False
        self.moving_left = False
        
    def handle_weapons(self, display):     #weapon class for player
        mouse_x, mouse_y = pygame.mouse.get_pos()       #find mouse position
        rel_x, rel_y = mouse_x - player.x, mouse_y - player.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)     #calculate gun angle
        player_weapon_copy = pygame.transform.scale(pygame.transform.rotate(player_weapon, angle), (100, 100))  #solution for twisted gun and increase size
        
        display.blit(player_weapon_copy, (self.x+16-int(player_weapon.get_width()/2), self.y+60-int(player_weapon_copy.get_height()/2)))
        #display code for weapon also gives position in relation to player
        
    def main(self, display):            
        if self.animation_count + 1 >= 16:
            self.animation_count = 0            #animations
    
        self.animation_count += 1
         
                                                 #specific animations for each key and idle
                                                    
        if self.moving_right:
            display.blit(pygame.transform.scale(player_walk_images_right[self.animation_count//4], (100, 100)), (self.x, self.y))
                                                
                                                    
        elif self.moving_left:
            display.blit(pygame.transform.scale(pygame.transform.flip(player_walk_images_right[self.animation_count//4], True, False), (100, 100)), (self.x, self.y))
    
        
        else:
            display.blit(pygame.transform.scale(player_idle_images[self.animation_count//4], (100, 100)), (self.x, self.y))
            
        self.handle_weapons(display)
            
        self.moving_right = False
        self.moving_left = False 





class PlayerBullet:
    def __init__(self, x, y, mouse_x, mouse_y):         #projectiles
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 30             #projectile speed
        self.angle = math.atan2(y-mouse_y, x-mouse_x)       #annoying math for projectiles
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
    
    
    def main(self, display):
        self.x -= int(self.x_vel)       
        self.y -= int(self.y_vel)
        
        
        #display.blit(projectile_image, (self.x+60, self.y+15))
        pygame.draw.circle(display, (0, 0, 0), (self.x+60, self.y+60), 5) #bullet image
        #test bullet
   
    
   
    
    #first enemy
class AlienTrooper:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.animation_images = [pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test enemy.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test enemy.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test enemy.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test enemy.png")]
        self.animation_count = 0                    #enemy images
        self.reset_offset = 0
        self.offset_x = random.randrange(-300, 300)
        self.offset_y = random.randrange(-300, 300)
    def main(self,display):
        if self.animation_count + 1 == 16:
            self.animation_count = 0 
        self.animation_count += 1
        
        if self.reset_offset == 0:
            self.offset_x = random.randrange(-300, 300)     #enemy ai
            self.offset_y = random.randrange(-300, 300)
            self.reset_offset = random.randrange(120, 150)
        else:
            self.reset_offset -= 1
            
        if player.x + self.offset_x > self.x-display_scroll[0]:     #x-axis
            self.x += 1
            
        elif player.x + self.offset_x < self.x-display_scroll[0]:
            self.x -= 1
   
        if player.y + self.offset_y > self.y-display_scroll[1]:     #y-axis
            self.y += 1
            
        elif player.y + self.offset_y < self.y-display_scroll[1]:
            self.y -= 1
   
        display.blit(pygame.transform.scale(self.animation_images[self.animation_count//4], (100, 100)), (self.x-display_scroll[0], self.y-display_scroll[1]))
        #enemy animation
        
#enemies list
enemies = [AlienTrooper(400, 300)]
    
   
    
player = Player(784, 484, 32, 32)       #location, image
        
display_scroll = [0,0]
   

player_bullets = []         #bullet updates

    

    
while True:
    display.fill((0, 201, 87))      #background
    mouse_x, mouse_y = pygame.mouse.get_pos()     #position of mouse  
    
   
    display.blit(cursor_image, (mouse_x, mouse_y))
    
    
    for event in pygame.event.get():        #quit mechanic
    
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
            
            
        if event.type == pygame.MOUSEBUTTONDOWN:        #bullet mouse click
            if event.button == 1:
                player_bullets.append(PlayerBullet(player.x, player.y, mouse_x, mouse_y))
        
    keys = pygame.key.get_pressed()         #control keys
    
    pygame.draw.rect(display, (255,255,255), (100-display_scroll[0], 100-display_scroll[1], 16, 16))
    #test object
    
    if keys[pygame.K_a]:
        display_scroll[0] -= 5
        player.moving_left = True
        for bullet in player_bullets:
            bullet.x +=5
        
    if keys[pygame.K_d]:                #wasd controls
        display_scroll[0] += 5
        player.moving_right = True
        for bullet in player_bullets:
            bullet.x -=5
        
    if keys[pygame.K_w]:
        display_scroll[1] -= 5
        for bullet in player_bullets:
            bullet.y +=5                  #code inbetween used to prevent bullets from moving with the player
        
    if keys[pygame.K_s]:
        display_scroll[1] += 5
        for bullet in player_bullets:
            bullet.y -=5
        
    
    if keys[pygame.K_LEFT]:
        display_scroll[0] -= 5              #the rest of the screen is moving, not the player
        player.moving_left = True
        for bullet in player_bullets:
            bullet.x +=5
        
    if keys[pygame.K_RIGHT]:
        display_scroll[0] += 5
        player.moving_right = True
        for bullet in player_bullets:
            bullet.x -=5
        
    if keys[pygame.K_UP]:                    #arrow key controls
        display_scroll[1] -= 5
        for bullet in player_bullets:
            bullet.y +=5
        
    if keys[pygame.K_DOWN]:
        display_scroll[1] += 5
        for bullet in player_bullets:
            bullet.y -=5
    

    
    player.main(display)        #put on screen
    
    for bullet in player_bullets:       
        bullet.main(display)
    
    for enemy in enemies:
        enemy.main(display)
    
    
    clock.tick(60)          #60 fps
    pygame.display.update()         #update command
    