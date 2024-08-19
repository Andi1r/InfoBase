A = -4
B = 1
C = 0
D = -2
E = 3

if A <= B and B > C:
    print (A)
else:
    print (B)

if E > C or C > D:
    print (C)

if E >= B and C > D or A < B and B >= C:
    print (D)


if A < D and D > E:
    print (E)
    if A < C:
        print (C)
    else:
        if E > A:
            if A > D:
                if C > B:
                    print ("unmöglich")
                elif C < B:
                    print ("unmöglich x2")
            print (42)
            if A == 5 or C != 0:
                if  B > C or B > 4:
                    print ("gürk")
                else:
                    print ("Benjamin Bandscheibe")
            print ("Leberkas")
        print ("Käsleberkas")
    print ("Döner Kebab")
else:
    print ("es ist wurscht!")
