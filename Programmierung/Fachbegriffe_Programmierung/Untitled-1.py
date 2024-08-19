

buchstaben = "Aawawaw"

for x in buchstaben:
    print (x)

    

for x in "abcdefg":
    print (x)


Fahrzeug = ["Auto", "Moped", "Motorrad"]

for x in Fahrzeug:
    if x == "Motorrad":
        break
    print (x)


Fahrzeug = ["Auto", "Moped", "Motorrad"]

for x in Fahrzeug:
    if x == "Moped":
        continue # "Moped" wird nicht geprintet!
    print (x)


for x in range(10):
    print (x)
else:
    print ("Fertig!")

error = "string"

for x in error:
    pass #Schleife wird übersprungen


for x in range(6):
    print (x)


for x in range (1, 8, 2):
    print (x)

adjektiv = ["Rote", "Gelbe", "Grüner"]
Früchte = ["Erdbeere", "Birne", "Apfel"]

for x in adjektiv:
    for y in Früchte:
        print (x, y)

