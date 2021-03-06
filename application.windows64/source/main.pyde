import scenes
import classes
import eindgame
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
    background(115, 167, 136)
    global playerName, savedPlayerName, interactiveObjects, cp5, font, scene, buttonNames, playersList, game, playerLevelList
    font = createFont("arial",30);
    scene = -1
    cp5 = ControlP5(this)
    interactiveObjects = []
    playersList = []
    playerLevelList = ["makkelijk", "makkelijk", "makkelijk", "makkelijk", 0, 0, 0, 0]
    game = 0
    interactiveObjects = scenes.titleScene(cp5, font, interactiveObjects)
    fullScreen()
    
def draw():
    global game
    pass
    
def keyPressed():
    global savedPlayerName, interactiveObjects, cp5, font, doom, scene, game, duelPressed, playerThatCanAnswer, vraag
    if keyCode == 9 and scene == 0:
        changeFocus()
    if scene == -1:
        background(115, 167, 136)
        deleteAllComponents()
        scene = 0
        interactiveObjects = scenes.playerNameScene(cp5, font, interactiveObjects)
        # print(cp5.getController("Player 1").getText())
    playerThatCanAnswer = None
    if key == "a" and scene == 7 and duelPressed == False:
        background(115, 167, 136)
        deleteAllComponents()
        font = createFont('arial', 20)
        textFont(font)
        text(str(vraag[0]), width * 0.02, height * 0.29)
        for i in range(1, 5):
            if vraag[i] != '':
                interactiveObjects.append(cp5.addButton(vraag[i]).setPosition(int(width* 0.10), int(height* 0.30+ 100 * i )).setSize(int(width* 0.80 ), int(height* 0.06 )).setFont(font).setColorBackground(color(131, 89, 73)).setColorActive(color(182, 123, 101)).setColorForeground(color(182, 123, 101)))
        text(game.playersTurn.name + " was als eerst! Je mag nu de vraag beantwoorden.", int(width* 0.1 ), int(height* 0.9 ))
        playerThatCanAnswer = game.playersTurn
        duelPressed = True
    if key == "l" and scene == 7 and duelPressed == False:
        background(115, 167, 136)
        deleteAllComponents()
        font = createFont('arial', 20)
        textFont(font)
        text(str(vraag[0]), width * 0.02, height * 0.29)
        for i in range(1, 5):
            if vraag[i] != '':
                interactiveObjects.append(cp5.addButton(vraag[i]).setPosition(int(width* 0.10), int(height* 0.30+ 100 * i )).setSize(int(width* 0.80 ), int(height* 0.06 )).setFont(font).setColorBackground(color(131, 89, 73)).setColorActive(color(182, 123, 101)).setColorForeground(color(182, 123, 101)))
        text(game.duelAgainst.name + " was als eerst! Je mag nu de vraag beantwoorden.", int(width* 0.1 ), int(height* 0.9 ))
        playerThatCanAnswer = game.duelAgainst
        duelPressed = True
