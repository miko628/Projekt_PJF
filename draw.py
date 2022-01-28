#  Copyright (c) 2022.
#  Programowanie w językach funkcyjnych WCY19IJ3S1 Michał Kutryj

import pygame


def draw_button(window, color1, color2, left, top, height, width, text, push):
    button = pygame.Rect(left, top, height, width)
    pygame.draw.rect(window, color1, button)
    draw_text(text, pygame.font.SysFont('corbel', 30), (255, 255, 255), window, button.left + push,
              button.center[1] - 10)
    return button


# def point_button()

def draw_text(text, font, color, surface, x, y):  # drawing text on rectangle
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


def draw_content(player, window):
    button_bar = pygame.Rect(1000, 0, 800, 1000)
    pygame.draw.rect(window, (60, 60, 60), button_bar)
    draw_text(("Pieniądze: " + str(player.cash)),
              pygame.font.SysFont(None, 30), (255, 255, 255), window, (button_bar.left + 60), 30)
    button_dice = pygame.Rect(950, 300, 150, 70)
    pygame.draw.rect(window, (50, 50, 50), button_dice)
    draw_text(("Rzuć kostką"), pygame.font.SysFont(None, 30), (255, 255, 255), window, button_dice.left + 5, button_dice.center[1] - 10)
    return button_bar, button_dice

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


def draw_fields(window):
    # pygame.init()
    pom1 = 0.131
    pom2 = 0.082
    List =[]

    a = 543/4.5 # szerokosc duzego prostokata
    b = 547/4.5 # wysokosc prostokata
    c = 335/4.5 # szerokosc malego prostokata

    List.append(pygame.Rect(a + c * 9, a + c * 9, b - 1, a))  # dolna linia
    List.append(pygame.Rect(a + c * 8, a + c * 9, c, a))
    List.append(pygame.Rect(a + c * 7, a + c * 9, c, a))
    List.append(pygame.Rect(a + c * 6, a + c * 9, c, a))
    List.append(pygame.Rect(a + c * 5, a + c * 9, c, a))
    List.append(pygame.Rect(a + c * 4, a + c * 9, c, a))
    List.append(pygame.Rect(a + c * 3, a + c * 9, c, a))
    List.append(pygame.Rect(a + c * 2, a + c * 9, c, a))
    List.append(pygame.Rect(a + c, a + c * 9, c, a))
    List.append(pygame.Rect(a, a + c * 9, c, a))

    List.append(pygame.Rect(0, a + c * 9, b, a))  # lewa linia
    List.append(pygame.Rect(0, a + c * 8, b, c))
    List.append(pygame.Rect(0, a + c * 7, b, c))
    List.append(pygame.Rect(0, a + c * 6, b, c))
    List.append(pygame.Rect(0, a + c * 5, b, c))
    List.append(pygame.Rect(0, a + c * 4, b, c))
    List.append(pygame.Rect(0, a + c * 3, b, c))
    List.append(pygame.Rect(0, a + c * 2, b, c))
    List.append(pygame.Rect(0, a + c, b, c))
    List.append(pygame.Rect(0, a, b, c))

    ##pygame.draw.rect(window, (0, 255, 0), (0, 0, a, a), 2)

    List.append(pygame.Rect(0, 0, a, b))
    List.append(pygame.Rect(a, 0, c, b))
    List.append(pygame.Rect(a + c, 0, c, b))
    List.append(pygame.Rect(a + c * 2, 0, c, b))
    List.append(pygame.Rect(a + c * 3, 0, c, b))
    List.append(pygame.Rect(a + c * 4, 0, c, b))
    List.append(pygame.Rect(a + c * 5, 0, c, b))
    List.append(pygame.Rect(a + c * 6, 0, c, b))
    List.append(pygame.Rect(a + c * 7, 0, c, b))
    List.append(pygame.Rect(a + c * 8, 0, c, b))
    List.append(pygame.Rect(a + c * 9, 0, a, b))  # gorna linia

    ##pygame.draw.rect(window, (0, 255, 0), (0, 0, a, a), 2)
    #List.append(pygame.Rect(a + c * 9, 0, a, b))
    List.append(pygame.Rect(a + c * 9, a, a, c))
    List.append(pygame.Rect(a + c * 9, a + c, a, c))
    List.append(pygame.Rect(a + c * 9, a + c * 2, a, c))
    List.append(pygame.Rect(a + c * 9, a + c * 3, a, c))
    List.append(pygame.Rect(a + c * 9, a + c * 4, a, c))
    List.append(pygame.Rect(a + c * 9, a + c * 5, a, c))
    List.append(pygame.Rect(a + c * 9, a + c * 6, a, c))
    List.append(pygame.Rect(a + c * 9, a + c * 7, a, c))
    List.append(pygame.Rect(a + c * 9, a + c * 8, a, c))
    List.append(pygame.Rect(a + c * 9, a + c * 9, a, b))#prawa linia




    for item in List:
        pygame.draw.rect(window,(0,0,0),item,1)
   # pygame.draw.rect(window, (255, 0, 0), (a + c * 9, a + c * 9, a, a), 1)  # prawa linia
    return List

def draw_player(window, player, box):  # drawing player
    player = pygame.draw.circle(box, player.color, 10, 100)
