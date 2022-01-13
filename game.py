#  Copyright (c) 2022.
#  Programowanie w językach funkcyjnych WCY19IJ3S1 Michał Kutryj

import pygame
from draw import draw_text


def draw_content(player,window):
    button_bar=pygame.Rect(1200,0,800,1000)
    pygame.draw.rect(window, (60, 60, 60), button_bar)
    draw_text(("Pieniądze: "+str(player.cash)), pygame.font.SysFont(None,30), (255, 255, 255), window, button_bar.left + 60, 30)


class Game:
    def __init__(self,pause,start):
        self.click = False
        self.start = start
        self.x, self.y = pygame.mouse.get_pos()
        self.pause = pause
        self.clock = pygame.time.Clock()