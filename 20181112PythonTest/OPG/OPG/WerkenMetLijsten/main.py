def printHoofding(tekst):
    print(tekst)
    print('=' * len(tekst))

getallen = [2,5,7,11]
woorden = ["bocht", "vier", "trefbal"]

printHoofding("Lengtes afdrukken")
print(len(getallen))
print(len(woorden))

printHoofding("Het dubbel van elk getal afdrukken")
for getal in getallen:
    print("Het dubbel van {} is {}".format(getal, getal*2))

printHoofding("Alle woorden in hoofdletters")
for woord in woorden:
    print(woord.upper())

printHoofding("Verwijderen van een element")
print(getallen)
print(woorden)
getallen.remove(7)
woorden.remove("trefbal")
print(getallen)
print(woorden)
