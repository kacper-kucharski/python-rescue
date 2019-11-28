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
    global playerName, savedPlayerName, textFields, cp5, font, scene
    font = createFont("arial",20);
    scene = 0
    cp5 = ControlP5(this)
    textFields = []
    textFields.append(cp5.addTextfield("Player 1").setPosition(20,20).setSize(100,30).setFont(font))
    textFields.append(cp5.addTextfield("Player 2").setPosition(150,20).setSize(100,30).setFont(font))
    textFields.append(cp5.addTextfield("Player 3").setPosition(280,20).setSize(100,30).setFont(font))
    textFields.append(cp5.addTextfield("Player 4").setPosition(410,20).setSize(100,30).setFont(font))
    textFields.append(cp5.addButton("Verder").setPosition(350,200).setSize(100,50).setFont(font))
    # doom.setup()
    
    size(800, 500)
    
    

def draw():
        pass
    
def keyPressed():
    global savedPlayerName, textFields, cp5, font
    if keyCode == 9:
        changeFocus()
def mousePressed():
    global cp5, scene, textFields
    try:
        if cp5.getController("Verder").isPressed():
            scene += 1
            print(scene)
            background(200)
            #Main Menu
            if scene == 1:
                deleteAllComponents()
                # cp5.addTextfield("Player 1").setPosition(20,120).setSize(100,30).setFont(font)
                # cp5.addTextfield("Player 2").setPosition(150,120).setSize(100,30).setFont(font)
                # cp5.addTextfield("Player 3").setPosition(280,120).setSize(100,30).setFont(font)
                # cp5.addTextfield("Player 4").setPosition(410,120).setSize(100,30).setFont(font)
                text("Menu", 400, 250)
                textFields.append(cp5.addButton("Verder").setPosition(600,400).setSize(100,50).setFont(font))
            #Vraag
            if scene == 2:
                deleteAllComponents()
                text("Vraag", 400, 250)
                textFields.append(cp5.addButton("Verder").setPosition(600,400).setSize(100,50).setFont(font))
                textFields.append(cp5.addButton("Terug").setPosition(100,400).setSize(100,50).setFont(font))
            #result
            if scene == 3:
                deleteAllComponents()
                text("Result", 400, 250)
                textFields.append(cp5.addButton("Verder").setPosition(600,400).setSize(100,50).setFont(font))
                textFields.append(cp5.addButton("Terug").setPosition(100,400).setSize(100,50).setFont(font))
            #Kans
            if scene == 4:
                deleteAllComponents()
                text("Kans", 400, 250)
                textFields.append(cp5.addButton("Verder").setPosition(600,400).setSize(100,50).setFont(font))
                textFields.append(cp5.addButton("Terug").setPosition(100,400).setSize(100,50).setFont(font))
            #Doom
            if scene == 5:
                deleteAllComponents()
                text("Doom", 400, 250)
                textFields.append(cp5.addButton("Verder").setPosition(600,400).setSize(100,50).setFont(font))
                textFields.append(cp5.addButton("Terug").setPosition(100,400).setSize(100,50).setFont(font))
            #Duel Start Screen
            if scene == 6:
                deleteAllComponents()
                text("Duel Start Screen", 400, 250)
                textFields.append(cp5.addButton("Terug").setPosition(100,400).setSize(100,50).setFont(font))
        elif cp5.getController("Terug").isPressed():
            scene -= 1
            print(scene)
            background(200)

            if scene == 0:
                deleteAllComponents()
                textFields.append(cp5.addTextfield("Player 1").setPosition(20,20).setSize(100,30).setFont(font))
                textFields.append(cp5.addTextfield("Player 2").setPosition(150,20).setSize(100,30).setFont(font))
                textFields.append(cp5.addTextfield("Player 3").setPosition(280,20).setSize(100,30).setFont(font))
                textFields.append(cp5.addTextfield("Player 4").setPosition(410,20).setSize(100,30).setFont(font))
                textFields.append(cp5.addButton("Verder").setPosition(350,200).setSize(100,50).setFont(font))
            if scene == 1:
                deleteAllComponents()
                text("Menu", 400, 250)
                textFields.append(cp5.addButton("Verder").setPosition(600,400).setSize(100,50).setFont(font))
            #Vraag
            if scene == 2:
                deleteAllComponents()
                text("Vraag", 400, 250)
                textFields.append(cp5.addButton("Verder").setPosition(600,400).setSize(100,50).setFont(font))
                textFields.append(cp5.addButton("Terug").setPosition(100,400).setSize(100,50).setFont(font))
            #result
            if scene == 3:
                deleteAllComponents()
                text("Result", 400, 250)
                textFields.append(cp5.addButton("Verder").setPosition(600,400).setSize(100,50).setFont(font))
                textFields.append(cp5.addButton("Terug").setPosition(100,400).setSize(100,50).setFont(font))
            #Kans
            if scene == 4:
                deleteAllComponents()
                text("Kans", 400, 250)
                textFields.append(cp5.addButton("Verder").setPosition(600,400).setSize(100,50).setFont(font))
                textFields.append(cp5.addButton("Terug").setPosition(100,400).setSize(100,50).setFont(font))
            #Doom
            if scene == 5:
                deleteAllComponents()
                text("Doom", 400, 250)
                textFields.append(cp5.addButton("Verder").setPosition(600,400).setSize(100,50).setFont(font))
                textFields.append(cp5.addButton("Terug").setPosition(100,400).setSize(100,50).setFont(font))
            #Duel Start Screen
            if scene == 6:
                deleteAllComponents()
                text("Duel Start Screen", 400, 250)
                textFields.append(cp5.addButton("Terug").setPosition(100,400).setSize(100,50).setFont(font))
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
