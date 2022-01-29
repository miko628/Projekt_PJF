#  Copyright (c) 2022.
#  Programowanie w językach funkcyjnych WCY19IJ3S1 Michał Kutryj

import pygame
# import time
# import os
import random
import players
import game
import card
import draw
from constants import *

# import constants
p1 = players.Player(1500)
p2 = players.Player(1500)
p3 = players.Player(1500)
p4 = players.Player(1500)
pygame.init()
# crate screen
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Projekt WCY19IJ3S1 Michał Kutryj")

background = pygame.transform.scale(background, (1800, 1000))
board = pygame.transform.scale(board, (910, 910))
board = pygame.transform.rotate(board, -90)
font = pygame.font.SysFont('corbel', 30)


def chance(chancelist):
    x = 0
    return x


def community_chest(communitylist):
    x = 0
    return x

def field_check(player):
    end = 0
    if player.field == 0:
        # start
        end = 0
    if player.field == 1:
        # konopacka
        if cardlist[0].bought == False and cardlist[0].cost<player.cash:
            card_loop(player, cardlist[0])
            end = 1
    if player.field == 2:
        # kasa spoleczna
        community_chest(communitylist)
    if player.field == 3:
        # stalowa
        if cardlist[1].bought == False and cardlist[1].cost<player.cash:
            card_loop(player, cardlist[1])
            end = 1
    if player.field == 4:
        # podatek dochodowy
        player.cash -= 200
    if player.field == 5:
        # dworzec zachodni
        if cardlist[2].bought == False and cardlist[2].cost<player.cash:
            card_loop(player, cardlist[2])
            end = 1
    if player.field == 6:
        # radzyminska
        if cardlist[3].bought == False and cardlist[3].cost<player.cash:
            card_loop(player, cardlist[3])
            end = 1
    if player.field == 7:
        # Szansa
        chance(chancelist)
    if player.field == 8:
        # jagiellonska
        if cardlist[4].bought == False and cardlist[4].cost<player.cash:
            card_loop(player, cardlist[4])
            end = 1
    if player.field == 9:
        # targowa
        if cardlist[5].bought == False and cardlist[5].cost<player.cash:
            card_loop(player, cardlist[5])
            end = 1
    if player.field == 10:
        # odwiedzanie
        end = 0
    if player.field == 11:
        # plowiecka
        if cardlist[6].bought == False and cardlist[6].cost<player.cash:
            card_loop(player, cardlist[6])
            end = 1
    if player.field == 12:
        # elektrownia
        if cardlist[7].bought == False and cardlist[7].cost<player.cash:
            card_loop(player, cardlist[7])
            end = 1
    if player.field == 13:
        # marsa
        if cardlist[8].bought == False and cardlist[8].cost<player.cash:
            card_loop(player, cardlist[8])
            end = 1
    if player.field == 14:
        # grochowska
        if cardlist[9].bought == False and cardlist[9].cost<player.cash:
            card_loop(player, cardlist[9])
            end = 1
    if player.field == 15:
        # dworzec gdanski
        if cardlist[10].bought == False and cardlist[10].cost<player.cash:
            card_loop(player, cardlist[10])
            end = 1
    if player.field == 16:
        # obozowa
        if cardlist[11].bought == False and cardlist[11].cost<player.cash:
            card_loop(player, cardlist[11])
            end = 1
    if player.field == 17:
        # kasa spoleczna
        community_chest(communitylist)
    if player.field == 18:
        # gorczewska
        if cardlist[12].bought == False and cardlist[12].cost<player.cash:
            card_loop(player, cardlist[12])
            end = 1
    if player.field == 19:
        # wolska
        if cardlist[13].bought == False and cardlist[13].cost<player.cash:
            card_loop(player, cardlist[13])
            end = 1
    if player.field == 20:
        # parking
        end = 0
    if player.field == 21:
        # mickiewicza
        if cardlist[14].bought == False and cardlist[14].cost<player.cash:
            card_loop(player, cardlist[14])
            end = 1
    if player.field == 22:
        # Szansa
        chance(chancelist)
    if player.field == 23:
        # slowackiego
        if cardlist[15].bought == False and cardlist[15].cost<player.cash:
            card_loop(player, cardlist[15])
            end = 1
    if player.field == 24:
        # plac wilsona
        if cardlist[16].bought == False and cardlist[16].cost<player.cash:
            card_loop(player, cardlist[16])
            end = 1
    if player.field == 25:
        # dworzec wschodni
        if cardlist[17].bought == False and cardlist[17].cost<player.cash:
            card_loop(player, cardlist[17])
            end = 1
    if player.field == 26:
        # swietokrzyska
        if cardlist[18].bought == False and cardlist[18].cost<player.cash:
            card_loop(player, cardlist[18])
            end = 1
    if player.field == 27:
        # krakowskie przedmiescie
        if cardlist[19].bought == False and cardlist[19].cost<player.cash:
            card_loop(player, cardlist[19])
            end = 1
    if player.field == 28:
        # wodociagi
        if cardlist[20].bought == False and cardlist[20].cost<player.cash:
            card_loop(player, cardlist[20])
            end = 1
    if player.field == 29:
        # nowy swiat
        if cardlist[21].bought == False and cardlist[21].cost<player.cash:
            card_loop(player, cardlist[21])
            end = 1
    if player.field == 30:
        # idz do wiezienia
        player.field = 10
    if player.field == 31:
        # plac trzech krzyzy
        if cardlist[22].bought == False and cardlist[22].cost<player.cash:
            card_loop(player, cardlist[22])
            end = 1
    if player.field == 32:
        # marszalkowska
        if cardlist[23].bought == False and cardlist[23].cost<player.cash:
            card_loop(player, cardlist[23])
            end = 1
    if player.field == 33:
        # kasa spoleczna
        community_chest(communitylist)
    if player.field == 34:
        # aleje jerozolimskie
        if cardlist[24].bought == False and cardlist[24].cost<player.cash:
            card_loop(player, cardlist[24])
            end = 1
    if player.field == 35:
        # dworzec centralny
        if cardlist[25].bought == False and cardlist[25].cost<player.cash:
            card_loop(player, cardlist[25])
            end = 1
    if player.field == 36:
        # Szansa
        chance(chancelist)
    if player.field == 37:
        # belwederska
        if cardlist[26].bought == False and cardlist[26].cost<player.cash:
            card_loop(player, cardlist[26])
            end = 1
    if player.field == 38:
        # domiar podatkowy
        player.cash -= 100
    if player.field == 39:
        # aleje ujazdowskie
        if cardlist[27].bought == False and cardlist[27].cost<player.cash:
            card_loop(player, cardlist[27])
            end = 1
    return end    #    card.card_buy(cardlist[26], player)



