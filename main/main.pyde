def setup():
    global playerName, savedPlayerName
    
    size(800, 500)
    playerName = ""
    savedPlayerName = None

def draw():
    pass
    
def keyPressed():
    global playerName, savedPlayerName
    playerName = playerName + str(key)
    if key == "\n":
        savedPlayerName = playerName
        playerName = ""
        print("Saved Name: ", savedPlayerName)
        print("Player Name: ", playerName)
