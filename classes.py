import csv
import random

# Create Player class with name, difficulty and optional currentPoints parameters.
class Player:
    def __init__(self, name, difficulty="makkelijk", currentPoints = 0, Exp = 5):
        self.name = name
        self.difficulty = difficulty
        self.currentPoints = currentPoints
        self.Exp = Exp
        self.lastQuestion = None
        self.lastAwnser = None

# Create Game class with changePlayerTurn function and parameters like amount of player, list of all players and optional maxPoints option.
class Game: 
    def __init__(self, amountOfPlayers, playerList, maxPoints = 4):
        self.amountOfPlayers = amountOfPlayers
        self.maxPoints = maxPoints
        self.playersList = playerList
        self.playersTurn = playerList[0]
        self.duelAgainst = None

    # Looks up the current player in the list and gives the turn to the next player, if last player goes back to first player
    def changePlayerTurn(self):
        for x in range(len(self.playersList)):
            if self.playersTurn.name == self.playersList[x].name:
                if x != len(self.playersList)-1:
                    self.playersTurn = self.playersList[x+1]
                    break
                else:
                    self.playersTurn = self.playersList[0]
                    break
    # Get a random question from an csv file with all the questions
    def getVraag(self):
        with open('./import_csv/Vraagkaarten.csv') as vraagKaarten:
            vraagKaarten = csv.reader(vraagKaarten, delimiter=',')
            list_questions = list(vraagKaarten)
            return list_questions[random.randint(0, len(list_questions) - 1)]
        
    def getDoom(self):
        with open('./import_csv/DoomKaarten.csv') as doomKaarten:
            doomKaarten = csv.reader(doomKaarten, delimiter=',')
            list_cards = list(doomKaarten)
            return str(list_cards[random.randint(0 , len(list_cards) - 1)]).strip("[]'")
        
    def getKans(self):
        with open('./import_csv/KansKaarten.csv') as kansKaarten:
            kansKaarten = csv.reader(kansKaarten, delimiter=',')
            list_cards = list(kansKaarten)
            return str(list_cards[random.randint(0 , len(list_cards) - 1)]).strip("[]'")
        
