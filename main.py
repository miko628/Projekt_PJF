#  Copyright (c) 2022.
#  Programowanie w językach funkcyjnych WCY19IJ3S1 Michał Kutryj

import pygame
# import time
# import os
import players
import game
import draw
from constants import *

# import constants

pygame.init()
# crate screen
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Projekt WCY19IJ3S1 Michał Kutryj")

background = pygame.transform.scale(background, (1800, 1000))
board = pygame.transform.scale(board, (1000, 1200))
board = pygame.transform.rotate(board, -90)
font = pygame.font.SysFont('corbel', 30)


def game_loop():
    g2 = game.Game(False, True)
    clock = pygame.time.Clock()
    # play = True
    p1 = players.Player(1500)
    p2 = players.Player(1500)
    draw.show_board(window, board)

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
            if p1.color == 0 and g2.pause is False:
                # draw.show_board(window, board)
                # draw.draw_content(p1, window)
                p1.color_choose(g2.x, g2.y, g2.click, window)
                if (p1.color != 0):
                    draw.show_board(window, board)
                    draw.draw_content(p1, window)
            print(g2.x, g2.y)
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
                game_loop()
                g1.pause = True
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
