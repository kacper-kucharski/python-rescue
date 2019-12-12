# Make a variable in player class for 'level': Now called playerturn.difficulty

# Make sure that if the player enters their level at the beginning of the game this is set in the class
# john's taak

# Make a system that randomizes one card based on the players level, so if gemiddeld give the randomizer the option to choose
# from makkelijk or gemiddeld and exclude moeilijk. 
# Edit the import function and make the csv files sorted on levels, import from the right csv file according to level
import csv
import random

def importKaarten(naam):
    with open(naam+'.csv') as kaarten:
        kaarten = csv.reader(kaarten, delimiter=',')
        return list(kaarten)

list_makkelijk = importKaarten('MakkelijkKaarten')
list_gemiddeld = importKaarten('GemiddeldKaarten')
list_moeilijk = importKaarten('MoeilijkKaarten')

def getVraag():
    if self.playerturn.difficulty == 'makkelijk':
        x = list_makkelijk
    elif self.playerturn.difficulty == 'gemiddeld':
        x = list_gemiddeld
    else:
        x = list_moeilijk
    randomVraag = x[random.randint(0, len(x)-1)]
    vraag = (randomVraag[0])
    vraag_antwoorden = (randomVraag[0], randomVraag[1], randomVraag[2], randomVraag[3], randomVraag[4])
    antwoord1 = randomVraag[1]
    antwoord2 = randomVraag[2]
    antwoord3 = randomVraag[3]
    antwoord4 = randomVraag[4]
    antwoord = (randomVraag[6])
    print(vraag)
    '\n'
    print(antwoord1)
    print(antwoord2)

    if antwoord3 == '':
        pass
    else:
        print(antwoord3)
    if antwoord4 == '':
        pass
    else:
        print(antwoord4)

    '\n'
    print(antwoord)

# add or decrease points based on correct or wrong answer, this will be in the answer check function
# this must be in john's code

# Make a points range for each level
# Make a function for changing a players level and call this after adding or taking a point

def level_change():
    if self.Exp < 4:
        self.difficulty = 'makkelijk'
    elif self.Exp >= 4 and self.currentPoints < 8:
        self.difficulty = 'gemiddeld'
    else:
        self.difficulty = 'moeilijk'

