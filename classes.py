# Create Player class with name, difficulty and optional currentPoints parameters.
class Player:
    def __init__(self, name, difficulty, currentPoints = 0):
        self.name = name
        self.currentPoints = currentPoints

# Create Game class with changePlayerTurn function and parameters like amount of player, list of all players and optional maxPoints option.
class Game: 
    def __init__(self, amountOfPlayers, playerList, maxPoints = 4):
        self.amountOfPlayers = amountOfPlayers
        self.maxPoints = maxPoints
        self.playersList = playerList
        self.playersTurn = playerList[0]

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

playersList = []

playersList.append(Player("John", "Expert"))
playersList.append(Player("Kacper", "Expert"))
playersList.append(Player("Do", "Advanced"))
playersList.append(Player("Rey", "Advanced"))

game = Game(len(playersList), playersList)
print(game.playersTurn.name)
game.changePlayerTurn()
print(game.playersTurn.name)