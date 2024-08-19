def funktion1():
    print ("geht")

funktion1()

runden = 0

def trinken(flasche):
    print ("Trinken")

while runden <= 10:
    runden = runden + 1
    print (runden)
    if runden == 10:
        trinken(flasche=5)

def schlafen(geschlaft = 0):
    print (geschlaft, "geschlaft!")

Schlafen = True
Stunden = 0
Aufgewacht = True

while Schlafen == True:
    Stunden = Stunden + 0.25
    Aufgewacht = False
    print(Stunden)

    if Stunden in range(7, 9):
        schlafen(geschlaft = Stunden)
        Schlafen = False
        Aufgewacht = True
        print ("Gute", Stunden, "Stunden geschlaft!")

