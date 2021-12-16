# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 22:36:01 2021

@author: joshu
"""

import pygame
pygame.init()
display = pygame.display.set_mode((1600,1000))
clock = pygame.time.Clock()

armor0_= pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/armorbar1.png")
armor1_= pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/armorbar2.png")
armor2_= pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/armorbar3.png")
armor3_= pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/armorbar4.png")
armor4_= pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/armorbar5.png")
armor5_= pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/armorbar6.png")
armor6_= pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/armorbar7.png")
armor7_= pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/armorbar8.png")
armor8_= pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/armorbar9.png")
armor9_= pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/armorbar10.png")
armor10_= pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/armorbar11.png")
armor11_= pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/armorbar12.png")
armor12_= pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/armorbar13.png")
armor13_= pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/armorbar14.png")
armor14_= pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/armorbar15.png")
armor15_= pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/armorbar16.png")
armor16_= pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/armorbar17.png")
armor17_= pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/armorbar18.png")
armor18_= pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/armorbar19.png")
armor19_= pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/armorbar20.png")
armor20_= pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/armorbar21.png")
#all armor bar images
armor0 = pygame.transform.scale(armor0_, (400, 40))
armor1 = pygame.transform.scale(armor1_, (400, 40)) 
armor2 = pygame.transform.scale(armor2_, (400, 40))
armor3 = pygame.transform.scale(armor3_, (400, 40))
armor4 = pygame.transform.scale(armor4_, (400, 40))
armor5 = pygame.transform.scale(armor5_, (400, 40))    
armor6 = pygame.transform.scale(armor6_, (400, 40))
armor7 = pygame.transform.scale(armor7_, (400, 40))
armor8 = pygame.transform.scale(armor8_, (400, 40))
armor9 = pygame.transform.scale(armor9_, (400, 40))
armor10 = pygame.transform.scale(armor10_, (400, 40))
armor11 = pygame.transform.scale(armor11_, (400, 40))
armor12 = pygame.transform.scale(armor12_, (400, 40))
armor13 = pygame.transform.scale(armor13_, (400, 40))
armor14 = pygame.transform.scale(armor14_, (400, 40))
armor15 = pygame.transform.scale(armor15_, (400, 40))
armor16 = pygame.transform.scale(armor16_, (400, 40))
armor17 = pygame.transform.scale(armor17_, (400, 40))
armor18 = pygame.transform.scale(armor18_, (400, 40))
armor19 = pygame.transform.scale(armor19_, (400, 40))
armor20 = pygame.transform.scale(armor20_, (400, 40))
#0-100% images for healthbar
zero1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/0%.png")
one1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/1%.png")
two1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/2%.png")
three1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/3%.png")
four1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/4%.png")
five1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/5%.png")
six1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/6%.png")
seven1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/7%.png")
eight1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/8%.png")
nine1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/9%.png")
ten1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/10%.png")
eleven1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/11%.png")
tweleve1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/12%.png")
thirteen1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/13%.png")
fourteen1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/14%.png")
fifteen1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/15%.png")
sixteen1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/16%.png")
seventeen1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/17%.png")
eighteen1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/18%.png")
nineteen1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/19%.png")
twenty1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/20%.png")
twenty_one1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/21%.png")
twenty_two1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/22%.png")
twenty_three1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/23%.png")
twenty_four1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/24%.png")
twenty_five1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/25%.png")
twenty_six1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/26%.png")
twenty_seven1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/27%.png")
twenty_eight1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/28%.png")
twenty_nine1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/29%.png")
thirty1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/30%.png")
thirty_one1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/31%.png")
thirty_two1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/32%.png")
thirty_three1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/33%.png")
thirty_four1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/34%.png")
thirty_five1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/35%.png")
thirty_six1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/36%.png")
thirty_seven1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/37%.png")
thirty_eight1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/38%.png")
thirty_nine1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/39%.png")
fourty1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/40%.png")
fourty_one1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/41%.png")
fourty_two1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/42%.png")
fourty_three1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/43%.png")
fourty_four1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/44%.png")
fourty_five1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/45%.png")
fourty_six1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/46%.png")
fourty_seven1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/47%.png")
fourty_eight1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/48%.png")
fourty_nine1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/49%.png")
fifty1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/50%.png")
fifty_one1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/51%.png")
fifty_two1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/52%.png")
fifty_three1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/53%.png")
fifty_four1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/54%.png")
fifty_five1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/55%.png")
fifty_six1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/56%.png")
fifty_seven1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/57%.png")
fifty_eight1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/58%.png")
fifty_nine1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/59%.png")
sixty1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/60%.png")
sixty_one1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/61%.png")
sixty_two1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/62%.png")
sixty_three1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/63%.png")
sixty_four1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/64%.png")
sixty_five1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/65%.png")
sixty_six1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/66%.png")
sixty_seven1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/67%.png")
sixty_eight1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/68%.png")
sixty_nine1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/69%.png")
seventy1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/70%.png")
seventy_one1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/71%.png")
seventy_two1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/72%.png")
seventy_three1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/73%.png")
seventy_four1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/74%.png")
seventy_five1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/75%.png")
seventy_six1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/76%.png")
seventy_seven1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/77%.png")
seventy_eight1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/78%.png")
seventy_nine1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/79%.png")
eighty1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/80%.png")
eighty_one1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/81%.png")
eighty_two1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/82%.png")
eighty_three1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/83%.png")
eighty_four1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/84%.png")
eighty_five1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/85%.png")
eighty_six1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/86%.png")
eighty_seven1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/87%.png")
eighty_eight1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/88%.png")
eighty_nine1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/89%.png")
ninety1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/90%.png")
ninety_one1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/91%.png")
ninety_two1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/92%.png")
ninety_three1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/93%.png")
ninety_four1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/94%.png")
ninety_five1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/95%.png")
ninety_six1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/96%.png")
ninety_seven1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/97%.png")
ninety_eight1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/98%.png")
ninety_nine1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/99%.png")
one_hundred1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/100%.png")

#resizing percentage images
zero = pygame.transform.scale(zero1, (50, 15))
one = pygame.transform.scale(one1, (50, 15))
two = pygame.transform.scale(two1, (50, 15))
three = pygame.transform.scale(three1, (50, 15))
four = pygame.transform.scale(four1, (50, 15))
five = pygame.transform.scale(five1, (50, 15))
six = pygame.transform.scale(six1, (50, 15))
seven = pygame.transform.scale(seven1, (50, 15))
eight = pygame.transform.scale(eight1, (50, 15))
nine = pygame.transform.scale(nine1, (50, 15))
ten = pygame.transform.scale(ten1, (100, 15))
eleven = pygame.transform.scale(eleven1, (100, 15))
tweleve = pygame.transform.scale(tweleve1, (100, 15))
thirteen = pygame.transform.scale(thirteen1, (100, 15))
fourteen = pygame.transform.scale(fourteen1, (100, 15))
fifteen = pygame.transform.scale(fifteen1, (100, 15))
sixteen = pygame.transform.scale(sixteen1, (100, 15))
seventeen = pygame.transform.scale(seventeen1, (100, 15))
eighteen = pygame.transform.scale(eighteen1, (100, 15))
nineteen = pygame.transform.scale(nineteen1, (100, 15))
twenty = pygame.transform.scale(twenty1, (100, 15))
twenty_one = pygame.transform.scale(twenty_one1, (100, 15))
twenty_two = pygame.transform.scale(twenty_two1, (100, 15))
twenty_three = pygame.transform.scale(twenty_three1, (100, 15))
twenty_four = pygame.transform.scale(twenty_four1, (100, 15))
twenty_five = pygame.transform.scale(twenty_five1, (100, 15))
twenty_six = pygame.transform.scale(twenty_six1, (100, 15))
twenty_seven = pygame.transform.scale(twenty_seven1, (100, 15))
twenty_eight = pygame.transform.scale(twenty_eight1, (100, 15))
twenty_nine = pygame.transform.scale(twenty_nine1, (100, 15))
thirty = pygame.transform.scale(thirty1, (100, 15))
thirty_one = pygame.transform.scale(thirty_one1, (100, 15))
thirty_two = pygame.transform.scale(thirty_two1, (100, 15))
thirty_three = pygame.transform.scale(thirty_three1, (100, 15))
thirty_four = pygame.transform.scale(thirty_four1, (100, 15))
thirty_five = pygame.transform.scale(thirty_five1, (100, 15))
thirty_six = pygame.transform.scale(thirty_six1, (100, 15))
thirty_seven = pygame.transform.scale(thirty_seven1, (100, 15))
thirty_eight = pygame.transform.scale(thirty_eight1, (100, 15))
thirty_nine = pygame.transform.scale(thirty_nine1, (100, 15))
fourty = pygame.transform.scale(fourty1, (100, 15))
fourty_one = pygame.transform.scale(fourty_one1, (100, 15))
fourty_two = pygame.transform.scale(fourty_two1, (100, 15))
fourty_three = pygame.transform.scale(fourty_three1, (100, 15))
fourty_four = pygame.transform.scale(fourty_four1, (100, 15))
fourty_five = pygame.transform.scale(fourty_five1, (100, 15))
fourty_six = pygame.transform.scale(fourty_six1, (100, 15))
fourty_seven = pygame.transform.scale(fourty_seven1, (100, 15))
fourty_eight = pygame.transform.scale(fourty_eight1, (100, 15))
fourty_nine = pygame.transform.scale(fourty_nine1, (100, 15))
fifty = pygame.transform.scale(fifty1, (100, 15))
fifty_one = pygame.transform.scale(fifty_one1, (100, 15))
fifty_two = pygame.transform.scale(fifty_two1, (100, 15))
fifty_three = pygame.transform.scale(fifty_three1, (100, 15))
fifty_four = pygame.transform.scale(fifty_four1, (100, 15))
fifty_five = pygame.transform.scale(fifty_five1, (100, 15))
fifty_six = pygame.transform.scale(fifty_six1, (100, 15))
fifty_seven = pygame.transform.scale(fifty_seven1, (100, 15))
fifty_eight = pygame.transform.scale(fifty_eight1, (100, 15))
fifty_nine = pygame.transform.scale(fifty_nine1, (100, 15))
sixty = pygame.transform.scale(sixty1, (100, 15))
sixty_one = pygame.transform.scale(sixty_one1, (100, 15))
sixty_two = pygame.transform.scale(sixty_two1, (100, 15))
sixty_three = pygame.transform.scale(sixty_three1, (100, 15))
sixty_four = pygame.transform.scale(sixty_four1, (100, 15))
sixty_five = pygame.transform.scale(sixty_five1, (100, 15))
sixty_six = pygame.transform.scale(sixty_six1, (100, 15))
sixty_seven = pygame.transform.scale(sixty_seven1, (100, 15))
sixty_eight = pygame.transform.scale(sixty_eight1, (100, 15))
sixty_nine = pygame.transform.scale(sixty_nine1, (100, 15))
seventy = pygame.transform.scale(seventy1, (100, 15))
seventy_one = pygame.transform.scale(seventy_one1, (100, 15))
seventy_two = pygame.transform.scale(seventy_two1, (100, 15))
seventy_three = pygame.transform.scale(seventy_three1, (100, 15))
seventy_four = pygame.transform.scale(seventy_four1, (100, 15))
seventy_five = pygame.transform.scale(seventy_five1, (100, 15))
seventy_six = pygame.transform.scale(seventy_six1, (100, 15))
seventy_seven = pygame.transform.scale(seventy_seven1, (100, 15))
seventy_eight = pygame.transform.scale(seventy_eight1, (100, 15))
seventy_nine = pygame.transform.scale(seventy_nine1, (100, 15))
eighty = pygame.transform.scale(eighty1, (100, 15))
eighty_one = pygame.transform.scale(eighty_one1, (100, 15))
eighty_two = pygame.transform.scale(eighty_two1, (100, 15))
eighty_three = pygame.transform.scale(eighty_three1, (100, 15))
eighty_four = pygame.transform.scale(eighty_four1, (100, 15))
eighty_five = pygame.transform.scale(eighty_five1, (100, 15))
eighty_six = pygame.transform.scale(eighty_six1, (100, 15))
eighty_seven = pygame.transform.scale(eighty_seven1, (100, 15))
eighty_eight = pygame.transform.scale(eighty_eight1, (100, 15))
eighty_nine = pygame.transform.scale(eighty_nine1, (100, 15))
ninety = pygame.transform.scale(ninety1, (100, 15))
ninety_one = pygame.transform.scale(ninety_one1, (100, 15))
ninety_two = pygame.transform.scale(ninety_two1, (100, 15))
ninety_three = pygame.transform.scale(ninety_three1, (100, 15))
ninety_four = pygame.transform.scale(ninety_four1, (100, 15))
ninety_five = pygame.transform.scale(ninety_five1, (100, 15))
ninety_six = pygame.transform.scale(ninety_six1, (100, 15))
ninety_seven = pygame.transform.scale(ninety_seven1, (100, 15))
ninety_eight = pygame.transform.scale(ninety_eight1, (100, 15))
ninety_nine = pygame.transform.scale(ninety_nine1, (100, 15))
one_hundred = pygame.transform.scale(one_hundred1, (100, 15))
#gui 
gui1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/gui2.png")
gui = pygame.transform.scale(gui1, (600, 200))
gui_background1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/grey bar.png")
gui_background = pygame.transform.scale(gui_background1, (450, 125))
heart1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/heart icon.PNG")
shield_icon1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/energy shield.png")
heart = pygame.transform.scale(heart1, (38, 38))
shield_icon = pygame.transform.scale(shield_icon1, (45, 45))
bar_end1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/bar ends.png")
bar_end = pygame.transform.scale(bar_end1, (200, 200))
portrait1 = pygame.image.load("C:/Users/joshu/OneDrive/Desktop/Programming class/sprites/portrait.png")
portrait = pygame.transform.scale(portrait1, (200, 200))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #test
        self.image=pygame.Surface((40, 40))
      
        self.rect=self.image.get_rect(center = (784, 484))
        self.current_health = 100
        self.target_health = 100
        self.max_health = 100
        self.health_bar_length = 385
        self.health_ratio = self.max_health / self.health_bar_length
        self.health_change_speed = 0.5
        #health bar properties
        self.current_shield = 100
        self.target_shield = 100
        self.max_shield = 100
        self.shield_bar_length = 345
        self.shield_ratio = self.max_shield / self.shield_bar_length
        self.shield_change_speed = 0.5
        #shield bar
        self.current_armor = 17
        self.damage_reduction = 0
        #armor bar
        
    def get_damage(self,amount):
        if self.target_health > 0:
            self.target_health -= amount
        if self.target_health < 0:
            self.target_health = 0

    def get_health(self,amount):
        if self.target_health < self.max_health:
            self.target_health += amount
        if self.target_health > self.max_health:
            self.target_health -= self.max_health

    
    def get_armor_mechanics(self):
        if self.current_armor < 0:      #max, min armor
            self.current_armor = 0
        if self.current_armor > 20:
            self.current_armor = 20

    
    def get_damage_reduction(self):
        if self.current_armor == 0:
            self.damage_reduction = 0
            
        if self.current_armor == 1:
            self.damage_reduction = 5
            
        if self.current_armor == 2:
            self.damage_reduction = 10
            
        if self.current_armor == 3:
            self.damage_reduction = 15
            
        if self.current_armor == 4:
            self.damage_reduction = 20
            
        if self.current_armor == 5:
            self.damage_reduction = 25
            
        if self.current_armor == 6:
            self.damage_reduction = 30
            
        if self.current_armor == 7:
            self.damage_reduction = 35
            
        if self.current_armor == 8:
            self.damage_reduction = 40
            
        if self.current_armor == 9:
            self.damage_reduction = 45
            
        if self.current_armor == 10:
            self.damage_reduction = 50      #damage reduction
            
        if self.current_armor == 11:
            self.damage_reduction = 55
            
        if self.current_armor == 12:
            self.damage_reduction = 60
            
        if self.current_armor == 13:
            self.damage_reduction = 65
            
        if self.current_armor == 14:
            self.damage_reduction = 70
            
        if self.current_armor == 15:
            self.damage_reduction = 75
            
        if self.current_armor == 16:
            self.damage_reduction = 80
            
        if self.current_armor == 17:
            self.damage_reduction = 85
            
        if self.current_armor == 18:
            self.damage_reduction = 90
            
        if self.current_armor == 19:
            self.damage_reduction = 95
            
        if self.current_armor == 20:
            self.damage_reduction = 100
 
        
    def get_damage_shield(self,amount):         #shield mechanics
        if self.target_shield > 0:
            self.target_shield -= amount
        if self.target_shield < 0:
            self.target_shield = 0
            
    def get_health_shield(self,amount):
        if self.target_shield < self.max_shield:
            self.target_shield += amount
        if self.target_shield > self.max_shield:
            self.target_shield -= self.max_shield
            
    def update(self):
        self.health()       #update stuff
        self.shield()
        self.armor()


    def armor(self):
        if self.current_armor == 0:
            display.blit(armor0, (200,180))
            
        if self.current_armor == 1:
            display.blit(armor1, (200,180))         #armor bar iamges
            
        if self.current_armor == 2:
            display.blit(armor2, (200,180))
            
        if self.current_armor == 3:
            display.blit(armor3, (200,180))
            
        if self.current_armor == 4:
            display.blit(armor4, (200,180))
            
        if self.current_armor == 5:
            display.blit(armor5, (200,180))
            
        if self.current_armor == 6:
            display.blit(armor6, (200,180))
            
        if self.current_armor == 7:
            display.blit(armor7, (200,180))
            
        if self.current_armor == 8:
            display.blit(armor8, (200,180))
            
        if self.current_armor == 9:
            display.blit(armor9, (200,180))
            
        if self.current_armor == 10:
            display.blit(armor10, (200,180))
            
        if self.current_armor == 11:
            display.blit(armor11, (200,180))
            
        if self.current_armor == 12:
            display.blit(armor12, (200,180))
            
        if self.current_armor == 13:
            display.blit(armor13, (200,180))
            
        if self.current_armor == 14:
            display.blit(armor14, (200,180))
            
        if self.current_armor == 15:
            display.blit(armor15, (200,180))
            
        if self.current_armor == 16:
            display.blit(armor16, (200,180))
            
        if self.current_armor == 17:
            display.blit(armor17, (200,180))
            
        if self.current_armor == 18:
            display.blit(armor18, (200,180))
            
        if self.current_armor == 19:
            display.blit(armor19, (200,180))
            
        if self.current_armor == 20:
            display.blit(armor20, (200,180))



    def shield(self):
        transition_width_shield = 0
        transition_color_shield = (28,134,238)
        #color

        if self.current_shield < self.target_shield:
            self.current_shield += self.shield_change_speed
            transition_width_shield = int((self.target_shield - self.current_shield) / self.shield_ratio)
            transition_color_shield = (0, 245, 255)
            #light blue gain health
        
        if self.current_shield > self.target_shield:
            self.current_shield -= self.shield_change_speed
            transition_width_shield = abs((self.target_shield - self.current_shield) / self.shield_ratio)
            transition_color_shield = (255, 128, 0)
            #orange damage bar

        shield_bar_width = int(self.current_shield / self.shield_ratio)
        shield_bar = pygame.Rect(200, 140,shield_bar_width, 30)
        transition_bar_shield = pygame.Rect(shield_bar.right, 140 ,transition_width_shield, 30)
        
        
        display.blit(gui_background, (140, 110))
        #blue bar
        pygame.draw.rect(display, (28,134,238),shield_bar)
        pygame.draw.rect(display, transition_color_shield,transition_bar_shield)
        display.blit(gui, (15, 65))
            #bar color, bar length
        
        #shield percentage image display
        if self.current_shield == 0:
            display.blit(zero, (360, 152))
            
        if self.current_shield == 1:
            display.blit(one, (333, 152))
            
        if self.current_shield == 2:
            display.blit(two, (333, 152))
            
        if self.current_shield == 3:
            display.blit(three, (333, 152))
            
        if self.current_shield == 4:
            display.blit(four, (333, 152))
            
        if self.current_shield == 5:
            display.blit(five, (333, 152))
            
        if self.current_shield == 6:
            display.blit(six, (333, 152))
            
        if self.current_shield == 7:
            display.blit(seven, (333, 152))
            
        if self.current_shield == 8:
            display.blit(eight, (333, 152))
            
        if self.current_shield == 9:
            display.blit(nine, (333, 152))
            
        if self.current_shield == 10:
            display.blit(ten, (333, 152))
            
        if self.current_shield == 11:
            display.blit(eleven, (333, 152))
            
        if self.current_shield == 12:
            display.blit(tweleve, (333, 152))
            
        if self.current_shield == 13:
            display.blit(thirteen, (333, 152))
            
        if self.current_shield == 14:
            display.blit(fourteen, (333, 152))
            
        if self.current_shield == 15:
            display.blit(fifteen, (333, 152))
            
        if self.current_shield == 16:
            display.blit(sixteen, (333, 152))
            
        if self.current_shield == 17:
            display.blit(seventeen, (333, 152))
            
        if self.current_shield == 18:
            display.blit(eighteen, (333, 152))
            
        if self.current_shield == 19:
            display.blit(nineteen, (333, 152))
            
        if self.current_shield == 20:
            display.blit(twenty, (333, 152))
            
        if self.current_shield == 21:
            display.blit(twenty_one, (333, 152))
            
        if self.current_shield == 22:
            display.blit(twenty_two, (333, 152))
            
        if self.current_shield == 23:
            display.blit(twenty_three, (333, 152))
            
        if self.current_shield == 24:
            display.blit(twenty_four, (333, 152))
            
        if self.current_shield == 25:
            display.blit(twenty_five, (333, 152))
            
        if self.current_shield == 26:
            display.blit(twenty_six, (333, 152))
            
        if self.current_shield == 27:
            display.blit(twenty_seven, (333, 152))
            
        if self.current_shield == 28:
            display.blit(twenty_eight, (333, 152))
            
        if self.current_shield == 29:
            display.blit(twenty_nine, (333, 152))
            
        if self.current_shield == 30:
            display.blit(thirty, (333, 152))
            
        if self.current_shield == 31:
            display.blit(thirty_one, (333, 152))
            
        if self.current_shield == 32:
            display.blit(thirty_two, (333, 152))
            
        if self.current_shield == 33:
            display.blit(thirty_three, (333, 152))
            
        if self.current_shield == 34:
            display.blit(thirty_four, (333, 152))
            
        if self.current_shield == 35:
            display.blit(thirty_five, (333, 152))
            
        if self.current_shield == 36:
            display.blit(thirty_six, (333, 152))
            
        if self.current_shield == 37:
            display.blit(thirty_seven, (333, 152))
            
        if self.current_shield == 38:
            display.blit(thirty_eight, (333, 152))
            
        if self.current_shield == 39:
            display.blit(thirty_nine, (333, 152))
            
        if self.current_shield == 40:
            display.blit(fourty, (333, 152))
            
        if self.current_shield == 41:
            display.blit(fourty_one, (333, 152))
            
        if self.current_shield == 42:
            display.blit(fourty_two, (333, 152))
            
        if self.current_shield == 43:
            display.blit(fourty_three, (333, 152))
            
        if self.current_shield == 44:
            display.blit(fourty_four, (333, 152))
            
        if self.current_shield == 45:
            display.blit(fourty_five, (333, 152))
            
        if self.current_shield == 46:
            display.blit(fourty_six, (333, 152))
            
        if self.current_shield == 47:
            display.blit(fourty_seven, (333, 152))
            
        if self.current_shield == 48:
            display.blit(fourty_eight, (333, 152))
            
        if self.current_shield == 49:
            display.blit(fourty_nine, (333, 152))
            
        if self.current_shield == 50:
            display.blit(fifty, (333, 152))
            
        if self.current_shield == 51:
            display.blit(fifty_one, (333, 152))
            
        if self.current_shield == 52:
            display.blit(fifty_two, (333, 152))
            
        if self.current_shield == 53:
            display.blit(fifty_three, (333, 152))
            
        if self.current_shield == 54:
            display.blit(fifty_four, (333, 152))
            
        if self.current_shield == 55:
            display.blit(fifty_five, (333, 152))
            
        if self.current_shield == 56:
            display.blit(fifty_six, (333, 152))
            
        if self.current_shield == 152:
            display.blit(fifty_seven, (333, 152))
            
        if self.current_shield == 58:
            display.blit(fifty_eight, (333, 152))
            
        if self.current_shield == 59:
            display.blit(fifty_nine, (333, 152))
            
        if self.current_shield == 60:
            display.blit(sixty, (333, 152))
            
        if self.current_shield == 61:
            display.blit(sixty_one, (333, 152))
            
        if self.current_shield == 62:
            display.blit(sixty_two, (333, 152))
            
        if self.current_shield == 63:
            display.blit(sixty_three, (333, 152))
            
        if self.current_shield == 64:
            display.blit(sixty_four, (333, 152))
            
        if self.current_shield == 65:
            display.blit(sixty_five, (333, 152))
            
        if self.current_shield == 66:
            display.blit(sixty_six, (333, 152))
            
        if self.current_shield == 67:
            display.blit(sixty_seven, (333, 152))
            
        if self.current_shield == 68:
            display.blit(sixty_eight, (333, 152))
            
        if self.current_shield == 69:
            display.blit(sixty_nine, (333, 152))
            
        if self.current_shield == 70:
            display.blit(seventy, (333, 152))
            
        if self.current_shield == 71:
            display.blit(seventy_one, (333, 152))
            
        if self.current_shield == 72:
            display.blit(seventy_two, (333, 152))
            
        if self.current_shield == 73:
            display.blit(seventy_three, (333, 152))
            
        if self.current_shield == 74:
            display.blit(seventy_four, (333, 152))
            
        if self.current_shield == 75:
            display.blit(seventy_five, (333, 152))
            
        if self.current_shield == 76:
            display.blit(seventy_six, (333, 152))
            
        if self.current_shield == 77:
            display.blit(seventy_seven, (333, 152))
            
        if self.current_shield == 78:
            display.blit(seventy_eight, (333, 152))
            
        if self.current_shield == 79:
            display.blit(seventy_nine, (333, 152))
            
        if self.current_shield == 80:
            display.blit(eighty, (333, 152))
            
        if self.current_shield == 81:
            display.blit(eighty_one, (333, 152))
            
        if self.current_shield == 82:
            display.blit(eighty_two, (333, 152))
            
        if self.current_shield == 83:
            display.blit(eighty_three, (333, 152))
            
        if self.current_shield == 84:
            display.blit(eighty_four, (333, 152))
            
        if self.current_shield == 85:
            display.blit(eighty_five, (333, 152))
            
        if self.current_shield == 86:
            display.blit(eighty_six, (333, 152))
            
        if self.current_shield == 87:
            display.blit(eighty_seven, (333, 152))
            
        if self.current_shield == 88:
            display.blit(eighty_eight, (333, 152))
            
        if self.current_shield == 89:
            display.blit(eighty_nine, (333, 152))
            
        if self.current_shield == 90:
            display.blit(ninety, (333, 152))
            
        if self.current_shield == 91:
            display.blit(ninety_one, (333, 152))
            
        if self.current_shield == 92:
            display.blit(ninety_two, (333, 152))
            
        if self.current_shield == 93:
            display.blit(ninety_three, (333, 152))
            
        if self.current_shield == 94:
            display.blit(ninety_four, (333, 152))
            
        if self.current_shield == 95:
            display.blit(ninety_five, (333, 152))
            
        if self.current_shield == 96:
            display.blit(ninety_six, (333, 152))
            
        if self.current_shield == 97:
            display.blit(ninety_seven, (333, 152))
            
        if self.current_shield == 98:
            display.blit(ninety_eight, (333, 152))
            
        if self.current_shield == 99:
            display.blit(ninety_nine, (333, 152))
            
        if self.current_shield == 100:
            display.blit(one_hundred, (333, 152))
        
        display.blit(shield_icon, (220, 140))
        display.blit(heart, (225, 95))
        display.blit(bar_end , (535, -17))
        display.blit(bar_end, (495, 29))
        display.blit(portrait, (10, 85))
        
    def health(self):
        transition_width_health = 0
        transition_color_health = (220,20,60)
        #color

        if self.current_health < self.target_health:
            self.current_health += self.health_change_speed
            transition_width_health = int((self.target_health - self.current_health) / self.health_ratio)
            transition_color_health = (0, 255, 0)
            #green gain health
        
        if self.current_health > self.target_health:
            self.current_health -= self.health_change_speed
            transition_width_health = abs((self.target_health - self.current_health) / self.health_ratio)
            transition_color_health = (255, 215, 0)
            #yellow damage bar

        health_bar_width = int(self.current_health / self.health_ratio)
        health_bar = pygame.Rect(200, 100, health_bar_width, 25)
        transition_bar = pygame.Rect(health_bar.right, 100, transition_width_health, 25)
        #health bar dimensions/mechanics
        
        display.blit(gui_background, (175, 68))
        #red bar
        pygame.draw.rect(display, (220,20,60), health_bar)
        pygame.draw.rect(display, transition_color_health, transition_bar)    
        display.blit(gui, (15, 65))
            #bar color, bar length
         
            #health percentages
        if self.current_health == 0:
            display.blit(zero, (382, 107))
            
        if self.current_health == 1:
            display.blit(one, (355, 107))
            
        if self.current_health == 2:
            display.blit(two, (355, 107))
            
        if self.current_health == 3:
            display.blit(three, (355, 107))
            
        if self.current_health == 4:
            display.blit(four, (355, 107))
            
        if self.current_health == 5:
            display.blit(five, (355, 107))
            
        if self.current_health == 6:
            display.blit(six, (355, 107))
            
        if self.current_health == 7:
            display.blit(seven, (355, 107))
            
        if self.current_health == 8:
            display.blit(eight, (355, 107))
            
        if self.current_health == 9:
            display.blit(nine, (355, 107))
            
        if self.current_health == 10:
            display.blit(ten, (355, 107))
            
        if self.current_health == 11:
            display.blit(eleven, (355, 107))
            
        if self.current_health == 12:
            display.blit(tweleve, (355, 107))
            
        if self.current_health == 13:
            display.blit(thirteen, (355, 107))
            
        if self.current_health == 14:
            display.blit(fourteen, (355, 107))
            
        if self.current_health == 15:
            display.blit(fifteen, (355, 107))
            
        if self.current_health == 16:
            display.blit(sixteen, (355, 107))
            
        if self.current_health == 17:
            display.blit(seventeen, (355, 107))
            
        if self.current_health == 18:
            display.blit(eighteen, (355, 107))
            
        if self.current_health == 19:
            display.blit(nineteen, (355, 107))
            
        if self.current_health == 20:
            display.blit(twenty, (355, 107))
            
        if self.current_health == 21:
            display.blit(twenty_one, (355, 107))
            
        if self.current_health == 22:
            display.blit(twenty_two, (355, 107))
            
        if self.current_health == 23:
            display.blit(twenty_three, (355, 107))
            
        if self.current_health == 24:
            display.blit(twenty_four, (355, 107))
            
        if self.current_health == 25:
            display.blit(twenty_five, (355, 107))
            
        if self.current_health == 26:
            display.blit(twenty_six, (355, 107))
            
        if self.current_health == 27:
            display.blit(twenty_seven, (355, 107))
            
        if self.current_health == 28:
            display.blit(twenty_eight, (355, 107))
            
        if self.current_health == 29:
            display.blit(twenty_nine, (355, 107))
            
        if self.current_health == 30:
            display.blit(thirty, (355, 107))
            
        if self.current_health == 31:
            display.blit(thirty_one, (355, 107))
            
        if self.current_health == 32:
            display.blit(thirty_two, (355, 107))
            
        if self.current_health == 33:
            display.blit(thirty_three, (355, 107))
            
        if self.current_health == 34:
            display.blit(thirty_four, (355, 107))
            
        if self.current_health == 35:
            display.blit(thirty_five, (355, 107))
            
        if self.current_health == 36:
            display.blit(thirty_six, (355, 107))
            
        if self.current_health == 37:
            display.blit(thirty_seven, (355, 107))
            
        if self.current_health == 38:
            display.blit(thirty_eight, (355, 107))
            
        if self.current_health == 39:
            display.blit(thirty_nine, (355, 107))
            
        if self.current_health == 40:
            display.blit(fourty, (355, 107))
            
        if self.current_health == 41:
            display.blit(fourty_one, (355, 107))
            
        if self.current_health == 42:
            display.blit(fourty_two, (355, 107))
            
        if self.current_health == 43:
            display.blit(fourty_three, (355, 107))
            
        if self.current_health == 44:
            display.blit(fourty_four, (355, 107))
            
        if self.current_health == 45:
            display.blit(fourty_five, (355, 107))
            
        if self.current_health == 46:
            display.blit(fourty_six, (355, 107))
            
        if self.current_health == 47:
            display.blit(fourty_seven, (355, 107))
            
        if self.current_health == 48:
            display.blit(fourty_eight, (355, 107))
            
        if self.current_health == 49:
            display.blit(fourty_nine, (355, 107))
            
        if self.current_health == 50:
            display.blit(fifty, (355, 107))
            
        if self.current_health == 51:
            display.blit(fifty_one, (355, 107))
            
        if self.current_health == 52:
            display.blit(fifty_two, (355, 107))
            
        if self.current_health == 53:
            display.blit(fifty_three, (355, 107))
            
        if self.current_health == 54:
            display.blit(fifty_four, (355, 107))
            
        if self.current_health == 55:
            display.blit(fifty_five, (355, 107))
            
        if self.current_health == 56:
            display.blit(fifty_six, (355, 107))
            
        if self.current_health == 107:
            display.blit(fifty_seven, (355, 107))
            
        if self.current_health == 58:
            display.blit(fifty_eight, (355, 107))
            
        if self.current_health == 59:
            display.blit(fifty_nine, (355, 107))
            
        if self.current_health == 60:
            display.blit(sixty, (355, 107))
            
        if self.current_health == 61:
            display.blit(sixty_one, (355, 107))
            
        if self.current_health == 62:
            display.blit(sixty_two, (355, 107))
            
        if self.current_health == 63:
            display.blit(sixty_three, (355, 107))
            
        if self.current_health == 64:
            display.blit(sixty_four, (355, 107))
            
        if self.current_health == 65:
            display.blit(sixty_five, (355, 107))
            
        if self.current_health == 66:
            display.blit(sixty_six, (355, 107))
            
        if self.current_health == 67:
            display.blit(sixty_seven, (355, 107))
            
        if self.current_health == 68:
            display.blit(sixty_eight, (355, 107))
            
        if self.current_health == 69:
            display.blit(sixty_nine, (355, 107))
            
        if self.current_health == 70:
            display.blit(seventy, (355, 107))
            
        if self.current_health == 71:
            display.blit(seventy_one, (355, 107))
            
        if self.current_health == 72:
            display.blit(seventy_two, (355, 107))
            
        if self.current_health == 73:
            display.blit(seventy_three, (355, 107))
            
        if self.current_health == 74:
            display.blit(seventy_four, (355, 107))
            
        if self.current_health == 75:
            display.blit(seventy_five, (355, 107))
            
        if self.current_health == 76:
            display.blit(seventy_six, (355, 107))
            
        if self.current_health == 77:
            display.blit(seventy_seven, (355, 107))
            
        if self.current_health == 78:
            display.blit(seventy_eight, (355, 107))
            
        if self.current_health == 79:
            display.blit(seventy_nine, (355, 107))
            
        if self.current_health == 80:
            display.blit(eighty, (355, 107))
            
        if self.current_health == 81:
            display.blit(eighty_one, (355, 107))
            
        if self.current_health == 82:
            display.blit(eighty_two, (355, 107))
            
        if self.current_health == 83:
            display.blit(eighty_three, (355, 107))
            
        if self.current_health == 84:
            display.blit(eighty_four, (355, 107))
            
        if self.current_health == 85:
            display.blit(eighty_five, (355, 107))
            
        if self.current_health == 86:
            display.blit(eighty_six, (355, 107))
            
        if self.current_health == 87:
            display.blit(eighty_seven, (355, 107))
            
        if self.current_health == 88:
            display.blit(eighty_eight, (355, 107))
            
        if self.current_health == 89:
            display.blit(eighty_nine, (355, 107))
            
        if self.current_health == 90:
            display.blit(ninety, (355, 107))
            
        if self.current_health == 91:
            display.blit(ninety_one, (355, 107))
            
        if self.current_health == 92:
            display.blit(ninety_two, (355, 107))
            
        if self.current_health == 93:
            display.blit(ninety_three, (355, 107))
            
        if self.current_health == 94:
            display.blit(ninety_four, (355, 107))
            
        if self.current_health == 95:
            display.blit(ninety_five, (355, 107))
            
        if self.current_health == 96:
            display.blit(ninety_six, (355, 107))
            
        if self.current_health == 97:
            display.blit(ninety_seven, (355, 107))
            
        if self.current_health == 98:
            display.blit(ninety_eight, (355, 107))
            
        if self.current_health == 99:
            display.blit(ninety_nine, (355, 107))
            
        if self.current_health == 100:
            display.blit(one_hundred, (355, 107))
                 
            
            
player = pygame.sprite.GroupSingle(Player())        #group


while True:
    for event in pygame.event.get():
       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.sprite.get_health_shield(10)        #test add subtract health and shield
                player.sprite.get_health(10)
                    
                
            if event.key == pygame.K_DOWN:
                player.sprite.get_damage_shield(10)
                if player.sprite.target_shield == 0:
                    player.sprite.get_damage(10)
           

   
    
    
    display.fill((0, 201, 87))      #background
    player.update()             #display
    pygame.display.update()
    clock.tick(60)