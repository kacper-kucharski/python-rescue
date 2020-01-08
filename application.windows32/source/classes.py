import csv
import random

# Create Player class with name, difficulty and optional currentPoints parameters.
class Player:
    def __init__(self, name, difficulty="makkelijk", Exp = 0, currentPoints = 0):
        self.name = name
        self.difficulty = difficulty
        self.currentPoints = currentPoints
        self.Exp = Exp
        self.lastQuestion = None
        self.lastAwnser = None
        self.skipTurn = 0
        self.eindvraagAntwoorden = []
    def level_change(self):
        if self.Exp < 4:
            self.difficulty = 'makkelijk'
        elif self.Exp >= 4 and self.Exp < 8:
            self.difficulty = 'gemiddeld'
        else:
            self.difficulty = 'moeilijk'
    

# Create Game class with changePlayerTurn function and parameters like amount of player, list of all players and optional maxPoints option.
class Game:
    global list_makkelijk, list_gemiddeld, list_moeilijk
    # Import all questions and answers and sort them by difficulty 
    def importKaarten(naam):
        with open(naam+'.csv') as kaarten:
            kaarten = csv.reader(kaarten, delimiter=',')
            return list(kaarten)        
    

# Return a question based on the players' level
    def getVraag(self):
        global list_makkelijk, list_gemiddeld, list_moeilijk
        self.playersTurn.level_change()
        if self.playersTurn.difficulty == 'makkelijk':
            x = list_makkelijk
        elif self.playersTurn.difficulty == 'gemiddeld':
            x = list_gemiddeld
        else:
            x = list_moeilijk
        self.playersTurn.lastQuestion = x[random.randint(0, len(x)-1)]
        print(self.playersTurn.difficulty)
        print(self.playersTurn.lastQuestion[5])
        return self.playersTurn.lastQuestion

# Get a random card from an csv file      
    def getDoom(self):
        with open('./import_csv/DoomKaarten.csv') as doomKaarten:
            doomKaarten = csv.reader(doomKaarten, delimiter=',')
            list_cards = list(doomKaarten)
            return str(list_cards[random.randint(0 , len(list_cards) - 1)]).strip("[]'")
        
# Get a random card from an csv file    
    def getKans(self):
        with open('./import_csv/KansKaarten.csv') as kansKaarten:
            kansKaarten = csv.reader(kansKaarten, delimiter=',')
            list_cards = list(kansKaarten)
            return str(list_cards[random.randint(0 , len(list_cards) - 1)]).strip("[]'")
    
    def __init__(self, playerList, maxPoints = 4):
        self.amountOfPlayers = len(playerList)
        self.maxPoints = maxPoints
        self.playersList = playerList
        self.playersTurn = playerList[0]
        self.duelAgainst = None
        self.eindvraagAntwoorden = ['input', 'input', 'int', 'int', 'age', 'name', 'year']
        
    list_makkelijk = importKaarten('import_csv/Leveltracker/MakkelijkKaarten')
    list_gemiddeld = importKaarten('import_csv/Leveltracker/GemiddeldKaarten')
    list_moeilijk = importKaarten('import_csv/Leveltracker/MoeilijkKaarten')

    # Looks up the current player in the list and gives the turn to the next player, if last player goes back to first player
    def changePlayerTurn(self):
        for x in range(len(self.playersList)):
            if self.playersTurn.name == self.playersList[x].name:
                if x != len(self.playersList)-1 and self.playersList[x+1].name != "":
                    self.playersTurn = self.playersList[x+1]
                else:
                    self.playersTurn = self.playersList[0]
                break
    def checkPlayerSkip():          
        if Game.playersTurn.skipTurn > 0:
            Game.playersTurn.skipTurn -= 1 
            print("Players turn skipped!")
            self.changePlayerTurn()