def card_loop(player, card):

    g4 = game.Game(False, True)
    #card.image=pygame.transform.scale(card.image, (559.166666667, 361.666666667))
    while g4.start:
        g4.clock.tick(60)
        g4.click = False
        g4.x, g4.y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g4.start = False
                quit()
            # keys_pressed = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if g4.pause is True:
                        g4.pause = False
                        draw.show_board(window, board)
                    else:
                        # click = False
                        g4.pause = True
                        draw.show_window(window, background)
                        draw.draw_text("PAUZA", pygame.font.SysFont(None, 170), (0, 0, 0), window, 675, 375)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    g4.click = True
            if g4.pause is False:
                if draw.draw_buy_menu(card,window,g4.x,g4.y,g4.click,player) == 0:
                    game_loop()
                    pygame.quit()
        pygame.display.update()
    pygame.quit()
def color_loop():
    g3 = game.Game(False, True)
    draw.show_board(window, board)
    fieldsList = []
    fieldsList.extend(draw.draw_fields(window))
    ColorList = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    while g3.start:
        g3.clock.tick(60)
        g3.click = False
        g3.x, g3.y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g3.start = False
                quit()
            # keys_pressed = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if g3.pause is True:
                        g3.pause = False
                        draw.show_board(window, board)
                    else:
                        # click = False
                        g3.pause = True
                        draw.show_window(window, background)
                        draw.draw_text("PAUZA", pygame.font.SysFont(None, 170), (0, 0, 0), window, 675, 375)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    g3.click = True
            if p1.color == 0 and g3.pause is False:
                # draw.show_board(window, board)
                # draw.draw_content(p1, window)

                c = p1.color_choose(g3.x, g3.y, g3.click, window)
                if p1.color != 0:
                    ColorList.remove(c)
                    p2.color = random.choice(ColorList)
                    ColorList.remove(p2.color)
                    p3.color = random.choice(ColorList)
                    ColorList.remove(p3.color)
                    p4.color = random.choice(ColorList)
                    del ColorList
                    game_loop()
                    return

        pygame.display.update()


