#  Copyright (c) 2022.
#  Programowanie w językach funkcyjnych WCY19IJ3S1 Michał Kutryj

import pygame
# import time
# import os
import random
import players
import game
import card
import functions
import draw
from constants import *

# import constants
p1 = players.Player(0,1500)
p2 = players.Player(1,1500)
p3 = players.Player(2,1500)
p4 = players.Player(3,1500)
pygame.init()
# crate screen
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Projekt WCY19IJ3S1 Michał Kutryj")

background = pygame.transform.scale(background, (1800, 1000))
board = pygame.transform.scale(board, (910, 910))
board = pygame.transform.rotate(board, -90)
font = pygame.font.SysFont('corbel', 30)



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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if g3.pause is True:
                        g3.pause = False
                        draw.show_board(window, board)
                    else:
                        g3.pause = True
                        draw.show_window(window, background)
                        draw.draw_text("PAUZA", pygame.font.SysFont(None, 170), (0, 0, 0), window, 675, 375)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    g3.click = True

            if p1.color == 0 and g3.pause is False:
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
    dice_event = pygame.USEREVENT + 0
    player_event = pygame.USEREVENT + 1
    n1 = 4
    end = 0
    current_time = 0
    b1 = None
    num = 0
    next=0
    action_time = 0
    playerList = []
    playerList.append(p1)
    playerList.append(p2)
    playerList.append(p3)
    playerList.append(p4)
    g2.x, g2.y = 0,0
    cash_window, button_dice,button_end = draw.draw_content(p1, window)
    fieldsList = [] # lista pol
    fieldsList.extend(draw.draw_fields(window))
    draw.show_board(window, board)
    draw.draw_content(p1, window)
    p1.draw_players(window, fieldsList[p1.field], p1.number)
    p2.draw_players(window, fieldsList[p2.field], p2.number)
    p3.draw_players(window, fieldsList[p3.field], p3.number)
    p4.draw_players(window, fieldsList[p4.field], p4.number)

    while g2.start:
        print("p1 "+str(p1.cash))
        print("p2 "+str(p2.cash))
        print("p3 "+str(p3.cash))
        print("p4 "+str(p4.cash))
        if p1.cash<=0:
            print("Przegrales")
            menu_loop()
            pygame.quit()
        elif p2.cash<=0:
            print("Gracz 2 przegral")
            menu_loop()
            pygame.quit()
        elif p3.cash<=0:
            print("Gracz 3 przegral")
            menu_loop()
            pygame.quit()
        elif p4.cash<=0:
            print("Gracz 4 przegral")
            menu_loop()
            pygame.quit()
        g2.click = False
        g2.clock.tick(60)
        g2.x, g2.y = pygame.mouse.get_pos()
        current_time = pygame.time.get_ticks()
        #print(current_time)

        for event2 in pygame.event.get():

            if event2.type == pygame.QUIT:
                g2.start = False
                quit()

            if event2.type == pygame.KEYDOWN:
                if event2.key == pygame.K_ESCAPE:
                    if g2.pause is True:
                        g2.pause = False
                        draw.show_board(window, board)
                    else:
                        g2.pause = True
                        draw.show_window(window, background)
                        draw.draw_text("PAUZA", pygame.font.SysFont(None, 170), (0, 0, 0), window, 675, 375)

            if event2.type == pygame.MOUSEBUTTONDOWN:
                if event2.button == 1:
                    g2.click = True


            if event2.type == dice_event:
                g2.back = True
                draw.show_board(window, board)
                draw.draw_content(p1, window)
                p1.throw_dice(window)
                print("dice event")
                n1,n2,n3 = functions.field_check(p1,cardlist,playerList)
                p1.draw_players(window, fieldsList[p1.field], p1.number)
                p2.draw_players(window, fieldsList[p2.field], p2.number)
                p3.draw_players(window, fieldsList[p3.field], p3.number)
                p4.draw_players(window, fieldsList[p4.field], p4.number)
                #draw.draw_content(p1,window )
                action_time=current_time+600
                pygame.time.set_timer(dice_event, 0)

            if event2.type == player_event:
                print("player")
                p2.throw_dice(window)
                n1, n2, n3 = functions.field_check(p2, cardlist,playerList)
                if n1==0:
                    draw.show_board(window, board)
                    draw.draw_content(p1, window)
                    p1.draw_players(window, fieldsList[p1.field], p1.number)
                    p2.draw_players(window, fieldsList[p2.field], p2.number)
                    p3.draw_players(window, fieldsList[p3.field], p3.number)
                    p4.draw_players(window, fieldsList[p4.field], p4.number)
                if n1==1:
                    if p2.cash>500:
                        p2.cash-=cardlist[n3].cost
                        p2.cards += 1
                        cardlist[n3].owner = p2.number
                        p2.street.append(cardlist[n3])
                        cardlist[n3].bought = True
                if n1==2:
                    draw.show_board(window, board)
                    draw.draw_content(p1, window)
                    num = functions.random1(current_time)
                    b1, b2, b3 = functions.community_chest(playerList[n2], num)
                    p1.draw_players(window, fieldsList[p1.field], p1.number)
                    p2.draw_players(window, fieldsList[p2.field], p2.number)
                    p3.draw_players(window, fieldsList[p3.field], p3.number)
                    p4.draw_players(window, fieldsList[p4.field], p4.number)
                if n1==3:
                    draw.show_board(window, board)
                    draw.draw_content(p1, window)
                    num = functions.random1(current_time)
                    b1, b2, b3 = functions.chance(playerList[n2], num)
                    p1.draw_players(window, fieldsList[p1.field], p1.number)
                    p2.draw_players(window, fieldsList[p2.field], p2.number)
                    p3.draw_players(window, fieldsList[p3.field], p3.number)
                    p4.draw_players(window, fieldsList[p4.field], p4.number)
                    # player 3
                p3.throw_dice(window)
                n1, n2, n3 = functions.field_check(p3, cardlist,playerList)
                if n1 == 0:
                    draw.show_board(window, board)
                    draw.draw_content(p1, window)
                    p1.draw_players(window, fieldsList[p1.field], p1.number)
                    p2.draw_players(window, fieldsList[p2.field], p2.number)
                    p3.draw_players(window, fieldsList[p3.field], p3.number)
                    p4.draw_players(window, fieldsList[p4.field], p4.number)
                if n1 == 1:
                    if p3.cash > 500:
                        p3.cash -= cardlist[n3].cost
                        p3.cards += 1
                        cardlist[n3].owner = p3.number
                        p3.street.append(cardlist[n3])
                        cardlist[n3].bought = True
                if n1 == 2:
                    draw.show_board(window, board)
                    draw.draw_content(p1, window)
                    num = functions.random1(current_time)
                    functions.community_chest(playerList[n2], num)
                    p1.draw_players(window, fieldsList[p1.field], p1.number)
                    p2.draw_players(window, fieldsList[p2.field], p2.number)
                    p3.draw_players(window, fieldsList[p3.field], p3.number)
                    p4.draw_players(window, fieldsList[p4.field], p4.number)
                if n1 == 3:
                    draw.show_board(window, board)
                    draw.draw_content(p1, window)
                    num = functions.random1(current_time)
                    functions.chance(playerList[n2], num)
                    p1.draw_players(window, fieldsList[p1.field], p1.number)
                    p2.draw_players(window, fieldsList[p2.field], p2.number)
                    p3.draw_players(window, fieldsList[p3.field], p3.number)
                    p4.draw_players(window, fieldsList[p4.field], p4.number)
                    #player 4
                p4.throw_dice(window)
                n1, n2, n3 = functions.field_check(p4, cardlist,playerList)
                if n1 == 0:
                    draw.show_board(window, board)
                    draw.draw_content(p1, window)
                    p1.draw_players(window, fieldsList[p1.field], p1.number)
                    p2.draw_players(window, fieldsList[p2.field], p2.number)
                    p3.draw_players(window, fieldsList[p3.field], p3.number)
                    p4.draw_players(window, fieldsList[p4.field], p4.number)
                if n1 == 1:
                    if p4.cash > 500:
                        p4.cash -= cardlist[n3].cost
                        p4.cards += 1
                        cardlist[n3].owner = p4.number
                        p4.street.append(cardlist[n3])
                        cardlist[n3].bought = True
                if n1 == 2:
                    draw.show_board(window, board)
                    draw.draw_content(p1, window)
                    num = functions.random1(current_time)
                    functions.community_chest(playerList[n2], num)
                    p1.draw_players(window, fieldsList[p1.field], p1.number)
                    p2.draw_players(window, fieldsList[p2.field], p2.number)
                    p3.draw_players(window, fieldsList[p3.field], p3.number)
                    p4.draw_players(window, fieldsList[p4.field], p4.number)
                if n1 == 3:
                    draw.show_board(window, board)
                    draw.draw_content(p1, window)
                    num = functions.random1(current_time)
                    functions.chance(playerList[n2], num)
                    p1.draw_players(window, fieldsList[p1.field], p1.number)
                    p2.draw_players(window, fieldsList[p2.field], p2.number)
                    p3.draw_players(window, fieldsList[p3.field], p3.number)
                    p4.draw_players(window, fieldsList[p4.field], p4.number)

                n1=4
                draw.show_board(window, board)
                draw.draw_content(p1, window)
                p1.draw_players(window, fieldsList[p1.field], p1.number)
                p2.draw_players(window, fieldsList[p2.field], p2.number)
                p3.draw_players(window, fieldsList[p3.field], p3.number)
                p4.draw_players(window, fieldsList[p4.field], p4.number)
                g2.back=False
                end=0
                next=0
                pygame.time.set_timer(player_event, 0)


            if n1==0 and current_time>=action_time:
                draw.draw_content(p1, window)
                next = 1
            if n1==2 and current_time>=action_time:
                if g2.pause is False:
                    #g2.back = True
                    num = functions.random1(current_time)
                    print("community event")
                    if b1 is None:
                        print(num)
                        b1, b2, b3 = functions.community_chest(playerList[n2],num)
                    if b1 == 0:
                        if draw.draw_specialmenu(window,g2.click,g2.x,g2.y,communitylist[b3].image,p1)==0:
                            n1=4
                            b1 = None
                            draw.show_board(window, board)
                            p1.draw_players(window, fieldsList[p1.field], p1.number)
                            p2.draw_players(window, fieldsList[p2.field], p2.number)
                            p3.draw_players(window, fieldsList[p3.field], p3.number)
                            p4.draw_players(window, fieldsList[p4.field], p4.number)
                            draw.draw_content(p1, window)
                            next = 1

                    elif b1 == 1:
                        # zaplata za domy
                        if draw.draw_specialmenu(window, g2.click, g2.x, g2.y, communitylist[b3].image, p1)==0:
                            n1=4
                            b1 = None
                            draw.show_board(window, board)
                            p1.draw_players(window, fieldsList[p1.field], p1.number)
                            p2.draw_players(window, fieldsList[p2.field], p2.number)
                            p3.draw_players(window, fieldsList[p3.field], p3.number)
                            p4.draw_players(window, fieldsList[p4.field], p4.number)
                            draw.draw_content(p1, window)
                            next=1


            elif n1 == 3 and current_time>=action_time:
                if g2.pause is False:
                    #g2.back = True
                    num = functions.random1(current_time)
                    print("chance event")
                    if b1 is None:
                        b1,b2,b3=functions.chance(playerList[n2],num)
                    if b1 == 0:
                        if draw.draw_specialmenu(window,g2.click,g2.x,g2.y,chancelist[b3].image,p1) == 0:
                            n1 =4
                            draw.show_board(window, board)
                            p1.draw_players(window, fieldsList[p1.field], p1.number)
                            p2.draw_players(window, fieldsList[p2.field], p2.number)
                            p3.draw_players(window, fieldsList[p3.field], p3.number)
                            p4.draw_players(window, fieldsList[p4.field], p4.number)
                            draw.draw_content(p1, window)
                            next=1
                    elif b1 == 1:
                        # zaplata za domy
                        if draw.draw_specialmenu(window,g2.click,g2.x,g2.y,chancelist[b3].image,p1) == 0:
                            n1=4
                            draw.show_board(window, board)
                            p1.draw_players(window, fieldsList[p1.field], p1.number)
                            p2.draw_players(window, fieldsList[p2.field], p2.number)
                            p3.draw_players(window, fieldsList[p3.field], p3.number)
                            p4.draw_players(window, fieldsList[p4.field], p4.number)
                            draw.draw_content(p1, window)
                            next=1

            elif n1 == 1 and current_time>=action_time:
                if g2.pause is False:
                    x = draw.draw_buy_menu(cardlist[n3], window, g2.x,g2.y, g2.click, playerList[n2])
                    if x == 0:
                        draw.show_board(window, board)
                        p1.draw_players(window, fieldsList[p1.field], p1.number)
                        p2.draw_players(window, fieldsList[p2.field], p2.number)
                        p3.draw_players(window, fieldsList[p3.field], p3.number)
                        p4.draw_players(window, fieldsList[p4.field], p4.number)
                        draw.draw_content(p1, window)
                        next=1
                        n1=4


        if g2.pause is False:
            if button_dice.collidepoint((g2.x, g2.y)) and g2.back == False:
                pygame.draw.rect(window, (30, 30, 30), button_dice)
                draw.draw_text(("Rzuć kostką"), pygame.font.SysFont(None, 30), (255, 255, 255), window,
                                   button_dice.left + 5, button_dice.center[1] - 10)

                if g2.click is True:
                    pygame.time.set_timer(dice_event,200)
                    g2.click = False

            elif g2.back == False:
                pygame.draw.rect(window, (40, 40, 40), button_dice)
                draw.draw_text(("Rzuć kostką"), pygame.font.SysFont(None, 30), (255, 255, 255), window,
                    button_dice.left + 5, button_dice.center[1] - 10)
            elif next==1 and end==0:
                if button_end.collidepoint((g2.x, g2.y)):
                    pygame.draw.rect(window, (30, 30, 30), button_end)
                    draw.draw_text(("Koniec"), pygame.font.SysFont(None, 30), (255, 255, 255), window, button_end.left + 5,
                      button_dice.center[1] - 10)
                    if g2.click is True:
                        pygame.time.set_timer(player_event, 400)
                        end =1
                else:
                    pygame.draw.rect(window, (40, 40, 40), button_end)
                    draw.draw_text(("Koniec"), pygame.font.SysFont(None, 30), (255, 255, 255), window, button_end.left + 5,
                               button_dice.center[1] - 10)
        pygame.display.update()



def menu_loop():
    g1 = game.Game(False, True)
    g1.click = False
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
        if button_menu.collidepoint((g1.x, g1.y)):
            pygame.draw.rect(window, (70, 70, 70), button_menu)
            draw.draw_text("Graj", font, (255, 255, 255), window, button_menu.left + 25, button_menu.center[1] - 10)
            if g1.click is True:
                pygame.draw.rect(window, (170, 170, 170), button_menu)
                color_loop()
                pygame.quit()
        button_exit = draw.draw_button(window, (0, 0, 0), (255, 255, 255), 800, 500, 200, 60, "Wyjście", 60)
        if button_exit.collidepoint((g1.x, g1.y)):
            pygame.draw.rect(window, (70, 70, 70), button_exit)
            draw.draw_text("Wyjście", font, (255, 255, 255), window, button_exit.left + 25, button_exit.center[1] - 10)
            if g1.click is True:
                g1.start = False
        pygame.display.flip()
    pygame.quit()
    return


def main():
    # pygame.quit()
    return 0


if __name__ == "__main__":
    menu_loop()
