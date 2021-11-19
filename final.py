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

bullet_img = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/test bullet.png")

#player walking images
player_walk_images_right = [pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test Character sprite.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test Character sprite.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test Character sprite.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test Character sprite.png")]
player_idle_images = [pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test Character sprite.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test Character sprite.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test Character sprite.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test Character sprite.png")]

#Zari Trooper Walking images

#Zari Commando walking images

#Zari tank moving images

#Zari mech moving images

#Palaxia pig moving images

#Palaxia porkchop

#Zari Trooper Weapon
zari_weapon = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/zari test gun.png")
zari_weapon_flipped = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/zari test gun flipped.png")
#Zari Commando Weapon

#Zari tank turret

#Zari Mech Arm Cannon

#Zari Trooper Weapon projectile

#Zari Commando Weapon projectile

#Zari tank turret projectile

#Zari Mech Arm Cannon projectile

#player plasma shotgun images
player_weapon = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/test gun.png")
player_weapon_flipped = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/test gun flipped.png")


#gauss rifle images

#Antimatter Rocket launcher images

#Lazer Machine Gun images

#Calamity Cannon projectile images

#gauss rifle projectile images

#Antimatter Rocket launcher projectile images

#Lazer Machine Gun projectile images

#Calamity Cannon projectile images

#Grass images

#Tree images

#rock images:
    
#player health images

#player shield images

#Zari Trooper health images

#Zari Commando health images

#Zari tank health images

#Zari mech health images

#inventory ui images

#ui image

#hotbar image

#titlescreen images

#controlscreen images

#scrap image

#fusion core image

#Wire image

#Bolt image

#water images


#mouse images
a = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/test cursor 3.png")
cursor_image = pygame.transform.scale(a, (100, 100))
pygame.mouse.set_visible(False)


#Projectile images
b = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/test projectile.png")
projectile_image = pygame.transform.scale(b, (100, 100))

#class World_Border:

class Player:           #player for game
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.moving_right = False
        self.moving_left = False
        '''
        self.shoot = False
        '''
    def handle_weapons(self, display):     #weapon class for player
        mouse_x, mouse_y = pygame.mouse.get_pos()       #find mouse position
        rel_x, rel_y = mouse_x - player.x, mouse_y - player.y
        #rel_x, rel_y = mouse_x-display_scroll[0] - player.x, mouse_y-display_scroll[1] - player.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)     #calculate gun angle
        player_weapon_copy = pygame.transform.scale(pygame.transform.flip(pygame.transform.rotate(player_weapon, angle * -1), True, False), (100, 100))  #solution for twisted gun and increase size
        player_weapon_copy_flipped = pygame.transform.scale(pygame.transform.rotate(player_weapon_flipped, angle), (100, 100))  #solution for twisted gun and increase size
      
        if rel_x > 0:
            display.blit(player_weapon_copy, (self.x+16-int(player_weapon.get_width()/2), self.y+30-int(player_weapon.get_height()/2)))
            #display code for weapon also gives position in relation to player
        else:
            display.blit(player_weapon_copy_flipped, (self.x+16-int(player_weapon.get_width()/2), self.y+30-int(player_weapon.get_height()/2)))
        #to make weapon look better when mouse is pointed other way
        '''
        if self.shoot:
            bullet = Bullet(self.x, self.y, angle)
            bullet_group.add(bullet)
        else:
            self.shoot = False
        '''
        
    def main(self, display):            
        if self.animation_count + 1 >= 16:
            self.animation_count = 0            #animations
    
        self.animation_count += 1
                                                 #specific animations for each key and idle
                                     
            
        if self.moving_right:
            display.blit(pygame.transform.scale(player_walk_images_right[self.animation_count//4], (100, 100)), (self.x, self.y))
            display.blit(pygame.transform.scale(player_walk_images_right[self.animation_count//4], (100, 100)), (self.x, self.y))                                 
                                                    
        elif self.moving_left:
            display.blit(pygame.transform.scale(pygame.transform.flip(player_walk_images_right[self.animation_count//4], True, False), (100, 100)), (self.x, self.y))
    
        
        else:
            display.blit(pygame.transform.scale(player_idle_images[self.animation_count//4], (100, 100)), (self.x, self.y))
            
        self.handle_weapons(display)
            
        self.moving_right = False
        self.moving_left = False 
        

'''
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
   
bullet_group = pygame.sprite.Group()
'''


        
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
        
        
        #display.blit(bullet_img, (self.x+60), (self.y+15))
        pygame.draw.circle(display, (0, 0, 0), (self.x+60, self.y+60), 5) #bullet image
        #test bullet

    
    
 

    
#class palaxia pig:   
    
    #first enemy
class ZariTrooper:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.gun_angle = 0
        self.bullet_angle = 0
        self.x_vel = 0
        self.y_vel = 0
        self.speed = 2
        self.bulletx = self.x+60
        self.bullety = self.y+16
        self.animation_images = [pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test enemy.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test enemy.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test enemy.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test enemy.png")]
        self.animation_count = 0                    #enemy images
        self.reset_offset = 0
        self.shoot = 0
        self.offset_x = random.randrange(-300, 300)
        self.offset_y = random.randrange(-300, 300)
        
        
    def handle_weapons(self, display):     #weapon class for enemy
    
        rel_x, rel_y = self.x-display_scroll[0] - player.x, self.y-display_scroll[1] - player.y
        gun_angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)     #calculate gun angle
        zari_weapon_copy = pygame.transform.scale(pygame.transform.flip(pygame.transform.rotate(zari_weapon, gun_angle * -1), True, False), (100, 100))  #solution for twisted gun and increase size
        zari_weapon_copy_flipped = pygame.transform.scale(pygame.transform.rotate(zari_weapon_flipped, gun_angle), (100, 100))  #solution for twisted gun and increase size         
        
            
        if rel_x > 0:   #left
            display.blit(zari_weapon_copy, (self.x-display_scroll[0], self.y+11-display_scroll[1]))
            
            #display code for weapon also gives position in relation to enemy
        else:   #right
            display.blit(zari_weapon_copy_flipped, (self.x-display_scroll[0], self.y+11-display_scroll[1]))
            #to make weapon look better when mouse is pointed other way
    
    def bullet(self, display):
        if pygame.time.get_ticks()%5000 == 0 or pygame.time.get_ticks()==0:
            self.shoot = 0
            rel_x, rel_y = self.x-display_scroll[0] - player.x, self.y-display_scroll[1] - player.y
            bullet_angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
            self.x_vel = math.cos(bullet_angle) * self.speed
            self.y_vel = math.sin(bullet_angle) * self.speed
        
        if self.shoot < 100000:
            self.bulletx += int(self.x_vel)       
            self.bullety += int(self.y_vel)
            
            pygame.draw.circle(display, (0, 0, 0), (self.bulletx+60, self.bullety+60), 5) #bullet image
            #test bullet 
            self.shoot += 1
            
              
            
        
            
        
    def main(self, display):
        
        
        
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
        
        self.handle_weapons(display)
        
        
        
        self.bullet(display)
        
        
   

        
















#enemies list
enemies = [ZariTrooper(700, 100)]

    
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
                '''
                shoot = True
                '''
    keys = pygame.key.get_pressed()         #control keys
    
    pygame.draw.rect(display, (255,255,255), (100-display_scroll[0], 100-display_scroll[1], 16, 16))
    #test object
    
    if keys[pygame.K_a]:
        player.x -= 4
        display_scroll[0] -= 4            #the rest of the screen is moving, not the player
        player.moving_left = True
        for bullet in player_bullets:
            bullet.x +=4
        
    if keys[pygame.K_d]:                #wasd controls
        player.x += 4
        display_scroll[0] += 4
        player.moving_right = True
        for bullet in player_bullets:
            bullet.x -=4
        
    if keys[pygame.K_w]:
        player.y -= 4
        display_scroll[1] -= 4
        for bullet in player_bullets:
            bullet.y +=4                  #code inbetween used to prevent bullets from moving with the player
        
    if keys[pygame.K_s]:
        player.y += 4
        display_scroll[1] += 4
        for bullet in player_bullets:
            bullet.y -=4
    
    if keys[pygame.K_SPACE]:
        player_bullets.append(PlayerBullet(player.x, player.y, mouse_x, mouse_y))
        '''
        shoot = True
        '''
    if keys[pygame.K_LEFT]:
        player.x -= 4
        display_scroll[0] -= 4            #the rest of the screen is moving, not the player
        player.moving_left = True
        for bullet in player_bullets:
            bullet.x +=4
        
    if keys[pygame.K_RIGHT]:
        player.x += 4
        display_scroll[0] += 4
        player.moving_right = True
        for bullet in player_bullets:
            bullet.x -=4
        
    if keys[pygame.K_UP]:                    #arrow key controls
        player.y -= 4
        display_scroll[1] -= 4
        for bullet in player_bullets:
            bullet.y +=4
        
    if keys[pygame.K_DOWN]:
        player.y += 4
        display_scroll[1] += 4
        for bullet in player_bullets:
            bullet.y -=4
    
    
    
    player.main(display)        #put on screen
    
    for bullet in player_bullets:       
        bullet.main(display)
    
 
    
    for enemy in enemies:
        enemy.main(display)
    '''
    bullet_group.update()
    bullet_group.draw(display)
    '''
    clock.tick(60)          #60 fps
    pygame.display.update()         #update command
    