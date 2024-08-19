# Konditionen
Konditionen sind bedingungen die erfüllt (oder nicht erfüllt) werden müssen um den folgenden Code (nicht) auszuführen zu können.

Zum Beispiel: Falls es regnen aufhört dann kann ich laufen gehen. 
Oder Falls es regnet muss ich warten bis es nicht regnet bevor ich laufen gehen kann.

 In diesem Fall wurde der Code nicht ausgeführt weil die bedingung nicht erfüllt war.

### Beispiele: 
Falls ich müde bin dann gehe ich schlafen
    
    müde = True

    if müde == True:
        schlafen = True

Falls es zu warm ist kann man schwer arbeiten

    Hitze = True

    if Hitze == True:
        Arbeit = False

Falls ich nicht arbeite bekomme ich kein Geld

    if Arbeit == False:
        Geld = False

Falls ich kein Geld habe kann ich mir das essen nicht mehr leisten

    if Geld == False:
        Essen = False

Falls ich Krank bin dann gehe ich zum Arzt

    Krank = True

    if Krank == True:
        Arztbesuch = True



# Schleifen
Schleifen sind teile des Codes die für eine bestimmte (oder unendliche) länge ausgeführt werden sollte. 

Wie bei der Konditionen benötigen Schleifen eine bedingung.

Zum Beispiel: Trinke jede stunde 1 Liter Wasser bis man 4 Liter getrunken hat. In solchen beispiel ist die bedingung das Liter des Wassers den ich getrunken habe.

### Beispiele:

Runden laufen bis 5 Runden 

    runden = 0

    while runden != 5: 
        runden = runden + 1
    
        print (runden)

    print ("Alle", runden, "Runden geschafft!")

Arbeite jeden Tag bis 5 tage fertig sind dann gehe ich daheim

    ArbeitstageWoche = 5
    Tag = 2

    while Tag != ArbeitstageWoche:
        Tag = Tag + 1
        print (Tag)

    print ("Wieder nach hause gehen!")

Duschen bis man 30 mal in der Woche geduscht hat

    DuschenWoche = 30
    Geduscht = 2
    loop = True

    while loop == True:
        Geduscht = + 2
        print (Geduscht)
        if DuschenWoche == Geduscht:
            print ("Genug geduscht! Loopen aus!")
            loop == False

Falls das wetter gut ist dann gehe ich rad fahren bis das wetter wieder schlecht ist

    WetterGut = True
    RadFahren = False
    KM = 0

    if WetterGut == True:
        RadFahren = True
    elif WetterGut == False:
        RadFahren = False

    while WetterGut and RadFahren == True:
        KM = KM + 1
        print (KM)
        if KM == 30:
            WetterGut = False
            print ("Das Wetter ist plötzlich schlecht geworden! Ich konnte nur", KM, "Kilometer machen!")
        elif KM == 10:
            print ("Hoffentlich wird das wetter gut sein!")

Bandscheiben hinzufügen bis man 23 Bandscheiben hat

    Bandscheiben = 0

    while Bandscheiben != 23:
        Bandscheiben = + 1
        print (Bandscheiben)




# Funktionen
Funktionen sind stücke Code die später im Programm ausgeführt werden können um etwas zu tun. 

Zum Beispiel: Eine Tür absperren, dafür werde ich die "Funktion" "Tür absperren" benötigen und sperre dann die tür ab durch den "Code" in dieser "Funktion"

### Beispiele:

Jemanden begrüßen

    def Begrüßen():
        print ("Hallo!")
    
    Begrüßen():

Nach einigen runden laufen etwas Wasser trinken.

    runden = 0

    def trinken(flasche):
        print ("Trinken")

    while runden <= 10:
        runden = runden + 1
        print (runden)
        if runden == 10:
            trinken(flasche=5)

Einschlafen

    Schlafen = False

    def einschlafen():
        Schlafen = True
        print ("ZzZzZzZ...")

Das licht einschalten

    Licht = False

    def LichtEin():
        Licht = True
        print ("Jetzt kann ich was sehen!")
    
Etwas essen

    Essen = True

    def EtwasEssen():
        Essen = False





# Klassen
Klassen sind code die bestimmte Attribute für ein gewisses Objekt speichern. Man kann in Klassen auch mehr Code einbausen und so Programmieren.

