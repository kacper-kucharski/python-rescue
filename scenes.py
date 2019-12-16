# scene = -1
def titleScene(cp5, font, interactiveObjects):
    # image(loadImage('../assets/titlePicture.jpg'),0,0,width,height)
    font = createFont('arial', 350)
    textFont(font)
    text("PYTHON ", width * 0.02, height* 0.30)
    text("RESCUE.", width * 0.02, height* 0.60)
    font = createFont('arial', 50)
    textFont(font)
    text("Gemaakt door John Klees, Kacper Kucharski, Reynethan Leon en Dominique Mahu", width * 0.02, height* 0.75 )
    text("Druk ergens om verder te gaan!", width * 0.02, height* 0.92 )
    interactiveObjects.append(cp5.addButton("Verder").setPosition(width + 100,width+ 100).setSize(int(width* 0.11 ), int(height* 0.05 )).setFont(font))
    return interactiveObjects
# scene = 0
def playerNameScene(cp5, font, interactiveObjects):
    font = createFont('arial', 40)
    text(" Vul hier de namen van de spelers in \n en start het spel. Veel plezier!", width * 0.45, height* 0.36)
    interactiveObjects.append(cp5.addTextfield("Speler 1").setPosition(int(width* 0.02 ), int(height* 0.14 )).setSize(int(width* 0.41 ), int(height* 0.09 )).setFont(font).setColorBackground(color(131, 89, 73)))
    interactiveObjects.append(cp5.addTextfield("Speler 2").setPosition(int(width* 0.02 ), int(height* 0.34 )).setSize(int(width* 0.41 ), int(height* 0.09 )).setFont(font).setColorBackground(color(131, 89, 73)))
    interactiveObjects.append(cp5.addTextfield("Speler 3").setPosition(int(width* 0.02 ), int(height* 0.55 )).setSize(int(width* 0.41 ), int(height* 0.09 )).setFont(font).setColorBackground(color(131, 89, 73)))
    interactiveObjects.append(cp5.addTextfield("Speler 4").setPosition(int(width* 0.02 ), int(height* 0.75 )).setSize(int(width* 0.41 ), int(height* 0.09 )).setFont(font).setColorBackground(color(131, 89, 73)))
    interactiveObjects.append(cp5.addButton("Begin Spel").setPosition(int(width* 0.62 ), int(height* 0.76)).setSize(int(width* 0.27 ), int(height* 0.12 )).setFont(font).setColorBackground(color(131, 89, 73)).setColorActive(color(182, 123, 101))
                              .setColorForeground(color(182, 123, 101)))
   # .setColorActive(color(182, 123, 101)).setColorForeground(color(182, 123, 101))
   # .setColorActive(color(255, 0, 0)).setColorForeground(color(255, 0, 0)))
    return interactiveObjects
# scene = 1
def mainMenu(cp5, font, interactiveObjects, game):
    text("Aan de beurt: " + str(game.playersTurn.name), width * 0.05, height * 0.15)
    text("Aantal punten: " + str(game.playersTurn.currentPoints), width * 0.05, height * 0.20)   
    interactiveObjects.append(cp5.addButton("Verander beurt").setPosition(int(width* 0.79 ), int(height* 0.12 )).setSize(int(width* 0.15 ), int(height* 0.07 )).setFont(font).setColorBackground(color(131, 89, 73)).setColorActive(color(182, 123, 101)).setColorForeground(color(182, 123, 101)))
    interactiveObjects.append(cp5.addTextlabel("Kaarten").setPosition(int(width* 0.03 ), int(height* 0.05 )).setSize(int(width* 0.05 ), int(height* 0.05 )).setFont(font).setColorBackground(color(131, 89, 73)).setColorActive(color(182, 123, 101)).setColorForeground(color(182, 123, 101)))
    interactiveObjects.append(cp5.addButton("Eindig Spel").setPosition(int(width* 0.79 ), int(height* 0.03 )).setSize(int(width* 0.12 ), int(height* 0.07 )).setFont(font).setColorBackground(color(19, 94, 70)).setColorActive(color(71, 137, 102)).setColorForeground(color(71, 137, 102)))
    font = createFont("arial",150);
    
    if game.playersTurn.currentPoints == game.maxPoints:
        font = createFont("arial",100);
        pass
        font = createFont("arial",120);
        interactiveObjects.append(cp5.addButton("Eind Vraag").setPosition(int(width* 0.05 ), int(height* 0.24 )).setSize(int(width* 0.41 ), int(height* 0.24 )).setFont(font).setColorBackground(color(131, 89, 73)).setColorActive(color(182, 123, 101)).setColorForeground(color(182, 123, 101)))
    else:
        font = createFont("arial",150);
        interactiveObjects.append(cp5.addButton("Vraag").setPosition(int(width* 0.05 ), int(height* 0.24 )).setSize(int(width* 0.41 ), int(height* 0.24 )).setFont(font).setColorBackground(color(131, 89, 73)).setColorForeground(color(182, 123, 101)))
    font = createFont("arial",150);
    interactiveObjects.append(cp5.addButton("Doom").setPosition(int(width* 0.53 ), int(height* 0.24 )).setSize(int(width* 0.41 ), int(height* 0.24 )).setFont(font).setColorBackground(color(131, 89, 73)).setColorActive(color(182, 123, 101)).setColorForeground(color(182, 123, 101)))
    interactiveObjects.append(cp5.addButton("Kans").setPosition(int(width* 0.05 ), int(height* 0.60 )).setSize(int(width* 0.41 ), int(height* 0.24 )).setFont(font).setColorBackground(color(131, 89, 73)).setColorActive(color(182, 123, 101)).setColorForeground(color(182, 123, 101)))
    interactiveObjects.append(cp5.addButton("Duel").setPosition(int(width* 0.53 ), int(height* 0.60 )).setSize(int(width* 0.41 ), int(height* 0.24 )).setFont(font).setColorBackground(color(131, 89, 73)).setColorActive(color(182, 123, 101)).setColorForeground(color(182, 123, 101)))
    return interactiveObjects
