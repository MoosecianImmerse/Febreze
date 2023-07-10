#Import Neccesary Modules
import pygame
import time
import math
import os
from pygame.locals import *

#Define Variables
bal = False
tral = False
skin = 0
ral = True
balo = False
ftime = True
ruuun = 2
fps = 60
runn = True
screen_width = 640
screen_height = 320
cnter = 0
nativescreen = 0
cral = False       

#Initialize and Set Up Pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Olympians')

#Define Pre-Function Image Variables
bag_img = pygame.image.load("img/ManorWo.png")


def rr2():
        #Gloabilize Variables
        global event
        global cnter
        global skin
        global clock
        global fps
        global ral
        global bal
        global balo
        global ftime
        global screen
        global bag_img
        global cral
        global ruuun
        global tral
        global nativescreen
        global event
        global cnter
        global skin
        global clock
        global fps
        global ral
        global bal
        global balo
        global ftime
        global screen
        global bag_img
        global ruuun
        global runn
        global tral

        #Define Function Images Neccesary
        pale = "C:img/paleman.png"
        white = "C:img/whiteman.png"
        brown = "C:img/brownman.png"
        browner = "C:img/brownerman.png"
        palea = "C:img/palea.png"
        whitea = "C:img/whitea.png"
        browna = "C:img/browna.png"
        brownera = "C:img/brownera.png"
        paleb = "C:img/paleb.png"
        whiteb = "C:img/whiteb.png"
        brownb = "C:img/brownb.png"
        brownerb = "C:img/brownerb.png"
        new_file_name = "img/guy.png"
        new_file_name2 = "img/guyb.png"
        new_file_name3 = "img/guya.png"
        MorW = pygame.image.load("img/ManorWo.png")
        Man = pygame.image.load("img/Man.png")
        Woman = pygame.image.load("img/Woman.png")
        bg_img = pygame.image.load('img/pickpla.png')
        re_img = pygame.image.load('img/readyscr.png')
        home = pygame.image.load ('img/homeload.png')
        sklo = pygame.image.load ('img/skinload.png')
        

        #Define Mouse
        (mouseX, mouseY) = pygame.mouse.get_pos()

        #Run CLock In Frames Per Second
        clock.tick(fps)

        if cral and skin != 0:
                guy = pygame.image.load ('img/guy.png')
                guy = pygame.transform.scale(guy, (80,80))

                #Choose Background Image
                if nativescreen == 0:
                        bag_img = home
                if nativescreen == 1:
                        bag_img = sklo
                     
                #Display Background Image
                screen.blit(bag_img, (0, 0))
                
                #Program For Termination        
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()

                print (mouseX, mouseY)

                if nativescreen == 0:
                        if event.type == pygame.MOUSEBUTTONDOWN and 432>mouseX >210 and 309 >mouseY> 267:
                                #Run Game
                                import Game.py
                        if event.type == pygame.MOUSEBUTTONDOWN and 211>mouseX >114 and 36 >mouseY> 7:
                                #Skin Page
                                nativescreen = 1
                if nativescreen == 1:
                        if skin != 0:
                                screen.blit(guy,(70,90))
                        if event.type == pygame.MOUSEBUTTONDOWN and 114>mouseX >10 and 36 >mouseY> 7:
                                #Home Page
                                nativescreen = 0
                        if event.type == pygame.MOUSEBUTTONDOWN and 432>mouseX >210 and 309 >mouseY> 267:
                                #Run Game
                                import Game.py
                        if event.type == pygame.MOUSEBUTTONDOWN and 219>mouseX >12 and 239 >mouseY> 200:
                                #Reset And Change Skin
                                #If White Skin
                                if skin == 1:
                                        os.rename(new_file_name, white)
                                        os.rename(new_file_name2, whiteb)
                                        os.rename(new_file_name3, whitea)
                                        skin = 0
                                        cral = False
                                #If Browner Skin
                                if skin == 2:
                                        os.rename(new_file_name, browner)
                                        os.rename(new_file_name2, brownerb)
                                        os.rename(new_file_name3, brownera)
                                        skin = 0
                                        cral = False
                                #If Brown Skin
                                if skin == 4:
                                        os.rename(new_file_name, brown)
                                        os.rename(new_file_name2, brownb)
                                        os.rename(new_file_name3, browna)
                                        skin = 0
                                        cral = False
                                if skin == 3:
                                        os.rename(new_file_name, pale)
                                        os.rename(new_file_name2, paleb)
                                        os.rename(new_file_name3, palea)
                                        skin = 0
                                        cral = False


        if cral == False:
                #Display Background Image
                screen.blit(bag_img, (0, 0))
                
                #Program For Termination        
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                
                #Program for Gender Selection Section                
                if ral:
                        #If Man
                        if event.type == pygame.MOUSEBUTTONDOWN and 320>mouseX >0 and 320 >mouseY> 0 or bal == True:
                                bag_img = Man
                                bal = True
                                cnter += 1
                                if cnter == 100:
                                        cnter = 0
                                        tral = True
                                        ral = False
                                        balo = False
                        #If Woman
                        if event.type == pygame.MOUSEBUTTONDOWN and 640>mouseX >320 and 320 >mouseY> 0 or balo == True:
                                print (cnter)
                                bag_img = Woman
                                balo = True
                                cnter += 1
                                if cnter == 100:
                                        cnter = 0
                                        tral = True
                                        ral = False
                                        bal = False
                #Program for Skin Color Selection Program
                if tral:

                        #Change Background Image Variable
                        if bag_img == Man or bag_img == Woman:
                                bag_img = bg_img

                        #If White Skin
                        if event.type == pygame.MOUSEBUTTONDOWN and 320>mouseX >0 and 160 >mouseY> 0:
                            os.rename(white, new_file_name)
                            os.rename(whiteb, new_file_name2)
                            os.rename(whitea, new_file_name3)
                            screen.blit(re_img, (0, 0))
                            runn = True
                            while runn:
                                cnter += 1
                                if cnter == 360:
                                        skin = 1
                                        cral = True
                                        runn = False
                                pygame.display.update()

                        #If Browner Skin
                        if event.type == pygame.MOUSEBUTTONDOWN and 640>mouseX >321 and 160 >mouseY> 0:
                            os.rename(browner, new_file_name)
                            os.rename(brownerb, new_file_name2)
                            os.rename(brownera, new_file_name3)
                            screen.blit(re_img, (0, 0))
                            while runn:
                                cnter += 1
                                if cnter > 360:
                                        skin = 2
                                        cral = True
                                        runn = False
                                pygame.display.update()

                        #If Pale Skin
                        if event.type == pygame.MOUSEBUTTONDOWN and 320>mouseX >0 and 320 >mouseY> 161:
                            os.rename(pale, new_file_name)
                            os.rename(paleb, new_file_name2)
                            os.rename(palea, new_file_name3)
                            screen.blit(re_img, (0, 0))
                            while runn:
                                cnter += 1
                                if cnter > 360:
                                        skin = 3
                                        cral = True
                                        runn = False
                                pygame.display.update()

                        #If Brown Skin
                        if event.type == pygame.MOUSEBUTTONDOWN and 640>mouseX >321 and 320 >mouseY> 161:
                            os.rename(brown, new_file_name)
                            os.rename(brownb, new_file_name2)
                            os.rename(browna, new_file_name3)
                            screen.blit(re_img, (0, 0))
                            while runn:
                                print (cnter)
                                cnter += 1
                                if cnter > 360:
                                        skin = 4
                                        cral = True
                                        runn = False
                                pygame.display.update()

        pygame.display.update()
                                

#While Loop TO Run Program On Loop
run = True
while run:
        if ruuun == 2:
                rr2()
pygame.quit()
