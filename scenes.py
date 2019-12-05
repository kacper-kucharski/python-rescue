def titleScene(cp5, font, interactiveObjects):
    img = loadImage('../assets/titlePicture.png')
    image(img, 0, 0, width, height)
    font = createFont('arial', 50)
    textFont(font)
    text("Druk ergens om verder te gaan!", width * 0.25, height* 0.75 + int(width* 0.05 ), int(height* 0.05 ))
    interactiveObjects.append(cp5.addButton("Verder").setPosition(width + 100,width+ 100).setSize(int(width* 0.11 ), int(height* 0.05 )).setFont(font))
    return interactiveObjects

def playerNameScene(cp5, font, interactiveObjects):
    interactiveObjects.append(cp5.addTextfield("Player 1").setPosition(int(width* 0.03 ), int(height* 0.05 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font))
    interactiveObjects.append(cp5.addTextfield("Player 2").setPosition(int(width* 0.16 ), int(height* 0.05 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font))
    interactiveObjects.append(cp5.addTextfield("Player 3").setPosition(int(width* 0.29 ), int(height* 0.05 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font))
    interactiveObjects.append(cp5.addTextfield("Player 4").setPosition(int(width* 0.42 ), int(height* 0.05 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font))
    interactiveObjects.append(cp5.addButton("Verder").setPosition(int(width* 0.45 ), int(height* 0.28 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font))
    return interactiveObjects
    
def mainMenu(cp5, font, interactiveObjects):
    interactiveObjects.append(cp5.addButton("Cards").setPosition(int(width* 0.03 ), int(height* 0.05 )).setSize(int(width* 0.05 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Leaderboards").setPosition(int(width* 0.19 ), int(height* 0.05 )).setSize(int(width* 0.11 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Rules").setPosition(int(width* 0.4 ), int(height* 0.05 )).setSize(int(width* 0.05 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("End Game").setPosition(int(width* 0.55 ), int(height* 0.05 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Vraag").setPosition(int(width* 0.05 ), int(height* 0.24 )).setSize(int(width* 0.28 ), int(height* 0.18 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Doom").setPosition(int(width* 0.34 ), int(height* 0.24 )).setSize(int(width* 0.28 ), int(height* 0.18 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Kans").setPosition(int(width* 0.05 ), int(height* 0.51 )).setSize(int(width* 0.28 ), int(height* 0.18 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Duel").setPosition(int(width* 0.34 ), int(height* 0.51 )).setSize(int(width* 0.28 ), int(height* 0.18 )).setFont(font).setColorBackground(color(255,0,0)))
    return interactiveObjects

def vraagScene(cp5, font, interactiveObjects):
    text("Vraag", 53, 37)
    interactiveObjects.append(cp5.addRadioButton("radioButton", width/2, height/2).setItemsPerRow(4).setSpacingColumn(35).addItem("ZET HIER VRAAG 1", 1.0).addItem("ZET HIER VRAAG 2", 2.0).addItem("ZET HIER VRAAG 3", 3.0).addItem("ZET HIER VRAAG 4", 3.0).setSize(int(width* 0.03 ), int(height* 0.05 )))
    interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.52 ), int(height* 0.65 )).setSize(int(width* 0.11 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Terug").setPosition(int(width* 0.56 ), int(height* 0.04 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
    return interactiveObjects
def doomScene(cp5, font, interactiveObjects):
    text("Doom", int(width* 0.03 ), int(height* 0.03 ))
    text("Sla 3 beurten over", int(width* 0.25 ), int(height* 0.3 ))
    interactiveObjects.append(cp5.addButton("Verzenden").setPosition(989,700).setSize(210,51).setFont(font))
    return interactiveObjects
def kansScene(cp5, font, interactiveObjects):
    text("Kans", int(width* 0.03 ), int(height* 0.04 ))
    text("Go 3 stappen naar achter", int(width* 0.19 ), int(height* 0.29 ))
    interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.52 ), int(height* 0.65 )).setSize(int(width* 0.11 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
    return interactiveObjects
def duelScene(cp5, font, interactiveObjects):
    text("Duel", int(width* 0.02 ), int(height* 0.02 ))
    interactiveObjects.append(cp5.addButton("Terug").setPosition(int(width* 0.56 ), int(height* 0.02 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
    text("VS WHO?", int(width* 0.07 ), int(height* 0.32 ))
    interactiveObjects.append(cp5.addButton("Player 1").setPosition(int(width* 0.25 ), int(height* 0.19 )).setSize(int(width* 0.17 ), int(height* 0.08 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Player 2").setPosition(int(width* 0.25 ), int(height* 0.31 )).setSize(int(width* 0.17 ), int(height* 0.08 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Player 3").setPosition(int(width* 0.25 ), int(height* 0.43 )).setSize(int(width* 0.17 ), int(height* 0.08 )).setFont(font).setColorBackground(color(255,0,0)))
    return interactiveObjects
def resultScene(cp5, font, interactiveObjects):
    text("Result", 400, 250)
    interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.07 ), int(height* 0.44 )).setSize(int(width* 0.07 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
    return interactiveObjects
def duelresultScene(cp5, font, interactiveObjects):
    text("Vraag", int(width* 0.03 ), int(height* 0.03 ))
    interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.52 ), int(height* 0.65 )).setSize(int(width* 0.11 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Terug").setPosition(int(width* 0.56 ), int(height* 0.04 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
    return interactiveObjects
