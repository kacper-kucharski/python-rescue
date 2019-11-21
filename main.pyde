import chance
import doom
import duel
import menu
import questions
import result
import title_screen
add_library('controlP5')
print("dominique change")
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
    global playerName, savedPlayerName, textFields
    font = createFont("arial",20);
    cp5 = ControlP5(this)
    textFields = {
    1: '',
    2: '',
    3: '',
    4: ''
    }
    textFields[1] = cp5.addTextfield("Player 1").setPosition(20,20).setSize(100,30).setFont(font)
    textFields[2] = cp5.addTextfield("Player 2").setPosition(150,20).setSize(100,30).setFont(font)
    textFields[3] = cp5.addTextfield("Player 3").setPosition(280,20).setSize(100,30).setFont(font)
    textFields[4] = cp5.addTextfield("Player 4").setPosition(410,20).setSize(100,30).setFont(font)
    size(800, 500)

def draw():
    pass
    
def keyPressed():
    global savedPlayerName, textFields
    if keyCode == 9:
        changeFocus()
    if key == "\n":
        savedPlayerName1 = textFields[1].getText()
        savedPlayerName2 = textFields[2].getText()
        savedPlayerName3 = textFields[3].getText()
        savedPlayerName4 = textFields[4].getText()
        print(savedPlayerName1)
        print(savedPlayerName2)
        print(savedPlayerName3)
        print(savedPlayerName4)
