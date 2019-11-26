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
            if i == len(textFields):
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
    textFields.append(cp5.addTextfield("Player 1").setPosition(20,20).setSize(100,30).setFont(font).setId(1))
    textFields.append(cp5.addTextfield("Player 2").setPosition(150,20).setSize(100,30).setFont(font).setId(2))
    textFields.append(cp5.addTextfield("Player 3").setPosition(280,20).setSize(100,30).setFont(font).setId(3))
    textFields.append(cp5.addTextfield("Player 4").setPosition(410,20).setSize(100,30).setFont(font).setId(4))
    textFields.append(cp5.addButton("Verder").setPosition(350,200).setSize(100,50).setFont(font).setId(5))
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
    global cp5
    try:
        if cp5.getController("Verder").isPressed():
            background(200)
            try:
                cp5.getController("Player 1").remove()
                cp5.getController("Player 2").remove()
                cp5.getController("Player 3").remove()
                cp5.getController("Player 4").remove()
                cp5.addTextfield("Player 1").setPosition(20,120).setSize(100,30).setFont(font)
                cp5.addTextfield("Player 2").setPosition(150,120).setSize(100,30).setFont(font)
                cp5.addTextfield("Player 3").setPosition(280,120).setSize(100,30).setFont(font)
                cp5.addTextfield("Player 4").setPosition(410,120).setSize(100,30).setFont(font)
                cp5.getController("Verder").remove()
                print(textFields)
            except:
                pass
    except:
        pass
def changeGameState(number):
    global cp5