# scene = 2
def vraagScene(cp5, font, interactiveObjects, game):
    vraag = game.getVraag()
    text(str(vraag[0]), width * 0.02, height * 0.29)
    for i in range(1, 5):
        if vraag[i] != '':
            interactiveObjects.append(cp5.addButton(vraag[i]).setPosition(int(width* 0.10), int(height* 0.30+ 100 * i )).setSize(int(width* 0.80 ), int(height* 0.06 )).setFont(font).setColorBackground(color(131, 89, 73)).setColorActive(color(182, 123, 101)).setColorForeground(color(182, 123, 101)))
    interactiveObjects.append(cp5.addButton("Terug").setPosition(int(width* 0.74 ), int(height* 0.05 )).setSize(int(width* 0.11 ), int(height* 0.06 )).setFont(font).setColorBackground(color(131, 89, 73)).setColorActive(color(182, 123, 101)).setColorForeground(color(182, 123, 101)))
    return interactiveObjects
# scene = 5
def doomScene(cp5, font, interactiveObjects, game):
    doom = str(game.getDoom())
    font = createFont('arial', 50)
    if doom == "Sla twee beurten over":
        game.playersTurn.skipTurn += 2
    if doom == "Sla een beurt over":
        game.playersTurn.skipTurn += 1
    if doom == "leg een van jouw munten terug":
        if  game.playersTurn.currentPoints > 0:
            game.playersTurn.currentPoints -= 1
    text("" + doom, int(width* 0.09 ), int(height* 0.3 ))
    interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.77 ), int(height* 0.86 )).setSize(int(width* 0.18 ), int(height* 0.08 )).setFont(font).setColorBackground(color(131, 89, 73)).setColorActive(color(182, 123, 101)).setColorForeground(color(182, 123, 101)))
    game.changePlayerTurn()
    return interactiveObjects
# scene = 4
def kansScene(cp5, font, interactiveObjects, game):
    kans = str(game.getKans())
    font = createFont('arial', 50)
    if kans == "Sla een beurt over":
        game.playersTurn.skipTurn = 1
    if kans == "Pak een doom kaart":
        interactiveObjects.append(cp5.addButton("Pak een doomkaart!").setPosition(int(width* 0.52 ), int(height* 0.65 )).setSize(int(width* 0.30 ), int(height* 0.05 )).setFont(font).setColorBackground(color(131, 89, 73)).setColorActive(color(182, 123, 101)).setColorForeground(color(182, 123, 101)))
    else:
        interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.77 ), int(height* 0.86 )).setSize(int(width* 0.18 ), int(height* 0.08 )).setFont(font).setColorBackground(color(131, 89, 73)).setColorActive(color(182, 123, 101)).setColorForeground(color(182, 123, 101)))        
    text(kans, int(width* 0.09 ), int(height* 0.3 ))
    game.changePlayerTurn()
    
    return interactiveObjects
