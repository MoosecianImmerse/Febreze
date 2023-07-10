import pygame
import time
import math
import os
import random
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60
screen_width = 1280
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('The Last of Febreeze')

#define game variables
tile_size = 20
game_over = 0
egame_over = 0
eagame_over = 0
hitbox = False
engame_over = 0
scene = 0
rep = False
loadcnter = 0
loadcounter = 1
sprint = True
speed = 5
Tack = False
chasey = 0
playerDirection = 0
chasex = 0
chest1 = True
Defe = False
ealive = True
worlddirection = 3
colcnter = 1
eaalive = True
sceneo = scene
mapo = False
npcangle = 0
pd = 1
score = 0
fc = True
playerRectx = 0
playerDirection = -2
playerRecty= 0
npcRectx = 0
npcRecty= 0
enemyRectx = 0
enemyRecty = 0
eqa = False
terminate = True
pegame_over = 0
eanemyRectx = 0
eanemyRecty = 0
tackcooldown = 700
bulletRect = pygame.Rect(0, 0, 20, 20)
playerRect = pygame.Rect(0, 0, 20, 20)
npcRect = pygame.Rect(0, 0, 20, 20)
eanemyRect = pygame.Rect(0, 0, 20, 20)


#load images
im16 = pygame.image.load('img/funload1.png')
im9 = pygame.image.load('img/funload2.png')
im10 = pygame.image.load('img/funload3.png')
im11 = pygame.image.load('img/funload4.png')
im12 = pygame.image.load('img/funload5.png')
im13 = pygame.image.load('img/funload6.png')
im14 = pygame.image.load('img/funload7.png')
im15 = pygame.image.load('img/funload8.png')
im1 = pygame.image.load('img/Loadbase1.png')
im2 = pygame.image.load('img/Loadbase2.png')
im3 = pygame.image.load('img/Loadbase3.png')
im4 = pygame.image.load('img/Loadbase4.png')
im5 = pygame.image.load('img/Loadbase5.png')
im6 = pygame.image.load('img/Loadbase6.png')
im7 = pygame.image.load('img/Loadbase7.png')
im8 = pygame.image.load('img/Loadbase8.png')
text = pygame.image.load('img/text.png')
text4 = pygame.image.load('img/text4.png')
text1 = pygame.image.load('img/text1.png')
text2 = pygame.image.load('img/text2.png')
text3= pygame.image.load('img/text3.png')
text5 = pygame.image.load('img/text5.png')
text6 = pygame.image.load('img/text6.png')
text7 = pygame.image.load('img/text7.png')
bg_img = pygame.image.load('img/ground.png')
stimg = pygame.image.load('img/statbox.png')
hurt = pygame.image.load('img/hurt.png')
map1= pygame.image.load('img/map1.1.png')
pausemenu= pygame.image.load('img/PauseMenu.png')
settingsmenu= pygame.image.load('img/settingsmenu.png')
gear = pygame.image.load('img/Gear.png')
poof = pygame.image.load('img/poof.png')




