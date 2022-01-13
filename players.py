#  Copyright (c) 2022.
#  Programowanie w językach funkcyjnych WCY19IJ3S1 Michał Kutryj

import pygame
import draw
class Player:
    def __init__(self,cash):
        self.color=0
        self.x=0
        self.y=0
        self.cash=cash
        self.street=[]
    def color_choose(self,x,y,click,window):
        button_outline=pygame.Rect(595, 395, 410, 210)
        pygame.draw.rect(window, (0, 0, 0), button_outline)
        button_choose = pygame.Rect(600, 400, 400, 200)
        pygame.draw.rect(window, (60, 60, 60), button_choose)
        draw.draw_text("Wybierz kolor gracza:", pygame.font.SysFont(None,30), (255, 255, 255), window, button_choose.left + 80, button_choose.center[1]-60 )
        red = pygame.Rect(button_choose.left+25, 500, 50, 50)
        pygame.draw.rect(window, (255, 0, 0), red)
        if red.collidepoint((x, y)):
            pygame.draw.rect(window, (200, 0, 0), red)
            if click is True:
                self.color=(255,0,0)
        green = pygame.Rect(button_choose.left+125, 500, 50, 50)
        pygame.draw.rect(window, (0, 255, 0), green)
        if green.collidepoint((x, y)):
            pygame.draw.rect(window, (0,200, 0), green)
            if click is True:
                self.color=(0,255,0)
        blue = pygame.Rect(button_choose.left+225, 500, 50, 50)
        pygame.draw.rect(window, (0, 0, 255), blue)
        if blue.collidepoint((x, y)):
            pygame.draw.rect(window, (0, 0, 200), blue)
            if click is True:
                self.color=(255,0,0)
        yellow = pygame.Rect(button_choose.left+325, 500, 50, 50)
        pygame.draw.rect(window, (255, 255, 0), yellow)
        if yellow.collidepoint((x, y)):
            pygame.draw.rect(window, (200, 200, 0), yellow)
            if click is True:
                self.color=(255,255,0)
                return 1
    def calc_position(self):
        self.x+=20
    def draw(self,window):
        pygame.draw.circle(window,self.color,(self.x,self.y),20)