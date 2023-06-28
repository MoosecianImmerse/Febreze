#Import Neccesary Modules
import pygame
import time
import math
import os
from pygame.locals import *

#Define Variables
bal = False
tral = False
ral = True
balo = False
ftime = True
ruuun = 1
fps = 60
screen_width = 640
screen_height = 320
cnter = 0

#Initialize and Set Up Pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Olympians')

#Define Pre-Function Image Variables
bag_img = pygame.image.load("img/ManorWo.png")

def rr1():
        #Gloabilize Variables
        global event
        global cnter
        global clock
        global fps
        global ral
        global bal
        global balo
        global ftime
        global screen
        global bag_img
        global ruuun
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

        #Define Mouse
        (mouseX, mouseY) = pygame.mouse.get_pos()

        #Run CLock In Frames Per Second
        clock.tick(fps)

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
                        if cnter == 3600:
                                pygame.quit()
                        pygame.display.update()

                #If Browner Skin
                if event.type == pygame.MOUSEBUTTONDOWN and 640>mouseX >321 and 160 >mouseY> 0:
                    os.rename(browner, new_file_name)
                    os.rename(brownerb, new_file_name2)
                    os.rename(brownera, new_file_name3)
                    screen.blit(re_img, (0, 0))
                    runn = True
                    while runn:
                        cnter += 1
                        if cnter == 3600:
                                pygame.quit()
                        pygame.display.update()

                #If Pale Skin
                if event.type == pygame.MOUSEBUTTONDOWN and 320>mouseX >0 and 320 >mouseY> 161:
                    os.rename(pale, new_file_name)
                    os.rename(paleb, new_file_name2)
                    os.rename(palea, new_file_name3)
                    screen.blit(re_img, (0, 0))
                    runn = True
                    while runn:
                        cnter += 1
                        if cnter == 3600:
                                pygame.quit()
                        pygame.display.update()

                #If Brown Skin
                if event.type == pygame.MOUSEBUTTONDOWN and 640>mouseX >321 and 320 >mouseY> 161:
                    os.rename(brown, new_file_name)
                    os.rename(brownb, new_file_name2)
                    os.rename(browna, new_file_name3)
                    screen.blit(re_img, (0, 0))
                    runn = True
                    while runn:
                        cnter += 1
                        if cnter == 3600:
                                pygame.quit()
                        pygame.display.update()

        #Update Frames
        pygame.display.update()


#While Loop TO Run Program On Loop
run = True
while run:
        if ruuun == 1:
                rr1()
        
