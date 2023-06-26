import pygame
import time
import math
bal = False
import os
tral = False
ral = True
balo = False
ftime = True
ruuun = 1
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60
screen_width = 640
screen_height = 320
bag_img = pygame.image.load("img/ManorWo.png")
cnter = 0

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Olympians')

def rr1():
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
        pale = "C:img/paleman.png"
        white = "C:img/whiteman.png"
        brown = "C:img/brownman.png"
        browner = "C:img/brownerman.png"
        palea = "C:img/palea.png"
        whitea = "C:img/whitea.png"
        browna = "C:img/browna.png"
        brownera = "C:img/brownera.png"
        paleb = "C:img/palemb.png"
        whiteb = "C:img/whiteb.png"
        brownb = "C:img/brownb.png"
        brownerb = "C:img/brownerb.png"
        new_file_name = "img/guy.png"
        new_file_name2 = "img/guyb.png"
        new_file_name3 = "img/guya.png"
        MorW = pygame.image.load("img/ManorWo.png")
        Man = pygame.image.load("img/Man.png")
        Woman = pygame.image.load("img/Woman.png")
        
        (mouseX, mouseY) = pygame.mouse.get_pos()

        bg_img = pygame.image.load('img/pickpla.png')
        re_img = pygame.image.load('img/readyscr.png')
        clock.tick(fps)

                
        screen.blit(bag_img, (0, 0))

        

        if pygame.key.get_pressed()[pygame.K_c]:
                pm = True
                
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()

        
        if ral:
                if event.type == pygame.MOUSEBUTTONDOWN and 320>mouseX >0 and 320 >mouseY> 0 or bal == True:
                        bag_img = Man
                        bal = True
                        cnter += 1
                        if cnter == 100:
                                cnter = 0
                                tral = True
                                ral = False
                if event.type == pygame.MOUSEBUTTONDOWN and 640>mouseX >320 and 320 >mouseY> 0 or balo == True:
                        print (cnter)
                        bag_img = Woman
                        balo = True
                        cnter += 1
                        if cnter == 100:
                                cnter = 0
                                tral = True
                                ral = False

        if tral:
                if bag_img == Man or bag_img == Woman:
                        bag_img = bg_img
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


        pygame.display.update()



run = True
while run:
        if ruuun == 1:
                rr1()
        
