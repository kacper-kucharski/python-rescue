import chance
import doom 
import duel
import menu
import questions
import result
import title_screen

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
    doom.setup()
    size(800, 500)
    
    

def draw():
        pass
    
def keyPressed():
    global savedPlayerName, textFields, cp5, font
    if keyCode == 9:
        changeFocus()
    if key == "w":
        background(200)
        try:
            for i in textFields:
                cp5.getController(i.getName()).remove()
        except:
            print("deze is al verwijderd.")
    elif key == "s":
        cp5.addTextfield("Player 1").setPosition(20,20).setSize(100,30).setFont(font)
        cp5.addTextfield("Player 2").setPosition(150,20).setSize(100,30).setFont(font)
        cp5.addTextfield("Player 3").setPosition(280,20).setSize(100,30).setFont(font)
        cp5.addTextfield("Player 4").setPosition(410,20).setSize(100,30).setFont(font)
        cp5.addButton("Verder").setPosition(350,200).setSize(100,50).setFont(font)
    if key == "\n":
        savedPlayerName1 = cp5.getController("Player 1").getText()
        savedPlayerName2 = textFields[1].getText()
        savedPlayerName3 = textFields[2].getText()
        savedPlayerName4 = textFields[3].getText()
        print(savedPlayerName1)
        print(savedPlayerName2)
        print(savedPlayerName3)
        print(savedPlayerName4)
        
def mousePressed():
    global cp5, scene
    try:
        if cp5.getController("Verder").isPressed():
            scene += 1
            print(scene)
            background(200)
            try:
                if scene == 1:
                    for i in textFields:
                        cp5.getController(i.getName()).remove()
                    # cp5.addTextfield("Player 1").setPosition(20,120).setSize(100,30).setFont(font)
                    # cp5.addTextfield("Player 2").setPosition(150,120).setSize(100,30).setFont(font)
                    # cp5.addTextfield("Player 3").setPosition(280,120).setSize(100,30).setFont(font)
                    # cp5.addTextfield("Player 4").setPosition(410,120).setSize(100,30).setFont(font)
                    textFields.append(cp5.addButton("Verder").setPosition(600,400).setSize(100,50).setFont(font))
                    textFields.append(cp5.addButton("Terug").setPosition(100,400).setSize(100,50).setFont(font))
                    textFields.append(cp5.addSlider("GELD!").setSize(100,30).setRange(0,50).setFont(font))
                    text("Menu", 400, 250)
                    
                    # print(textFields)
            except:
                pass
        elif cp5.getController("Terug").isPressed():
            print(scene)
            scene -= 1
            background(200)
            try:
                if scene == 0:
                    cp5.getController("Player 1").remove()
                    cp5.getController("Player 2").remove()
                    cp5.getController("Player 3").remove()
                    cp5.getController("Player 4").remove()
                    textFields.append(cp5.addTextfield("Player 1").setPosition(20,20).setSize(100,30).setFont(font))
                    textFields.append(cp5.addTextfield("Player 2").setPosition(150,20).setSize(100,30).setFont(font))
                    textFields.append(cp5.addTextfield("Player 3").setPosition(280,20).setSize(100,30).setFont(font))
                    textFields.append(cp5.addTextfield("Player 4").setPosition(410,20).setSize(100,30).setFont(font))
                    textFields.append(cp5.addButton("Verder").setPosition(350,200).setSize(100,50).setFont(font))
            except:
                pass
    except:
        pass
def GetGameState(number):
    global cp5
