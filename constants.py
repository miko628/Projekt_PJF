#  Copyright (c) 2022.
#  Programowanie w językach funkcyjnych WCY19IJ3S1 Michał Kutryj
import os
import pygame
import card
width, height = 1600, 950
colors = [(255, 0, 0), (0, 255, 0), (255, 0, 0), (255, 255, 0)]
board = pygame.image.load(os.path.join('Assets', 'board.png'))
background = pygame.image.load(os.path.join('Assets', 'background.jpg'))
streetimagelist=[]
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u0.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u1.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u2.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u3.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u4.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u5.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u6.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u7.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u8.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u9.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u10.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u11.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u12.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u13.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u14.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u15.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u16.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u17.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u18.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u19.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u20.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u21.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u22.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u23.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u24.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u25.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u26.png')))
streetimagelist.append(pygame.image.load(os.path.join('Assets', 'u27.png')))#27

chanceimagelist=[]
chanceimagelist.append(pygame.image.load(os.path.join('Assets', 's0.png')))
chanceimagelist.append(pygame.image.load(os.path.join('Assets', 's1.png')))
chanceimagelist.append(pygame.image.load(os.path.join('Assets', 's2.png')))
chanceimagelist.append(pygame.image.load(os.path.join('Assets', 's3.png')))
chanceimagelist.append(pygame.image.load(os.path.join('Assets', 's4.png')))
chanceimagelist.append(pygame.image.load(os.path.join('Assets', 's5.png')))
chanceimagelist.append(pygame.image.load(os.path.join('Assets', 's6.png')))
chanceimagelist.append(pygame.image.load(os.path.join('Assets', 's7.png')))
chanceimagelist.append(pygame.image.load(os.path.join('Assets', 's8.png')))
chanceimagelist.append(pygame.image.load(os.path.join('Assets', 's9.png')))
chanceimagelist.append(pygame.image.load(os.path.join('Assets', 's10.png')))
chanceimagelist.append(pygame.image.load(os.path.join('Assets', 's11.png')))
chanceimagelist.append(pygame.image.load(os.path.join('Assets', 's12.png')))
chanceimagelist.append(pygame.image.load(os.path.join('Assets', 's13.png')))
chanceimagelist.append(pygame.image.load(os.path.join('Assets', 's14.png')))
chanceimagelist.append(pygame.image.load(os.path.join('Assets', 's15.png')))

communityimagelist=[]
communityimagelist.append(pygame.image.load(os.path.join('Assets', 'k0.png')))
communityimagelist.append(pygame.image.load(os.path.join('Assets', 'k1.png')))
communityimagelist.append(pygame.image.load(os.path.join('Assets', 'k2.png')))
communityimagelist.append(pygame.image.load(os.path.join('Assets', 'k3.png')))
communityimagelist.append(pygame.image.load(os.path.join('Assets', 'k4.png')))
communityimagelist.append(pygame.image.load(os.path.join('Assets', 'k5.png')))
communityimagelist.append(pygame.image.load(os.path.join('Assets', 'k6.png')))
communityimagelist.append(pygame.image.load(os.path.join('Assets', 'k7.png')))
communityimagelist.append(pygame.image.load(os.path.join('Assets', 'k8.png')))
communityimagelist.append(pygame.image.load(os.path.join('Assets', 'k9.png')))
communityimagelist.append(pygame.image.load(os.path.join('Assets', 'k10.png')))
communityimagelist.append(pygame.image.load(os.path.join('Assets', 'k11.png')))
communityimagelist.append(pygame.image.load(os.path.join('Assets', 'k12.png')))
communityimagelist.append(pygame.image.load(os.path.join('Assets', 'k13.png')))
communityimagelist.append(pygame.image.load(os.path.join('Assets', 'k14.png')))
communityimagelist.append(pygame.image.load(os.path.join('Assets', 'k15.png')))

cardlist = []
cardlist.append(card.Card(0, 60, streetimagelist[0], 30,2))
cardlist.append(card.Card(1, 60, streetimagelist[1], 30,4))
cardlist.append(card.Card(2, 200, streetimagelist[2], 100,25))
cardlist.append(card.Card(3, 100, streetimagelist[3], 50,6))
cardlist.append(card.Card(4, 100, streetimagelist[4], 50,6))
cardlist.append(card.Card(5, 120, streetimagelist[5], 60,8))
cardlist.append(card.Card(6, 140, streetimagelist[6], 70,10))
cardlist.append(card.Card(7, 150, streetimagelist[7], 70,12))
cardlist.append(card.Card(8, 140, streetimagelist[8], 30,10))
cardlist.append(card.Card(9, 160, streetimagelist[9], 80,12))
cardlist.append(card.Card(10, 200, streetimagelist[10], 100,25))
cardlist.append(card.Card(11, 180, streetimagelist[11], 90,14))
cardlist.append(card.Card(12, 180, streetimagelist[12], 90,14))
cardlist.append(card.Card(13, 200, streetimagelist[13], 100,16))
cardlist.append(card.Card(14, 220, streetimagelist[14], 110,18))
cardlist.append(card.Card(15, 220, streetimagelist[15], 110,18))
cardlist.append(card.Card(16, 240, streetimagelist[16], 120,20))
cardlist.append(card.Card(17, 200, streetimagelist[17], 100,25))
cardlist.append(card.Card(18, 260, streetimagelist[18], 130,22))
cardlist.append(card.Card(19, 260, streetimagelist[19], 130,22))
cardlist.append(card.Card(20, 150, streetimagelist[20], 75,12))
cardlist.append(card.Card(21, 280, streetimagelist[21], 140,24))
cardlist.append(card.Card(22, 300, streetimagelist[22], 150,26))
cardlist.append(card.Card(23, 300, streetimagelist[23], 150,26))
cardlist.append(card.Card(24, 320, streetimagelist[24], 160,28))
cardlist.append(card.Card(25, 200, streetimagelist[25], 100,25))
cardlist.append(card.Card(26, 350, streetimagelist[26], 175,35))
cardlist.append(card.Card(27, 400, streetimagelist[27], 200,50))

chancelist=[]
number=0
for cards in chanceimagelist:
    chancelist.append(card.Card(number,0,chanceimagelist[number],0,0))
    number+=1


communitylist=[]
number=0
for cards in communityimagelist:
    communitylist.append(card.Card(number,0,communityimagelist[number],0,0))
    number+=1
