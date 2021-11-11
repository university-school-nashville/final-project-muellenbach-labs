# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:42:21 2021

@author: joshu
"""
# needed libraries
import pygame
import sys
import math

pygame.init()       #add pygame, sys, 

display_width = 1600    
display_height = 1000       #display screen

display = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()


#player walking

player_walk_images = [pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test Character sprite.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test Character sprite.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test Character sprite.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test Character sprite.png")]
    


class Player:           #player for game
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        
    def main(self, display):            
        if self.animation_count + 1 >= 16:
            self.animation_count = 0
    
        self.animation_count += 1
    
        display.blit(pygame.transform.scale(player_walk_images[self.animation_count//4], (64, 64)), (self.x, self.y))
    
        #test
        #pygame.draw.rect(display, (0, 255, 255), (self.x, self.y, self.width, self.height))


class PlayerBullet:
    def __init__(self, x, y, mouse_x, mouse_y):         #projectiles
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 15             #projectile speed
        self.angle = math.atan2(y-mouse_y, x-mouse_x)       #annoying math for projectiles
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
    
    
    def main(self, display):
        self.x -= int(self.x_vel)       
        self.y -= int(self.y_vel)
        
        pygame.draw.circle(display, (0, 0, 0), (self.x, self.y), 5) #bullet image
        
        
player = Player(784, 484, 32, 32)       #location, image
        
display_scroll = [0,0]
   

player_bullets = []         #bullet updates

     
while True:
    display.fill((0, 201, 87))      #background
    mouse_x, mouse_y = pygame.mouse.get_pos()       
    
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
        for bullet in player_bullets:
            bullet.x +=5
        
    if keys[pygame.K_d]:                #wasd controls
        display_scroll[0] += 5
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
        for bullet in player_bullets:
            bullet.x +=5
        
    if keys[pygame.K_RIGHT]:
        display_scroll[0] += 5
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
    
    clock.tick(60)          #60 fps
    pygame.display.update()         #update command
    