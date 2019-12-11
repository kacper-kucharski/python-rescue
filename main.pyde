import scenes
import classes
add_library('controlP5')

def changeFocus():
    global interactiveObjects, cp5
    textFields = []
    for i in interactiveObjects:
        if isinstance(i, Textfield):
            textFields.append(i)
    for i in range(len(textFields)):
        if textFields[i].isFocus():
            if i == 3:
                textFields[i].setFocus(False)
                textFields[0].setFocus(True)
                break
            textFields[i].setFocus(False)
            textFields[i+1].setFocus(True)
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
    game = 0
    interactiveObjects = scenes.titleScene(cp5, font, interactiveObjects)
    fullScreen()
    
def draw():
    pass
    
def keyPressed():
    global savedPlayerName, interactiveObjects, cp5, font, doom, scene, game
    if keyCode == 9 and scene == 0:
        changeFocus()
    if scene == -1:
        background(200)
        deleteAllComponents()
        scene = 0
        interactiveObjects = scenes.playerNameScene(cp5, font, interactiveObjects)
        # print(cp5.getController("Player 1").getText())
def mousePressed():
    global cp5, scene, interactiveObjects, playersList, game
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
                        same = 0
                        # check of input niet leeg is en maakt vervolgens een player object met de gegeven naam
                        if cp5.getController("Player 1").getText() != "":
                            playersList.append(classes.Player(cp5.getController("Player 1").getText()))
                        if cp5.getController("Player 2").getText() != "":
                            playersList.append(classes.Player(cp5.getController("Player 2").getText()))
                        if cp5.getController("Player 3").getText() != "":
                            playersList.append(classes.Player(cp5.getController("Player 3").getText()))
                        if cp5.getController("Player 4").getText() != "":
                            playersList.append(classes.Player(cp5.getController("Player 4").getText()))
                        # for i in playerList:
                        #     print(i.name)
                            # for y in playerList:
                            #     print(x.name,y.name)
                            #     if x.name == y.name:
                            #         same == 1
                            
                        if len(playersList) >= 2:
                            deleteAllComponents()
                            scene = 1
                            game = classes.Game(len(playersList), playersList)
                            interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)
                        elif same == 1:
                            playersList = []
                            text("Er moeten wel unieke namen ingevoerd worden.", width * 0.01, height/2)   
                        else:
                            playersList = []
                            text("Er moet wel meer dan 1 persoon ingevuld worden om het spel te beginnnen.", width * 0.01, height/2)    
                        break
                    deleteAllComponents()
                    if x == "Cards" and scene == 0:
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)
                        break
                    if x == "Leaderboards" and scene == 0:
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)
                        break
                    if x == "Rules" and scene == 0:
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)
                        break
                    if x == "End Game":
                        exit()
                        break
                    if x == "Vraag":
                        scene = 2
                        interactiveObjects = scenes.vraagScene(cp5, font, interactiveObjects, game)
                        break
                    if x == "Doom":
                        interactiveObject = scenes.doomScene(cp5, font, interactiveObjects, game)
                        scene = 5
                        break
                    if x == "Kans":
                        scene = 4
                        interactiveObject = scenes.kansScene(cp5, font, interactiveObjects, game)
                        break
                    if x == "Duel":
                        scene = 6
                        interactiveObjects = scenes.duelScene(cp5, font, interactiveObjects, game)
                        break
                    if x == "Verzenden" and scene == 4 or scene == 5 or scene == 3:
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)
                        break
                    if x == "Verzenden" and scene == 7:
                        scene = 3
                        interactiveObjects = scenes.resultScene(cp5, font, interactiveObjects, game)
                        break
                    if x == "Verder" and scene == 8:
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)
                        break
                    if x == "Terug" and scene == 2 or scene == 6:
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)
                        break
                    if x == "Terug" and scene == 7:
                        scene = 6
                        interactiveObjects = scenes.duelScene(cp5, font, interactiveObjects, game)
                        break
                    if x == "Player 1" or x == "Player 2" or x == "Player 3":
                        scene = 7
                        interactiveObjects = scenes.duelQuestionScene(cp5, font, interactiveObjects, game)
                        break
                    if x == "Change turn":
                        game.changePlayerTurn()
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)
                        break
                     # This checks if the awnser commited is right or wrong.
                    if scene == 2:
                    #compares string of the button with the string of the awnser
                        if str(x) == str(game.playersTurn.lastQuestion[6]):  
                            scene = 8
                            game.playersTurn.currentPoints += 1
                            game.changePlayerTurn()
                            interactiveObjects = scenes.resultSceneRight(cp5, font, interactiveObjects, game)
                        else:  
                            print('fout!')
                            scene = 8
                            game.changePlayerTurn()
                            interactiveObjects = scenes.resultSceneWrong(cp5, font, interactiveObjects, game)
                    
            except:
                print(sys.exc_info()[1])
                
    except:
        pass      
def deleteAllComponents():
    global cp5
    for i in interactiveObjects:
        try:
            # print(type(i))
            i.remove()
            # if type(i) == 'radioButton':
            #     i.removeItem('1')
        except:
            pass
