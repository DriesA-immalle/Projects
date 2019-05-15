import datetime

class Persoon:
    def __init__(self, achternaam, voornaam, geboortedatum = None):
        self.achternaam = achternaam
        self.voornaam = voornaam
        self.geboortedatum = geboortedatum

    def printPersoon(self):
        print("{} {} {}".format(self.achternaam, self.voornaam, self.geboortedatum))

    def __str__(self):
        persoon = "{} {} {}".format(self.achternaam, self.voornaam, self.geboortedatum)
        return persoon
        
    pass

p1 = Persoon("Janssens", "Joske")

p2 = Persoon("Peeters", "Willy", datetime.date(2001,10,10))

p1.printPersoon()
p2.printPersoon()

print(p1)
print(p2)

print(Persoon.__doc__)

print(Persoon.__dict__)
print(p1.__dict__)

# __dict__ is een dictionary die de symbol table bevat. __doc__ bevat de documentation string.

print(type(p1))
print(type(Persoon))
