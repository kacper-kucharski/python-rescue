def startEindgame(cp5, font, interactiveObjects, game):
    text('Eerste vraag', int(width * 0.10), int(height * 0.20))
    eersteKleur = color(19, 94, 70)
    tweedeKleur = color(71, 137, 102)
    interactiveObjects.append(cp5.addButton('antwoord 1').setPosition(int(width* 0.55 ), int(height* 0.10 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('input'))
    interactiveObjects.append(cp5.addButton('antwoord 2').setPosition(int(width* 0.55 ), int(height* 0.30 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('int'))
    interactiveObjects.append(cp5.addButton('antwoord 3').setPosition(int(width* 0.55 ), int(height* 0.50 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('str'))
    interactiveObjects.append(cp5.addButton('antwoord 4').setPosition(int(width* 0.55 ), int(height* 0.70 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('print'))
    interactiveObjects.append(cp5.addButton('Terug').setLabel('Geef beurt door!').setPosition(int(width * 0.00), int(height* 0.00)).setSize(int(width), int(height* 0.05 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur))
    return interactiveObjects
def tweedeEindvraag(cp5, font, interactiveObjects, game):
    text('Tweede vraag', int(width * 0.10), int(height * 0.20))
    eersteKleur = color(19, 94, 70)
    tweedeKleur = color(71, 137, 102)
    interactiveObjects.append(cp5.addButton('antwoord 5').setPosition(int(width* 0.55 ), int(height* 0.10 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('input'))
    interactiveObjects.append(cp5.addButton('antwoord 6').setPosition(int(width* 0.55 ), int(height* 0.30 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('int'))
    interactiveObjects.append(cp5.addButton('antwoord 7').setPosition(int(width* 0.55 ), int(height* 0.50 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('str'))
    interactiveObjects.append(cp5.addButton('antwoord 8').setPosition(int(width* 0.55 ), int(height* 0.70 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('print'))
    interactiveObjects.append(cp5.addButton('Terug').setLabel('Geef beurt door!').setPosition(int(width * 0.00), int(height* 0.00)).setSize(int(width), int(height* 0.05 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur))
    return interactiveObjects
def derdeEindvraag(cp5, font, interactiveObjects, game):
    text('Derde vraag', int(width * 0.10), int(height * 0.20))
    eersteKleur = color(19, 94, 70)
    tweedeKleur = color(71, 137, 102)
    interactiveObjects.append(cp5.addButton('antwoord 1').setPosition(int(width* 0.55 ), int(height* 0.10 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('input'))
    interactiveObjects.append(cp5.addButton('antwoord 2').setPosition(int(width* 0.55 ), int(height* 0.30 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('int'))
    interactiveObjects.append(cp5.addButton('antwoord 3').setPosition(int(width* 0.55 ), int(height* 0.50 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('str'))
    interactiveObjects.append(cp5.addButton('antwoord 4').setPosition(int(width* 0.55 ), int(height* 0.70 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('print'))
    interactiveObjects.append(cp5.addButton('Terug').setLabel('Geef beurt door!').setPosition(int(width * 0.00), int(height* 0.00)).setSize(int(width), int(height* 0.05 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur))
    return interactiveObjects
def vierdeEindvraag(cp5, font, interactiveObjects, game):
    text('Vierde vraag', int(width * 0.10), int(height * 0.20))
    eersteKleur = color(19, 94, 70)
    tweedeKleur = color(71, 137, 102)
    interactiveObjects.append(cp5.addButton('antwoord 5').setPosition(int(width* 0.55 ), int(height* 0.10 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('input'))
    interactiveObjects.append(cp5.addButton('antwoord 6').setPosition(int(width* 0.55 ), int(height* 0.30 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('int'))
    interactiveObjects.append(cp5.addButton('antwoord 7').setPosition(int(width* 0.55 ), int(height* 0.50 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('str'))
    interactiveObjects.append(cp5.addButton('antwoord 8').setPosition(int(width* 0.55 ), int(height* 0.70 )).setSize(int(width* 0.40 ), int(height* 0.15 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur).setLabel('print'))
    interactiveObjects.append(cp5.addButton('Terug').setLabel('Geef beurt door!').setPosition(int(width * 0.00), int(height* 0.00)).setSize(int(width), int(height* 0.05 )).setFont(font).setColorBackground(eersteKleur).setColorForeground(tweedeKleur))
    return interactiveObjects
