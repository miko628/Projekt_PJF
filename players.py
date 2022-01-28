#  Copyright (c) 2022.
#  Programowanie w językach funkcyjnych WCY19IJ3S1 Michał Kutryj

import pygame
import draw
import random
import card

class Player:
    def __init__(self, cash):
        self.color = 0
        self.x = 0
        self.y = 0
        self.cash = cash
        self.field = 0
        self.street = []
        self.cards = 0

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
                #draw.show_board(window, board)
        return self.color

    def calc_position(self):
        self.x = 1100
        self.y = 900

    def show_player(self, window,color):
        #self.calc_position()
        pygame.draw.circle(window, color, (self.x, self.y), 20)

    def throw_dice(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        # animacja kostek ? XD
        #self.field = (self.field+1)%40
        self.field = (self.field + dice1 + dice2)%40

    def draw_players(self,window, List, n):
        #List[self.field]
        if n == 1 or n==2:
            n2 = 1
        else:
            n2 = 2
        n1 = n%2 +1
        pygame.draw.circle(window, self.color,  (List.left+30*n1,List.top+50*n2),12)
    def card_show(self):
        for a in self.street:
            return

    def field_check(self, cardlist):
        if self.field == 0:
            #pole zerowe
            card.card_buy(cardlist[0],self)
        if self.field ==1:
            # konopacka
            card.card_buy(cardlist[1],self)
        if self.field ==2:
            # kasa spoleczna
            card.card_buy(cardlist[2],self)
        if self.field ==3:
            # stalowa
            card.card_buy(cardlist[3],self)
        if self.field ==4:
            self.cash-=200
        if self.field ==5:
            # dworzec zachodni
            card.card_buy(cardlist[1],self)
        if self.field ==6:
            # radzyminska
            card.card_buy(cardlist[1],self)
        if self.field ==7:
            # Szansa
            card.card_buy(cardlist[1],self)
        if self.field ==8:
            # jagiellonska
            card.card_buy(cardlist[1],self)
        if self.field ==9:
            # targowa
            card.card_buy(cardlist[1],self)
        if self.field ==10:
            # odwiedzanie
            card.card_buy(cardlist[1],self)
        if self.field ==11:
            # plowiecka
            card.card_buy(cardlist[1],self)
        if self.field ==12:
            # elektrownia
            card.card_buy(cardlist[1],self)
        if self.field ==13:
            # marsa
            card.card_buy(cardlist[1],self)
        if self.field ==14:
            # grochowska
            card.card_buy(cardlist[1],self)
        if self.field ==15:
            # dworzec gdanski
            card.card_buy(cardlist[1],self)
        if self.field ==16:
            # obozowa
            card.card_buy(cardlist[1],self)
        if self.field ==17:
            # kasa spoleczna
            card.card_buy(cardlist[1],self)
        if self.field ==18:
            # gorczewska
            card.card_buy(cardlist[1],self)
        if self.field ==19:
            # wolska
            card.card_buy(cardlist[1],self)
        if self.field ==20:
            # parking
            card.card_buy(cardlist[1],self)
        if self.field ==21:
            # mickiewicza
            card.card_buy(cardlist[1],self)
        if self.field ==22:
            # Szansa
            card.card_buy(cardlist[1],self)
        if self.field ==23:
            # slowackiego
            card.card_buy(cardlist[-14],self)
        if self.field ==24:
            # plac wilsona
            card.card_buy(cardlist[-13],self)
        if self.field ==25:
            # dworzec wschodni
            card.card_buy(cardlist[-12],self)
        if self.field ==26:
            # swietokrzyska
            card.card_buy(cardlist[-10],self)
        if self.field ==27:
            # krakowskie przedmiescie
            card.card_buy(cardlist[-9],self)
        if self.field ==28:
            # wodociagi
            card.card_buy(cardlist[-8],self)
        if self.field ==29:
            # nowy swiat
            card.card_buy(cardlist[-7],self)
        if self.field ==30:
            # idz do wiezienia
            card.card_buy(cardlist[1],self)
        if self.field ==31:
            # plac trzech krzyzy
            card.card_buy(cardlist[-6],self)
        if self.field ==32:
            # marszalkowska
            card.card_buy(cardlist[-5],self)
        if self.field ==33:
            # kasa spoleczna
            card.card_buy(cardlist[1],self)
        if self.field ==34:
            # aleje jerozolimskie
            card.card_buy(cardlist[-4],self)
        if self.field ==35:
            # dworzec centralny
            card.card_buy(cardlist[-3],self)
        if self.field ==36:
            # Szansa
            card.card_buy(cardlist[1],self)
        if self.field ==37:
            # belwederska
            card.card_buy(cardlist[-2],self)
        if self.field ==38:
            # domiar podatkowy
            self.cash-=100
        if self.field ==39:
            # aleje ujazdowskie
            card.card_buy(cardlist[-1],self)