#  Copyright (c) 2022.
#  Programowanie w językach funkcyjnych WCY19IJ3S1 Michał Kutryj

import pygame
import os
import time
import players
import game
import draw
import constants
pygame.init()
width, height = 1800, 1000
colors = [(255, 0, 0), (0, 255, 0), (255, 0, 0), (255, 255, 0)]
#crate screen
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Projekt WCY19IJ3S1 Michał Kutryj")
background = pygame.image.load(os.path.join('Assets', 'background.jpg'))
board = pygame.image.load(os.path.join('Assets', 'board.png'))
background = pygame.transform.scale(background, (1800, 1000))
board = pygame.transform.scale(board, (1200, 1200))
board = pygame.transform.rotate(board, -90)
font = pygame.font.SysFont(None, 30)


def game_loop():
    click = False
    pause = False
    start = True
    clock = pygame.time.Clock()
    play = True
    p1 = players.Player(1500)
    p2 = players.Player(1500)
    draw.show_board(window, board)
    while play:
        clock.tick(60)
        x, y = pygame.mouse.get_pos()
        for event2 in pygame.event.get():
            if event2.type == pygame.QUIT:
                play = False
                quit()
            #keys_pressed = pygame.key.get_pressed()
            if event2.type == pygame.KEYDOWN:
                if event2.key == pygame.K_ESCAPE:
                    if pause is True:
                        pause = False
                        draw.show_board(window, board)
                    else:
                        #click = False
                        pause = True
                        draw.show_window(window, background)
                        draw.draw_text("PAUZA", pygame.font.SysFont(None, 170), (0, 0, 0), window, 675, 375)
            if event2.type == pygame.MOUSEBUTTONDOWN:
                if event2.button == 1:
                    click = True
        if pause is False:
            if start is False:
                draw.show_board(window, board)
                game.draw_content(p1, window)
                pygame.display.update()
            if start is True:
                colors1 = p1.color_choose(x, y, click, window)
                if p1.color != 0:
                    start = False
        click = False
        pygame.display.flip()


def main():
    #player[0]
    click = False
    pause = True
    clock = pygame.time.Clock()
    play = True
    draw.show_window(window, background)
    #menu loop
    while play:
        clock.tick(60)
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                quit()
       #keys_pressed=pygame.key.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click =True
        button_menu = pygame.Rect(800, 400, 200, 60)
        pygame.draw.rect(window, (0, 0, 0), button_menu)
        draw.draw_text("Graj", font, (255, 255, 255), window, button_menu.left + 60, button_menu.center[1]-10)
        if button_menu.collidepoint((x, y)):
            pygame.draw.rect(window, (70, 70, 70), button_menu)
            draw.draw_text("Graj", font, (255, 255, 255), window, button_menu.left + 25, button_menu.center[1] - 10)
            if click is True:
                pygame.draw.rect(window, (170, 170, 170), button_menu)
                pause = False
                #show_board()
                game_loop()
                    #time.sleep(1)
        button_exit = pygame.Rect(800, 500, 200, 60)
        pygame.draw.rect(window, (0, 0, 0), button_exit)
        draw.draw_text("Wyjście", font, (255, 255, 255), window, button_exit.left + 60, button_exit.center[1] - 10)
        if button_exit.collidepoint((x, y)):
            pygame.draw.rect(window, (70, 70, 70), button_exit)
            draw.draw_text("Wyjście", font, (255, 255, 255), window, button_exit.left + 25, button_exit.center[1] - 10)
            if click is True:
                play = False
        pygame.display.flip()
    pygame.quit()
    quit()
    return


if __name__ == "__main__":
        main()