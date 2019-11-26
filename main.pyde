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
    global playerName, savedPlayerName, textFields, cp5, font
    font = createFont("arial",20);
    cp5 = ControlP5(this)
    textFields = []
    textFields.append(cp5.addTextfield("Player 1").setPosition(20,20).setSize(100,30).setFont(font))
    textFields.append(cp5.addTextfield("Player 2").setPosition(150,20).setSize(100,30).setFont(font))
    textFields.append(cp5.addTextfield("Player 3").setPosition(280,20).setSize(100,30).setFont(font))
    textFields.append(cp5.addTextfield("Player 4").setPosition(410,20).setSize(100,30).setFont(font))
    textFields.append(cp5.addButton("Verder").setPosition(350,200).setSize(100,50).setFont(font))
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
            cp5.getController("Player 1").remove()
            print(textFields)
        except:
            print("deze is al verwijderd.")
    elif key == "s":
        cp5.addTextfield("Player 1").setPosition(20,20).setSize(100,30).setFont(font)
    if key == "\n":
        savedPlayerName1 = textFields[0].getText()
        savedPlayerName2 = textFields[1].getText()
        savedPlayerName3 = textFields[2].getText()
        savedPlayerName4 = textFields[3].getText()
        print(savedPlayerName1)
        print(savedPlayerName2)
        print(savedPlayerName3)
        print(savedPlayerName4)
        
def mousePressed():
    global cp5
    if cp5.getController("Verder").isPressed():
        print("knop: Verder is geklikt.")
