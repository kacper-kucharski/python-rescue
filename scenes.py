# scene = -1
def titleScene(cp5, font, interactiveObjects):
    img = loadImage('../assets/titlePicture.jpg')
    image(img, 0, 0, width, height)
    font = createFont('arial', 50)
    textFont(font)
    text("Druk ergens om verder te gaan!", width * 0.25, height* 0.75 + 100, 50)
    interactiveObjects.append(cp5.addButton("Verder").setPosition(width + 100,width+ 100).setSize(210,51).setFont(font))
    return interactiveObjects
# scene = 0
def playerNameScene(cp5, font, interactiveObjects):
    interactiveObjects.append(cp5.addTextfield("Player 1").setPosition(int(width* 0.03 ), int(height* 0.06 )).setSize(int(width* 0.1 ), int(height* 0.06 )).setFont(font))
    interactiveObjects.append(cp5.addTextfield("Player 2").setPosition(int(width* 0.21 ), int(height* 0.06 )).setSize(int(width* 0.1 ), int(height* 0.06 )).setFont(font))
    interactiveObjects.append(cp5.addTextfield("Player 3").setPosition(int(width* 0.38 ), int(height* 0.06 )).setSize(int(width* 0.1 ), int(height* 0.06 )).setFont(font))
    interactiveObjects.append(cp5.addTextfield("Player 4").setPosition(int(width* 0.56 ), int(height* 0.06 )).setSize(int(width* 0.1 ), int(height* 0.06 )).setFont(font))
    interactiveObjects.append(cp5.addButton("Verder").setPosition(int(width* 0.47 ), int(height* 0.33 )).setSize(int(width* 0.07 ), int(height* 0.06 )).setFont(font))
    return interactiveObjects
# scene = 1
def mainMenu(cp5, font, interactiveObjects):
    interactiveObjects.append(cp5.addButton("Cards").setPosition(int(width* 0.04 ), int(height* 0.07 )).setSize(int(width* 0.07 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Leaderboards").setPosition(int(width* 0.25 ), int(height* 0.07 )).setSize(int(width* 0.14 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Rules").setPosition(int(width* 0.53 ), int(height* 0.07 )).setSize(int(width* 0.07 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("End Game").setPosition(int(width* 0.74 ), int(height* 0.07 )).setSize(int(width* 0.11 ), int(height* 0.07 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Vraag").setPosition(width* 0.06,height* 0.29).setSize(int(width* 0.37 ), int(height* 0.21 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Doom").setPosition(int(width* 0.45 ), int(height* 0.29 )).setSize(int(width* 0.37 ), int(height* 0.21 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Kans").setPosition(int(width* 0.06 ), int(height* 0.61 )).setSize(int(width* 0.37 ), int(height* 0.21 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Duel").setPosition(int(width* 0.45 ), int(height* 0.61 )).setSize(int(width* 0.37 ), int(height* 0.21 )).setFont(font).setColorBackground(color(255,0,0)))
    return interactiveObjects
# scene = 2
def vraagScene(cp5, font, interactiveObjects):
    text("Vraag", 53, 37)
    interactiveObjects.append(cp5.addRadioButton("radioButton", width/2, height/2).setItemsPerRow(4).setSpacingColumn(35).addItem("ZET HIER VRAAG 1", 1.0).addItem("ZET HIER VRAAG 2", 2.0).addItem("ZET HIER VRAAG 3", 3.0).addItem("ZET HIER VRAAG 4", 3.0).setSize(50,50).setFont(font))
    interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.69 ), int(height* 0.78 )).setSize(int(width* 0.15 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Terug").setPosition(int(width* 0.74 ), int(height* 0.05 )).setSize(int(width* 0.11 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
    return interactiveObjects
# scene = 5
def doomScene(cp5, font, interactiveObjects):
    text("Doom", 48, 35)
    text("Sla 3 beurten over", 477, 325)
    interactiveObjects.append(cp5.addButton("Verzenden").setPosition(989,700).setSize(210,51).setFont(font))
    return interactiveObjects
# scene = 4
def kansScene(cp5, font, interactiveObjects):
    text("Kans", 48, 43)
    text("Go 3 stappen naar achter", 358, 317)
    interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.7 ), int(height* 0.78 )).setSize(int(width* 0.15 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
    return interactiveObjects
# scene = 6
def duelScene(cp5, font, interactiveObjects):
    text("Duel", 44, 20)
    interactiveObjects.append(cp5.addButton("Terug").setPosition(int(width* 0.74 ), int(height* 0.03 )).setSize(int(width* 0.11 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
    text("VS WHO?", 141, 344)
    interactiveObjects.append(cp5.addButton("Player 1").setPosition(int(width* 0.33 ), int(height* 0.22 )).setSize(int(width* 0.23 ), int(height* 0.09 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Player 2").setPosition(int(width* 0.33 ), int(height* 0.37 )).setSize(int(width* 0.23 ), int(height* 0.09 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Player 3").setPosition(int(width* 0.33 ), int(height* 0.51 )).setSize(int(width* 0.23 ), int(height* 0.09 )).setFont(font).setColorBackground(color(255,0,0)))
    return interactiveObjects
# scene = 3
def resultScene(cp5, font, interactiveObjects):
    text("Result", 400, 250)
    interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.07 ), int(height* 0.44 )).setSize(int(width* 0.07 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
    return interactiveObjects
# scene = 7
def duelresultScene(cp5, font, interactiveObjects):
    text("Vraag", 53, 37)
    interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.69 ), int(height* 0.78 )).setSize(int(width* 0.15 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Terug").setPosition(int(width* 0.74 ), int(height* 0.05 )).setSize(int(width* 0.11 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
    return interactiveObjects
