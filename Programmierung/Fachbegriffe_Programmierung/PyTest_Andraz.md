Befehl              Tätigkeit
-------------------------------------------------------- # 1
1.                  Programmstart
2.                  Initialisiere a
3.                  Initialisiere b
4.                  Initialisiere c
5.                  Checke a, b und c, 
6.                      wenn a plus b größer c, dann gehe zu Befehl 11
7.                  oder,
8.                      wenn a plus c größer b, dann gehe zu Befehl 11
9.                  oder,
10.                     wenn b plus c größer a, dann gehe zu Befehl 11
11.                 gebe aus "gültig"
12.                 Programmende

Befehl              Tätigkeit
-------------------------------------------------------- # 2
1.                  Programmstart
2.                  Initialisiere Eingabe
3.                  Checke Eingabe,
4.                      wenn Eingabe Großbuchstabe, dann gebe aus "Großbuchstabe!"
5.                  oder,
6.                      wenn Eingabe Kleinbuchstabe, dann gebe aus "Kleinbuchstabe!"
7.                  oder,  
8.                      wenn Eingabe ist Nummer, dann gebe aus "Kein Buchstabe!"
9.                 Programmende

Befehl              Tätigkeit
-------------------------------------------------------- # 3
1.                  Programmstart
2.                  Initialisiere Flaschen
3.                  Initialisiere Geldwert
4.                  Initialisiere EuroFlaschen (0,15 €)
4.                  Checke Flaschen
5.                      wenn Flasche eingegeben, dann Geldwert ist gleich EuroFlaschen plus Geldwert
6.                  Funktion Taste_gedrückt
7.                      wenn Taste_gedrückt, dann Geldwert ausgeben und gehe zu Befehl 8
8.                 Programmende


Theoretische Fragen:

1. ( /3) Eine If-Schleife ist eine Kontrollstruktur, welche in vielen verschiedenen Programmiersprachen
verwendet wird.
Ja 
If schleifen sind Kontrollstrukturen die auch in anderen Programmiersprachen verwendet werden.

2. ( /3) Der Datentyp ’char’, also ’Character’, wird fur einzelne Buchstaben verwendet. Der Datentyp ¨
’str’, also ’String’ wird fur ganze Wörter verwendet.



3. ( /3) Eine Klasse kann direkt von mehreren anderen Klassen erben.


4. ( /3) In folgendem Code stehen Kommentare welche die Besetzung von ’a’ zu jedem Zeitpunkt zeigen.
Stimmen diese?

    a = 5                       # 1. a = 5
    def f(a = 7):               # 3. a = 7
        def g(a = 11):          # 4. a = 11
            print(a)            # 6. 11 wird ausgegeben
        g(a)                    # 5. Führe g mit a = 7 aus
    f(a)                        # 2. Führe g mit a = 5 aus




5. ( /3) Design patterns nutzt man im Kontext von Klassen. Fur Programme die lediglich Funktionen ¨
beinhalten sind Patterns unnotwendiger Overhead.

