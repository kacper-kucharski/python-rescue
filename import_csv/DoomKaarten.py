import csv

with open('DoomKaarten.csv') as doomKaarten:
    doomKaarten = csv.reader(doomKaarten, delimiter=',')
    line_count = 0
    for row in doomKaarten:
        print(row[0])
        line_count += 1
print(line_count)
