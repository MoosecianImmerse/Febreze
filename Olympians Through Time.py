import pygame
import time
import math
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 120

screen_width = 1280
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Olympians')

#define game variables
tile_size = 20
game_over = 0
egame_over = 0
eagame_over = 0
engame_over = 0
scene = 0
sprint = True
Tack = False
chest1 = True
Defe = False
ealive = True
eaalive = True
sceneo = scene
mapo = False
npcangle = 0
score = 0
playerRectx = 0
playerRecty= 0
npcRectx = 0
npcRecty= 0
enemyRectx = 0
enemyRecty = 0
eqa = False
eanemyRectx = 0
eanemyRecty = 0
tackcooldown = 700
playerRect = pygame.Rect(0, 0, 20, 20)
npcRect = pygame.Rect(0, 0, 20, 20)
eanemyRect = pygame.Rect(0, 0, 20, 20)


#load images
text = pygame.image.load('img/text.png')
text1 = pygame.image.load('img/text1.png')
text2 = pygame.image.load('img/text2.png')
bg_img = pygame.image.load('img/ground.png')
stimg = pygame.image.load('img/statbox.png')
hurt = pygame.image.load('img/hurt.png')
map1= pygame.image.load('img/map1.1.png')
pausemenu= pygame.image.load('img/PauseMenu.png')
settingsmenu= pygame.image.load('img/settingsmenu.png')
gear = pygame.image.load('img/Gear.png')


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
                global map1
                global playerRectx
                global playerRecty
                global playerRect
                global tackcooldown
                global chest1
                global enemdie
                global Defe
                global Tack
                global eqa
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
                                dy -= 5
                                self.counter += 1
                                self.direction = -2
                                self.vel_y = -1
                                self.image = self.images_right[self.index]
                        if key[pygame.K_DOWN]:
                                dy += 5
                                self.counter += 1
                                self.direction = -1
                                self.vel_y = 1
                                self.image = self.images_left[self.index]
                        if key[pygame.K_LEFT]:
                                dx -= 5
                                self.counter += 1
                                self.direction = 2
                                self.image = self.images_lefto[self.index]
                        if key[pygame.K_RIGHT]:
                                dx += 5
                                self.counter += 1
                                self.direction = 1
                                self.image = self.images_righto[self.index]
                        if key[pygame.K_LEFT] and key[pygame.K_LSHIFT]:
                                dx -= 10
                                self.counter += 1
                                self.direction = 2
                                self.image = self.images_lefto[self.index]
                        if key[pygame.K_RIGHT] and key[pygame.K_LSHIFT]:
                                dx += 10
                                self.counter += 1
                                self.direction = 1
                                self.image = self.images_righto[self.index]
                        if key[pygame.K_UP] and key[pygame.K_LSHIFT]:
                                dy -= 10
                                self.counter += 1
                                self.direction = -2
                                self.vel_y = -1
                                self.image = self.images_right[self.index]
                        if key[pygame.K_DOWN] and key[pygame.K_LSHIFT]:
                                dy += 10
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
                        
                                        

                        
                        #check for collision
                        for tile in world.tile_list:
                                #check for collision in x direction
                                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                                        dx = 0
                                #check for collision in y direction
                                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                                        dy = 0
                                #check if above the ground i.e. falling
                                        dy = 0
                                if 1280 < self.rect.x < 0 or 640 < self.rect.x < 0:
                                        dx = 0
                                        dy = 0

                        
                        
                        
                        
        
                        #update player coordinates
                        self.rect.x += dx
                        self.rect.y += dy

                if game_over == -1:
                        self.image = self.dead_image
                        screen.fill((0,0,1))
                        pygame.draw.rect(screen, (255, 255,255), pygame.Rect(0, 320, 6000000, 6000))
                        draw_text('GAME OVER!', font, white, (screen_width // 2) - 200, screen_height // 2 - 100)
                        draw_text('Take The L And Search Up A Walkthrough!', font_score, blue, (screen_width // 2)-450, screen_height // 2 + 100)
                        if self.rect.y > 150:
                                self.rect.y -= 5
                
                                        
                                


                #draw player onto screen
                screen.blit(self.image, self.rect)
                playerRect = self.rect
                playerRecty = self.rect.y
                playerRectx = self.rect.x
                

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
                global eanemyRectx
                global eqa
                dx = 0
                dy = 0
                if eagame_over == 0:
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

                
                        #check for collision
                        for tile in world.tile_list:
                                #check for collision in x direction
                                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                                        dx = 0
                                #check for collision in y direction
                                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                                        dy = 0
                                #check if above the ground i.e. falling
                                        dy = 0
                                if 1280 < self.rect.x < 0 or 640 < self.rect.x < 0:
                                        dx = 0
                                        dy = 0

                        
                        
                        
                        
        
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
                        img_lefto = pygame.transform.rotate(img_right, 90)
                        img_righto = pygame.transform.rotate(img_right, 270)
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
                global npcRect

                #calculate angle of view
                angx = abs(self.rect.x - playerRectx)
                angy = abs(self.rect.y - playerRecty)
                hypotnuse = math.sqrt(angy**2+ angx**2)
                if hypotnuse > 0:
                        npcangle = math.degrees(math.atan(angy/hypotnuse))
                print (npcangle)

                if playerRecty > npcRecty and npcangle > 22:
                        self.image = self.images_left[self.index]
                if playerRecty < npcRecty and npcangle > 22:
                        self.image = self.images_right[self.index]
                if playerRecty > npcRecty and npcangle < 22:
                        self.image = self.images_lefto[self.index]
                if playerRecty < npcRecty and npcangle < 22:
                        self.image = self.images_righto[self.index]
         
                        
                        



                #draw player onto screen
                screen.blit(self.image, self.rect)
                npcRect = self.rect
                npcRecty = self.rect.y
                npcRectx = self.rect.x


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
                        pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)







world_data2 = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1], 
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
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 0, 0, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
world_data1 = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1],
[1, 0, 0, 2, 3, 3, 3, 0, 0, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 2, 0, 1],
[1, 0, 0, 0, 2, 2, 2, 0, 0, 2, 2, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 2, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 2, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 0, 0, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]



player = Player(300, screen_height - 130)
npc = Npc(300, screen_height - 100)
player1 = Player(20, 280)
bloba = Eanemies(300, 280)


lava_group = pygame.sprite.Group()
npc_group = pygame.sprite.Group()
chest_group = pygame.sprite.Group()

world2 = World(world_data2)
world1 = World(world_data1)
pmmi = 0

def mapi():
        global pmmi
        global pm
        global fps
        print (fps)
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
                if event.type == pygame.MOUSEBUTTONDOWN and 100>mouseX >0 and 100 >mouseY> 0:
                        pmmi = 4
        if pmmi == 1:
                pygame.quit()
        if pmmi == 2:
                pm = False
        if pmmi == 3:
                if scene == 2:
                        map1= pygame.image.load('img/map1.8.png')
                if scene == 1:
                        map1= pygame.image.load('img/map1.1.png')
                screen.blit(map1, (0, 0))
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        pmmi = 0
        if pmmi == 4:
                screen.blit(settingsmenu, (0, 0))
                screen.blit(gear, (0, 0))
        
                (mouseX, mouseY) = pygame.mouse.get_pos()
                if (event.type == pygame.MOUSEBUTTONDOWN and 784>mouseX >490 and 619 >mouseY> 400):
                        if fps == 30:
                                fps = 60
                        if fps == 60:
                                fps = 120
                        if fps == 120:
                                fps = 30
                        draw_text(' ='+ str(fps) +'', font_stats, (0,0,0), (screen_width // 2)-620, 30)
                
                

        

def scene1():
        global scene
        global fps
        global text
        global text1
        global bg_img
        global world
        global eanemyRect
        global playerRect
        global pm
        global pmmi
        global eagame_over
        global game_over
        global eaalive
        global playerRectx
        global playerRecty
        global Defe
        global Tack
        global tackcooldown
        global event
        global score
        global world
        global runn
        global eqa
        bg_img = pygame.image.load('img/ground.png')
        clock.tick(fps)
        text = text1
        engame_over = 0
        scene = 1
        world = world2
                
        screen.blit(bg_img, (0, 0))

        

        world.draw()
        pygame.draw.rect(screen, (255, 255, 255), playerRect, 2)
        pygame.draw.rect(screen, (255, 255, 255), eanemyRect, 2)



        if pygame.key.get_pressed()[pygame.K_c] or pm == True:
                pm = True
                mapi()
                if pmmi == 2:
                        pmmi = 0
        if pm == False:
                engame_over = npc.update(engame_over)
                eagame_over = bloba.update(eagame_over)
                game_over = player.update(game_over)

                if playerRect.colliderect(npcRect):
                        screen.blit(text, (0, 0))

                if playerRectx > 1280:
                        eqa = True
                        runn = 2
                        

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


                        

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        pygame.display.update()
def scene2():
        global scene
        global fps
        global text
        global text1
        global bg_img
        global world
        global eanemyRect
        global playerRect
        global npcRect
        global npcRecty
        global npcRectx
        global pm
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
                
        screen.blit(bg_img, (0, 0))

        

        world.draw()
        pygame.draw.rect(screen, (255, 255, 255), playerRect, 2)
        pygame.draw.rect(screen, (255, 255, 255), eanemyRect, 2)

        if playerRect.colliderect(npcRect):
                        screen.blit(text, (0, 0))

        


        if pygame.key.get_pressed()[pygame.K_c] or pm == True:
                pm = True
                mapi()
                if pmmi == 2:
                        pmmi = 0
        if pm == False:
                eagame_over = bloba.update(eagame_over)
                engame_over = npc.update(engame_over)
                game_over = player1.update(game_over)

                if playerRectx < 0:
                        eqa = True
                        runn = 1
                
                        

                if eagame_over == 0:
                        if playerRect.colliderect(eanemyRect):
                                if Defe == False and Tack == True:
                                        Tack = Tack
                                if Defe == False and Tack == False:
                                        game_over = -1
                                if Tack == True:
                                        eagame_over = -1
                                        score += 100
                else:
                        if playerRect.colliderect(eanemyRect):
                                if tackcooldown >= 11:
                                        tackcooldown -= 10


                        

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        pygame.display.update()
pm = False

runn = 1
run = True
while run:
        if runn == 1:
                scene1()
        elif runn == 2:
                scene2()
pygame.quit()
