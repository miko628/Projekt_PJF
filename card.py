#  Copyright (c) 2022.
#  Programowanie w językach funkcyjnych WCY19IJ3S1 Michał Kutryj
import pygame
import os
class Card:
    def __init__(self, number, cost, image, mortgage ):
        self.number = number
        self.cost = cost
        self.image = image
        self.mortgage = mortgage

        def card_buy(self, player):
                player.cards += 1
                player.street.add(self)

