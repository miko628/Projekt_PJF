#  Copyright (c) 2022.
#  Programowanie w językach funkcyjnych WCY19IJ3S1 Michał Kutryj

import pygame
def draw_button(window,color1,color2,left,top,height,width,text,push):
    button = pygame.Rect(left, top, height, width)
    pygame.draw.rect(window, color1, button)
    draw_text(text, pygame.font.SysFont('corbel', 30), (255, 255, 255), window, button.left + push, button.center[1] - 10)
    return button

#def point_button()

def draw_text(text, font, color, surface, x, y):  # drawing text on rectangle
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def draw_content(player, window):
    button_bar = pygame.Rect(1200, 0, 800, 1000)
    pygame.draw.rect(window, (60, 60, 60), button_bar)
    draw_text(("Pieniądze: " + str(player.cash)),
              pygame.font.SysFont(None, 30), (255, 255, 255), window, (button_bar.left + 60), 30)

def show_window(window, background):  # showing background
    window.fill((255, 255, 255))
    # background loading
    window.blit(background, (0, 0))
    # surf=pygame.surface((800,808),pygame.SRCALPHA)
    pygame.display.update()


def show_board(window, board):  # showing board
    window.fill((60, 60, 60))
    window.blit(board, (0, 0))
    pygame.display.update()


def draw_player(window, player, box):  # drawing player
    player = pygame.draw.circle(box, player.color, 10, 100)
