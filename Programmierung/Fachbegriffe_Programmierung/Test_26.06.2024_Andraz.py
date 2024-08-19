# a

Seite1 = 5
Seite2 = 5

if Seite1 == Seite2:
    print ("Quadrat")
elif Seite1 != Seite2:
    print ("Rechteck")

# b

Elrike = 33725
Gunther = 88755
Friedeman = 43225

Namen = [Elrike, Gunther, Friedeman]

for x in Namen:
    if x >= 80001:
        print (x, "ist in der Steuerklasse: D")
    elif x >= 40001:
        print (x, "ist in der Steuerklasse: C")
    elif x >= 20001:
        print (x, "ist in der Steuerklasse: B")
    elif x <= 20000:
        print (x, "ist in der Steuerklasse: A") # funktioniert nicht so wie ich es wollte

