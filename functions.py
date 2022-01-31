#  Copyright (c) 2022.
#  Programowanie w językach funkcyjnych WCY19IJ3S1 Michał Kutryj
from constants import *
import random
from datetime import datetime
from main import p1, p2, p3, p4


def field_check(player, cardlist, playerList):
    if player.field == 0:
        # start
        return 0, player.number, 0
    if player.field == 1:
        # konopacka
        if cardlist[0].bought == False and cardlist[0].cost < player.cash:
            # card_loop(player, cardlist[0])
            return 1, player.number, 0
        elif cardlist[0].bought == True:
            player.cash -= cardlist[0].rent
            playerList[cardlist[0].owner].cash += cardlist[0].rent
        return 0, player.number, 0
    if player.field == 2:
        # kasa spoleczna
        return 2, player.number, 0
    if player.field == 3:
        # stalowa
        if cardlist[1].bought == False and cardlist[1].cost < player.cash:
            # card_loop(player, cardlist[1])
            return 1, player.number, 1
        elif cardlist[1].bought == True:
            player.cash -= cardlist[1].rent
            playerList[cardlist[1].owner].cash += cardlist[1].rent
        return 0, player.number, 0
    if player.field == 4:
        # podatek dochodowy
        player.cash -= 200
        return 0, player.number, 0
    if player.field == 5:
        # dworzec zachodni
        if cardlist[2].bought == False and cardlist[2].cost < player.cash:
            # card_loop(player, cardlist[2])
            return 1, player.number, 2
        elif cardlist[2].bought == True:
            player.cash -= cardlist[2].rent
            playerList[cardlist[2].owner].cash += cardlist[2].rent
        return 0, player.number, 0
    if player.field == 6:
        # radzyminska
        if cardlist[3].bought == False and cardlist[3].cost < player.cash:
            # card_loop(player, cardlist[3])
            return 1, player.number, 3
        elif cardlist[3].bought == True:
            player.cash -= cardlist[3].rent
            playerList[cardlist[3].owner].cash += cardlist[3].rent
        return 0, player.number, 0
    if player.field == 7:
        # Szansa
        return 3, player.number, 0
    if player.field == 8:
        # jagiellonska
        if cardlist[4].bought == False and cardlist[4].cost < player.cash:
            return 1, player.number, 4
        elif cardlist[4].bought == True:
            player.cash -= cardlist[4].rent
            playerList[cardlist[4].owner].cash += cardlist[4].rent
        return 0, player.number, 0
    if player.field == 9:
        # targowa
        if cardlist[5].bought == False and cardlist[5].cost < player.cash:
            return 1, player.number, 5
        elif cardlist[5].bought == True:
            player.cash -= cardlist[5].rent
            playerList[cardlist[5].owner].cash += cardlist[5].rent
        return 0, player.number, 0
    if player.field == 10:
        # odwiedzanie
        return 0, player.number, 0
    if player.field == 11:
        # plowiecka
        if cardlist[6].bought == False and cardlist[6].cost < player.cash:
            return 1, player.number, 6
        elif cardlist[6].bought == True:
            player.cash -= cardlist[6].rent
            playerList[cardlist[6].owner].cash += cardlist[6].rent
        return 0, player.number, 0
    if player.field == 12:
        # elektrownia
        if cardlist[7].bought == False and cardlist[7].cost < player.cash:
            return 1, player.number, 7
        elif cardlist[7].bought == True:
            player.cash -= cardlist[7].rent
            playerList[cardlist[7].owner].cash += cardlist[7].rent
        return 0, player.number, 0
    if player.field == 13:
        # marsa
        if cardlist[8].bought == False and cardlist[8].cost < player.cash:
            return 1, player.number, 8
        elif cardlist[2].bought == True:
            player.cash -= cardlist[8].rent
            playerList[cardlist[8].owner].cash += cardlist[8].rent
        return 0, player.number, 0
    if player.field == 14:
        # grochowska
        if cardlist[9].bought == False and cardlist[9].cost < player.cash:
            return 1, player.number, 9
        elif cardlist[2].bought == True:
            player.cash -= cardlist[9].rent
            playerList[cardlist[9].owner].cash += cardlist[9].rent
        return 0, player.number, 0
    if player.field == 15:
        # dworzec gdanski
        if cardlist[10].bought == False and cardlist[10].cost < player.cash:
            return 1, player.number, 10
        elif cardlist[2].bought == True:
            player.cash -= cardlist[10].rent
            playerList[cardlist[10].owner].cash += cardlist[10].rent
        return 0, player.number, 0
    if player.field == 16:
        # obozowa
        if cardlist[11].bought == False and cardlist[11].cost < player.cash:
            return 1, player.number, 11
        elif cardlist[11].bought == True:
            player.cash -= cardlist[11].rent
            playerList[cardlist[11].owner].cash += cardlist[11].rent
        return 0, player.number, 0
    if player.field == 17:
        # kasa spoleczna
        return 2, player.number, 0
    if player.field == 18:
        # gorczewska
        if cardlist[12].bought == False and cardlist[12].cost < player.cash:
            return 1, player.number, 12
        elif cardlist[12].bought == True:
            player.cash -= cardlist[12].rent
            playerList[cardlist[12].owner].cash += cardlist[12].rent
        return 0, player.number, 0
    if player.field == 19:
        # wolska
        if cardlist[13].bought == False and cardlist[13].cost < player.cash:
            return 1, player.number, 13
        elif cardlist[13].bought == True:
            player.cash -= cardlist[13].rent
            playerList[cardlist[13].owner].cash += cardlist[13].rent
        return 0, player.number, 0
    if player.field == 20:
        # parking
        return 0, player.number, 0
    if player.field == 21:
        # mickiewicza
        if cardlist[14].bought == False and cardlist[14].cost < player.cash:
            return 1, player.number, 14
        elif cardlist[14].bought == True:
            player.cash -= cardlist[14].rent
            playerList[cardlist[14].owner].cash += cardlist[14].rent
        return 0, player.number, 0
    if player.field == 22:
        # Szansa
        return 3, player.number, 0
    if player.field == 23:
        # slowackiego
        if cardlist[15].bought == False and cardlist[15].cost < player.cash:
            return 1, player.number, 15
        elif cardlist[15].bought == True:
            player.cash -= cardlist[15].rent
            playerList[cardlist[15].owner].cash += cardlist[15].rent
        return 0, player.number, 0
    if player.field == 24:
        # plac wilsona
        if cardlist[16].bought == False and cardlist[16].cost < player.cash:
            return 1, player.number, 16
        elif cardlist[16].bought == True:
            player.cash -= cardlist[16].rent
            playerList[cardlist[16].owner].cash += cardlist[16].rent
        return 0, player.number, 0
    if player.field == 25:
        # dworzec wschodni
        if cardlist[17].bought == False and cardlist[17].cost < player.cash:
            return 1, player.number, 17
        elif cardlist[17].bought == True:
            player.cash -= cardlist[17].rent
            playerList[cardlist[2].owner].cash += cardlist[17].rent
        return 0, player.number, 0
    if player.field == 26:
        # swietokrzyska
        if cardlist[18].bought == False and cardlist[18].cost < player.cash:
            return 1, player.number, 18
        elif cardlist[18].bought == True:
            player.cash -= cardlist[18].rent
            playerList[cardlist[18].owner].cash += cardlist[18].rent
        return 0, player.number, 0
    if player.field == 27:
        # krakowskie przedmiescie
        if cardlist[19].bought == False and cardlist[19].cost < player.cash:
            return 1, player.number, 19
        elif cardlist[19].bought == True:
            player.cash -= cardlist[19].rent
            playerList[cardlist[19].owner].cash += cardlist[19].rent
        return 0, player.number, 0
    if player.field == 28:
        # wodociagi
        if cardlist[20].bought == False and cardlist[20].cost < player.cash:
            return 1, player.number, 20
        elif cardlist[20].bought == True:
            player.cash -= cardlist[20].rent
            playerList[cardlist[20].owner].cash += cardlist[20].rent
        return 0, player.number, 0
    if player.field == 29:
        # nowy swiat
        if cardlist[21].bought == False and cardlist[21].cost < player.cash:
            return 1, player.number, 21
        elif cardlist[21].bought == True:
            player.cash -= cardlist[21].rent
            playerList[cardlist[21].owner].cash += cardlist[21].rent
        return 0, player.number, 0
    if player.field == 30:
        # idz do wiezienia
        player.field = 10
        player.prison = True
        return 0, player.number, 0
    if player.field == 31:
        # plac trzech krzyzy
        if cardlist[22].bought == False and cardlist[22].cost < player.cash:
            return 1, player.number, 22
        elif cardlist[22].bought == True:
            player.cash -= cardlist[22].rent
            playerList[cardlist[22].owner].cash += cardlist[22].rent
        return 0, player.number, 0
    if player.field == 32:
        # marszalkowska
        if cardlist[23].bought == False and cardlist[23].cost < player.cash:
            return 1, player.number, 23
        elif cardlist[23].bought == True:
            player.cash -= cardlist[23].rent
            playerList[cardlist[23].owner].cash += cardlist[23].rent
        return 0, player.number, 0
    if player.field == 33:
        # kasa spoleczna
        return 2, player.number, 0
    if player.field == 34:
        # aleje jerozolimskie
        if cardlist[24].bought == False and cardlist[24].cost < player.cash:
            return 1, player.number, 24
        elif cardlist[24].bought == True:
            player.cash -= cardlist[24].rent
            playerList[cardlist[24].owner].cash += cardlist[24].rent
        return 0, player.number, 0
    if player.field == 35:
        # dworzec centralny
        if cardlist[25].bought == False and cardlist[25].cost < player.cash:
            return 1, player.number, 25
        elif cardlist[25].bought == True:
            player.cash -= cardlist[25].rent
            playerList[cardlist[25].owner].cash += cardlist[25].rent
        return 0, player.number, 0
    if player.field == 36:
        # Szansa
        return 3, player.number, 0
    if player.field == 37:
        # belwederska
        if cardlist[26].bought == False and cardlist[26].cost < player.cash:
            return 1, player.number, 26
        elif cardlist[26].bought == True:
            player.cash -= cardlist[26].rent
            playerList[cardlist[26].owner].cash += cardlist[26].rent
        return 0, player.number, 0
    if player.field == 38:
        # domiar podatkowy
        player.cash -= 100
        return 0, player.number, 0
    if player.field == 39:
        # aleje ujazdowskie
        if cardlist[27].bought == False and cardlist[27].cost < player.cash:
            return 1, player.number, 27
        elif cardlist[27].bought == True:
            player.cash -= cardlist[27].rent
            playerList[cardlist[27].owner].cash += cardlist[27].rent
        return 0, player.number, 0


