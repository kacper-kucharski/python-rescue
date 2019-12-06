import csv
import random

with open('DoomKaarten.csv') as doomKaarten:
    doomKaarten = csv.reader(doomKaarten, delimiter=',')
    list_cards = list(doomKaarten)
    print(list_cards[random.randint(0 , len(list_cards) - 1)])
