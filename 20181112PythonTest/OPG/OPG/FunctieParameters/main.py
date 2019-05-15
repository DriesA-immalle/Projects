
def printHoofding(tekst, onderlijning, legeRegel=True):
    print(tekst)
    print(onderlijning * len(tekst))
    if legeRegel:
        print()

print(">>begin<<")
printHoofding("Hoofding 1", "=")
printHoofding("Hoofding 2", "~", False)
printHoofding("Hoofding3", "-", False)
print(">>einde<<")