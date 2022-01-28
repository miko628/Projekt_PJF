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

pygame.init()
# crate screen
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Projekt WCY19IJ3S1 Michał Kutryj")

background = pygame.transform.scale(background, (1800, 1000))
board = pygame.transform.scale(board, (910, 910))
board = pygame.transform.rotate(board, -90)
font = pygame.font.SysFont('corbel', 30)
def street_fill():
    streetlist=[]
    streetlist.append(card.card(0,60,streetimagelist[0],30))
    streetlist.append(card.card(1, 60, streetimagelist[1], 30))
    streetlist.append(card.card(2, 200, streetimagelist[2], 100))
    streetlist.append(card.card(3, 100, streetimagelist[3], 50))
    streetlist.append(card.card(4, 100, streetimagelist[4], 50))
    streetlist.append(card.card(5, 120, streetimagelist[5], 60))
    streetlist.append(card.card(6, 140, streetimagelist[6], 70))
    streetlist.append(card.card(7, 150, streetimagelist[7], 70))
    streetlist.append(card.card(8, 140, streetimagelist[8], 30))
    streetlist.append(card.card(9, 160, streetimagelist[9], 80))
    streetlist.append(card.card(10, 200, streetimagelist[10], 100))
    streetlist.append(card.card(11, 180, streetimagelist[11], 90))
    streetlist.append(card.card(12, 180, streetimagelist[12], 90))
    streetlist.append(card.card(13, 200, streetimagelist[13], 100))
    streetlist.append(card.card(14, 220, streetimagelist[14], 110))
    streetlist.append(card.card(15, 220, streetimagelist[15], 110))
    streetlist.append(card.card(16, 240, streetimagelist[16], 120))
    streetlist.append(card.card(17, 200, streetimagelist[17], 100))
    streetlist.append(card.card(18, 260, streetimagelist[18], 130))
    streetlist.append(card.card(19, 260, streetimagelist[19], 130))
    streetlist.append(card.card(20, 150, streetimagelist[20], 75))
    streetlist.append(card.card(21, 280, streetimagelist[21], 140))
    streetlist.append(card.card(22, 300, streetimagelist[22], 150))
    streetlist.append(card.card(23, 300, streetimagelist[23], 150))
    streetlist.append(card.card(24, 320, streetimagelist[24], 160))
    streetlist.append(card.card(25, 200, streetimagelist[25], 100))
    streetlist.append(card.card(26, 350, streetimagelist[26], 175))
    streetlist.append(card.card(27, 400, streetimagelist[27], 200))


def color_loop():
    g3 = game.Game(False,True)
    g3.clock=pygame.time.Clock()
    p1 = players.Player(1500)
    p2 = players.Player(1500)
    p3 = players.Player(1500)
    p4 = players.Player(1500)
    draw.show_board(window, board)
    fieldsList = []
    fieldsList.extend(draw.draw_fields(window))
    ColorList = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    while g3.start:
        g3.clock.tick(60)
        g3.click=False
        g3.x,g3.y=pygame.mouse.get_pos()
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
                    game_loop(p1,p2,p3,p4)
                    return

        pygame.display.update()

def game_loop(p1,p2,p3,p4):
    g2 = game.Game(False, True)
    g2.clock = pygame.time.Clock()
    # play = True
    #ColorList=[(255, 0, 0),(0, 255, 0), (0, 0, 255),(255, 255, 0)]
    playerList=[]
    playerList.append(p1)
    playerList.append(p2)
    playerList.append(p3)
    playerList.append(p4)

    cash_window,button_dice = draw.draw_content(p1, window)
    fieldsList=[]
    draw.show_board(window, board)
    draw.draw_content(p1, window)
    fieldsList.extend(draw.draw_fields(window))
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
            #button_menu = draw.draw_button(window, (0, 0, 0), (255, 255, 255), 800, 400, 200, 60, "Graj", 60)
            # pygame.draw.rect(window, (0, 0, 0), button_menu)
            # draw.draw_text("Graj", font, (255, 255, 255), window, button_menu.left + 60, button_menu.center[1] - 10)
            if g2.pause is False:
                if button_dice.collidepoint((g2.x, g2.y)):
                    pygame.draw.rect(window, (30, 30, 30), button_dice)
                    draw.draw_text(("Rzuć kostką"), pygame.font.SysFont(None, 30), (255, 255, 255), window, button_dice.left + 5, button_dice.center[1] - 10)
                    if g2.click is True:
                        p1.throw_dice()
                        draw.show_board(window, board)
                        draw.draw_content(p1, window)
                        p1.draw_players(window, fieldsList[p1.field],1)
                        p2.draw_players(window, fieldsList[p2.field], 2)
                        p3.draw_players(window, fieldsList[p3.field], 3)
                        p4.draw_players(window, fieldsList[p4.field], 4)
                else:
                    pygame.draw.rect(window, (50, 50, 50), button_dice)
                    draw.draw_text(("Rzuć kostką"), pygame.font.SysFont(None, 30), (255, 255, 255), window, button_dice.left + 5,
                    button_dice.center[1] - 10)
        #pygame.display.update()

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
                return
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
