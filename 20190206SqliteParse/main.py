import sqlite3
import os

db_filename = 'leerplandoelen_db.sqlite3'

conn = sqlite3.connect(db_filename)
c = conn.cursor()

competenties = []
deelcompetenties = []
leerplandoelen = []
c.execute('DROP TABLE competentie;')
c.execute('DROP TABLE deelcompetentie;')
c.execute('DROP TABLE leerplandoel;')

c.execute('CREATE TABLE competentie(nummer INTEGER, omschrijving TEXT);')
c.execute('CREATE TABLE deelcompetentie(nummer INTEGER, competentie INTEGER, omschrijving TEXT);')
c.execute('CREATE TABLE leerplandoel(nummer INTEGER, omschrijving TEXT);')

with open('leerplandoelen_text.txt') as f:
    for line in f:
        if line.startswith('Competentie'):
            #Competenties
            competenties.append(line)
        elif line.startswith('Deelcompetentie'):
            #Deelcompetenties
            deelcompetenties.append(line)
        elif line[0].isdigit():
            #Leerplandoelen
            leerplandoelen.append(line)
        else:
            #lege regel
            pass

for competentie in competenties:
    #nummer
    print(competentie[12])
    nummer = competentie[12]

    #omschrijving
    print(competentie[16:])
    omschrijving = competentie[16:]

    c.execute(f'INSERT INTO competentie VALUES({nummer},"{omschrijving}");')
    conn.commit()

for deelcompetentie in deelcompetenties:
    #nummer
    print(deelcompetentie[16:19]) 
    nummer = deelcompetentie[16:19]

    #competentie
    print(deelcompetentie[16]) 
    competentie = deelcompetentie[16]

    #omschrijving
    print(deelcompetentie[23:])
    omschrijving = deelcompetentie[23:]

    c.execute(f'INSERT INTO deelcompetentie(nummer, competentie, omschrijving) VALUES({nummer},"{competentie}","{omschrijving}");')
    conn.commit()

for leerplandoel in leerplandoelen:
    #code
    print(leerplandoel[0:5])
    code = leerplandoel[0:5]

    #omschrijving
    print(leerplandoel[6:])
    omschrijving = leerplandoel[6:]

    c.execute(f'INSERT INTO leerplandoel(nummer, omschrijving) VALUES("{code}","{omschrijving}");')
    conn.commit()


