#  Copyright (c) 2022.
#  Programowanie w językach funkcyjnych WCY19IJ3S1 Michał Kutryj

import pygame
import draw
import random
#import constants


class Player:
    def __init__(self,number, cash):
        self.number = number
        self.color = 0
        self.x = 0
        self.y = 0
        self.cash = cash
        self.field = 0
        self.street = []
        self.cards = 0
        self.prison = False
        self.prisoncard = False

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
            self.show_player(window, (255, 0, 0))
            if click is True:
                self.color = (255, 0, 0)
                # window.fill(255,255,255)
                # draw.show_board(window, board)
        green = pygame.Rect(button_choose.left + 125, 500, 50, 50)
        pygame.draw.rect(window, (0, 255, 0), green)
        if green.collidepoint((x, y)):
            self.x = 750
            self.y = 620
            pygame.draw.rect(window, (0, 200, 0), green)
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
                # draw.show_board(window, board)
        return self.color


    def show_player(self, window, color):
        # self.calc_position()
        pygame.draw.circle(window, color, (self.x, self.y), 20)

    def throw_dice(self, window):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if self.prison == False:
            button_dice = pygame.Rect(1050, 170, 150, 70)
            pygame.draw.rect(window, (50, 50, 50), button_dice)
            draw.draw_text(("Wynik: "+str(dice1)+" "+str(dice2)), pygame.font.SysFont(None, 30), (255, 255, 255), window, button_dice.left + 5,
                  button_dice.center[1] - 10)
            if self.field > 0 and (self.field + dice1 + dice2) % 40 <self.field:
                self.cash+=200
            self.field = (self.field + dice1 + dice2) % 40
            #self.field += 1
        else:
            button_dice = pygame.Rect(1050, 170, 150, 70)
            pygame.draw.rect(window, (50, 50, 50), button_dice)
            draw.draw_text(("Wynik: " + str(dice1) + " " + str(dice2)), pygame.font.SysFont(None, 30), (255, 255, 255),
                           window, button_dice.left + 5,
                           button_dice.center[1] - 10)
            if dice1 == dice2:
                self.prison=False
        #self.field=2

    def draw_players(self, window, List, n):
        # List[self.field]
        if n == 0 or n == 1:
            n2 = 1
        else:
            n2 = 2
        n1 = n % 2 + 1
        pygame.draw.circle(window, self.color, (List.left+10 +23 * n1, List.top + 50 * n2), 10)

    def card_show(self, window):
        n=30

        for a in self.street:
            window.blit(a.image, (50+n, 50))
