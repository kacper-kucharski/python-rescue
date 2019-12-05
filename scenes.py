def titleScene(cp5, font, interactiveObjects):
    font = createFont('arial', 50)
    textFont(font)
    text("Title", 48, 50, 50)
    interactiveObjects.append(cp5.addButton("Verder").setPosition(989,700).setSize(210,51).setFont(font))
    return interactiveObjects

def playerNameScene(cp5, font, interactiveObjects):
    # interactiveObjects.append(cp5.addRadioButton("radioButton", width/2, height/2).setItemsPerRow(4).setSpacingColumn(35).addItem("Black", 0.0).addItem("Red", 1.0).addItem("Blue", 2.0).addItem("Green", 3.0).setSize(50,50))
    interactiveObjects.append(cp5.addTextfield("Player 1").setPosition(int(width* 0.03 ), int(height* 0.06 )).setSize(int(width* 0.1 ), int(height* 0.06 )).setFont(font))
    interactiveObjects.append(cp5.addTextfield("Player 2").setPosition(int(width* 0.21 ), int(height* 0.06 )).setSize(int(width* 0.1 ), int(height* 0.06 )).setFont(font))
    interactiveObjects.append(cp5.addTextfield("Player 3").setPosition(int(width* 0.38 ), int(height* 0.06 )).setSize(int(width* 0.1 ), int(height* 0.06 )).setFont(font))
    interactiveObjects.append(cp5.addTextfield("Player 4").setPosition(int(width* 0.56 ), int(height* 0.06 )).setSize(int(width* 0.1 ), int(height* 0.06 )).setFont(font))
    interactiveObjects.append(cp5.addButton("Verder").setPosition(int(width* 0.47 ), int(height* 0.33 )).setSize(int(width* 0.07 ), int(height* 0.06 )).setFont(font))
    return interactiveObjects
    
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
def vraagScene(cp5, font, interactiveObjects):
    text("Vraag", 53, 37)
    interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.69 ), int(height* 0.78 )).setSize(int(width* 0.15 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
    interactiveObjects.append(cp5.addButton("Terug").setPosition(int(width* 0.74 ), int(height* 0.05 )).setSize(int(width* 0.11 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
def doomScene(cp5, font, interactiveObjects):
    text("Doom", 48, 35)
    text("Sla 3 beurten over", 477, 325)
    interactiveObjects.append(cp5.addButton("Verzenden").setPosition(989,700).setSize(210,51).setFont(font))
    return interactiveObjects
