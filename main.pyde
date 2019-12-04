import doom

add_library('controlP5')
def changeFocus():
    global interactiveObjects
    len(interactiveObjects)
    for i in interactiveObjects:
        if interactiveObjects[i].isFocus() == True:
            if i == 4:
                interactiveObjects[i].setFocus(False)
                interactiveObjects[1].setFocus(True)
                break
            interactiveObjects[i].setFocus(False)
            interactiveObjects[i+1].setFocus(True)
            break
        
def setup():
    global playerName, savedPlayerName, interactiveObjects, cp5, font, scene, buttonNames
    font = createFont("arial",20);
    scene = 0
    cp5 = ControlP5(this)
    interactiveObjects = []
    buttonNames = ["Cards","Leaderboards","Rules","End Game","Vraag","Doom","Kans","Duel","Verzenden","Terug","Player 1","Player 2","Player 3", "Verder"]
    mousePressed()
    fullScreen()
    
def draw():
    pass
    
def keyPressed():
    global savedPlayerName, interactiveObjects, cp5, font, doom
    if keyCode == 9:
        changeFocus()
def mousePressed():
    global cp5, scene, interactiveObjects
    try:
        for x in buttonNames:
            try:
                if cp5.getController(x).isPressed():
                    if x == buttonNames[13]:
                        scene = 1
                        break
                    if x == "Cards":
                        scene = 1
                        break
                    if x == "Leaderboards":
                        scene = 1
                        break
                    if x == "Rules":
                        scene = 1
                        break
                    if x == "End Game":
                        exit()
                        break
                    if x == "Vraag":
                        scene = 2
                        break
                    if x == "Doom":
                        scene = 5
                        break
                    if x == "Kans":
                        scene = 4
                        break
                    if x == "Duel":
                        scene = 6
                        break
                    if x == "Verzenden" and scene == 2:
                        scene = 3
                        break
                    if x == "Verzenden" and scene == 4:
                        scene = 1
                        break
                    if x == "Verzenden" and scene == 5:
                        scene = 1
                        break
                    if x == "Verzenden" and scene == 3:
                        scene = 1
                        break
                    if x == "Verzenden" and scene == 7:
                        scene = 3
                        break
                    if x == "Terug"  and scene == 2:
                        scene = 1
                        break
                    if x == "Terug"  and scene == 6:
                        scene = 1
                        break
                    if x == "Terug"  and scene == 7:
                        scene = 6
                        break
                    if x == "Player 1" or x == "Player 2" or x == "Player 3":
                        scene = 7
                        break
            except:
                pass
        background(200)
        if scene == 0:
            deleteAllComponents()
            interactiveObjects.append(cp5.addTextfield("Player 1").setPosition(int(width* 0.03 ), int(height* 0.06 )).setSize(int(width* 0.1 ), int(height* 0.06 )).setFont(font))
            interactiveObjects.append(cp5.addTextfield("Player 2").setPosition(int(width* 0.21 ), int(height* 0.06 )).setSize(int(width* 0.1 ), int(height* 0.06 )).setFont(font))
            interactiveObjects.append(cp5.addTextfield("Player 3").setPosition(int(width* 0.38 ), int(height* 0.06 )).setSize(int(width* 0.1 ), int(height* 0.06 )).setFont(font))
            interactiveObjects.append(cp5.addTextfield("Player 4").setPosition(int(width* 0.56 ), int(height* 0.06 )).setSize(int(width* 0.1 ), int(height* 0.06 )).setFont(font))
            interactiveObjects.append(cp5.addButton("Verder").setPosition(int(width* 0.47 ), int(height* 0.33 )).setSize(int(width* 0.07 ), int(height* 0.06 )

        
).setFont(font))
        if scene == 1:
            deleteAllComponents()
            interactiveObjects.append(cp5.addButton("Cards").setPosition(int(width* 0.04 ), int(height* 0.07 )).setSize(int(width* 0.07 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("Leaderboards").setPosition(int(width* 0.25 ), int(height* 0.07 )).setSize(int(width* 0.14 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("Rules").setPosition(int(width* 0.53 ), int(height* 0.07 )).setSize(int(width* 0.07 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("End Game").setPosition(int(width* 0.74 ), int(height* 0.07 )).setSize(int(width* 0.11 ), int(height* 0.07 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("Vraag").setPosition(width* 0.06,height* 0.29).setSize(int(width* 0.37 ), int(height* 0.21 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("Doom").setPosition(int(width* 0.45 ), int(height* 0.29 )).setSize(int(width* 0.37 ), int(height* 0.21 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("Kans").setPosition(int(width* 0.06 ), int(height* 0.61 )).setSize(int(width* 0.37 ), int(height* 0.21 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("Duel").setPosition(int(width* 0.45 ), int(height* 0.61 )).setSize(int(width* 0.37 ), int(height* 0.21 )).setFont(font).setColorBackground(color(255,0,0)))
        #Vraag
        if scene == 2:
            deleteAllComponents()
            text("Vraag", 53, 37)
            interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.69 ), int(height* 0.78 )).setSize(int(width* 0.15 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("Terug").setPosition(int(width* 0.74 ), int(height* 0.05 )).setSize(int(width* 0.11 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
        #result
        if scene == 3:
            deleteAllComponents()
            text("Result", 400, 250)
            interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.07 ), int(height* 0.44 )).setSize(int(width* 0.07 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
        #Kans
        if scene == 4:
            deleteAllComponents()
            text("Kans", 48, 43)
            text("Go 3 stappen naar achter", 358, 317)
            interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.7 ), int(height* 0.78 )).setSize(int(width* 0.15 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
        #Doom
        if scene == 5:
            deleteAllComponents()
            interactiveObjects = doom.startScene(cp5, font, interactiveObjects)
        #Duel Start Screen
        if scene == 6:
            deleteAllComponents()
            text("Duel", 44, 20)
            interactiveObjects.append(cp5.addButton("Terug").setPosition(int(width* 0.74 ), int(height* 0.03 )).setSize(int(width* 0.11 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
            text("VS WHO?", 141, 344)
            interactiveObjects.append(cp5.addButton("Player 1").setPosition(int(width* 0.33 ), int(height* 0.22 )).setSize(int(width* 0.23 ), int(height* 0.09 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("Player 2").setPosition(int(width* 0.33 ), int(height* 0.37 )).setSize(int(width* 0.23 ), int(height* 0.09 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("Player 3").setPosition(int(width* 0.33 ), int(height* 0.51 )).setSize(int(width* 0.23 ), int(height* 0.09 )).setFont(font).setColorBackground(color(255,0,0)))
       #Duel Fight
        if scene == 7:
            deleteAllComponents()
            text("Vraag", 53, 37)
            interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.69 ), int(height* 0.78 )).setSize(int(width* 0.15 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("Terug").setPosition(int(width* 0.74 ), int(height* 0.05 )).setSize(int(width* 0.11 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
    except ValueError:
        print(ValueError)
def GetGameState(number):
    global cp5
def deleteAllComponents():
    global cp5
    for i in interactiveObjects:
        try:
            cp5.getController(i.getName()).remove()
        except:
            pass