class Poof():
        def __init__(self, x, y):
                self.images_right = []
                self.images_righto = []
                self.images_left = []
                self.images_lefto = []
                self.images_attack = []
                self.images_battack = []
                self.images_lattack = []
                self.images_rattack = []
                self.images_block = []
                self.images_blockl=[]
                self.images_blockr = []
                self.images_blockb = []
                self.index = 0
                self.counter = 0
                img_right = pygame.image.load('img/poof.png')
                for num in range(1, 5):
                        img_right = pygame.image.load('img/poof.png')
                        img_right = pygame.transform.scale(img_right, (40, 40))
                        img_left = pygame.transform.rotate(img_right,180)
                        img_lefto = pygame.transform.rotate(img_right,90)
                        img_righto = pygame.transform.rotate(img_right,270)
                        self.images_right.append(img_right)
                        self.images_righto.append(img_righto)
                        self.images_left.append(img_left)
                        self.images_lefto.append(img_lefto)
                self.image = self.images_right[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.width = self.image.get_width()
                self.height = self.image.get_height()
                self.vel_y = 0
                self.jumped = False
                self.direction = 0

        def update(self, pegame_over):
                #globalize neccesary variables
                global map1
                global chasex
                global chasey
                global playerRectx
                global playerRecty
                global bulletRect
                global playerRect
                global pd
                global engame_over
                global tackcooldown
                global playerDirection
                global chest1
                global hitbox
                global speed
                global rep
                global Defe
                global Tack
                global eqa
                global terminate
                
                plcol = True
                dx = 0
                dy = 0
                walk_cooldown = 5
                
                if rep:
                        if playerDirection == -2:
                                pd = -2
                                self.image = self.images_lefto[self.index]
                                rep = False
                        if playerDirection == -1:
                                pd = -1
                                self.image = self.images_righto[self.index]
                                rep = False
                        if playerDirection == 2:
                                pd = 2
                                self.image = self.images_left[self.index]
                                rep = False
                        if playerDirection == 1:
                                pd = 1
                                self.image = self.images_right[self.index]
                                rep = False

                if pd == -2:
                        dy -= 20
                if pd == -1:
                        dy += 20
                if pd == 1:
                        dx += 20
                if pd == 2:
                        dx -= 20
                

                #check for collision
                for tile in world.tile_list:
                        #check for collision in x direction
                        if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                                terminate = True
                        #check for collision in y direction
                        if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                                terminate = True
                        #check if above the ground i.e. falling
                        if 1280 < self.rect.x < 0 or 640 < self.rect.y < 0:
                                terminate = True

                self.rect.x += dx
                self.rect.y += dy
                bulletRect = self.rect

                screen.blit(self.image, self.rect)



class Player():
        def __init__(self, x, y):
                self.images_right = []
                self.images_righto = []
                self.images_left = []
                self.images_lefto = []
                self.images_attack = []
                self.images_battack = []
                self.images_lattack = []
                self.images_rattack = []
                self.images_block = []
                self.images_blockl=[]
                self.images_blockr = []
                self.images_blockb = []
                self.index = 0
                self.counter = 0
                img_right = pygame.image.load('img/guy.png')
                for num in range(1, 5):
                        img_right = pygame.image.load('img/guy.png')
                        img_block = pygame.image.load('img/guyb.png')
                        img_blockb = pygame.transform.rotate(img_block,180)
                        img_blockl = pygame.transform.rotate(img_block,90)
                        img_blockr = pygame.transform.rotate(img_block,270)
                        img_right = pygame.transform.scale(img_right, (40, 40))
                        img_left = pygame.transform.rotate(img_right,180)
                        img_attack = pygame.image.load('img/guya.png')
                        img_battack = pygame.transform.rotate(img_attack,180)
                        img_lattack = pygame.transform.rotate(img_attack,90)
                        img_rattack = pygame.transform.rotate(img_attack,270)
                        img_lefto = pygame.transform.rotate(img_right,90)
                        img_righto = pygame.transform.rotate(img_right,270)
                        self.images_block.append(img_block)
                        self.images_blockr.append(img_blockr)
                        self.images_blockl.append(img_blockl)
                        self.images_blockb.append(img_blockb)
                        self.images_right.append(img_right)
                        self.images_attack.append(img_attack)
                        self.images_battack.append(img_battack)
                        self.images_lattack.append(img_lattack)
                        self.images_rattack.append(img_rattack)
                        self.images_righto.append(img_righto)
                        self.images_left.append(img_left)
                        self.images_lefto.append(img_lefto)
                self.dead_image = pygame.image.load('img/ghost.png')
                self.image = self.images_right[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.width = self.image.get_width()
                self.height = self.image.get_height()
                self.vel_y = 0
                self.jumped = False
                self.direction = 0

        def update(self, game_over):
                #globalize neccesary variables
                global map1
                global chasex
                global chasey
                global playerRectx
                global playerRecty
                global playerRect
                global engame_over
                global tackcooldown
                global chest1
                global rep
                global hitbox
                global speed
                global pegame_over
                global poof
                global Defe
                global playerDirection
                global Tack
                global eqa
                global terminate
                plcol = True
                dx = 0
                dy = 0
                walk_cooldown = 5
                screen.blit(stimg, (0, 0))
                draw_text('-Game Stats-', font_stats, (0,0,0,), (screen_width // 2)-620, 10)
                draw_text('Score ='+ str(score) +'', font_stats, (0,0,0), (screen_width // 2)-620, 50)
                

                if game_over == 0:
                        #get keypresses
                        key = pygame.key.get_pressed()
                        if tackcooldown <= 50:
                                screen.blit(hurt, (0, 0))
                        if key[pygame.K_UP]:
                                dy -= speed
                                self.counter += 1
                                self.direction = -2
                                self.vel_y = -1
                                self.image = self.images_right[self.index]
                        if key[pygame.K_DOWN]:
                                dy += speed
                                self.counter += 1
                                self.direction = -1
                                self.vel_y = 1
                                self.image = self.images_left[self.index]
                        if key[pygame.K_LEFT]:
                                dx -= speed
                                self.counter += 1
                                self.direction = 2
                                self.image = self.images_lefto[self.index]
                        if key[pygame.K_RIGHT]:
                                dx += speed
                                self.counter += 1
                                self.direction = 1
                                self.image = self.images_righto[self.index]
                        if key[pygame.K_LEFT] and key[pygame.K_LSHIFT]:
                                dx -= speed * 2
                                self.counter += 1
                                self.direction = 2
                                self.image = self.images_lefto[self.index]
                        if key[pygame.K_RIGHT] and key[pygame.K_LSHIFT]:
                                dx += speed * 2
                                self.counter += 1
                                self.direction = 1
                                self.image = self.images_righto[self.index]
                        if key[pygame.K_UP] and key[pygame.K_LSHIFT]:
                                dy -= speed * 2
                                self.counter += 1
                                self.direction = -2
                                self.vel_y = -1
                                self.image = self.images_right[self.index]
                        if key[pygame.K_DOWN] and key[pygame.K_LSHIFT]:
                                dy += speed * 2
                                self.counter += 1
                                self.direction = -1
                                self.vel_y = 1
                                self.image = self.images_left[self.index]
                        if key[pygame.K_x] == False:
                                Tack = False
                                if tackcooldown < 0:
                                        game_over = -1
                                if self.direction == 2:
                                        self.image = self.images_lefto[self.index]
                                if self.direction == -2:
                                        self.image = self.images_right[self.index]
                                if self.direction == -1:
                                        self.image = self.images_left[self.index]
                                if self.direction == 1:
                                        self.image = self.images_righto[self.index]
                                draw_text('Mana ='+ str(tackcooldown) +'', font_stats, (0,0,0), (screen_width // 2)-620, 30)
                        if key[pygame.K_z] == False:
                                Defe = False
                                if tackcooldown < 0:
                                        game_over = -1
                                if self.direction == 2:
                                        self.image = self.images_lefto[self.index]
                                if self.direction == -2:
                                        self.image = self.images_right[self.index]
                                if self.direction == -1:
                                        self.image = self.images_left[self.index]
                                if self.direction == 1:
                                        self.image = self.images_righto[self.index]
                                draw_text('Mana ='+ str(tackcooldown) +'', font_stats, (0,0,0), (screen_width // 2)-620, 30)
                        if key[pygame.K_z]:
                                tackcooldown -= 10
                                Defe = True
                                dounter = 0
                                if tackcooldown < 0:
                                        game_over = -1
                                if self.direction == 2:
                                        self.image = self.images_blockl[self.index]
                                if self.direction == -2:
                                        self.image = self.images_block[self.index]
                                if self.direction == -1:
                                        self.image = self.images_blockb[self.index]
                                if self.direction == 1:
                                        self.image = self.images_blockr[self.index]
                                draw_text('Mana ='+ str(tackcooldown) +'', font_stats, (0,0,0), (screen_width // 2)-620, 30)
                        if key[pygame.K_x]:
                                tackcooldown -= 20
                                Tack = True
                                dounter = 0
                                if tackcooldown < 0:
                                        game_over = -1
                                if self.direction == 2:
                                        self.image = self.images_lattack[self.index]
                                if self.direction == -2:
                                        self.image = self.images_attack[self.index]
                                if self.direction == -1:
                                        self.image = self.images_battack[self.index]
                                if self.direction == 1:
                                        self.image = self.images_rattack[self.index]
                                draw_text('Mana ='+ str(tackcooldown) +'', font_stats, (0,0,0), (screen_width // 2)-620, 30)
                        if key[pygame.K_SPACE]:
                                plcol = False
                                tackcooldown -= 30
                                if self.rect.y > 640:
                                        dx = 0 
                        if key[pygame.K_v]:
                                terminate = False
                                rep = True
                        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False and key[pygame.K_DOWN] and key[pygame.K_UP] :
                                self.counter = 0
                                self.index = 0
                                if self.direction == 1:
                                        self.image = self.images_righto[self.index]
                                if self.direction == -1:
                                        self.image = self.images_left[self.index]
                                if self.direction == -2:
                                        self.image = self.images_left[self.index]
                                if self.direction == 2:
                                        self.image = self.images_lefto[self.index]


                        if terminate == False:
                                if rep:
                                        poof = Poof(playerRectx, playerRecty)
                                pegame_over = poof.update(pegame_over)
                        
                                        

                        if plcol == True:
                                #check for collision
                                for tile in world.tile_list:
                                        if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height) or tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                                                #check for collision in x direction
                                                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                                                        dx = 0
                                                #check for collision in y dircetion
                                                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                                                        dy = 0


                                                


                        #update player coordinates
                        if dx > 0:
                                chasex = self.rect.x -50
                        if dy > 0:
                                chasey = self.rect.y -50
                        if dx < 0:
                                chasex = self.rect.x +50
                        if dy < 0:
                                chasey = self.rect.y +50
                        if dx == 0:
                                chasex = self.rect.x
                        if dy == 0:
                                chasey = self.rect.y
                        if dx == 0 and dy == 0:
                                chasey = 30000
                        
                        self.rect.x += dx
                        self.rect.y += dy

                        
                        
                #details what to do once player dies
                if game_over == -1:
                        #creates game over scene
                        self.image = self.dead_image
                        screen.fill((0,0,1))
                        pygame.draw.rect(screen, (255, 255,255), pygame.Rect(0, 320, 6000000, 6000))
                        if tackcooldown > 0:
                                draw_text('GAME OVER!', font, white, (screen_width // 2) - 200, screen_height // 2 - 100)
                        if tackcooldown < 1:
                                draw_text('GAME OVER!', font, (205, 50, 255), (screen_width // 2) - 200, screen_height // 2 - 100)
                        if engame_over == 0:
                                draw_text('Take The L And Search Up A Walkthrough!', font_score, blue, (screen_width // 2)-450, screen_height // 2 + 100)
                        if engame_over == 1:
                                draw_text('Take The L & Search Up A Walkthrough! Or Just Dont Kill', font_score, blue, 0, screen_height // 2 + 100)
                        if self.rect.y > 150:
                                self.rect.y -= 5
                
                                        
                                


                #draw player onto screen
                screen.blit(self.image, self.rect)


                #draw chasing enemy
                ene = pygame.image.load('img/blobo.png')
                ene = pygame.transform.scale(ene, (40, 40))
                if engame_over == 1:
                        if game_over == 0:
                                screen.blit(ene, (chasex, chasey))

                #create global variables for player location
                playerRect = self.rect
                playerRecty = self.rect.y
                playerRectx = self.rect.x
                playerDirection = self.direction
                

                return game_over
                



                
                                        
                                
class Eanemies():
        def __init__(self, x, y):
                self.images_right = []
                self.index = 0
                self.counter = 0
                img_right = pygame.image.load('img/blobo.png')
                for num in range(1, 5):
                        img_right = pygame.image.load('img/blobo.png')
                        img_right = pygame.transform.scale(img_right, (40, 40))
                        self.images_right.append(img_right)
                self.dead_image = pygame.image.load('img/gosto.png')
                self.image = self.images_right[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.width = self.image.get_width()
                self.height = self.image.get_height()
                self.vel_y = 0
                self.jumped = False
                self.direction = 0
                

        def update(self, eagame_over):
                global eanemyRect
                global Tack
                global eaalive
                global playerRecty
                global playerRectx
                global eanemyRecty
                global bulletRect
                global eanemyRectx
                global colcnter
                global eqa
                dx = 0
                dy = 0
                if eagame_over == 0:

                        if bulletRect.colliderect(self.rect):
                                eagame_over = -1
                        
                        if eanemyRectx > playerRectx:
                                dx -= 5
                        if eanemyRectx < playerRectx:
                                dx += 5
                        if eanemyRecty > playerRecty:
                                dy -= 5
                        if eanemyRecty < playerRecty:
                                dy += 5
                        self.image = self.images_right[self.index]
                        eaalive = True
                        
                        holdx = dx
                        holdy = dy
                
                        #check for collision
                        for tile in world.tile_list:
                                #check for collision in x direction
                                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                                        dx = 0
                                #check for collision in y direction
                                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                                        dy = 0
                                #check if above the ground i.e. falling
                                if 1280 < self.rect.x < 0 or 640 < self.rect.y < 0:
                                        dx = 0
                                        dy = 0

                        if holdx and holdy != 0:
                               if dx == 0 and dy == 0:
                                        if colcnter == 1:
                                                if holdx > 0:
                                                        dx = (holdx - (holdx *2))*2
                                                if holdx < 0:
                                                        dx = (holdx - (holdx *2))*2
                                                colcnter = 0
                                        elif colcnter == 0:
                                                if holdy > 0:
                                                        dy = (holdy - (holdy *2))*2
                                                if holdy < 0:
                                                        dy = (holdy - (holdy *2))*2
                                                colcnter = 1
                        #update player coordinates
                        self.rect.x += dx
                        self.rect.y += dy

                if eagame_over == -1:
                        eaalive = False
                        self.image = self.dead_image
                        if self.rect.y > 1500:
                                self.rect.y -= 5

                if eqa == True:
                        eqa = False
                        eagame_over = 0
                
                                        
                                


                #draw player onto screen
                screen.blit(self.image, self.rect)

                eanemyRect = self.rect
                eanemyRecty = self.rect.y
                eanemyRectx = self.rect.x


                return eagame_over
class Npc():
        def __init__(self, x, y):
                global npcangle
                self.images_right = []
                self.images_righto = []
                self.images_left = []
                self.images_lefto = []
                self.images_nw = []
                self.images_ne = []
                self.index = 0
                self.counter = 0
                img_right = pygame.image.load('img/npc.png')
                for num in range(1, 5):
                        img_right = pygame.image.load('img/npc.png')
                        img_left = pygame.transform.rotate(img_right, 180)
                        img_lefto = pygame.transform.rotate(img_right, 270)
                        img_righto = pygame.transform.rotate(img_right, 90)
                        img_right = pygame.transform.scale(img_right, (40, 40))
                        self.images_right.append(img_right)
                        self.images_left.append(img_left)
                        self.images_lefto.append(img_lefto)
                        self.images_righto.append(img_righto)                        
                self.dead_image = pygame.image.load('img/gosto.png')
                self.image = self.images_right[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.width = self.image.get_width()
                self.height = self.image.get_height()
                self.vel_y = 0
                self.jumped = False
                self.direction = 0

        def update(self, engame_over):
                global playerRecty
                global playerRectx
                global playerRect
                global npcangle
                global npcRecty
                global npcRectx
                global tackcooldown
                global npcRect
                brokenho = pygame.image.load('img/brokenhorror.png')
                meme = pygame.image.load('img/blinkscreen.png')
                
                if engame_over == 0:
                        #calculate angle of view
                        angx = abs(self.rect.x - playerRectx)
                        angy = abs(self.rect.y - playerRecty)
                        hypotnuse = math.sqrt(angy**2+ angx**2)
                        if hypotnuse > 0:
                                npcangle = math.degrees(math.atan(angy/hypotnuse))

                        if playerRecty > npcRecty and npcangle > 22:
                                self.image = self.images_left[self.index]
                        if playerRecty < npcRecty and npcangle > 22:
                                self.image = self.images_right[self.index]
                        if playerRectx > npcRectx and npcangle < 22:
                                self.image = self.images_lefto[self.index]
                        if playerRectx < npcRectx and npcangle < 22:
                                self.image = self.images_righto[self.index]
                 
                        #draw player onto screen
                        screen.blit(self.image, self.rect)
                        npcRect = self.rect
                        npcRecty = self.rect.y
                        npcRectx = self.rect.x

                if engame_over == 1:
                        listo = [1,2,3,4,5,6,7,8,9,10,11,22,33,44,55,66,77,88,99]
                        listc = random.choice(listo)
                        screen.blit(brokenho, (0,0))
                        tackcooldown -= 1
                        if listc == 1:
                                screen.blit (meme, (0, 0))


                return engame_over




white = (255, 255, 255)
blue = (101, 137, 255)

font = pygame.font.SysFont('Bauhaus 93', 70)
font_score = pygame.font.SysFont('Bauhaus 93', 50)
font_stats = pygame.font.SysFont('inkfree', 20)

def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

        


class World():
        def __init__(self, data):
                self.tile_list = []
                global scene
                global sceneo
                global hitbox

                #load images
                dirt_img = pygame.image.load('img/stone.png')
                grass_img = pygame.image.load('img/wood.png')
                roof_img = pygame.image.load('img/roof.png')               

                row_count = 0
                if scene == sceneo :
                        for row in data:
                                col_count = 0
                                for tile in row:
                                        if tile == 1:
                                                img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                                                img_rect = img.get_rect()
                                                img_rect.x = col_count * tile_size
                                                img_rect.y = row_count * tile_size
                                                tile = (img, img_rect)
                                                self.tile_list.append(tile)
                                        if tile == 2:
                                                img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                                                img_rect = img.get_rect()
                                                img_rect.x = col_count * tile_size
                                                img_rect.y = row_count * tile_size
                                                tile = (img, img_rect)
                                                self.tile_list.append(tile)
                                        if tile == 3:
                                                img = pygame.transform.scale(roof_img, (tile_size, tile_size))
                                                img_rect = img.get_rect()
                                                img_rect.x = col_count * tile_size
                                                img_rect.y = row_count * tile_size
                                                tile = (img, img_rect)
                                                self.tile_list.append(tile)

                                        col_count += 1
                                row_count += 1
                scene = sceneo 

        def draw(self):
                for tile in self.tile_list:
                        screen.blit(tile[0], tile[1])
                        if hitbox == True:
                                pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)
                                        
                                






world_data2 = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 0, 0, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
world_data1 = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1],
[1, 0, 0, 2, 3, 3, 3, 0, 0, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 2, 0, 1],
[1, 0, 0, 0, 2, 2, 2, 0, 0, 2, 2, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 2, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 2, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 0, 0, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

world_data3 = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1],
[1, 0, 0, 2, 3, 3, 3, 0, 0, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 2, 0, 1],
[1, 0, 0, 0, 2, 2, 2, 0, 0, 2, 2, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 2, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 2, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 2, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 2, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 2, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 2, 0, 0],
[1, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 2, 2, 3, 3, 2, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 0, 0, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

world_data4 = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
[1, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 2, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 2, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 1],
[1, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 0, 0, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 2, 0, 0, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 2, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 2, 0, 0, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 3, 3, 3, 3, 3, 3, 2, 0, 0, 1],
[1, 2, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 3, 3, 3, 3, 3, 3, 2, 0, 0, 1],
[1, 2, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 2, 0, 0, 1],
[1, 2, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 2, 0, 0, 1],
[1, 2, 3, 3, 3, 3, 3, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 2, 0, 0, 1],
[1, 2, 3, 3, 3, 3, 3, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 2, 0, 0, 1],
[1, 2, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

world_data5 = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

world_data6 = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 2, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 2, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 2, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 2, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 0, 0, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2],
[0, 0, 0, 0, 0, 0, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2],
[0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2],
[0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 2, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


world_data11 = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 2, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 2, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 2, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 2, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


player = Player(1200, 280)
npc = Npc(300, 250)
npc2 = Npc(860, 340)
npc1 = Npc(860, 340)
player1 = Player(20, 280)
bloba = Eanemies(640, 320)
player2 = Player (10, 280)
player4 = Player(20, 280)
player6 = Player(20, 280)
player7 = Player(20, 280)
player8 = Player(20, 280)
player9 = Player(20, 280)


world2 = World(world_data2)
world3 = World(world_data3)
world1 = World(world_data1)
world4 = World(world_data4)
world5 = World(world_data5)
world6 = World(world_data6)
world11 = World(world_data11)
pmmi = 0

def mapi():
        global pmmi
        global pm
        global fps
        global speed
        global hitbox
        global mapcnter
        global tackcooldown
        global game_over
        if pmmi == 0:
                screen.blit(pausemenu, (0, 0))
                screen.blit(gear, (0, 0))
                (mouseX, mouseY) = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN and 1150>mouseX >857 and 619 >mouseY> 400:
                        pmmi = 1
                if (event.type == pygame.MOUSEBUTTONDOWN and 784>mouseX >490 and 619 >mouseY> 400):
                        pmmi = 2
                if event.type == pygame.MOUSEBUTTONDOWN and 423>mouseX >125 and 619 >mouseY> 400:
                        pmmi = 3
                        mapcnter = 120
                if event.type == pygame.MOUSEBUTTONDOWN and 100>mouseX >0 and 100 >mouseY> 0:
                        pmmi = 4
        if pmmi == 1:
                pygame.quit()
        if pmmi == 2:
                pm = False
        if pmmi == 3:
                mapcnter -= 1
                if scene == 2:
                        map1= pygame.image.load('img/map1.8.png')
                if scene == 3:
                        map1= pygame.image.load('img/map1.7.png')
                if scene == 4:
                        map1= pygame.image.load('img/map1.6.png')
                if scene == 5:
                        map1= pygame.image.load('img/map1.10.png')
                if scene == 1:
                        map1= pygame.image.load('img/map1.1.png')
                if scene == 6:
                        map1= pygame.image.load('img/map1.11.png')
                if game_over == -1:
                        map1= pygame.image.load('img/mapded.png')
                screen.blit(map1, (0, 0))
                if (event.type == pygame.MOUSEBUTTONDOWN) and mapcnter <  0:
                        pmmi = 0
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        pmmi = 0
        if pmmi == 4:
                screen.blit(settingsmenu, (0, 0))
        
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print (mouseX)
                if (event.type == pygame.MOUSEBUTTONDOWN and 650>mouseX >200 and 75 >mouseY> 30):
                        hitbox = False
                        pmmi = 2
                if (event.type == pygame.MOUSEBUTTONDOWN and 1120>mouseX >710 and 75 >mouseY> 30):
                        hitbox = True
                        pmmi = 2
                if (event.type == pygame.MOUSEBUTTONDOWN and 487>mouseX >200 and 153 >mouseY> 111):
                        speed =1
                        pmmi = 2
                if (event.type == pygame.MOUSEBUTTONDOWN and 800>mouseX >500 and 153 >mouseY> 111):
                        speed =5
                        pmmi = 2
                if (event.type == pygame.MOUSEBUTTONDOWN and 1193>mouseX >814 and 153 >mouseY> 111):
                        speed =10
                        pmmi = 2
                if (event.type == pygame.MOUSEBUTTONDOWN and 650>mouseX >200 and 220 >mouseY> 180):
                        tackcooldown = 10
                        pmmi = 2
                if (event.type == pygame.MOUSEBUTTONDOWN and 1120>mouseX >710 and 220 >mouseY> 180):
                        tackcooldown = 1000
                        pmmi = 2
                if (event.type == pygame.MOUSEBUTTONDOWN and 434>mouseX >205 and 291 >mouseY> 251):
                        fps = 10
                        pmmi = 2
                if (event.type == pygame.MOUSEBUTTONDOWN and 687>mouseX >445 and 291 >mouseY> 251):
                        fps = 30
                        pmmi = 2
                if (event.type == pygame.MOUSEBUTTONDOWN and 943>mouseX >700 and 291 >mouseY> 251):
                        fps = 60
                        pmmi = 2
                if (event.type == pygame.MOUSEBUTTONDOWN and 1185>mouseX >945 and 291 >mouseY> 251):
                        fps = 120
                        pmmi = 2

                        
#If approach is from:
#Top, then direction = 1
#Bottom, then direction = 2
#Right side side, then direction = 3
#Left side, then direction = 4
# Refrence to the destination, not point of origin

def load():
        global loadcnter
        global loadcounter
        global fps
        global im16
        global im9
        global im10
        global im11
        global im12
        global im13
        global im14
        global im15
        global im1
        global im2
        global im3
        global im4
        global runn
        global im5
        global im6
        global im7
        global im8
        global event
        clock.tick(fps)
        (mouseX, mouseY) = pygame.mouse.get_pos()
        print (mouseY)
        if loadcounter == 1:
                screen.blit(im1, (0, 0))
                loadcnter += 1
                if loadcnter == fps:
                        loadcnter = 0
                        loadcounter += 1
        if loadcounter == 2:
                screen.blit(im2, (0,0))
                loadcnter += 1
                if loadcnter == fps:
                        loadcnter = 0
                        loadcounter += 1
        if loadcounter == 3:
                screen.blit(im3, (0,0))
                loadcnter += 1
                if loadcnter == fps:
                        loadcnter = 0
                        loadcounter += 1
        if loadcounter == 4:
                screen.blit(im4, (0,0))
                loadcnter += 1
                if loadcnter == fps:
                        loadcnter = 0
                        loadcounter += 1
        if loadcounter == 5:
                screen.blit(im5, (0,0))
                loadcnter += 1
                if loadcnter == fps:
                        loadcnter = 0
                        loadcounter += 1
        if loadcounter == 6:
                screen.blit(im6, (0,0))
                loadcnter += 1
                if loadcnter == fps:
                        loadcnter = 0
                        loadcounter += 1
        if loadcounter == 7:
                screen.blit(im7, (0,0))
                loadcnter += 1
                if loadcnter == fps:
                        loadcnter = 0
                        loadcounter += 1
        if loadcounter == 8:
                screen.blit(im8, (0,0))
                loadcnter += 1
                if loadcnter == fps:
                        loadcnter = 0
                        loadcounter += 1
        if loadcounter == 9:
                screen.blit(im9, (0,0))
                loadcnter += 1
                if loadcnter == fps:
                        loadcnter = 0
                        loadcounter += 1
        if loadcounter == 10:
                screen.blit(im10, (0,0))
                loadcnter += 1
                if loadcnter == fps:
                        loadcnter = 0
                        loadcounter += 1
        if loadcounter == 11:
                screen.blit(im11, (0,0))
                loadcnter += 1
                if loadcnter == fps:
                        loadcnter = 0
                        loadcounter += 1
        if loadcounter == 12:
                screen.blit(im12, (0,0))
                loadcnter += 1
                if loadcnter == fps:
                        loadcnter = 0
                        loadcounter += 1
        if loadcounter == 13:
                screen.blit(im13, (0,0))
                loadcnter += 1
                if loadcnter == fps:
                        loadcnter = 0
                        loadcounter += 1
        if loadcounter == 14:
                screen.blit(im14, (0,0))
                loadcnter += 1
                if loadcnter == fps:
                        loadcnter = 0
                        loadcounter += 1
        if loadcounter == 15:
                screen.blit(im15, (0,0))
                loadcnter += 1
                if loadcnter == fps:
                        loadcnter = 0
                        loadcounter += 1
        if loadcounter == 16:
                screen.blit(im16, (0,0))
                loadcnter += 1
                if loadcnter == fps:
                        loadcnter = 0
                        loadcounter = 9
        pygame.display.update()
        
def scene1():
        global scene
        global fps
        global text
        global text1
        global bg_img
        global world
        global eanemyRect
        global worlddirection
        global playerRect
        global pm
        global pmmi
        global eagame_over
        global rep
        global terminate
        global pegame_over
        global poof
        global game_over
        global eaalive
        global playerRectx
        global playerRecty
        global hitbox
        global Defe
        global fc
        global npc
        global player
        global bloba
        global Tack
        global tackcooldown
        global event
        global score
        global world
        global runn
        global eqa
        global engame_over
        bg_img = pygame.image.load('img/ground.png')
        clock.tick(fps)
        text = text1
        scene = 1
        world = world2

        if fc ==  True:
                player = Player(1200, 280)
                npc = Npc(280, 260)
                npc1 = Npc(860, 340)
                player1 = Player(20, 280)
        fc = False
                
                
        screen.blit(bg_img, (0, 0))


        

        world.draw()
        if hitbox == True:
                pygame.draw.rect(screen, (255, 255, 255), playerRect, 2)
                pygame.draw.rect(screen, (255, 255, 255), npcRect, 2)



        if pygame.key.get_pressed()[pygame.K_c] or pm == True:
                pm = True
                mapi()
                if pmmi == 2:
                        pmmi = 0
        if pm == False:
                engame_over = npc.update(engame_over)
                if worlddirection == 3:
                        game_over = player.update(game_over)

                if playerRect.colliderect(npcRect) and engame_over == 0:
                        if game_over == 0:
                                screen.blit(text, (0, 0))

                if playerRect.colliderect(npcRect) and Tack == True:
                        engame_over = 1

                        
                if playerRectx > 1280:
                        eqa = True
                        fc = True
                        runn = 2
                        worlddirection = 4
                        



               
                         

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        pygame.display.update()
def scene2():
        global scene
        global worlddirection
        global fps
        global text
        global text1
        global player4
        global bg_img
        global world
        global im1
        global eanemyRect
        global playerRect
        global npc1
        global player1
        global bloba
        global npcRect
        global npcRecty
        global hitbox
        global npcRectx
        global pm
        global fc
        global pmmi
        global eagame_over
        global game_over
        global eaalive
        global playerRectx
        global playerRecty
        global Defe
        global Tack
        global tackcooldown
        global engame_over
        global event
        global score
        global world
        global runn
        global eqa
        bg_img = pygame.image.load('img/ground1.png')
        clock.tick(fps)
        text = text2
        scene = 2
        world = world1

        if fc:
                player = Player(1200, 280)
                npc = Npc(300, screen_height - 100)
                npc1 = Npc(860, 340)
                player1 = Player(1270, 280)
                player4 = Player(20, 280)
        fc = False
                
        screen.blit(bg_img, (0, 0))

        

        world.draw()
        if hitbox == True:
                pygame.draw.rect(screen, (255, 255, 255), playerRect, 2)
                pygame.draw.rect(screen, (255, 255, 255), eanemyRect, 2)
                pygame.draw.rect(screen, (255, 255, 255), npcRect, 2)

        if playerRect.colliderect(npcRect):
                        screen.blit(text, (0, 0))

        


        if pygame.key.get_pressed()[pygame.K_c] or pm == True:
                pm = True
                mapi()
                if pmmi == 2:
                        pmmi = 0
        if pm == False:
                engame_over = npc1.update(engame_over)
                if worlddirection == 4:
                        game_over = player4.update(game_over)
                if worlddirection == 3:
                        game_over = player1.update(game_over)


                if playerRect.colliderect(npcRect) and engame_over == 0:
                        if game_over == 0:
                                screen.blit(text, (0, 0))

                if playerRect.colliderect(npcRect) and Tack == True:
                        engame_over = 1

                if playerRectx < 0:
                        worlddirection = 3
                        eqa = True
                        fc = True
                        runn = 1
                if playerRectx > 1280:
                        worlddirection = 4
                        eqa = True
                        fc = True
                        runn = 3
                
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        pygame.display.update()
def scene3():
        global scene
        global worlddirection
        global fps
        global text
        global text1
        global bg_img
        global world
        global im1
        global eanemyRect
        global playerRect
        global npc1
        global player1
        global bloba
        global npcRect
        global player6
        global npcRecty
        global text5
        global hitbox
        global npcRectx
        global pm
        global fc
        global player2
        global pmmi
        global eagame_over
        global game_over
        global eaalive
        global playerRectx
        global playerRecty
        global player7
        global Defe
        global Tack
        global tackcooldown
        global engame_over
        global event
        global score
        global world
        global runn
        global eqa
        bg_img = pygame.image.load('img/ground2.png')
        clock.tick(fps)
        text = text5
        scene = 3
        world = world3

        if fc:
                player = Player(1200, 280)
                player2 = Player(10, 280)
                player6 = Player(300, 10)
                player7 = Player(920, 620)
                npc = Npc(300, screen_height - 100)
                npc1 = Npc(860, 340)
                player1 = Player(20, 280)
        fc = False
                
        screen.blit(bg_img, (0, 0))

        

        world.draw()
        if hitbox == True:
                pygame.draw.rect(screen, (255, 255, 255), playerRect, 2)
                pygame.draw.rect(screen, (255, 255, 255), eanemyRect, 2)
                pygame.draw.rect(screen, (255, 255, 255), npcRect, 2)

        if playerRect.colliderect(npcRect):
                        screen.blit(text, (0, 0))

        


        if pygame.key.get_pressed()[pygame.K_c] or pm == True:
                pm = True
                mapi()
                if pmmi == 2:
                        pmmi = 0
        if pm == False:
                engame_over = npc1.update(engame_over)
                if worlddirection == 4:
                        game_over = player2.update(game_over)

                if worlddirection == 1:
                        game_over = player7.update(game_over)
                        
                if playerRect.colliderect(npcRect) and engame_over == 0:
                        if game_over == 0:
                                screen.blit(text, (0, 0))

                if playerRect.colliderect(npcRect) and Tack == True:
                        engame_over = 1

                if playerRectx < 0:
                        worlddirection = 3
                        eqa = True
                        fc = True
                        runn = 2
                if playerRecty > 640:
                        worlddirection = 1
                        eqa = True
                        fc = True
                        runn = 4
                
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        pygame.display.update()

def scene4():
        global scene
        global fps
        global text
        global text3
        global bg_img
        global world
        global eanemyRect
        global worlddirection
        global playerRect
        global pm
        global pmmi
        global eagame_over
        global game_over
        global eaalive
        global playerRectx
        global playerRecty
        global hitbox
        global player6
        global player9
        global Defe
        global fc
        global npc
        global npc2
        global player
        global bloba
        global Tack
        global tackcooldown
        global event
        global score
        global world
        global runn
        global eqa
        global engame_over
        bg_img = pygame.image.load('img/ground6.png')
        clock.tick(fps)
        text = text3
        scene = 4
        world = world4

        if fc ==  True:
                player = Player(1200, 280)
                npc = Npc(280, 260)
                npc1 = Npc(860, 340)
                npc2 = Npc(760, 540)
                player6 = Player(600, 100)
                player9 = Player(1270, 300)
                player1 = Player(20, 280)
        fc = False
                
                
        screen.blit(bg_img, (0, 0))


        

        world.draw()
        if hitbox == True:
                pygame.draw.rect(screen, (255, 255, 255), playerRect, 2)
                pygame.draw.rect(screen, (255, 255, 255), eanemyRect, 2)



        if pygame.key.get_pressed()[pygame.K_c] or pm == True:
                pm = True
                mapi()
                if pmmi == 2:
                        pmmi = 0
        if pm == False:
                engame_over = npc2.update(engame_over)
                if worlddirection == 1:
                        game_over = player6.update(game_over)
                if worlddirection == 4:
                        game_over = player9.update(game_over)

                if playerRecty < 100:
                        eqa = True
                        fc = True
                        runn = 3
                        worlddirection = 1
                if playerRectx > 1280:
                        eqa = True
                        fc = True
                        runn = 5
                        worlddirection = 3
                        
                if playerRect.colliderect(npcRect) and engame_over == 0:
                        if game_over == 0:
                                screen.blit(text, (0, 0))

                if playerRect.colliderect(npcRect) and Tack == True:
                        engame_over = 1
                                
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        pygame.display.update()

def scene5():
        global scene
        global fps
        global text
        global text1
        global text4
        global bg_img
        global world
        global eanemyRect
        global worlddirection
        global playerRect
        global pm
        global pmmi
        global eagame_over
        global game_over
        global eaalive
        global playerRectx
        global playerRecty
        global hitbox
        global Defe
        global fc
        global npc
        global player8
        global bloba
        global Tack
        global tackcooldown
        global event
        global score
        global world
        global runn
        global player9
        global engame_over
        global text4
        global eqa
        bg_img = pygame.image.load('img/ground7.png')
        clock.tick(fps)
        text = text4
        scene = 5
        world = world5

        if fc ==  True:
                player8 = Player(20, 280)
                player9 = Player(1260, 280)
                npc = Npc(280, 260)
                npc1 = Npc(860, 340)
                player1 = Player(20, 320)
        fc = False
                
                
        screen.blit(bg_img, (0, 0))


        

        world.draw()
        if hitbox == True:
                pygame.draw.rect(screen, (255, 255, 255), playerRect, 2)
                pygame.draw.rect(screen, (255, 255, 255), eanemyRect, 2)
                pygame.draw.rect(screen, (255, 255, 255), npcRect, 2)



        if pygame.key.get_pressed()[pygame.K_c] or pm == True:
                pm = True
                mapi()
                if pmmi == 2:
                        pmmi = 0
        if pm == False:
                engame_over = npc.update(engame_over)
                eagame_over = bloba.update(eagame_over)
                if worlddirection == 3:
                        game_over = player8.update(game_over)
                if worlddirection == 4:
                        game_over = player9.update(game_over)

                if playerRect.colliderect(npcRect) and engame_over == 0:
                        if game_over == 0:
                                screen.blit(text, (0, 0))

                if playerRect.colliderect(npcRect) and Tack == True:
                        engame_over = 1

                if playerRectx < 0:
                        eqa = True
                        fc = True
                        runn = 4
                        worlddirection = 4
                if playerRectx > 1280:
                        eqa = True
                        fc = True
                        runn = 6
                        worlddirection = 3
                        

                if eagame_over == 0:
                        if playerRect.colliderect(eanemyRect):
                                if Defe == False and Tack == True:
                                        Tack = Tack
                                if Defe == False and Tack == False:
                                        game_over = -1
                                if Tack == True:
                                        eagame_over = -1
                                if tackcooldown >= 11:
                                        tackcooldown -= 10
                else:
                        if playerRect.colliderect(eanemyRect):
                                if tackcooldown >= 11:
                                        tackcooldown -= 10


               
                         

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        pygame.display.update()

def scene6():
        global scene
        global fps
        global text
        global text1
        global text4
        global bg_img
        global world
        global player1
        global world6
        global eanemyRect
        global worlddirection
        global playerRect
        global pm
        global pmmi
        global eagame_over
        global game_over
        global eaalive
        global playerRectx
        global playerRecty
        global hitbox
        global Defe
        global fc
        global npc
        global engame_over
        global player8
        global bloba
        global Tack
        global tackcooldown
        global event
        global score
        global runn
        global text4
        global eqa
        bg_img = pygame.image.load('img/ground7.png')
        clock.tick(fps)
        text = text7
        scene = 6
        world = world6

        if fc ==  True:
                player8 = Player(20, 280)
                npc = Npc(620, 450)
                npc1 = Npc(860, 340)
                player1 = Player(740, 270)
        fc = False
                
                
        screen.blit(bg_img, (0, 0))


        

        world.draw()
        if hitbox == True:
                pygame.draw.rect(screen, (255, 255, 255), playerRect, 2)
                pygame.draw.rect(screen, (255, 255, 255), eanemyRect, 2)
                pygame.draw.rect(screen, (255, 255, 255), npcRect, 2)



        if pygame.key.get_pressed()[pygame.K_c] or pm == True:
                pm = True
                mapi()
                if pmmi == 2:
                        pmmi = 0
        if pm == False:
                engame_over = npc.update(engame_over)
                #eagame_over = bloba.update(eagame_over)
                if worlddirection == 3:
                        game_over = player8.update(game_over)
                if worlddirection == 5:
                        game_over = player1.update(game_over)

                if playerRect.colliderect(npcRect) and engame_over == 0:
                        if game_over == 0:
                                screen.blit(text, (0, 0))

                if playerRect.colliderect(npcRect) and Tack == True:
                        engame_over = 1

                if playerRectx < 0:
                        eqa = True
                        fc = True
                        runn = 5
                        worlddirection = 4

                if playerRect == (740, 240, 40, 40):
                        eqa = True
                        fc = True
                        runn = 11
                        worlddirection = 3
                        

                if eagame_over == 0:
                        if playerRect.colliderect(eanemyRect):
                                if Defe == False and Tack == True:
                                        Tack = Tack
                                if Defe == False and Tack == False:
                                        game_over = -1
                                if Tack == True:
                                        eagame_over = -1
                                if tackcooldown >= 11:
                                        tackcooldown -= 10
                else:
                        if playerRect.colliderect(eanemyRect):
                                if tackcooldown >= 11:
                                        tackcooldown -= 10


               
                         

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        pygame.display.update()
def scene11():
        global scene
        global fps
        global text
        global text1
        global text4
        global bg_img
        global world
        global world6
        global eanemyRect
        global worlddirection
        global playerRect
        global pm
        global pmmi
        global eagame_over
        global game_over
        global eaalive
        global playerRectx
        global playerRecty
        global hitbox
        global Defe
        global fc
        global npc
        global player8
        global bloba
        global Tack
        global tackcooldown
        global event
        global score
        global runn
        global text6
        global eqa
        global engame_over
        bg_img = pygame.image.load('img/sorhouse.png')
        clock.tick(fps)
        text = text6
        scene = 6
        world = world11

        if fc ==  True:
                player8 = Player(580, 500)
                npc = Npc(950, 320)
                npc1 = Npc(860, 340)
                player1 = Player(20, 320)
        fc = False
                
                
        screen.blit(bg_img, (0, 0))


        

        world.draw()
        if hitbox == True:
                pygame.draw.rect(screen, (255, 255, 255), playerRect, 2)
                pygame.draw.rect(screen, (255, 255, 255), eanemyRect, 2)
                pygame.draw.rect(screen, (255, 255, 255), npcRect, 2)



        if pygame.key.get_pressed()[pygame.K_c] or pm == True:
                pm = True
                mapi()
                if pmmi == 2:
                        pmmi = 0
        if pm == False:
                engame_over = npc.update(engame_over)
                if worlddirection == 3:
                        game_over = player8.update(game_over)

                if playerRect.colliderect(npcRect) and engame_over == 0:
                        if game_over == 0:
                                screen.blit(text, (0, 0))

                if playerRect.colliderect(npcRect) and Tack == True:
                        engame_over = 1

                if playerRecty > 540:
                        eqa = True
                        fc = True
                        runn = 6
                        worlddirection = 5


               
                         

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        pygame.display.update()


pm = False

runn = 1
run = True
while run:
        print (rep)
        if runn == 1:
                scene1()
        elif runn == 2:
                scene2()
        elif runn == 3:
                scene3()
        elif runn == 4:
                scene4()
        elif runn == 5:
                scene5()
        elif runn == 6:
                scene6()
        elif runn == 11:
                scene11()
        elif runn == -1:
                load()
pygame.quit()