def chance(player, x):
    if x == 0:
        # grzywna zaplac 20
        player.cash -= 20
        return 0, player.number, 0
    if x == 1:
        # przejdz na start
        player.field = 0
        return 0, player.number, 1
    if x == 2:
        # otrzymales kredyt budowlany pobierz 150
        player.cash += 150
        return 0, player.number, 2
    if x == 3:
        # mandat za przekroczenie predkosci zaplac 15
        player.cash -= 15
        return 0, player.number, 3
    if x == 4:
        # przejdz na aleje ujazdowskie
        player.field = 39
        return 0, player.number, 4
    if x == 5:
        # zaplac za szkole 150
        player.cash -= 150
        return 0, player.number, 5
    if x == 6:
        # cofnij sie o trzy pola
        player.field -= 3
        if player.field < 0:
            player.field += 39
        return 0, player.number, 6
    if x == 7:
        # zaplac 40 za kazdy dom, 115 za kazdy hotel
        return 1, player.number, 7
    if x == 8:
        # przejdz na ulice plowiecka jesli miniesz start pobierz 200
        if player.field > 0 and player.field <= 11:
            player.cash += 200
        player.field = 11
        return 0, player.number, 8
    if x == 9:
        # idz do wiezienia
        player.field = 10
        player.prison = True
        return 0, player.number, 9
    if x == 10:
        # przejdz na dworzec gdanski
        if player.field > 0 and player.field <= 15:
            player.cash += 200
        player.field = 15
        return 0, player.number, 10
    if x == 11:
        # bank wyplaca ci dywidende 50
        player.cash += 50
        return 0, player.number, 11
    if x == 12:
        # remont 25 za kazdy dom 100 za kazdy hotel
        # return 0, player.number, 3
        return 1, player.number, 12
    if x == 13:
        # wygrales konkurs krzyzkowkowy pobierz 100
        player.cash += 100
        return 0, player.number, 13
    if x == 14:
        # przejdz na plac wilsona
        if player.field > 0 and player.field <= 24:
            player.cash += 200
        player.field = 24
        return 0, player.number, 14
    if x == 15:
        # wyjscie z wiezienia
        player.prisoncard = True
        return 0, player.number, 15