Zum Beispiel: Eine Ente hat 2 Beine, kann schwimmen und fliegen und ist gerade am boden.

### Beispiele:

Eine Katze kann Miauen

    class Katze:
        def Miau():
            print ("Miau!")

Ein Hund kann Bellen

    class Hund:
        def Woof():
            print ("Woof!")

Ein Mensch mit 2 Beinen und 2 Arme der laufen kann, essen und sprechen kann, und hungrig ist.

    class Mensch:
        beine = 2
        laufen = True
        arme = 2
        hungrig = True
        def sprechen():
            print ("Hallo Welt!")
        def essen():
            hungrig = False

Bandscheiben sind gebrochen und ihre Anzahl wird gegeben. Der Status wird auch gegeben

    class Bandscheiben:
        Gebrochen = True
        Anzahl = 23
        Status = "könnten besser sein"

Der Computer ist eingeschaltet und kann programme ausführen und funktioniert

    class Computer:
        eingeschaltet = True
        funktioniert = True
        def ProgrammeAusführen():
            print ("Programme werden ausgeführt!")

# Objektorientiertes Programmieren
Objektorientiertes Programmieren (OOP) ist das Programmieren durch Objekte die durch den Befehl "class" erstellt wurde. 

Das ermöglicht die Organisation von Software in wiederverwendbare, modularisierte und skalierbare Einheiten.

Einige Konzepte des OOP sind: Die Vererbung und das Polymorphismus.

## Vererbung
Vererbung bedeutet das Klassen die Attribute und die Methoden von anderen "Basisklassen" übernehmen.

### Beispiel: 

Die Oberclasse "Tier" erstellt die Attribute "self.Name, self.sprechen...." die dann weiterverwendet werden um die attribute der Klasse "Katze" zu setzen. Die Attribute kann man dann selbst aufrufen von der Unterklasse.

    class Tier(): 
        def __init__(self, Name, sprechen, farbe)
            self.Name = Name
            self.sprechen = sprechen
            self.farbe = farbe
    
    class Katze():

    Katze_1 = Katze("Katze", "Miau!", "orange")
    print (Katze_1.farbe)

    class Bankkonto():
        def __init__(self, Saldo, Schulden)
            self.Saldo = Saldo
            self.Schulden = Schulden
    
    class MeinKonto():

    Kontostand = MeinKonto("5 Euro", "-5000 Euro")
    print (Kontostand.Schulden)

    class Computer():
        def __init__(self, eingeschaltet, leistung)
            self.eingeschaltet = eingeschaltet
            self.leistung = leistung

    class MeinPC():

    PC = MeinPC("True", "100%")
    print (PC.leistung)

## Polymorphismus
Polymorphismus ist die Fähigkeit, dass unterschiedliche Klassen Methoden mit demselben namen haben können.

### Beispiel:
Bei diesem Beispiel kann man noch mehr Tiere hinzufügen die die selben attribute haben als wie andere klassen ohne das sie mit sich selbst konflikte machen.

    class Tier:
        def __init__(self, Farbe)
            self.Farbe = Farbe
        
        def meine_Farbe(self):
            print ("Farbe:", self.Farbe)

    class Katze(Tier):
        def __init__(self, Farbe, Sprechen)
            super().__init__(Farbe)
            self.Sprechen = Sprechen
        
        def meine_Farbe_Sprechen(self):
            print (f"Farbe: {self.Farbe}, Sprechen: {self.Sprechen}")

    class Bank:
        def __init__(self, Stand)
            self.Stand = Stand
        
        def mein_Stand(self):
            print ("Stand:", self.Stand)

    class Konto(Bank):
        def __init__(self, Stand, Schulden)
            super().__init__(Stand)
            self.Schulden = Schulden
        
        def mein_Stand_Schulden(self):
            print (f"Kontostand: {self.Stand}, Schulden: {self.Schulden}")

    class Computer:
        def __init__(self, AN)
            self.AN = AN
        
        def mein_Status(self):
            print ("AN:", self.AN)

    class PC(Computer):
        def __init__(self, AN, Leistung)
            super().__init__(AN)
            self.Leistung = Leistung
        
        def mein_Status_Leistung(self):
            print (f"Status: {self.AN}, Leistung: {self.Leistung}")

