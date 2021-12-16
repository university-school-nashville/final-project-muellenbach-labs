# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 19:32:18 2021

@author: joshu
"""

import pygame
import sys




WHITE = (255, 255, 255)
RED = (255, 0, 0)





#game settings/options
title = "Game"
display_width = 1600
display_height = 1000
FPS = 60
BGCOLOR = (0, 201, 87)

#player setup
DEFUALT_HP = 1000
DEFUALT_PROT = 0
DEFUALT_ATK = 0

STATPOSX = 50       #stat x coordinates

uiheight = 450  #inventory height

invtilesize = 95    #tile size
#COINOFFSET = 4


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y, hp, prot, atk):
        #PYGAME
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
     
     
        self.x = x
        self.y = y

        #Player attr
        self.hp = hp
        self.prot = prot
        self.hp_max = hp
        self.atk = atk
        self.armor = {'head': None, 'chest': None, 'legs': None, 'feet': None}
        self.weapon = {'weapon1': None, 'weapon2': None, 'weapon3': None, 'weapon4': None, 'weapon5': None, 'weapon6': None}
        #slots
        
    def addHp(self, hp_gain):
        self.hp += hp_gain
        if self.hp > self.hp_max:
            self.hp = self.hp_max

    def addProt(self, prot_gain):
        self.prot += prot_gain

    def equip_armor(self, item):
        if self.armor[item.slot] != None:
            self.unequip_armor(item.slot)
        self.armor[item.slot] = item
        self.prot += item.prot

    def unequip_armor(self, slot):
        if self.armor[slot] != None:
            self.prot -= self.armor[slot].prot
            self.armor[slot] = None

    def equip_weapon(self, item):
        if self.weapon[item.slot] != None:
            self.unequip_weapon(item.slot)      #equip mechanics
        self.weapon[item.slot] = item
        self.atk += item.atk

    def unequip_weapon(self, slot):
        if self.weapon[slot] != None:
            self.atk -= self.weapon[slot].atk
            self.weapon[slot] = None

    #def update(self):
        
        

    def check_collision(self):
        pass
     
        

        
        
        #inventory class
class Inventory:
    def __init__(self, player, totalSlots, cols, rows):
        self.totalSlots = totalSlots
        self.rows = rows
        self.cols = cols
        self.inventory_slots = []
        self.armor_slots = []
        self.weapon_slots = []
        self.display_inventory = False
        self.player = player
        self.appendSlots()
        self.setSlotTypes()

        self.movingitem = None
        self.movingitemslot = None
        #inventory
    def appendSlots(self):      #adding the slots
        while len(self.inventory_slots) != self.totalSlots: 
            #800 - (97 * 5)/2 , 800 + (97 * 5)/2
            for x in range(display_width//2 - ((invtilesize+2) * self.cols)//2, display_width//2 + ((invtilesize+2) * self.cols) //2, 100):
                for y in range(uiheight, uiheight+invtilesize * self.rows, 100):
                    self.inventory_slots.append(InventorySlot(x, y - 200))

        while len(self.armor_slots) != 4:       #height of armor slots
            for y in range(uiheight-100, uiheight-100+(100) * 4, 100):
                self.armor_slots.append(EquipableSlot(self.inventory_slots[0].x - 300, y - 200))

        while len(self.weapon_slots) != 6:  #weapon slots
            for y in range(uiheight-100, uiheight-100+(100) * 6, 100):
                self.weapon_slots.append(EquipableSlot(self.inventory_slots[0].x - 200, y - 200))
                    #weapon slot pos
                    
    def setSlotTypes(self):                             #slot types
        self.armor_slots[0].slottype = 'head'
        self.armor_slots[1].slottype = 'chest'
        self.armor_slots[2].slottype = 'legs'
        self.armor_slots[3].slottype = 'feet'
        self.weapon_slots[0].slottype = 'weapon1'
        self.weapon_slots[1].slottype = 'weapon2'
        self.weapon_slots[2].slottype = 'weapon3'
        self.weapon_slots[3].slottype = 'weapon4'
        self.weapon_slots[4].slottype = 'weapon5'#create player slots
        self.weapon_slots[5].slottype = 'weapon6'
   

    def draw(self, screen):
        if self.display_inventory:
            for slot in self.armor_slots + self.inventory_slots + self.weapon_slots:
                slot.draw(screen)
            for slot in self.armor_slots + self.inventory_slots + self.weapon_slots:
                slot.drawItems(screen)

    def toggleInventory(self):
        self.display_inventory = not self.display_inventory

    def addItemInv(self, item, slot=None):
        if slot == None:
            for slots in self.inventory_slots:
                if slots.item == None:
                    slots.item = item
                    break
        if slot != None:
            if slot.item != None:                       #adding and taking items from inventory
                self.movingitemslot.item = slot.item
                slot.item = item
            else:
                slot.item = item

    def removeItemInv(self, item):
        for slot in self.inventory_slots:
            if slot.item == item:       #removing items
                slot.item = None
                break

    def moveItem(self, screen):
        mousepos = pygame.mouse.get_pos()
        for slot in self.inventory_slots + self.armor_slots + self.weapon_slots:    #moving stuff around inventory
            if slot.draw(screen).collidepoint(mousepos) and slot.item != None:
                slot.item.is_moving = True
                self.movingitem = slot.item
                self.movingitemslot = slot
                break

    def placeItem(self, screen):
        mousepos = pygame.mouse.get_pos()       #placing stuff down
        for slot in self.inventory_slots + self.armor_slots + self.weapon_slots:
            if slot.draw(screen).collidepoint(mousepos) and self.movingitem != None:
                if isinstance(self.movingitemslot, EquipableSlot) and isinstance(slot, InventorySlot) and not isinstance(slot, EquipableSlot) and slot.item == None:
                    self.unequipItem(self.movingitem)
                    break
                if isinstance(slot, InventorySlot) and not isinstance(slot, EquipableSlot) and not isinstance(self.movingitemslot, EquipableSlot):
                    self.removeItemInv(self.movingitem)
                    self.addItemInv(self.movingitem, slot)
                    break
                if isinstance(self.movingitemslot, EquipableSlot) and isinstance(slot.item, Equipable):
                    if self.movingitem.slot == slot.item.slot:
                        self.unequipItem(self.movingitem)
                        self.equipItem(slot.item)
                        break
                if isinstance(slot, EquipableSlot) and isinstance(self.movingitem, Equipable):
                    if slot.slottype == self.movingitem.slot:
                        self.equipItem(self.movingitem)
                        break
        if self.movingitem != None:
            self.movingitem.is_moving = False
            self.movingitem = None
            self.movingitemslot = None

    def checkSlot(self, screen, mousepos):          #checking the slots
        for slot in self.inventory_slots + self.armor_slots + self.weapon_slots:
            if isinstance(slot, InventorySlot):
                if slot.draw(screen).collidepoint(mousepos):
                    if isinstance(slot.item, Equipable):
                        self.equipItem(slot.item)
                    if isinstance(slot.item, Consumable):
                        self.useItem(slot.item)
            if isinstance(slot, EquipableSlot):
                if slot.draw(screen).collidepoint(mousepos):
                    if slot.item != None:
                        self.unequipItem(slot.item)

    def getEquipSlot(self, item):
        for slot in self.armor_slots + self.weapon_slots:
            if slot.slottype == item.slot:
                return slot

    def useItem(self, item):
        if isinstance(item, Consumable):
            item.use(self, self.player)

    def equipItem(self, item):
        if isinstance(item, Equipable):         #inventory actions
            item.equip(self, self.player)

    def unequipItem(self, item):
        if isinstance(item, Equipable):
            item.unequip(self)

class InventorySlot:
    def __init__(self, x, y):       
        self.x = x
        self.y = y
        self.item = None

    def draw(self, screen):     #draw inventory
        return pygame.draw.rect(screen, WHITE, (self.x, self.y, invtilesize, invtilesize))
    
    def drawItems(self, screen):
        if self.item != None and not self.item.is_moving:       #drawing the items
            self.image = pygame.image.load(self.item.img).convert_alpha()
            screen.blit(self.image, (self.x-7, self.y-7))
        if self.item != None and self.item.is_moving:
            mousepos1 = pygame.mouse.get_pos()
            self.image = pygame.image.load(self.item.img).convert_alpha()
            screen.blit(self.image, (mousepos1[0]-20,mousepos1[1]-20))

class EquipableSlot(InventorySlot):
    def __init__(self, x, y, slottype=None):        #equip inventory slots
        InventorySlot.__init__(self, x, y)
        self.slottype = slottype

class InventoryItem:
    def __init__(self, img, value):         #init items and pauses game when inventory is opened
        self.img = img
        self.value = value
        self.is_moving = False

class Consumable(InventoryItem):            
    def __init__(self, img, value, hp_gain=0, prot_gain=0):     #consumables
        InventoryItem.__init__(self, img, value)
        self.hp_gain = hp_gain
        self.prot_gain = prot_gain

    def use(self, inv, target):
        inv.removeItemInv(self)         #use consumables
        target.addHp(self.hp_gain)
        target.addProt(self.prot_gain)

class Equipable(InventoryItem):
    def __init__(self, img, value):             #for equipable objects
        InventoryItem.__init__(self, img, value)
        self.is_equipped = False
        self.equipped_to = None
        
    def equip(self, target):        #equip
        self.is_equipped = True
        self.equipped_to = target

    def unequip(self):                  #unequip
        self.is_equipped = False
        self.equipped_to = None

class Armor(Equipable):                         #armor
    def __init__(self, img, value, prot, slot):
        Equipable.__init__(self, img, value)    
        self.prot = prot
        self.slot = slot

    def equip(self, inv, target):
        if inv.getEquipSlot(self).item != None:         #equip
            inv.getEquipSlot(self).item.unequip(inv)
        Equipable.equip(self, target)
        target.equip_armor(self)
        inv.removeItemInv(self)
        inv.getEquipSlot(self).item = self

    def unequip(self, inv):
        self.equipped_to.unequip_armor(self.slot)           #unequip
        Equipable.unequip(self)
        inv.addItemInv(self)
        inv.getEquipSlot(self).item = None

class Weapon(Equipable):
    def __init__(self, img, value, atk, slot, wpn_type):        #weapons
        Equipable.__init__(self, img, value)
        self.atk = atk
        self.slot = slot
        self.wpn_type = wpn_type
        
        
    def equip(self, inv, target):
        
        if inv.getEquipSlot(self).item != None:     #equip
            inv.getEquipSlot(self).item.unequip(inv)
        Equipable.equip(self, target)
        target.equip_weapon(self)
        inv.removeItemInv(self)
        inv.getEquipSlot(self).item = self
        
    def unequip(self, inv):                     #unequip
        self.equipped_to.unequip_weapon(self.slot)
        Equipable.unequip(self)
        inv.addItemInv(self)
        inv.getEquipSlot(self).item = None
        
        
        


class Game():               #main game function
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Calibri', 25)    #game font
        self.screen = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

    def new(self):
        # start a new game
        self.all_sprites = pygame.sprite.Group()
        #self.all_coins = pygame.sprite.Group()
        self.player = Player(self, 15, 15, DEFUALT_HP, DEFUALT_PROT, DEFUALT_ATK)
        #self.coin = Coin(self, random.randrange(0, GRIDWIDTH), random.randrange(0, GRIDHEIGHT))
        self.inventory = Inventory(self.player, 10, 5, 2)       #inventory item images
        # = Weapon('', 20, 20, 'weapon1', 'gauss rifle')
        # = Weapon('', 10, 10, 'weapon2', '"space glock')
        # = Weapon('', 20, 20, 'weapon3', 'lazer machine gun')
        # = Weapon('', 20, 20, 'weapon4', 'plasma shotgun')
        # = Weapon('', 20, 20, 'weapon5', 'antimatter rocket launcher')
        # = Weapon('', 20, 20, 'weapon6', 'calamity cannon')
        # = Consumable('', 2, 30)
        # = Consumable('', 2, 30)
        # = Armor('', 10, 20, 'head')
        # = Armor('', 10, 40, 'chest')
        # = Armor('', 10, 40, 'legs')
        # = Armor('', 10, 80, 'feet')
        #self.inventory.addItemInv()
        #elf.inventory.addItemInv()
        #self.inventory.addItemInv()      #add stuff to inventory
        #self.inventory.addItemInv()
        #self.inventory.addItemInv()
        #self.inventory.addItemInv()
        #self.inventory.addItemInv()
        #self.inventory.addItemInv()
        #self.inventory.addItemInv()
        g.run()

    def run(self):
        # game loop
        while True:
            self.clock.tick(FPS)        #ties fps to game elements
            self.events()
            self.update()
            self.draw()

    def quit(self):
        sys.exit()
    def update(self):
        # game loop update
        self.all_sprites.update()       #updating game elements
        self.player.update()
        #self.all_coins.update()

    def events(self):
        # game loop events
        for event in pygame.event.get():
        # check for closing window
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:        #controls
                if event.key == pygame.K_e:
                    self.inventory.toggleInventory()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if self.inventory.display_inventory:
                    mouse_pos = pygame.mouse.get_pos()
                    self.inventory.checkSlot(self.screen, mouse_pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.inventory.display_inventory:
                    self.inventory.moveItem(self.screen)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.inventory.display_inventory:
                    self.inventory.placeItem(self.screen)
    
    #def new_coin(self):
        #self.coin.x = random.randrange(0, GRIDWIDTH)
        #self.coin.y = random.randrange(0, GRIDHEIGHT)
    
        
    

    def draw_player_stats(self):
        self.hp = self.myfont.render(f"{self.player.hp}" , False, RED)
        self.prot = self.myfont.render(f"{self.player.prot}" , False, WHITE)    #font color
        self.atk = self.myfont.render(f"{self.player.atk}" , False, WHITE)
        #self.coins = self.myfont.render(f"{self.player.p_coins}" , False, GOLD)
        self.hpimg = pygame.image.load('C:/Users/joshu/Downloads/pg-inventory-system-master/pg-inventory-system-master/img/heart.png').convert_alpha()
        self.protimg = pygame.image.load('C:/Users/joshu/Downloads/pg-inventory-system-master/pg-inventory-system-master/img/upg_shieldSmall.png').convert_alpha()
        self.atkimg = pygame.image.load('C:/Users/joshu/Downloads/pg-inventory-system-master/pg-inventory-system-master/img/upg_dagger.png').convert_alpha()
        #self.coinimg = pygame.image.load('C:/Users/joshu/Downloads/pygame-inventory-system-master/pygame-inventory-system-master/img/coin1.png').convert_alpha()
        self.screen.blit(self.hp,(STATPOSX,25))
        self.screen.blit(self.prot,(STATPOSX,75))       #display numbers
        self.screen.blit(self.atk,(STATPOSX,125))
        #self.screen.blit(self.coins,(STATPOSX,175))
        self.screen.blit(self.hpimg,(STATPOSX-50,5))
        self.screen.blit(self.protimg,(STATPOSX-50,55))     #display images
        self.screen.blit(self.atkimg,(STATPOSX-50,105))
        #self.screen.blit(self.coinimg,(STATPOSX-55,155))

    def draw(self):
        # game loop draw
        self.screen.fill(BGCOLOR)
       
        #self.all_sprites.draw(self.screen)
        self.inventory.draw(self.screen)
        #self.draw_player_stats()
        # flipping display after drawing
        pygame.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

g = Game()
while True:
    g.new()

pygame.quit()