# scene = 6
def duelScene(cp5, font, interactiveObjects, game):
    text("Duel", int(width* 0.05 ), int(height* 0.05 ))
    interactiveObjects.append(cp5.addButton("Terug").setPosition(int(width* 0.74 ), int(height* 0.05 )).setSize(int(width* 0.11 ), int(height* 0.06 )).setFont(font).setColorBackground(color(131, 89, 73)).setColorActive(color(182, 123, 101)).setColorForeground(color(182, 123, 101)))
    text("Tegen wie?", int(width* 0.07 ), int(height* 0.32 ))
    buttonHeight = [height* 0.19, height* 0.31, height* 0.43]
    _players = []
    for x in game.playersList:
        if x.name != game.playersTurn.name and x.name != "":
            _players.append(x)
    for x in range(len(_players)):
        print(_players[x].name)
        interactiveObjects.append(cp5.addButton(str(_players[x].name)).setPosition(int(width* 0.25 ), int(buttonHeight[x])).setSize(int(width* 0.17 ), int(height* 0.08 )).setFont(font).setColorBackground(color(131, 89, 73)))
    return interactiveObjects
# scene = 3
def vraagResultSceneRight(cp5, font, interactiveObjects, game):
    text("Goed!", 400, 250)
    interactiveObjects.append(cp5.addButton("Verder").setPosition(int(width* 0.07 ), int(height* 0.44 )).setSize(int(width* 0.07 ), int(height* 0.06 )).setFont(font).setColorBackground(color(131, 89, 73)))
    return interactiveObjects
def vraagResultSceneWrong(cp5, font, interactiveObjects, game):
    text("Fout!", 400, 250)
    interactiveObjects.append(cp5.addButton("Verder").setPosition(int(width* 0.07 ), int(height* 0.44 )).setSize(int(width* 0.07 ), int(height* 0.06 )).setFont(font).setColorBackground(color(131, 89, 73)))
    return interactiveObjects

# 9
def duelResultSceneRight(cp5, font, interactiveObjects, game, playerThatCanAnswer):
    text("Goed!", 400, 250)
    # Als verdediger the vraag goed beantwoord.
    if playerThatCanAnswer == game.duelAgainst:
        interactiveObjects.append(cp5.addButton("Pak een doomkaart!").setPosition(int(width* 0.52 ), int(height* 0.65 )).setSize(int(width* 0.30 ), int(height* 0.05 )).setFont(font).setColorBackground(color(131, 89, 73)).setColorActive(color(182, 123, 101)).setColorForeground(color(182, 123, 101)))
    else:
        interactiveObjects.append(cp5.addButton("Verder").setPosition(int(width* 0.07 ), int(height* 0.44 )).setSize(int(width* 0.07 ), int(height* 0.06 )).setFont(font).setColorBackground(color(131, 89, 73)).setColorActive(color(182, 123, 101)).setColorForeground(color(182, 123, 101)))
    return interactiveObjects
def duelResultSceneWrong(cp5, font, interactiveObjects, game, playerThatCanAnswer):
    text("Fout!", 400, 250)
    print(playerThatCanAnswer.name)
    # print(game.playersTurn.name)
    # Als verdediger verkeerd beantwordt
    if playerThatCanAnswer == game.duelAgainst:
        interactiveObjects.append(cp5.addButton("Verder").setPosition(int(width* 0.07 ), int(height* 0.44 )).setSize(int(width* 0.07 ), int(height* 0.06 )).setFont(font).setColorBackground(color(131, 89, 73)))
    else:
        interactiveObjects.append(cp5.addButton("Pak een doomkaart!").setPosition(int(width* 0.52 ), int(height* 0.65 )).setSize(int(width* 0.30 ), int(height* 0.05 )).setFont(font).setColorBackground(color(131, 89, 73)).setColorActive(color(182, 123, 101)).setColorForeground(color(182, 123, 101)))
    return interactiveObjects
# scene = 7
def duelQuestionScene(cp5, font, interactiveObjects, game, vraag):
    # text("Vraag", int(width* 0.03 ), int(height* 0.03 ))
    # text("Je speelt tegen " + game.duelAgainst.name, int(width* 0.03 ), int(height* 0.30 ))
    text(str(vraag[0]), width * 0.02, height * 0.29)
    text("Speler: " + game.playersTurn.name + " moet A drukken!", width * 0.02, height * 0.90)
    text("Speler: " + game.duelAgainst.name + " moet L drukken!", width * 0.5, height * 0.90)
    for i in range(1, 5):
        if vraag[i] != '':
            text(str(i) + ". " + vraag[i], width* 0.10, height* 0.30+ 100 * i )
    interactiveObjects.append(cp5.addButton("Terug").setPosition(int(width* 0.74 ), int(height* 0.05 )).setSize(int(width* 0.11 ), int(height* 0.06 )).setFont(font).setColorBackground(color(255,0,0)))
    return interactiveObjects
