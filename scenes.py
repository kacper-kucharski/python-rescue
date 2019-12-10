# scene = -1
def titleScene(cp5, font, interactiveObjects):
    # image(loadImage('../assets/titlePicture.jpg'),0,0,width,height)
    font = createFont('arial', 50)
    textFont(font)
    text("Druk ergens om verder te gaan!", width * 0.25, height* 0.75 + int(width* 0.05 ), int(height* 0.05 ))
    interactiveObjects.append(cp5.addButton("Verder").setPosition(width + 100,width+ 100).setSize(int(width* 0.11 ), int(height* 0.05 )).setFont(font))
    return interactiveObjects
# scene = 0
def playerNameScene(cp5, font, interactiveObjects):
    interactiveObjects.append(cp5.addTextfield("Player 1").setPosition(int(width* 0.03 ), int(height* 0.05 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font))
    interactiveObjects.append(cp5.addTextfield("Player 2").setPosition(int(width* 0.16 ), int(height* 0.05 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font))
    interactiveObjects.append(cp5.addTextfield("Player 3").setPosition(int(width* 0.29 ), int(height* 0.05 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font))
    interactiveObjects.append(cp5.addTextfield("Player 4").setPosition(int(width* 0.42 ), int(height* 0.05 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font))
    interactiveObjects.append(cp5.addButton("Verder").setPosition(int(width* 0.45 ), int(height* 0.28 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font))
    return interactiveObjects
# scene = 1
def mainMenu(cp5, font, interactiveObjects, game):
    text("Aan de beurt: " + game.playersTurn.name, width * 0.05, height * 0.20)
    interactiveObjects.append(cp5.addButton("Change turn").setPosition(int(width* 0.50 ), int(height* 0.17 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,150,100)))
    interactiveObjects.append(cp5.addTextlabel("Cards").setPosition(int(width* 0.03 ), int(height* 0.05 )).setSize(int(width* 0.05 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("End Game").setPosition(int(width* 0.55 ), int(height* 0.05 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font).setColorBackground(color(0,0,0)))
    font = createFont("arial",50);
    interactiveObjects.append(cp5.addButton("Vraag").setPosition(int(width* 0.05 ), int(height* 0.24 )).setSize(int(width* 0.28 ), int(height* 0.18 )).setFont(font).setColorBackground(color(0,255,0)))
    interactiveObjects.append(cp5.addButton("Doom").setPosition(int(width* 0.34 ), int(height* 0.24 )).setSize(int(width* 0.28 ), int(height* 0.18 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Kans").setPosition(int(width* 0.05 ), int(height* 0.51 )).setSize(int(width* 0.28 ), int(height* 0.18 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Duel").setPosition(int(width* 0.34 ), int(height* 0.51 )).setSize(int(width* 0.28 ), int(height* 0.18 )).setFont(font).setColorBackground(color(255,0,0)))
    return interactiveObjects
# scene = 2
def vraagScene(cp5, font, interactiveObjects, game):
    vraag = game.getVraag()
    text(str(vraag[0]), width * 0.09, height * 0.29)
    # cp5.setControlFont(font)
    radioButtons = cp5.addRadioButton("radioButton", width/2, height/2).setSize(50,50).setItemsPerRow(1).setSpacingColumn(35).setFont(font)
    for i in range(1, 5):
        if vraag[i] != '':
            radioButtons.addItem(str(vraag[i]), float(i))
    interactiveObjects.append(radioButtons)
    interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.69 ), int(height* 0.78 )).setSize(int(width* 0.15 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Terug").setPosition(int(width* 0.74 ), int(height* 0.05 )).setSize(int(width* 0.11 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
    return interactiveObjects
# scene = 5
def doomScene(cp5, font, interactiveObjects, game):
    doom = str(game.getDoom())
    text("" + doom, int(width* 0.09 ), int(height* 0.3 ))
    interactiveObjects.append(cp5.addButton("Verzenden").setPosition(989,700).setSize(210,51).setFont(font))
    return interactiveObjects
# scene = 4
def kansScene(cp5, font, interactiveObjects, game):
    kans = str(game.getKans())
    text(kans, int(width* 0.09 ), int(height* 0.3 ))
    interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.52 ), int(height* 0.65 )).setSize(int(width* 0.11 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
    return interactiveObjects
# scene = 6
def duelScene(cp5, font, interactiveObjects, game):
    text("Duel", int(width* 0.02 ), int(height* 0.02 ))
    interactiveObjects.append(cp5.addButton("Terug").setPosition(int(width* 0.56 ), int(height* 0.02 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
    text("VS WHO?", int(width* 0.07 ), int(height* 0.32 ))
    buttonHeight = [height* 0.19, height* 0.31, height* 0.43]
    _players = []
    for x in game.playersList:
        if x.name != game.playersTurn.name:
            _players.append(x)
    for x in range(len(_players)):
        interactiveObjects.append(cp5.addButton(str(_players[x].name)).setPosition(int(width* 0.25 ), int(buttonHeight[x])).setSize(int(width* 0.17 ), int(height* 0.08 )).setFont(font).setColorBackground(color(255,0,0)))
    return interactiveObjects
# scene = 3
def resultScene(cp5, font, interactiveObjects, game):
    text("Result", 400, 250)
    interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.07 ), int(height* 0.44 )).setSize(int(width* 0.07 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
    return interactiveObjects
# scene = 7
def duelQuestionScene(cp5, font, interactiveObjects, game):
    text("Vraag", int(width* 0.03 ), int(height* 0.03 ))
    text("Je speelt tegen " + game.duelAgainst.name, int(width* 0.03 ), int(height* 0.30 ))
    vraag = game.getVraag()
    text(str(vraag[0]), width * 0.09, height * 0.29)
    # cp5.setControlFont(font)
    radioButtons = cp5.addRadioButton("radioButton", width/2, height/2).setSize(50,50).setItemsPerRow(1).setSpacingColumn(35).setFont(font)
    for i in range(1, 5):
        if vraag[i] != '':
            radioButtons.addItem(str(vraag[i]), float(i))
    interactiveObjects.append(radioButtons)
    interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.69 ), int(height* 0.78 )).setSize(int(width* 0.15 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Terug").setPosition(int(width* 0.74 ), int(height* 0.05 )).setSize(int(width* 0.11 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
    return interactiveObjects
