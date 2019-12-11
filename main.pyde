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
    global savedPlayerName, interactiveObjects, cp5, font, doom, scene, game, duelPressed
    if keyCode == 9 and scene == 0:
        changeFocus()
    if scene == -1:
        background(200)
        deleteAllComponents()
        scene = 0
        interactiveObjects = scenes.playerNameScene(cp5, font, interactiveObjects)
        # print(cp5.getController("Player 1").getText())
    if key == "a" and scene == 7 and duelPressed == False:
        print(game.playersTurn.name)
        text(game.playersTurn.name + " was first! He can now answer the question.", int(width* 0.1 ), int(height* 0.5 ))
        duelPressed = True
    if key == "l" and scene == 7 and duelPressed == False:
        print(game.duelAgainst.name)
        text(game.duelAgainst.name + " was first! He can now answer the question.", int(width* 0.1 ), int(height* 0.5 ))
        duelPressed = True
def mousePressed():
    global cp5, scene, interactiveObjects, playersList, game, duelPressed
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
                        # If there are more than 1 player in the playerlist, it will initialize the game and go towards the main menu. 
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
                        deleteAllComponents()
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)
                        break
                    if x == "Leaderboards" and scene == 0:
                        deleteAllComponents()
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)
                        break
                    if x == "Rules" and scene == 0:
                        deleteAllComponents()
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)
                        break

                        exit()
                        break
                    if x == "Vraag":
                        deleteAllComponents()
                        scene = 2
                        interactiveObjects = scenes.vraagScene(cp5, font, interactiveObjects, game)
                        break
                    if x == "Doom":
                        deleteAllComponents()
                        interactiveObject = scenes.doomScene(cp5, font, interactiveObjects, game)
                        scene = 5
                        break
                    if x == "Kans":
                        deleteAllComponents()
                        scene = 4
                        interactiveObject = scenes.kansScene(cp5, font, interactiveObjects, game)
                        break
                    if x == "Duel":
                        deleteAllComponents()
                        scene = 6
                        interactiveObjects = scenes.duelScene(cp5, font, interactiveObjects, game)
                        break
                    if x == "Verzenden" and scene == 4 or scene == 5 or scene == 3:
                        deleteAllComponents()
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)
                        break
                    if x == "Verzenden" and scene == 7:
                        deleteAllComponents()
                        scene = 3
                        interactiveObjects = scenes.resultScene(cp5, font, interactiveObjects, game)
                        break
                    if x == "Verder" and scene == 8:
                        deleteAllComponents()
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)
                        break
                    if x == "Terug" and scene == 2 or scene == 6:
                        deleteAllComponents()
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)
                        break
                    if x == "Terug" and scene == 7:
                        deleteAllComponents()
                        scene = 6
                        interactiveObjects = scenes.duelScene(cp5, font, interactiveObjects, game)
                        break
                    if x == game.playersList[0].name:
                        deleteAllComponents()
                        scene = 7
                        game.duelAgainst = game.playersList[0]
                        interactiveObjects = scenes.duelQuestionScene(cp5, font, interactiveObjects, game)
                        break
                    if x == game.playersList[1].name:
                        deleteAllComponents()
                        scene = 7
                        duelPressed = False
                        game.duelAgainst = game.playersList[1]
                        interactiveObjects = scenes.duelQuestionScene(cp5, font, interactiveObjects, game)
                        break
                    if x == game.playersList[2].name:
                        deleteAllComponents()
                        scene = 7
                        duelPressed = False
                        game.duelAgainst = game.playersList[2]
                        interactiveObjects = scenes.duelQuestionScene(cp5, font, interactiveObjects, game)
                        break
                    if x == game.playersList[3].name:
                        deleteAllComponents()
                        scene = 7
                        duelPressed = False
                        game.duelAgainst = game.playersList[3]
                        interactiveObjects = scenes.duelQuestionScene(cp5, font, interactiveObjects, game)
                        break
                    if x == "Change turn":
                        deleteAllComponents()
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
