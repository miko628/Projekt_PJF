#  Copyright (c) 2022.
#  Programowanie w językach funkcyjnych WCY19IJ3S1 Michał Kutryj

import pygame
import draw
from constants import board

class Player:
    def __init__(self, cash):
        self.color = 0
        self.x = 0
        self.y = 0
        self.cash = cash
        self.street = []

    def color_choose(self, x, y, click, window):
        button_outline = pygame.Rect(595, 395, 410, 310)
        pygame.draw.rect(window, (0, 0, 0), button_outline)
        button_choose = pygame.Rect(600, 400, 400, 300)
        pygame.draw.rect(window, (60, 60, 60), button_choose)
        draw.draw_text("Wybierz kolor gracza:", pygame.font.SysFont(None, 30),
                       (255, 255, 255), window, button_choose.left + 80, button_choose.center[1] - 120)
        red = pygame.Rect(button_choose.left + 25, 500, 50, 50)
        pygame.draw.rect(window, (255, 0, 0), red)
        if red.collidepoint((x, y)):
            pygame.draw.rect(window, (200, 0, 0), red)
            self.x = 650
            self.y = 620
            self.show_player(window,(255, 0, 0))
            if click is True:
                self.color = (255, 0, 0)
                #window.fill(255,255,255)
                #draw.show_board(window, board)
        green = pygame.Rect(button_choose.left + 125, 500, 50, 50)
        pygame.draw.rect(window, (0, 255, 0), green)
        if green.collidepoint((x, y)):
            self.x = 750
            self.y = 620
            #pygame.draw.rect(window, (0, 200, 0), green)
            self.show_player(window, (0, 255, 0))
            if click is True:
                self.color = (0, 255, 0)
               # draw.show_board(window, board)
        blue = pygame.Rect(button_choose.left + 225, 500, 50, 50)
        pygame.draw.rect(window, (0, 0, 255), blue)
        if blue.collidepoint((x, y)):
            pygame.draw.rect(window, (0, 0, 200), blue)
            self.x = 850
            self.y = 620
            self.show_player(window, (0, 0, 255))
            if click is True:
                self.color = (0, 0, 255)
               # draw.show_board(window, board)
        yellow = pygame.Rect(button_choose.left + 325, 500, 50, 50)
        pygame.draw.rect(window, (255, 255, 0), yellow)
        if yellow.collidepoint((x, y)):
            pygame.draw.rect(window, (200, 200, 0), yellow)
            self.x = 950
            self.y = 620
            self.show_player(window, (255, 255, 0))
            if click is True:
                self.color = (255, 255, 0)
                #draw.show_board(window, board)
                return 1

    def calc_position(self):
        self.x = 1100
        self.y = 900

    def show_player(self, window,color):
        #self.calc_position()
        pygame.draw.circle(window, color, (self.x, self.y), 20)
