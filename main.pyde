add_library('controlP5')

def setup():
    
    font = createFont("arial",20);
    cp5 = ControlP5(this)
    global playerName, savedPlayerName, textField
    textField = cp5.addTextfield("").setPosition(20,20).setSize(100,30).setFont(font)
    size(800, 500)
    playerName = ""
    savedPlayerName = None

def draw():
    pass
    
def keyPressed():
    global playerName, savedPlayerName, textField
    playerName = playerName + str(key)
    if key == "\n":
        print(textField.getText())
        playerName = textField.getText()
        playerName = playerName.replace("\n", "")
        playerName = playerName.replace("65535", "")
        savedPlayerName = playerName
        print("Saved Name: ", savedPlayerName)
        print("Player Name: ", playerName)
