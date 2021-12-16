# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 16:15:14 2021

@author: joshu
"""

import pygame
import sys




## image load

BG_COLOR = pygame.Color('gray12')
PLAYER_IMG = pygame.Surface((30, 50), pygame.SRCALPHA)
pygame.draw.polygon(PLAYER_IMG, pygame.Color('dodgerblue'), [(0, 50), (15, 0), (30, 50)])
ENEMY_IMG = pygame.Surface((50, 30))
ENEMY_IMG.fill(pygame.Color('darkorange1'))
BULLET_IMG = pygame.Surface((9, 15))
BULLET_IMG.fill(pygame.Color('aquamarine2'))



## Classes
class Bullet(pygame.sprite.Sprite):                             #The bullet class is a sprite object
    def __init__(self, pos, target, *sprite_groups):
        """
        Parameters
        ----------
        pos : the bullet origin, where the bullet spawns
        target : the mouse position, where the bullet is aiming
        *sprite_groups : the different groups you can add your object to

        """
        super().__init__(*sprite_groups)                        # super init is required for pygame... I dont especially know why
        
        
        self.pos = pygame.Vector2(pos)                          #creating a vector from the screen_topleft to the origin of the bullet
        self.pos2 = pygame.Vector2(target)                      #creating a vector from the screen_topleft to the mouse position
        
        self.vel = self.pos2-self.pos                           #vector subtraction
        self. vel = self.vel.normalize()                        #vector normalization
        
        """
        BREAKDOWN:
            
            in the code above, I basically drew an arrow (VECTOR) from the top left of the screen to 
            both the player and the mouse position.
            
            When you subtract these two vectors, this gives you an arrow pointing from the origin of 
            the bullet to the mouse position. lets call this vector V3
            
            This is exactly what we need to shoot bullets from the player
            
            I normalize V3, this means I take whatever arrow I have found and make it length 1. 
            Therefore the bullet does not travel faster when the mouse cursor is farther away
            
        """
        
        self.image = BULLET_IMG
        self.rect = self.image.get_rect(center=pos)             #get the image and rectangle for the bullet
        
    
    def update(self):
        """
        time to update the bullet. I just keep adding the position of the bullet 
        to the V3 I have found
        """
        self.pos += self.vel
        self.rect.center = self.pos                             #updating the 
        
        
        '''
        i dont have any code to kill the bullets yet, but I would put something in if you want your code to run well
        
        if self.rect.bottom <= 0:
            self.kill()
        '''
        


class Player(pygame.sprite.Sprite):                             #Player is a sprite object
    """
    
    """
    def __init__(self, pos,sprites,bullets):
        """
        Parameters
        ----------
        pos : position of the player, can be changed to move the player
        sprites : 
        bullets : groups that I added so I can add the generated  bullets to these groups

        """
        super().__init__()                                      #again, you need super(), i dont know why... its a pygame thing
        self.pos = pos
        self.image = PLAYER_IMG
        self.rect = self.image.get_rect(center=pos)             #get the rectangle of your dude
        
        self.sprites = sprites
        self.bullets = bullets
        self.add(self.sprites)                                  #add the player to your general sprite group
        
    def update(self):
        self.rect.center = self.pos
        
        mouse_pressed = pygame.mouse.get_pressed()
        
        #if pygame.event.get() == key
        
        if mouse_pressed[0]:
            """
            checks if the mouse is down, there is no delay to the bullets yet
            """

            Bullet(self.pos, pygame.mouse.get_pos(), self.bullets, self.sprites)
            """
            creating a new instance of your bullet object, notice how I am adding the bullets to both these groups
            """
        
        
        
## Pygame code
def main():
    global DISPLAY, FPS_CLOCK
    pygame.init()                                           #initiate the pygame sequence

    FPS_CLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((400,400))            #create your display
    CENTER = (200,200)                                      #variable for the center of the screen
    
    crashed = False                                         #not crashed, checks if crashed
    
    bullets = pygame.sprite.Group()                         #creates the sprite groups
    sprites = pygame.sprite.Group()                         #creates the sprite groups
    
    player = Player(CENTER,sprites,bullets)
    
    
    
    def handle_events():
        """
        
        function to handle what to do if the game crashes, i put it in a function so it is out of the way

        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                crashed = True
        pygame.display.update()
        
    def draw():
        """
        fills the display with a preset background color

        draws all the sprites in the sprite groups named "sprite"
        this is why sprite groups are so powerful, i can draw everything I need with one line

        """
        DISPLAY.fill(BG_COLOR)
        sprites.draw(DISPLAY)
        
    while not crashed:
        """
        while loop to loop through all the functions I have created
        """
        sprites.update()                            #updates all the sprites in the the sprite group, this is why all the classes have an update function
        handle_events()
        draw()
        
main()