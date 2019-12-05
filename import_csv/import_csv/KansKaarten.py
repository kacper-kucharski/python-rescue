import csv

with open('kansKaarten.csv') as kansKaarten:
    kansKaarten = csv.reader(kansKaarten, delimiter=',')
    line_count = 0
    for row in kansKaarten:
        print(row[0])
        line_count += 1
print(line_count)
