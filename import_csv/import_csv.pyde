import csv
import random

with open('Vraagkaarten.csv') as vraagKaarten:
    vraagKaarten = csv.reader(vraagKaarten, delimiter=',')
    list_questions = list(vraagKaarten)
randomVraag = list_questions[random.randint(0, len(list_questions)-1)]
vraag = (randomVraag[0])
vraag_antwoorden = (randomVraag[0], randomVraag[1], randomVraag[2], randomVraag[3], randomVraag[4])
antwoord1 = randomVraag[1]
antwoord2 = randomVraag[2]
antwoord3 = randomVraag[3]
antwoord4 = randomVraag[4]
antwoord = (randomVraag[6])
print(vraag)
\n
print(antwoord1)
print(antwoord2)

if antwoord3 == '':
    pass
else:
    print(antwoord3)
if antwoord4 == '':
    pass
else:
    print(antwoord4)

\n
print(antwoord)
    
    
