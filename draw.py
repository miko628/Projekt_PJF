#  Copyright (c) 2022.
#  Programowanie w językach funkcyjnych WCY19IJ3S1 Michał Kutryj

import pygame
def draw_text(text,font,color,surface,x,y): #drawing text on rectangle
    text_obj=font.render(text,1,color)
    text_rect=text_obj.get_rect()
    text_rect.topleft =(x,y)
    surface.blit(text_obj,text_rect)
def show_window(window,background):#showing background
    window.fill((255,255,255))
    #background loading
    window.blit(background,(0,0))
    #surf=pygame.surface((800,808),pygame.SRCALPHA)
    pygame.display.update()

def show_board(window,board):#showing board
    #window.fill((255, 255, 255))
    window.blit(board,(0,-200))
    pygame.display.update()

def draw_player(window,player, box):#drawing player
    player = pygame.draw.circle(box, player.color, 10, 100)