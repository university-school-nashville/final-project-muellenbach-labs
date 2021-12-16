# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:42:21 2021

@author: joshu
"""
# needed libraries
import pygame
import math
import random
import time

pygame.init()

scroll = [0,100]

can_move_left = True
can_move_right = True
can_move_down = True
can_move_up = True

display_width = 1600    
display_height = 1000       #display screen

display = pygame.display.set_mode((display_width,display_height))

clock = pygame.time.Clock()
player_rect = pygame.Rect(784, 484, 50, 50)



#player walking images
player_walk_images_right = [pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/run 1.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/run 2.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/run 3.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/run 4.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/run 5.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/run 6.png")]
player_idle_images = [pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/idle 1.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/idle 2.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/idle 3.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/idle 4.png")]



#Zari Trooper Walking images
zaritrooper_walk_images_right = [pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test enemy.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test enemy.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test enemy.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test enemy.png")]
zaritrooper_idle_images = [pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test enemy.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test enemy.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test enemy.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test enemy.png")]

#Zari Commando walking images

#Zari tank moving images

#Zari mech moving images

#Palaxia pig moving images

#Palaxia porkchop

#Zari Trooper Weapon test
zari_weapon = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/zari test gun.png")
zari_weapon_flipped = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/zari test gun flipped.png")
#Zari Commando Weapon

#Zari tank turret

#Zari Mech Arm Cannon

#Zari Trooper Weapon projectile

#Zari Commando Weapon projectile

#Zari tank turret projectile

#Zari Mech Arm Cannon projectile

#player test gun
player_weapon = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/test gun.png")
player_weapon_flipped = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/test gun flipped.png")

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

#test
enemy_test_image = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test enemy.png")
enemy_test_image = pygame.transform.scale(enemy_test_image, (100, 100))

#mouse images
a = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/test cursor 3.png")
cursor_image = pygame.transform.scale(a, (100, 100))
pygame.mouse.set_visible(False)


#Test Projectile images
b = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/test projectile.png")
projectile_image = pygame.transform.scale(b, (100, 100))

enemy_bullet_image = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/e bullet 1.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/e bullet 2.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/e bullet 3.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/e bullet 4.png")
#enemy_bullet_image.set_colorkey((255,255,255))
enemy_bullet_image_2 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/test bullet.png")
enemy_bullet_image_2.set_colorkey((255,255,255))
enemy_bullets_images = [enemy_bullet_image, enemy_bullet_image_2]

#test payer images without animation
#player_image = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Test Character sprite.png")
#player_image = pygame.transform.scale(player_image, (100, 100))


#weapon images
spaceglock_image = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/pistol sprite 2.png")
spaceglock_image = pygame.transform.scale(spaceglock_image, (250, 250))
spaceglock_image_flipped = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/pistol sprite flipped.png")
spaceglock_image_flipped = pygame.transform.scale(spaceglock_image_flipped, (250, 250))

gaussrifle_image = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/rifle with hands sprite.png")
gaussrifle_image = pygame.transform.scale(gaussrifle_image, (250, 250))
gaussrifle_image_flipped = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/rifle flipped.png")
gaussrifle_image_flipped = pygame.transform.scale(gaussrifle_image_flipped, (250, 250))

lazermachinegun_image = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Minigun with hands sprite.png")
lazermachinegun_image = pygame.transform.scale(lazermachinegun_image, (250, 250))
lazermachinegun_image_flipped = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/Minigun flipped.png")
lazermachinegun_image_flipped = pygame.transform.scale(lazermachinegun_image_flipped, (250, 250))

plasmashotgun_image = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/shotgun with hands sprite.png")
plasmashotgun_image = pygame.transform.scale(plasmashotgun_image, (250, 250))
plasmashotgun_image_flipped = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/shotgun flipped.png")
plasmashotgun_image_flipped = pygame.transform.scale(plasmashotgun_image_flipped, (250, 250))

antimatterrocketlauncher_image = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/rocket launcher with hands sprite.png")
antimatterrocketlauncher_image = pygame.transform.scale(antimatterrocketlauncher_image, (250, 250))
antimatterrocketlauncher_image_flipped = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/rocket launcher flipped.png")
antimatterrocketlauncher_image_flipped = pygame.transform.scale(antimatterrocketlauncher_image_flipped, (250, 250))

calamitycannon_image = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/calamity cannon with hands sprite.png")
calamitycannon_image = pygame.transform.scale(calamitycannon_image, (250, 250))
calamitycannon_image_flipped = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/calamity cannon flipped.png")
calamitycannon_image_flipped = pygame.transform.scale(calamitycannon_image_flipped, (250, 250))

bullet_image = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/bullet 1.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/bullet 2.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/bullet 3.png"), pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/bullet 4.png")
#bullet_image = pygame.transform.scale(bullet_image, (10, 4))
#bullet_image.set_colorkey((255,255,255))


class EnemyBullet:
    def __init__(self, x, y):           #general enemy bullet class
        self.x = x
        self.y = y
        self.x_dir = random.randrange(-10, 10)
        self.y_dir = random.randrange(-10, 10)
        self.lifetime = 70
        self.hitbox = pygame.Rect(self.x, self.y, 5, 5)
        
    def main(self, display):
        self.hitbox = pygame.Rect(self.x-scroll[0]+5, self.y-scroll[1]+5, 10, 10)
        self.lifetime -= 1
        if self.x_dir == 0:
            self.x_dir = random.randrange(-10, 10) #no homing problems
        if self.y_dir == 0:
            self.dir = random.randrange(-10, 10) 
        self.x += (self.x_dir) // 2 * dt
        self.y += (self.y_dir) // 2 * dt
        
        display.blit(enemy_bullets_images[0], (self.x-scroll[0], self.y-scroll[1]))

class ZariTrooperBullet:
    def __init__(self, x, y, player_x, player_y):       #bullets for zari trooper
        self.x = x
        self.y = y
        self.player_x = player_x
        self.player_y = player_y
        self.lifetime = 250
        self.speed = 8
        self.angle = math.atan2(player_y-y, player_x-x) 
        self.x_vel = math.cos(self.angle) * self.speed 
        self.y_vel = math.sin(self.angle) * self.speed
        self.hitbox = pygame.Rect(self.x, self.y, 5, 5)
        self.animation_count = 0


    def draw(self, display):
        self.hitbox = pygame.Rect(self.x+16, self.y+16, 32,32)
        self.x -= -int(self.x_vel)   * dt
        self.y -= -int(self.y_vel)   * dt
        self.lifetime -= 1
        
        if self.animation_count + 1 >= 16:
            self.animation_count = 0            #animations for bullets
    
        self.animation_count += 1
        #display.blit(pygame.transform.scale(enemy_bullets_images[0], (64, 64)), (self.x, self.y))
        #display.blit(pygame.transform.scale(enemy_bullet_image[self.animation_count//4], (64, 64)), (self.x, self.y))
        display.blit(pygame.transform.rotate(enemy_bullet_image[self.animation_count//4], self.angle), (self.x, self.y))
        
class ZariTrooper:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.offset_x = random.randrange(-200, 200)
        self.offset_y = random.randrange(-200, 200)     #1st enemy
        self.reset_offset = 0
        self.moving_left = False
        self.moving_right = False
        self.bullet_cooldown = 0
        self.name = name
        self.hitbox = pygame.Rect(self.x, self.y, 64, 90)
        self.health = 50
        self.animation_count = 0
        
        
    def handle_weapons(self, display):     #weapon class for enemy
    
        rel_x, rel_y = self.x-scroll[0] - player.x, self.y-scroll[1] - player.y
        gun_angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)     #calculate gun angle
        zari_weapon_copy = pygame.transform.scale(pygame.transform.flip(pygame.transform.rotate(zari_weapon, gun_angle * -1), True, False), (100, 100))  #solution for twisted gun and increase size
        zari_weapon_copy_flipped = pygame.transform.scale(pygame.transform.rotate(zari_weapon_flipped, gun_angle), (100, 100))  #solution for twisted gun and increase size         
        
            
        if rel_x > 0:   #left
            display.blit(zari_weapon_copy, (self.x+15-scroll[0], self.y+30-scroll[1]))
            self.moving_left = True
            #display code for weapon also gives position in relation to enemy
        else:   #right
            display.blit(zari_weapon_copy_flipped, (self.x+15-scroll[0], self.y+30-scroll[1]))
            self.moving_right = True
            #to make weapon look better when mouse is pointed other way
    
    def main(self, display, player_pos_x, player_pos_y):
        dist = math.hypot(self.x-player_pos_x, self.y-player_pos_y)
        self.hitbox = pygame.Rect(self.x-scroll[0]+16,self.y-scroll[1],32,70)
        #fix hitbox
        if self.bullet_cooldown == 0:
            zari_bullets.append(ZariTrooperBullet(self.x-scroll[0], self.y-scroll[1], player.x+10, player.y+20))

            self.bullet_cooldown = random.randrange(450, 550)
        else:
            self.bullet_cooldown -= 1
     
            #random movement
        if self.reset_offset == 0:
            self.offset_x = random.randrange(-400, 400)
            self.offset_y = random.randrange(-400, 400)
            self.reset_offset = random.randrange(75, 100)
        else:
            self.reset_offset -= 1

        
        if player_pos_x + self.offset_x > self.x-scroll[0]:
            self.x += random.randrange(1, 3)   * dt
        elif player_pos_x + self.offset_x < self.x-scroll[0]:
            self.x -= random.randrange(1, 3)   * dt 

        if player_pos_y + self.offset_y > self.y-scroll[1]:
            self.y += random.randrange(1, 3)  * dt 
        elif player_pos_y + self.offset_y < self.y-scroll[1]:
            self.y -= random.randrange(1, 3)   * dt
            #scroll so it doesn't move when player does
            
        if self.animation_count + 1 >= 16:
            self.animation_count = 0            #animations
    
        self.animation_count += 1
                                                 #specific animations for each key and idle
        if self.moving_right:
            display.blit(pygame.transform.scale(zaritrooper_walk_images_right[self.animation_count//4], (100, 100)), (self.x-scroll[0]+10, self.y+15-scroll[1]))
            
            #display.blit(pygame.transform.scale(player_walk_images_right[self.animation_count//4], (100, 100)), (self.x-scroll[0]+10, self.y+15-scroll[1]))                                 
                                                    
        elif self.moving_left:
            display.blit(pygame.transform.scale(pygame.transform.flip(zaritrooper_walk_images_right[self.animation_count//4], True, False), (100, 100)), (self.x-scroll[0]+10, self.y+15-scroll[1]))
    
        
        else:
            display.blit(pygame.transform.scale(zaritrooper_idle_images[self.animation_count//4], (100, 100)), (self.x-scroll[0]+10, self.y+15-scroll[1]))
            
        #display.blit(enemy_test_image, (self.x-scroll[0]+10, self.y+15-scroll[1], 48, 48))
        #test image
        #pygame.draw.rect(display, (100, 0, 0), (self.x-scroll[0]+10, self.y+15-scroll[1], 48, 48))
        
        self.handle_weapons(display)
        #pygame.draw.rect(display, (0, 0, 255), (self.x+15, self.y+10, 64, 90))

class Bullet:
    def __init__(self, x, y, mouse_x, mouse_y, mouse_angle, damage):        #bullets for player
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.lifetime = 70
        self.speed = 15
        self.angle = math.atan2(mouse_y-y, mouse_x-x)       #angles
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
        self.hitbox = pygame.Rect(self.x, self.y, 5, 5)
        self.mouse_angle = mouse_angle
        self.damage = 0
        self.animation_count = 0
        
    def draw(self, display):        
        self.hitbox = pygame.Rect(self.x+5, self.y+20, 15, 15)      
        self.x -= -int(self.x_vel)   * dt
        self.y -= -int(self.y_vel) * dt
        self.lifetime -= 1
        if self.animation_count + 1 >= 16:
            self.animation_count = 0            #animations
    
        self.animation_count += 1
        #display.blit(pygame.transform.rotate(bullet_image, self.mouse_angle), (self.x, self.y))
        display.blit(pygame.transform.rotate(bullet_image[self.animation_count//4], self.mouse_angle), (self.x, self.y))

class Player:
    def __init__(self, x, y, width, height, player_speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.player_speed = player_speed
        self.moving_left = False
        self.moving_right = False
        self.moving_down = False
        self.moving_up = False
        self.can_scroll_right = True
        self.animation_count = 0
        self.hitbox = pygame.Rect(self.x+15, self.y+10, 64, 90)
       
    def get_hits(self, tiles):
        
        hits = []
        for tile in tiles:
            if self.hitbox.colliderect(tile):
                hits.append(tile)
        return hits
    
    def checkCollisionsx(self, tiles):      #collision
        try:
            collisions = self.get_hits(tiles)
            for tile in collisions:
                if self.moving_right:  # Hit tile moving right
                    scroll[0] -= 32  
                if self.moving_left:  # Hit tile moving left
                    scroll[0] += 32   
                if self.moving_down:  # Hit tile from the top
                    scroll[1] -= 32  
                if self.moving_up:  # Hit tile from the bottom
                    scroll[1]  += 32
                if self.moving_down and self.moving_right:  # Hit tile from the top
                    scroll[1] -= 32  
                    scroll[0] -= 32  
                if self.moving_down and self.moving_left:  # Hit tile from the top
                    scroll[1] -= 32 
                    scroll[0] += 32
                if self.moving_up and self.moving_right:  # Hit tile from the top
                    scroll[1] += 32  
                    scroll[0] -= 32  
                if self.moving_down and self.moving_left:  # Hit tile from the top
                    scroll[1] -= 32 
                    scroll[0] += 32  
                if self.moving_up:  # Hit tile from the bottom
                    scroll[1]  += 32
        except:
            pass
                
    def draw(self, display, tiles):
        rel_x, rel_y = mouse_x - player_rect.x, mouse_y - player_rect.y
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
            if rel_x > 0:
                display.blit(pygame.transform.scale(player_idle_images[self.animation_count//4], (100, 100)), (self.x, self.y))
            else: 
                display.blit(pygame.transform.scale(pygame.transform.flip(player_idle_images[self.animation_count//4],True, False), (100, 100)), (self.x, self.y))
                
        #self.moving_right = False
        #self.moving_left = False                              
        self.hitbox = pygame.Rect(self.x+16, self.y+9, 30, 40)      #hitbox properties
        self.checkCollisionsx(tiles)
        #test hitbox
        #pygame.draw.rect(display, (0, 0, 255), (self.x+15, self.y+10, 64, 90))


      
player = Player(784, 484, 50, 50, 8)


enemies = []
zari_bullets = []
enemy_bullets = []

screen_shake_cooldown = 0

shooting = False

framerate = 60

last_time = time.time()
bullets = []
shooting = False
cooldown = 0
weapon = "plasma shotgun"

scroll = [0,0]
#weapon index
guns = ["plasma shotgun", "space glock", "gauss rifle", "lazer machine gun", "antimatter rocket launcher", "calamity cannon"]
mouse_index = 0


for x in range(25):
    
    enemies.append(ZariTrooper(random.randrange(0, 2000), random.randrange(0, 2000), "Zari Trooper"))
   #add enemies

while True:
    dt = time.time() - last_time
    dt *= 60
    last_time = time.time()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    rel_x, rel_y = mouse_x - player.x, mouse_y - player.y
    angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)

    pygame.draw.rect(display, (0,0,0), (mouse_x, mouse_y, 5, 5))
    display.fill((0, 201, 87))      #background
    
    #fix player_rect.x and player_rect.y
    #display.blit(player_image, (player_rect.x, player_rect.y))
    #new mouse cursor image
    display.blit(cursor_image, (mouse_x, mouse_y))
    
    try:
            weapon = guns[mouse_index]
    except:
            mouse_index = 5
    
    #HANDLE SHOOTING
    if shooting:
            if cooldown == 0:
                  if weapon == "gauss rifle":
                        if angle < 0:
                              bullets.append(Bullet(player_rect.x + 0, player_rect.y + 0, mouse_x, mouse_y+15, angle, 5))
                              bullets.append(Bullet(player_rect.x + 0, player_rect.y + 0, mouse_x, mouse_y-15, angle, 5))
                              cooldown = 20
                        if angle > 0:
                              bullets.append(Bullet(player_rect.x + 0, player_rect.y + 0, mouse_x, mouse_y+15, angle, 5))
                              bullets.append(Bullet(player_rect.x + 0, player_rect.y + 0, mouse_x, mouse_y-15, angle, 5))
                              cooldown = 20
                  elif weapon == "space glock":
                        if angle < 0:
                              bullets.append(Bullet(player_rect.x + 0, player_rect.y + 0, mouse_x, mouse_y+15, angle, 2))
                              cooldown = 10
                        if angle > 0:
                              bullets.append(Bullet(player_rect.x + 0, player_rect.y + 0, mouse_x, mouse_y+15, angle, 2))
                              cooldown = 10
                  elif weapon == "lazer machine gun":
                        if angle < 0:
                              bullets.append(Bullet(player_rect.x + 0, player_rect.y + 0, mouse_x+random.randrange(-35, 35), mouse_y+random.randrange(-35, 35), angle, 50))
                              cooldown = 2
                        if angle > 0:
                              bullets.append(Bullet(player_rect.x + 0, player_rect.y + 0, mouse_x+random.randrange(-35, 35), mouse_y+random.randrange(-35, 35), angle, 50))
                              cooldown = 2
                  elif weapon == "plasma shotgun":
                        if angle < 0:
                              for x in range(5):
                                    bullets.append(Bullet(player_rect.x + 0, player_rect.y + 0, mouse_x+random.randrange(-64, 64), mouse_y+random.randrange(-64, 64), angle, 10))
                              cooldown = 80
                        if angle > 0:
                              for x in range(5):
                                    bullets.append(Bullet(player_rect.x + 0, player_rect.y + 0, mouse_x+random.randrange(-64, 64), mouse_y+random.randrange(-64, 64), angle, 10))
                              cooldown = 80
                  elif weapon == "antimatter rocket launcher":
                        if angle < 0:
                              bullets.append(Bullet(player_rect.x + 0, player_rect.y + 0, mouse_x, mouse_y, angle, 20))
                              cooldown = 100
                        if angle > 0:
                              bullets.append(Bullet(player_rect.x + 0, player_rect.y + 0, mouse_x, mouse_y, angle, 20))
                              cooldown = 100
                  elif weapon == "calamity cannon":
                        if angle < 0:
                              bullets.append(Bullet(player_rect.x + 0, player_rect.y + 0, mouse_x, mouse_y, angle, 20))
                              cooldown = 100
                        if angle > 0:
                              bullets.append(Bullet(player_rect.x + 0, player_rect.y + 0, mouse_x, mouse_y, angle, 20))
                              cooldown = 100
                
            else:
                  cooldown -= 1

    for bullet_ in bullets:
           bullet_.draw(display)
      
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  quit()
                  pygame.QUIT

            if event.type == pygame.MOUSEBUTTONDOWN:        #weapon controls and inventory scrolling
                  if event.button == 1:
                        shooting = True

            if event.type == pygame.MOUSEBUTTONUP:
                  if event.button == 1:
                        shooting = False

            if event.type == pygame.MOUSEWHEEL:
               if event.y < 0:
                   mouse_index  -= 1
               if event.y > 0:
                   mouse_index  += 1
 
    mouse_x, mouse_y = pygame.mouse.get_pos()

    rel_x, rel_y = mouse_x - player_rect.x, mouse_y - player_rect.y
    angle2 = math.atan2(rel_y, rel_x)
    angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
    player.draw(display, None)
    
      #HANDLE WEAPONS
    if weapon == "gauss rifle":
        gaussrifle_image_copy = pygame.transform.rotate(gaussrifle_image, angle)
        gaussrifle_image_copy_flipped = pygame.transform.rotate(gaussrifle_image_flipped, angle)
        if rel_x > 0:
            display.blit(gaussrifle_image_copy, (player_rect.x + 55 - int(gaussrifle_image_copy.get_width() / 2), player_rect.y + 25 - int(gaussrifle_image_copy.get_height() / 2) + 30))
        else:
            display.blit(gaussrifle_image_copy_flipped, (player_rect.x + 40 - int(gaussrifle_image_copy_flipped.get_width() / 2), player_rect.y + 25 - int(gaussrifle_image_copy_flipped.get_height() / 2) + 30))
            
    elif weapon == "space glock":
        spaceglock_image_copy = pygame.transform.rotate(spaceglock_image, angle)
        spaceglock_image_copy_flipped = pygame.transform.rotate(spaceglock_image_flipped, angle)
        if rel_x > 0:
            display.blit(spaceglock_image_copy, (player_rect.x + 65 - int(spaceglock_image_copy.get_width() / 2), player_rect.y + 15 - int(spaceglock_image_copy.get_height() / 2) + 30))
        else:
            display.blit(spaceglock_image_copy_flipped, (player_rect.x + 30 - int(spaceglock_image_copy_flipped.get_width() / 2), player_rect.y + 15 - int(spaceglock_image_copy_flipped.get_height() / 2) + 30))
            
    elif weapon == "lazer machine gun":
        lazermachinegun_image_copy = pygame.transform.rotate(lazermachinegun_image, angle)
        lazermachinegun_image_copy_flipped = pygame.transform.rotate(lazermachinegun_image_flipped, angle)
        if rel_x > 0:
            display.blit(lazermachinegun_image_copy, (player_rect.x + 70 - int(lazermachinegun_image_copy.get_width() / 2), player_rect.y + 30 - int(lazermachinegun_image_copy.get_height() / 2) + 30))
        else:  
            display.blit(lazermachinegun_image_copy_flipped, (player_rect.x + 30 - int(lazermachinegun_image_copy_flipped.get_width() / 2), player_rect.y + 30 - int(lazermachinegun_image_copy_flipped.get_height() / 2) + 30))
            
    elif weapon == "plasma shotgun":
        plasmashotgun_image_copy = pygame.transform.rotate(plasmashotgun_image, angle)
        plasmashotgun_image_copy_flipped = pygame.transform.rotate(plasmashotgun_image_flipped, angle)
        if rel_x > 0:
            display.blit(plasmashotgun_image_copy, (player_rect.x + 47 - int(plasmashotgun_image_copy.get_width() / 2), player_rect.y + 15 - int(plasmashotgun_image_copy.get_height() / 2) + 30))
        else:  
            display.blit(plasmashotgun_image_copy_flipped, (player_rect.x + 47 - int(plasmashotgun_image_copy_flipped.get_width() / 2), player_rect.y + 15 - int(plasmashotgun_image_copy_flipped.get_height() / 2) + 30))
            
    elif weapon == "antimatter rocket launcher":
        antimatterrocketlauncher_image_copy = pygame.transform.rotate(antimatterrocketlauncher_image, angle)
        antimatterrocketlauncher_image_copy_flipped = pygame.transform.rotate(antimatterrocketlauncher_image_flipped, angle)
        if rel_x > 0:
            display.blit(antimatterrocketlauncher_image_copy, (player_rect.x + 25 - int(antimatterrocketlauncher_image_copy.get_width() / 2), player_rect.y + 20 - int(antimatterrocketlauncher_image_copy.get_height() / 2) + 30))
        else:
            display.blit(antimatterrocketlauncher_image_copy_flipped, (player_rect.x + 75 - int(antimatterrocketlauncher_image_copy_flipped.get_width() / 2), player_rect.y + 20 - int(antimatterrocketlauncher_image_copy_flipped.get_height() / 2) + 30))
            
    elif weapon == "calamity cannon":
        calamitycannon_image_copy = pygame.transform.rotate(calamitycannon_image, angle)
        calamitycannon_image_copy_flipped = pygame.transform.rotate(calamitycannon_image_flipped, angle)
        if rel_x > 0:
            display.blit(calamitycannon_image_copy, (player_rect.x + 60 - int(calamitycannon_image_copy.get_width() / 2), player_rect.y + 30 - int(calamitycannon_image_copy.get_height() / 2) + 30))      
        else:
            display.blit(calamitycannon_image_copy_flipped, (player_rect.x + 30 - int(calamitycannon_image_copy_flipped.get_width() / 2), player_rect.y + 30 - int(calamitycannon_image_copy_flipped.get_height() / 2) + 30))      
   
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.moving_left = True
        scroll[0] -= player.player_speed  * dt
        for b in bullets:
            b.x += 8 * dt
        for zaribullets_ in zari_bullets:
            zaribullets_.x += 8 * dt
    
            
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.moving_right = True
        scroll[0] += player.player_speed   * dt
        for b in bullets:
            b.x -= 8 * dt
        for zaribullets_ in zari_bullets:
            zaribullets_.x -= 8 * dt

            
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.moving_up = True
        scroll[1] -= player.player_speed  * dt
        for b in bullets:
            b.y += 8 * dt
        for zaribullets_ in zari_bullets:
            zaribullets_.y += 8 * dt


            
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:         #key controls
        player.moving_down = True
        scroll[1] += player.player_speed  * dt
        for b in bullets:
            b.y -= 8 * dt
        for zaribullets_ in zari_bullets:
            zaribullets_.y -= 8  * dt


    if not keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.moving_down = False
    if not keys[pygame.K_w] or keys[pygame.K_UP]:
        player.moving_up = False
    if not keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.moving_left = False
    if not keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.moving_right = False

  




    for bullet_ in bullets:
        if bullet_.lifetime > 0:
            bullet_.draw(display)       #all bullets

            for e in enemies:
                if bullet_.hitbox.colliderect(e.hitbox):
                    e.x += bullet_.x_vel/2 * dt
                    e.y += bullet_.y_vel/2 * dt 

                    e.health -= 4
        else:
            bullets.remove(bullet_)

    for enemy_ in enemies:
        if enemy_.health > 0:
            enemy_.main(display, player.x, player.y)
        else:
            cooldown = 15
            while cooldown > 0:
                enemy_.main(display, player.x, player.y)

                enemy_.x += bullets[-1].x_vel/32
                enemy_.y += bullets[-1].y_vel/32

                enemy_.y -= 1

                cooldown -= 1

            enemies.remove(enemy_)

#enemy bullets
    for enemybullet_ in enemy_bullets:
        if enemybullet_.lifetime > 0:
            enemybullet_.main(display)
            if enemybullet_.hitbox.colliderect(player.hitbox):
                pass
                #Subtract Health Here
            
        else:
            enemy_bullets.pop(enemy_bullets.index(enemybullet_))


    for zaribullets_ in zari_bullets:
        if zaribullets_.lifetime > 0:
            zaribullets_.draw(display)
            if zaribullets_.hitbox.colliderect(player.hitbox):
                print("hit")
                #pass
            #Subtract Health Here


            
    
    pygame.display.update()
    clock.tick(60)
