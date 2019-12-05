if scene == 0:
            deleteAllComponents()
            interactiveObjects.append(cp5.addTextfield("Player 1").setPosition(int(width* 0.03 ), int(height* 0.05 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font))
            interactiveObjects.append(cp5.addTextfield("Player 2").setPosition(int(width* 0.16 ), int(height* 0.05 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font))
            interactiveObjects.append(cp5.addTextfield("Player 3").setPosition(int(width* 0.29 ), int(height* 0.05 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font))
            interactiveObjects.append(cp5.addTextfield("Player 4").setPosition(int(width* 0.42 ), int(height* 0.05 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font))
            interactiveObjects.append(cp5.addButton("Verder").setPosition(int(width* 0.45 ), int(height* 0.28 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font))
        if scene == 1:
            deleteAllComponents()
            interactiveObjects.append(cp5.addButton("Cards").setPosition(int(width* 0.03 ), int(height* 0.05 )).setSize(int(width* 0.05 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("Leaderboards").setPosition(int(width* 0.19 ), int(height* 0.05 )).setSize(int(width* 0.11 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("Rules").setPosition(int(width* 0.4 ), int(height* 0.05 )).setSize(int(width* 0.05 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("End Game").setPosition(int(width* 0.55 ), int(height* 0.05 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("Vraag").setPosition(int(width* 0.05 ), int(height* 0.24 )).setSize(int(width* 0.28 ), int(height* 0.18 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("Doom").setPosition(int(width* 0.34 ), int(height* 0.24 )).setSize(int(width* 0.28 ), int(height* 0.18 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("Kans").setPosition(int(width* 0.05 ), int(height* 0.51 )).setSize(int(width* 0.28 ), int(height* 0.18 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("Duel").setPosition(int(width* 0.34 ), int(height* 0.51 )).setSize(int(width* 0.28 ), int(height* 0.18 )).setFont(font).setColorBackground(color(255,0,0)))
        #Vraag
        if scene == 2:
            deleteAllComponents()
            text("Vraag", 53, 37)
            interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.52 ), int(height* 0.65 )).setSize(int(width* 0.11 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("Terug").setPosition(int(width* 0.56 ), int(height* 0.04 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
        #result
        if scene == 3:
            deleteAllComponents()
            text("Result", 400, 250)
            interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.05 ), int(height* 0.37 )).setSize(int(width* 0.05 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
        #Kans
        if scene == 4:
            deleteAllComponents()
            text("Kans", 48, 43)
            text("Go 3 stappen naar achter", 358, 317)
            interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.52 ), int(height* 0.65 )).setSize(int(width* 0.11 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
        #Doom
        if scene == 5:
            deleteAllComponents()
            interactiveObjects = doom.startScene(cp5, font, interactiveObjects)
        #Duel Start Screen
        if scene == 6:
            deleteAllComponents()
            text("Duel", 44, 20)
            interactiveObjects.append(cp5.addButton("Terug").setPosition(int(width* 0.56 ), int(height* 0.02 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
            text("VS WHO?", 141, 344)
            interactiveObjects.append(cp5.addButton("Player 1").setPosition(int(width* 0.25 ), int(height* 0.19 )).setSize(int(width* 0.17 ), int(height* 0.08 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("Player 2").setPosition(int(width* 0.25 ), int(height* 0.31 )).setSize(int(width* 0.17 ), int(height* 0.08 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("Player 3").setPosition(int(width* 0.25 ), int(height* 0.43 )).setSize(int(width* 0.17 ), int(height* 0.08 )).setFont(font).setColorBackground(color(255,0,0)))
       #Duel Fight
        if scene == 7:
            deleteAllComponents()
            text("Vraag", 53, 37)
            interactiveObjects.append(cp5.addButton("Verzenden").setPosition(int(width* 0.52 ), int(height* 0.65 )).setSize(int(width* 0.11 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
            interactiveObjects.append(cp5.addButton("Terug").setPosition(int(width* 0.56 ), int(height* 0.04 )).setSize(int(width* 0.08 ), int(height* 0.05 )).setFont(font).setColorBackground(color(255,0,0)))
