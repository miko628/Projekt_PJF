#  Copyright (c) 2022.
#  Programowanie w językach funkcyjnych WCY19IJ3S1 Michał Kutryj

import pygame

class Game:
    def __init__(self, pause, start):
        self.click = False
        self.start = start
        self.x, self.y = 0, 0
        self.pause = pause
        self.back = False
        self.clock = pygame.time.Clock()