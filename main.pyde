import scenes
import classes
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
    color(0)
    background(200)
    global playerName, savedPlayerName, interactiveObjects, cp5, font, scene, buttonNames, playersList
    font = createFont("arial",20);
    scene = -1
    cp5 = ControlP5(this)
    interactiveObjects = []
    playersList = []
    interactiveObjects = scenes.titleScene(cp5, font, interactiveObjects)
    fullScreen()
    
def draw():
    pass
    
def keyPressed():
    global savedPlayerName, interactiveObjects, cp5, font, doom, scene
    # if keyCode == 9 and scene == 0:
    #     changeFocus()
    if scene == -1:
        background(200)
        deleteAllComponents()
        scene = 0
        interactiveObjects = scenes.playerNameScene(cp5, font, interactiveObjects)
        # print(cp5.getController("Player 1").getText())
def mousePressed():
    global cp5, scene, interactiveObjects, playersList
    try:
        for x in interactiveObjects:
            if scene == -1:
                background(200)
                deleteAllComponents()
                scene = 0
                interactiveObjects = scenes.playerNameScene(cp5, font, interactiveObjects)
            try:
                if cp5.getController(x.getName()).isPressed():
                    background(200)
                    x = x.getName()
                    if x == 'Verder' and scene == 0:
                        # check of input niet leeg is en maakt vervolgens een player object met de gegeven naam
                        if cp5.getController("Player 1").getText() != "":
                            playersList.append(classes.Player(cp5.getController("Player 1").getText()))
                        if cp5.getController("Player 2").getText() != "":
                            playersList.append(classes.Player(cp5.getController("Player 2").getText()))
                        if cp5.getController("Player 3").getText() != "":
                            playersList.append(classes.Player(cp5.getController("Player 3").getText()))
                        if cp5.getController("Player 4").getText() != "":
                            playersList.append(classes.Player(cp5.getController("Player 4").getText()))
                        deleteAllComponents()
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects)
                        break
                    deleteAllComponents()
                    if x == "Cards" and scene == 0:
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects)
                        break
                    if x == "Leaderboards" and scene == 0:
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects)
                        break
                    if x == "Rules" and scene == 0:
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects)
                        break
                    if x == "End Game":
                        exit()
                        break
                    if x == "Vraag":
                        scene = 2
                        interactiveObjects = scenes.vraagScene(cp5, font, interactiveObjects)
                        break
                    if x == "Doom":
                        interactiveObject = scenes.doomScene(cp5, font, interactiveObjects)
                        scene = 5
                        break
                    if x == "Kans":
                        scene = 4
                        interactiveObject = scenes.kansScene(cp5, font, interactiveObjects)
                        break
                    if x == "Duel":
                        scene = 6
                        interactiveObjects = scenes.duelScene(cp5, font, interactiveObjects)
                        break
                    if x == "Verzenden" and scene == 2:
                        scene = 3
                        interactiveObjects = scenes.resultScene(cp5, font, interactiveObjects)
                        break
                    if x == "Verzenden" and scene == 4:
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects)
                        break
                    if x == "Verzenden" and scene == 5:
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects)
                        break
                    if x == "Verzenden" and scene == 3:
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects)
                        break
                    if x == "Verzenden" and scene == 7:
                        scene = 3
                        interactiveObjects = scenes.resultScene(cp5, font, interactiveObjects)
                        break
                    if x == "Terug" and scene == 2:
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects)
                        break
                    if x == "Terug" and scene == 6:
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects)
                        break
                    if x == "Terug" and scene == 7:
                        scene = 6
                        interactiveObjects = scenes.duelScene(cp5, font, interactiveObjects)
                        break
                    if x == "Player 1" or x == "Player 2" or x == "Player 3":
                        scene = 7
                        interactiveObjects = scenes.duelresultScene(cp5, font, interactiveObjects)
                        break
            except:
                pass
    except:
        pass      
def deleteAllComponents():
    global cp5
    for i in interactiveObjects:
        try:
            cp5.getController(i.getName()).remove()
            # if cp5.getController(i.getName()).get()
        except:
            pass