def mousePressed():
    global cp5, scene, interactiveObjects, playersList, game, duelPressed, playerThatCanAnswer, vraag, playerLevelList
    try:
        for x in interactiveObjects:
            if scene == -1:
                background(115, 167, 136)
                deleteAllComponents()
                scene = 0
                interactiveObjects = scenes.playerNameScene(cp5, font, interactiveObjects) 
            try:
                if cp5.getController(x.getName()).isPressed():
                    background(115, 167, 136)
                    if x.getName() == "Eind Vraag" and scene == 1:
                        deleteAllComponents()
                        scene = 1000
                        interactiveObjects = eindgame.startEindgame(cp5, font, interactiveObjects, game)
                    if (x.getName() == "antwoord 1" or x.getName() == "antwoord 2" or x.getName() == "antwoord 3" or x.getName() == "antwoord 4") and scene == 1000:
                        game.playersTurn.eindvraagAntwoorden = []
                        deleteAllComponents()
                        scene = 1001
                        game.playersTurn.eindvraagAntwoorden.append(x.getLabel())
                        interactiveObjects = eindgame.tweedeEindvraag(cp5, font, interactiveObjects, game)
                    elif (x.getName() == "antwoord 1" or x.getName() == "antwoord 2" or x.getName() == "antwoord 3" or x.getName() == "antwoord 4") and scene == 1001:
                        deleteAllComponents()
                        scene = 1002
                        game.playersTurn.eindvraagAntwoorden.append(x.getLabel())
                        interactiveObjects = eindgame.derdeEindvraag(cp5, font, interactiveObjects, game)
                    elif (x.getName() == "antwoord 1" or x.getName() == "antwoord 2" or x.getName() == "antwoord 3" or x.getName() == "antwoord 4") and scene == 1002:
                        deleteAllComponents()
                        scene = 1003
                        game.playersTurn.eindvraagAntwoorden.append(x.getLabel())
                        interactiveObjects = eindgame.vierdeEindvraag(cp5, font, interactiveObjects, game)
                    elif (x.getName() == "antwoord 1" or x.getName() == "antwoord 2" or x.getName() == "antwoord 3" or x.getName() == "antwoord 4") and scene == 1003:
                        deleteAllComponents()
                        scene = 1004
                        game.playersTurn.eindvraagAntwoorden.append(x.getLabel())
                        interactiveObjects = eindgame.vijfdeEindvraag(cp5, font, interactiveObjects, game)
                    elif (x.getLabel() == "name" or x.getLabel() == "age" or x.getLabel() == "year") and scene == 1004:
                        deleteAllComponents()
                        scene = 1005
                        game.playersTurn.eindvraagAntwoorden.append(x.getLabel())
                        interactiveObjects = eindgame.zesdeEindvraag(cp5, font, interactiveObjects, game)
                    elif (x.getLabel() == "name" or x.getLabel() == "age" or x.getLabel() == "year") and scene == 1005:
                        deleteAllComponents()
                        scene = 1006
                        game.playersTurn.eindvraagAntwoorden.append(x.getLabel())
                        interactiveObjects = eindgame.zevendeEindvraag(cp5, font, interactiveObjects, game)
                    elif (x.getLabel() == "name" or x.getLabel() == "age" or x.getLabel() == "year") and scene == 1006:
                        deleteAllComponents()
                        scene = 1007
                        game.playersTurn.eindvraagAntwoorden.append(x.getLabel())
                        interactiveObjects = eindgame.eindVraagResult(cp5, font, interactiveObjects, game)
                    elif x.getName() == "Terug" and (scene == 1000 or scene == 1001 or scene == 1002 or scene == 1003 or scene == 1004 or scene == 1005 or scene == 1006 or scene == 1007):
                        game.changePlayerTurn()
                        deleteAllComponents()
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)
                    x = x.getName()
                    if x == "player1_easy" and scene == 0:
                        playerLevelList[0] = "makkelijk"
                        playerLevelList[4] = 0
                    if x == "player1_medium" and scene == 0:
                        playerLevelList[0] = "gemiddeld"
                        playerLevelList[4] = 5
                    if x == "player1_hard" and scene == 0:
                        playerLevelList[0] = "moeilijk"
                        playerLevelList[4] = 8
                        
                    if x == "player2_easy" and scene == 0:
                        playerLevelList[1] = "makkelijk"
                        playerLevelList[5] = 0
                    if x == "player2_medium" and scene == 0:
                        playerLevelList[1] = "gemiddeld"
                        playerLevelList[5] = 5
                    if x == "player2_hard" and scene == 0:
                        playerLevelList[1] = "moeilijk"
                        playerLevelList[5] = 8
                        
                    if x == "player3_easy" and scene == 0:
                        playerLevelList[2] = "makkelijk"
                        playerLevelList[6] = 0 
                    if x == "player3_medium" and scene == 0:
                        playerLevelList[2] = "gemiddeld"
                        playerLevelList[6] = 5
                    if x == "player3_hard" and scene == 0:
                        playerLevelList[2] = "moeilijk"
                        playerLevelList[6] = 8
                        
                    if x == "player4_easy" and scene == 0:
                        playerLevelList[3] = "makkelijk"
                        playerLevelList[7] = 0
                    if x == "player4_medium" and scene == 0:
                        playerLevelList[3] = "gemiddeld"
                        playerLevelList[7] = 5
                    if x == "player4_hard" and scene == 0:
                        playerLevelList[3] = "moeilijk"
                        playerLevelList[7] = 8
                        
                    # for i in range(len(playerslist)):
                    #     playersList[i].difficulty
                    #     if playersList[i].difficulty == 'makkelijk':
                    #         text('Makkelijk',width * 0.46,height * 0.28 + 0.20 * i)
                    #     if playersList[i].difficulty == 'gemiddeld':
                    #         text('Gemiddeld',width * 0.66,height * 0.28 + 0.20 * i)
                    #     if playersList[i].difficulty == 'moeilijk':
                    #         text('Moeilijk',width * 0.86,height * 0.28 + 0.20 * i)
                            
                    
                    if x == 'Begin Spel' and scene == 0:
                        same = 0
                        # check of input niet leeg is en maakt vervolgens een player object met de gegeven naam
                        playersList.append(classes.Player(cp5.getController("Speler 1").getText(), playerLevelList[0], playerLevelList[4]))
                        playersList.append(classes.Player(cp5.getController("Speler 2").getText(), playerLevelList[1], playerLevelList[5]))
                        playersList.append(classes.Player(cp5.getController("Speler 3").getText(), playerLevelList[2], playerLevelList[6]))
                        playersList.append(classes.Player(cp5.getController("Speler 4").getText(), playerLevelList[3], playerLevelList[7]))
                        checkList = []
                        for i in playersList:
                            if i.name != '':
                                checkList.append(i)
                        if same == 1:
                            playersList = []
                            text("Er moeten wel unieke namen ingevoerd worden.", width * 0.20, height * 0.16)
                            text(" Vul hier de namen van de spelers in.                  Geef hier je niveau aan.", width * 0.02, height* 0.09)
                        if len(checkList) >= 2:
                            deleteAllComponents()
                            scene = 1
                            print(playersList)
                            game = classes.Game(playersList)
                            print(game.playersList[0].name, game.playersList[0].difficulty)
                            print(game.playersList[1].name, game.playersList[1].difficulty)
                            print(game.playersList[2].name, game.playersList[2].difficulty)
                            print(game.playersList[3].name, game.playersList[3].difficulty)
                            interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)   
                        else:
                            playersList = []
                            text(" Er moet wel meer dan 1 speler naam \n ingevuld worden om het spel te beginnen.", width * 0.12, height * 0.90)
                            text(" Vul hier de namen van de spelers in.                  Geef hier je niveau aan.", width * 0.02, height* 0.09)    
                        break   
                    if game != 0:
                        print(game.playersTurn.eindvraagAntwoorden)
                    print(x, scene)              
           
                    if x == "Eindig Spel":
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
                    if x == "Pak een doomkaart!" and scene == 4:
                        deleteAllComponents()
                        interactiveObject = scenes.doomScene(cp5, font, interactiveObjects, game)
                        scene = 5
                        break
                    if x == "Duel":
                        deleteAllComponents()
                        scene = 6
                        interactiveObjects = scenes.duelScene(cp5, font, interactiveObjects, game)
                        break
                    if x == "Verzenden" and scene == 2:
                        deleteAllComponents()
                        scene = 3
                        interactiveObjects = scenes.resultScene(cp5, font, interactiveObjects, game)
                        break
                    if x == "Verzenden" and scene == 4:
                        deleteAllComponents()
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)
                        break
                    if x == "Verzenden" and scene == 5:
                        deleteAllComponents()
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)
                        break
                    if x == "Verzenden" and scene == 3:
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
                    if x == "Terug" and scene == 2:
                        deleteAllComponents()
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)
                        break
                    if x == "Terug" and scene == 6:
                        deleteAllComponents()
                        scene = 1
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)
                        break
                    if x == "Terug" and scene == 7:
                        deleteAllComponents()
                        scene = 6
                        interactiveObjects = scenes.duelScene(cp5, font, interactiveObjects, game)
                        break
                    if x == "Verder" and scene == 10:
                        deleteAllComponents()
                        scene = 7
                        interactiveObjects = scenes.duelQuestionScene(cp5, font, interactiveObjects, game)
                    if x == game.playersList[0].name:
                        deleteAllComponents()
                        vraag = game.getVraag()
                        scene = 7
                        duelPressed = False
                        game.duelAgainst = game.playersList[0]
                        interactiveObjects = scenes.duelQuestionScene(cp5, font, interactiveObjects, game, vraag)
                        break
                    if x == game.playersList[1].name:
                        deleteAllComponents()
                        vraag = game.getVraag()
                        scene = 7
                        duelPressed = False
                        game.duelAgainst = game.playersList[1]
                        interactiveObjects = scenes.duelQuestionScene(cp5, font, interactiveObjects, game, vraag)
                        break
                    if x == game.playersList[2].name:
                        deleteAllComponents()
                        vraag = game.getVraag()
                        scene = 7
                        duelPressed = False
                        game.duelAgainst = game.playersList[2]
                        interactiveObjects = scenes.duelQuestionScene(cp5, font, interactiveObjects, game, vraag)
                        break
                    if x == game.playersList[3].name:
                        deleteAllComponents()
                        vraag = game.getVraag()
                        scene = 7
                        duelPressed = False
                        game.duelAgainst = game.playersList[3]
                        interactiveObjects = scenes.duelQuestionScene(cp5, font, interactiveObjects, game, vraag)
                        break
                    if x == "Pak een doomkaart!" and scene == 9:
                        deleteAllComponents()
                        interactiveObject = scenes.doomScene(cp5, font, interactiveObjects, game)
                        scene = 5
                        break
                    if x == "Verder" and scene == 9:
                        deleteAllComponents()
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)
                        scene = 1
                        break
                    if x == "Verander beurt":
                        game.changePlayerTurn()
                        deleteAllComponents()
                        interactiveObjects = scenes.mainMenu(cp5, font, interactiveObjects, game)
                        break
                     # This checks if the awnser commited is right or wrong.
                    if scene == 2:
                        deleteAllComponents()
                    #compares string of the button with the string of the awnser
                        if str(x) == str(game.playersTurn.lastQuestion[6]):  
                            scene = 8
                            game.playersTurn.currentPoints += 1
                            game.playersTurn.Exp += 2
                            game.changePlayerTurn()
                            interactiveObjects = scenes.vraagResultSceneRight(cp5, font, interactiveObjects, game)
                        else:  
                            scene = 8
                            game.changePlayerTurn()
                            game.playersTurn.Exp -= 1
                            interactiveObjects = scenes.vraagResultSceneWrong(cp5, font, interactiveObjects, game)
                           
                    if scene == 7:
                        deleteAllComponents()
                    #compares string of the button with the string of the awnser
                        if str(x) == str(game.playersTurn.lastQuestion[6]) and duelPressed:  
                            scene = 9
                            # Als aanvaller correct de vraag beantwoord.
                            if playerThatCanAnswer == game.playersTurn:
                                if  game.duelAgainst.currentPoints > 0:
                                    game.duelAgainst.currentPoints -= 1
                                game.changePlayerTurn()
                            interactiveObjects = scenes.duelResultSceneRight(cp5, font, interactiveObjects, game, playerThatCanAnswer)
                        else:  
                            scene = 9
                            # Als verdediger fout de vraag beantwoord.
                            if playerThatCanAnswer == game.duelAgainst:
                                if  game.duelAgainst.currentPoints > 0:
                                    game.duelAgainst.currentPoints -= 1
                                game.changePlayerTurn()
                            interactiveObjects = scenes.duelResultSceneWrong(cp5, font, interactiveObjects, game, playerThatCanAnswer) 
                    
                    if scene == 0:
                        text(" Vul hier de namen van de spelers in.                  Geef hier je niveau aan.", width * 0.02, height* 0.09)
            except:
                print(sys.exc_info()[1])
                
    except:
        pass     
def deleteAllComponents():
    global cp5
    for i in interactiveObjects:
        try:
            i.remove()
            # if type(i) == 'radioButton':
            #     i.removeItem('1')
        except:
            pass
