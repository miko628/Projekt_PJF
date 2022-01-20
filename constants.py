#  Copyright (c) 2022.
#  Programowanie w językach funkcyjnych WCY19IJ3S1 Michał Kutryj
import os
import pygame
width, height = 1800, 1000
colors = [(255, 0, 0), (0, 255, 0), (255, 0, 0), (255, 255, 0)]
background = pygame.image.load(os.path.join('Assets', 'background.jpg'))
board = pygame.image.load(os.path.join('Assets', 'board.png'))