def community_chest(player, x):
    if x == 0:
        # odziedziczyles w spadku 100
        player.cash += 100
        return 0, player.number, 0
    if x == 1:
        # wroc na ulice konopacka
        player.field = 1
        return 0, player.number, 1
    if x == 2:
        # blad bankowy na twoja korzysc 200
        player.cash += 200
        return 0, player.number, 2
    if x == 3:
        # urodziny pobierz od kazdego 15
        player.cash += 15
        if player.number != p1.number:
            p1.cash -= 15
        if player.number != p2.number:
            p2.cash -= 15
        if player.number != p3.number:
            p3.cash -= 15
        if player.number != p4.number:
            p4.cash -= 15
            return 0, player.number, 3
    if x == 4:
        # zaplac grzywne 10 ziko albo szansa
        return 1, player.number, 4
    if x == 5:
        # sprzedales obligacje pobierz 100
        player.cash += 100
        return 0, player.number, 5
    if x == 6:
        # honorarium lekarza zaplac 50
        player.cash -= 50
        return 0, player.number, 6
    if x == 7:
        # otrzymujesz zwrot od podatku dochodowego pobierz 20
        player.cash += 20
        return 0, player.number, 7
    if x == 8:
        # przejdz na start
        player.field = 0
        return 0, player.number, 8
    if x == 9:
        # Otrzymujesz 50 za sprzedane akcje
        player.cash += 50
        return 0, player.number, 9
    if x == 10:
        # zaplac rachunek za szpital 100
        player.cash -= 100
        return 0, player.number, 10
    if x == 11:
        # wiezienie
        player.field = 10
        player.prison = True
        return 0, player.number, 11
    if x == 12:
        # nagroda w konkursie pieknosci 10
        player.cash += 10
        return 0, player.number, 12
    if x == 13:
        # zaplac skladke ubezpieczeniowa 50
        player.cash -= 50
        return 0, player.number, 13
    if x == 14:
        # otrzymujesz odsetki od lokaty terminowej 25
        player.cash += 25
        return 0, player.number, 14
    if x == 15:
        # wyjscie z wiezienia
        player.prisoncard = True
        return 0, player.number, 15


def prison(player):
    return


def random1(seed):
    # random.seed(seed)
    x = random.randint(0, 15)
    return x
