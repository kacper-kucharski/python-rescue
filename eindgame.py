def startEindgame(cp5, font, interactiveObjects, game):
    text("Name = (1) ('Wat is jouw naam?: ')\nAge =(2) ((3) ' Hoe oud ben je?: '))\nYear = (4)((2019 -(5) )+100)\n\n\n\nprint((6) + ' zou 100 jaar zijn in het jaar '+(7) ", int(width * 0.01), int(height * 0.20))
    text('Vul nummer (1) in:', int(width * 0.01), int(height * 0.10))
    eersteKleur = color(19, 94, 70)
    tweedeKleur = color(71, 137, 102)
    interactiveObjects.append(cp5.addButton('antwoord 1').setPosition(int(width* 0.55 ), int(height* 0.10 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('input'))
    interactiveObjects.append(cp5.addButton('antwoord 2').setPosition(int(width* 0.55 ), int(height* 0.30 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('int'))
    interactiveObjects.append(cp5.addButton('antwoord 3').setPosition(int(width* 0.55 ), int(height* 0.50 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('str'))
    interactiveObjects.append(cp5.addButton('antwoord 4').setPosition(int(width* 0.55 ), int(height* 0.70 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('print'))
    interactiveObjects.append(cp5.addButton('Terug').setLabel('Geef beurt door!').setPosition(int(width * 0.00), int(height* 0.00)).setSize(int(width), int(height* 0.05 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur))
    return interactiveObjects
def tweedeEindvraag(cp5, font, interactiveObjects, game):
    text("Name = ("+ game.playersTurn.eindvraagAntwoorden[0] +") ('Wat is jouw naam?: ')\nAge =(2) ((3) ' Hoe oud ben je?: '))\nYear = (4)((2019 -(5) )+100)\n\n\n\nprint((6) + ' zou 100 jaar zijn in het jaar '+(7) ", int(width * 0.01), int(height * 0.20))
    text('Vul nummer (2) in:', int(width * 0.01), int(height * 0.10))
    eersteKleur = color(19, 94, 70)
    tweedeKleur = color(71, 137, 102)
    interactiveObjects.append(cp5.addButton('antwoord 1').setPosition(int(width* 0.55 ), int(height* 0.10 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('input'))
    interactiveObjects.append(cp5.addButton('antwoord 2').setPosition(int(width* 0.55 ), int(height* 0.30 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('int'))
    interactiveObjects.append(cp5.addButton('antwoord 3').setPosition(int(width* 0.55 ), int(height* 0.50 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('str'))
    interactiveObjects.append(cp5.addButton('antwoord 4').setPosition(int(width* 0.55 ), int(height* 0.70 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('print'))
    interactiveObjects.append(cp5.addButton('Terug').setLabel('Geef beurt door!').setPosition(int(width * 0.00), int(height* 0.00)).setSize(int(width), int(height* 0.05 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur))
    return interactiveObjects
def derdeEindvraag(cp5, font, interactiveObjects, game):
    text("Name = ("+ game.playersTurn.eindvraagAntwoorden[0] +") ('Wat is jouw naam?: ')\nAge =("+ game.playersTurn.eindvraagAntwoorden[1] +") ((3) ' Hoe oud ben je?: '))\nYear = (4)((2019 -(5) )+100)\n\n\n\nprint((6) + ' zou 100 jaar zijn in het jaar '+(7) ", int(width * 0.01), int(height * 0.20))
    text('Vul nummer (3) in:', int(width * 0.01), int(height * 0.10))
    eersteKleur = color(19, 94, 70)
    tweedeKleur = color(71, 137, 102)
    interactiveObjects.append(cp5.addButton('antwoord 1').setPosition(int(width* 0.55 ), int(height* 0.10 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('input'))
    interactiveObjects.append(cp5.addButton('antwoord 2').setPosition(int(width* 0.55 ), int(height* 0.30 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('int'))
    interactiveObjects.append(cp5.addButton('antwoord 3').setPosition(int(width* 0.55 ), int(height* 0.50 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('str'))
    interactiveObjects.append(cp5.addButton('antwoord 4').setPosition(int(width* 0.55 ), int(height* 0.70 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('print'))
    interactiveObjects.append(cp5.addButton('Terug').setLabel('Geef beurt door!').setPosition(int(width * 0.00), int(height* 0.00)).setSize(int(width), int(height* 0.05 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur))
    return interactiveObjects
def vierdeEindvraag(cp5, font, interactiveObjects, game):
    text("Name = ("+ game.playersTurn.eindvraagAntwoorden[0] +") ('Wat is jouw naam?: ')\nAge =("+ game.playersTurn.eindvraagAntwoorden[1] +") (("+ game.playersTurn.eindvraagAntwoorden[2] +") ' Hoe oud ben je?: '))\nYear = (4)((2019 -(5) )+100)\n\n\n\nprint((6) + ' zou 100 jaar zijn in het jaar '+(7) ", int(width * 0.01), int(height * 0.20))
    text('Vul nummer (4) in:', int(width * 0.01), int(height * 0.10))
    eersteKleur = color(19, 94, 70)
    tweedeKleur = color(71, 137, 102)
    interactiveObjects.append(cp5.addButton('antwoord 1').setPosition(int(width* 0.55 ), int(height* 0.10 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('input'))
    interactiveObjects.append(cp5.addButton('antwoord 2').setPosition(int(width* 0.55 ), int(height* 0.30 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('int'))
    interactiveObjects.append(cp5.addButton('antwoord 3').setPosition(int(width* 0.55 ), int(height* 0.50 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('str'))
    interactiveObjects.append(cp5.addButton('antwoord 4').setPosition(int(width* 0.55 ), int(height* 0.70 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('print'))
    interactiveObjects.append(cp5.addButton('Terug').setLabel('Geef beurt door!').setPosition(int(width * 0.00), int(height* 0.00)).setSize(int(width), int(height* 0.05 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur))
    return interactiveObjects
def vijfdeEindvraag(cp5, font, interactiveObjects, game):
    text("Name = ("+ game.playersTurn.eindvraagAntwoorden[0] +") ('Wat is jouw naam?: ')\nAge =("+ game.playersTurn.eindvraagAntwoorden[1] +") (("+ game.playersTurn.eindvraagAntwoorden[2] +") ' Hoe oud ben je?: '))\nYear = ("+game.playersTurn.eindvraagAntwoorden[3]+")((2019 -(5) )+100)\n\n\n\nprint((6) + ' zou 100 jaar zijn in het jaar '+(7) ", int(width * 0.01), int(height * 0.20))
    text('Vul nummer (5) in:', int(width * 0.01), int(height * 0.10))
    eersteKleur = color(19, 94, 70)
    tweedeKleur = color(71, 137, 102)
    interactiveObjects.append(cp5.addButton('antwoord 1').setPosition(int(width* 0.55 ), int(height* 0.10 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('name'))
    interactiveObjects.append(cp5.addButton('antwoord 2').setPosition(int(width* 0.55 ), int(height* 0.30 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('age'))
    interactiveObjects.append(cp5.addButton('antwoord 3').setPosition(int(width* 0.55 ), int(height* 0.50 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('year'))
    interactiveObjects.append(cp5.addButton('Terug').setLabel('Geef beurt door!').setPosition(int(width * 0.00), int(height* 0.00)).setSize(int(width), int(height* 0.05 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur))
    return interactiveObjects
def zesdeEindvraag(cp5, font, interactiveObjects, game):
    text("Name = ("+ game.playersTurn.eindvraagAntwoorden[0] +") ('Wat is jouw naam?: ')\nAge =("+ game.playersTurn.eindvraagAntwoorden[1] +") (("+ game.playersTurn.eindvraagAntwoorden[2] +") ' Hoe oud ben je?: '))\nYear = ("+game.playersTurn.eindvraagAntwoorden[3]+")((2019 -("+game.playersTurn.eindvraagAntwoorden[4]+") )+100)\n\n\n\nprint((6) + ' zou 100 jaar zijn in het jaar '+(7) ", int(width * 0.01), int(height * 0.20))
    text('Vul nummer (6) in:', int(width * 0.01), int(height * 0.10))
    eersteKleur = color(19, 94, 70)
    tweedeKleur = color(71, 137, 102)
    interactiveObjects.append(cp5.addButton('antwoord 1').setPosition(int(width* 0.55 ), int(height* 0.10 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('name'))
    interactiveObjects.append(cp5.addButton('antwoord 2').setPosition(int(width* 0.55 ), int(height* 0.30 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('age'))
    interactiveObjects.append(cp5.addButton('antwoord 3').setPosition(int(width* 0.55 ), int(height* 0.50 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('year'))
    interactiveObjects.append(cp5.addButton('Terug').setLabel('Geef beurt door!').setPosition(int(width * 0.00), int(height* 0.00)).setSize(int(width), int(height* 0.05 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur))
    return interactiveObjects
def zevendeEindvraag(cp5, font, interactiveObjects, game):
    text("Name = ("+ game.playersTurn.eindvraagAntwoorden[0] +") ('Wat is jouw naam?: ')\nAge =("+ game.playersTurn.eindvraagAntwoorden[1] +") (("+ game.playersTurn.eindvraagAntwoorden[2] +") ' Hoe oud ben je?: '))\nYear = ("+game.playersTurn.eindvraagAntwoorden[3]+")((2019 -("+game.playersTurn.eindvraagAntwoorden[4]+") )+100)\n\n\n\nprint(("+game.playersTurn.eindvraagAntwoorden[5]+") + ' zou 100 jaar zijn in het jaar '+(7) ", int(width * 0.01), int(height * 0.20))
    text('Vul nummer (7) in:', int(width * 0.01), int(height * 0.10))
    eersteKleur = color(19, 94, 70)
    tweedeKleur = color(71, 137, 102)
    interactiveObjects.append(cp5.addButton('antwoord 1').setPosition(int(width* 0.55 ), int(height* 0.10 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('name'))
    interactiveObjects.append(cp5.addButton('antwoord 2').setPosition(int(width* 0.55 ), int(height* 0.30 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('age'))
    interactiveObjects.append(cp5.addButton('antwoord 3').setPosition(int(width* 0.55 ), int(height* 0.50 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('year'))
    interactiveObjects.append(cp5.addButton('Terug').setLabel('Geef beurt door!').setPosition(int(width * 0.00), int(height* 0.00)).setSize(int(width), int(height* 0.05 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur))
    return interactiveObjects
def eindVraagResult(cp5, font, interactiveObjects, game):
    Fout = False
    for i in range(len(game.playersTurn.eindvraagAntwoorden)):
        if game.playersTurn.eindvraagAntwoorden[i] != game.eindvraagAntwoorden[i]:
            Fout = True
    if Fout:
        text('Fout!', int(width * 0.01), int(height * 0.10))
    else:
        text('Gefelicteerd, ' + game.playersTurn.name + ' je hebt gewonnen!', int(width * 0.01), int(height * 0.10))
    eersteKleur = color(19, 94, 70)
    tweedeKleur = color(71, 137, 102)
    interactiveObjects.append(cp5.addButton('Terug').setLabel('Geef beurt door!').setPosition(int(width * 0.00), int(height* 0.00)).setSize(int(width), int(height* 0.05 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur))
    return interactiveObjects
    
