import doom 
add_library('controlP5')

def changeFocus():
    global textFields
    len(textFields)
    for i in textFields:
        if textFields[i].isFocus() == True:
            if i == 4:
                textFields[i].setFocus(False)
                textFields[1].setFocus(True)
                break
            textFields[i].setFocus(False)
            textFields[i+1].setFocus(True)
            break
        
def setup():
    global playerName, savedPlayerName, textFields, cp5, font, scene, buttonNames
    font = createFont("arial",20);
    scene = 0
    cp5 = ControlP5(this)
    textFields = []
    buttonNames = {"Cards","Leaderboards","Rules","End Game","Vraag","Doom","Kans","Duel","Verzenden","Terug","Player 1","Player 2","Player 3", "Verder"}
    textFields.append(cp5.addTextfield("Player 1").setPosition(20,20).setSize(100,30).setFont(font))
    textFields.append(cp5.addTextfield("Player 2").setPosition(150,20).setSize(100,30).setFont(font))
    textFields.append(cp5.addTextfield("Player 3").setPosition(280,20).setSize(100,30).setFont(font))
    textFields.append(cp5.addTextfield("Player 4").setPosition(410,20).setSize(100,30).setFont(font))
    textFields.append(cp5.addButton("Verder").setPosition(350,200).setSize(100,50).setFont(font))
    # doom.setup()
    
    size(1280, 800)
    
    

def draw():
        pass
    
def keyPressed():
    global savedPlayerName, textFields, cp5, font
    if keyCode == 9:
        changeFocus()
def mousePressed():
    global cp5, scene, textFields
    try:
        for x in buttonNames:
            try:
                if cp5.getController(x).isPressed():
                    if x == "Verder":
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
                print(scene)
                background(200)
        if scene == 1:
            deleteAllComponents()
            textFields.append(cp5.addButton("Cards").setPosition(59,59).setSize(98,52).setFont(font))
            textFields.append(cp5.addButton("Leaderboards").setPosition(357,59).setSize(205,52).setFont(font))
            textFields.append(cp5.addButton("Rules").setPosition(762,59).setSize(98,52).setFont(font))
            textFields.append(cp5.addButton("End Game").setPosition(1060,59).setSize(161,59).setFont(font))
            textFields.append(cp5.addButton("Vraag").setPosition(91,259).setSize(532,193).setFont(font))
            textFields.append(cp5.addButton("Doom").setPosition(655,259).setSize(532,193).setFont(font))
            textFields.append(cp5.addButton("Kans").setPosition(91,548).setSize(532,193).setFont(font))
            textFields.append(cp5.addButton("Duel").setPosition(655,548).setSize(532,193).setFont(font))
        #Vraag
        if scene == 2:
            deleteAllComponents()
            text("Vraag", 53, 37)
            textFields.append(cp5.addButton("Verzenden").setPosition(989,700).setSize(210,51).setFont(font))
            textFields.append(cp5.addButton("Terug").setPosition(1067,45).setSize(161,53).setFont(font))
        #result
        if scene == 3:
            deleteAllComponents()
            text("Result", 400, 250)
            textFields.append(cp5.addButton("Verzenden").setPosition(100,400).setSize(100,50).setFont(font))
        #Kans
        if scene == 4:
            deleteAllComponents()
            text("Kans", 48, 43)
            text("Go 3 stappen naar achter", 358, 317)
            textFields.append(cp5.addButton("Verzenden").setPosition(1004,700).setSize(210,51).setFont(font))
        #Doom
        if scene == 5:
            deleteAllComponents()
            text("Doom", 48, 35)
            text("Sla 3 beurten over", 477, 325)
            textFields.append(cp5.addButton("Verzenden").setPosition(989,700).setSize(210,51).setFont(font))
        #Duel Start Screen
        if scene == 6:
            deleteAllComponents()
            text("Duel", 44, 20)
            textFields.append(cp5.addButton("Terug").setPosition(1070,23).setSize(161,53).setFont(font))
            text("VS WHO?", 141, 344)
            textFields.append(cp5.addButton("Player 1").setPosition(476,202).setSize(329,83).setFont(font))
            textFields.append(cp5.addButton("Player 2").setPosition(476,331).setSize(329,83).setFont(font))
            textFields.append(cp5.addButton("Player 3").setPosition(476,460).setSize(329,83).setFont(font))
       #Duel Fight
        if scene == 7:
            deleteAllComponents()
            text("Vraag", 53, 37)
            textFields.append(cp5.addButton("Verzenden").setPosition(989,700).setSize(210,51).setFont(font))
            textFields.append(cp5.addButton("Terug").setPosition(1067,45).setSize(161,53).setFont(font))
    except ValueError:
        print(ValueError)
def GetGameState(number):
    global cp5
def deleteAllComponents():
    global cp5
    for i in textFields:
        try:
            cp5.getController(i.getName()).remove()
        except:
            pass
