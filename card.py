#  Copyright (c) 2022.
#  Programowanie w językach funkcyjnych WCY19IJ3S1 Michał Kutryj
#import pygame
#import os


class Card:
    def __init__(self, number, cost, image, mortgage,rent):
        self.number = number
        self.cost = cost
        self.rent = rent
        self.image = image
        self.mortgage = mortgage
        self.bought = False
        self.owner = 0