def game_loop():
    g2 = game.Game(False, True)
    # play = True
    # ColorList=[(255, 0, 0),(0, 255, 0), (0, 0, 255),(255, 255, 0)]
    playerList = []
    playerList.append(p1)
    playerList.append(p2)
    playerList.append(p3)
    playerList.append(p4)
    g2.x, g2.y = 0,0
    cash_window, button_dice = draw.draw_content(p1, window)
    fieldsList = [] # lista pol
    fieldsList.extend(draw.draw_fields(window))
    draw.show_board(window, board)
    draw.draw_content(p1, window)
    p1.draw_players(window, fieldsList[p1.field], 1)
    p2.draw_players(window, fieldsList[p2.field], 2)
    p3.draw_players(window, fieldsList[p3.field], 3)
    p4.draw_players(window, fieldsList[p4.field], 4)
    # draw.show_board(window, board)
    # game.draw_content(p1, window)
    while g2.start:
        g2.clock.tick(60)
        g2.click = False
        g2.x, g2.y = pygame.mouse.get_pos()
        for event2 in pygame.event.get():
            if event2.type == pygame.QUIT:
                g2.start = False
                quit()
            # keys_pressed = pygame.key.get_pressed()
            if event2.type == pygame.KEYDOWN:
                if event2.key == pygame.K_ESCAPE:
                    if g2.pause is True:
                        g2.pause = False
                        draw.show_board(window, board)
                    else:
                        # click = False
                        g2.pause = True
                        draw.show_window(window, background)
                        draw.draw_text("PAUZA", pygame.font.SysFont(None, 170), (0, 0, 0), window, 675, 375)
            if event2.type == pygame.MOUSEBUTTONDOWN:
                if event2.button == 1:
                    g2.click = True
            # button_menu = draw.draw_button(window, (0, 0, 0), (255, 255, 255), 800, 400, 200, 60, "Graj", 60)
            # pygame.draw.rect(window, (0, 0, 0), button_menu)
            # draw.draw_text("Graj", font, (255, 255, 255), window, button_menu.left + 60, button_menu.center[1] - 10)
            if g2.pause is False:
                if button_dice.collidepoint((g2.x, g2.y)):
                    pygame.draw.rect(window, (30, 30, 30), button_dice)
                    draw.draw_text(("Rzuć kostką"), pygame.font.SysFont(None, 30), (255, 255, 255), window,
                                   button_dice.left + 5, button_dice.center[1] - 10)
                    if g2.click is True:
                        p1.throw_dice()
                        draw.show_board(window, board)
                        draw.draw_content(p1, window)
                        p1.draw_players(window, fieldsList[p1.field], 1)
                        p2.draw_players(window, fieldsList[p2.field], 2)
                        p3.draw_players(window, fieldsList[p3.field], 3)
                        p4.draw_players(window, fieldsList[p4.field], 4)
                        if field_check(p1) == 1:
                            pygame.quit()
                        p1.draw_players(window, fieldsList[p1.field], 1)
                        p2.draw_players(window, fieldsList[p2.field], 2)
                        p3.draw_players(window, fieldsList[p3.field], 3)
                        p4.draw_players(window, fieldsList[p4.field], 4)
                else:
                    pygame.draw.rect(window, (50, 50, 50), button_dice)
                    draw.draw_text(("Rzuć kostką"), pygame.font.SysFont(None, 30), (255, 255, 255), window,
                                   button_dice.left + 5,
                                   button_dice.center[1] - 10)
        # pygame.display.update()

        # p1.show_player(window, p1.color)
        pygame.display.update()
        # pygame.display.flip()


def menu_loop():
    # player[0]
    g1 = game.Game(False, True)
    # g2 = game.Game(False, False)
    g1.click = False
    # pause = True
    # clock = pygame.time.Clock()
    # play = True
    draw.show_window(window, background)
    # menu loop
    while g1.start:
        if g1.pause is True:
            return

        g1.clock.tick(60)
        g1.click = False
        g1.x, g1.y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g1.start = False
                quit()
        # keys_pressed=pygame.key.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                g1.click = True
        button_menu = draw.draw_button(window, (0, 0, 0), (255, 255, 255), 800, 400, 200, 60, "Graj", 60)
        # pygame.draw.rect(window, (0, 0, 0), button_menu)
        # draw.draw_text("Graj", font, (255, 255, 255), window, button_menu.left + 60, button_menu.center[1] - 10)
        if button_menu.collidepoint((g1.x, g1.y)):
            pygame.draw.rect(window, (70, 70, 70), button_menu)
            draw.draw_text("Graj", font, (255, 255, 255), window, button_menu.left + 25, button_menu.center[1] - 10)
            if g1.click is True:
                pygame.draw.rect(window, (170, 170, 170), button_menu)
                # g1.pause = True
                # show_board()
                color_loop()
                pygame.quit()
                # time.sleep(1)
        button_exit = draw.draw_button(window, (0, 0, 0), (255, 255, 255), 800, 500, 200, 60, "Wyjście", 60)
        # pygame.draw.rect(window, (0, 0, 0), button_exit)
        # draw.draw_text("Wyjście", font, (255, 255, 255), window, button_exit.left + 60, button_exit.center[1] - 10)
        if button_exit.collidepoint((g1.x, g1.y)):
            pygame.draw.rect(window, (70, 70, 70), button_exit)
            draw.draw_text("Wyjście", font, (255, 255, 255), window, button_exit.left + 25, button_exit.center[1] - 10)
            if g1.click is True:
                g1.start = False
        pygame.display.flip()
    pygame.quit()
    # quit()
    return


def main():
    # pygame.quit()
    return 0


if __name__ == "__main__":
    menu_loop()
