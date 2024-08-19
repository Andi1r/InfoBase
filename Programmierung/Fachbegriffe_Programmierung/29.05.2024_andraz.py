# 10. Lese und interpretiere die folgenden Python-Code Snippets. Erkläre Schritt für Schritt was passiert. 
# Beispiel 1.: Zahlen
v = 3.141 	# Die Variable „v“ hat nun den Wert „3.141“
w = 5 		# Die Variable „w“ hat nun den Wert „5“
x = 9j+2		 # Die Variable „x“ hat nun den Wert „9j+2“
z = 33E4 	# Die Variable „z“ hat nun den Wert „33E4“
y =-8.6e100	 # Die Variable „y“ hat nun den Wert „-8.6e100“
print(v, type(v)) # Printet den Wert der Variable und den Datentyp des Wertes.
print(w, type(w)) # Printet den Wert der Variable und den Datentyp des Wertes.
print(x, type(x)) # Printet den Wert der Variable und den Datentyp des Wertes.
print(y, type(y)) # Printet den Wert der Variable und den Datentyp des Wertes.
print(z, type(z)) # Printet den Wert der Variable und den Datentyp des Wertes.

# Beispiel 2.: Listen & Strings 
a = ’Apfel’ 			# gibt der Variable eine String an
b = (’Birne’), (’Banane’)		 # gibt der Variable mehrere Strings an
c = ["Schinken", "Salami"]	 # gibt der Variable mehrere Strings an
d = { 1: ["Pizza"], 2:("Bier", ’Wein’) }	# gibt der Variable mehrere Strings an
e = { 1: {a: (’Apfel’)}, 2: [’Spar‘, ’Billa’, "Penny Markt"]}	# gibt der Variable mehrere Strings an
print(a, type(a)) # Printet den Wert der Variable und den Datentyp des Wertes.
print(b, type(b)) # Printet den Wert der Variable und den Datentyp des Wertes.
print(c, type(c)) # Printet den Wert der Variable und den Datentyp des Wertes.
print(d, type(d)) # Printet den Wert der Variable und den Datentyp des Wertes.
print(e, type(e)) # Printet den Wert der Variable und den Datentyp des Wertes.

# 11. Für folgende Code-Snippets, welche Operationen sind zulässig, und welche nicht? Repariere unzulässige Operationen mit neuem Code, sodass das gesuchte Wort ausgegeben wird.

# 11. Beispiel 1

g = 65		# gibt der Variable eine String an
h = 77.77	# gibt der Variable eine String an
i = "Z" 	# gibt der Variable eine String an
j = "Hallo!"	# gibt der Variable eine String an
print(g, float(g), chr(g)) # printet und funktioniert
print(h, float(h), chr(h)) # float kann nicht als int dargestellt werden, abgeändert auf float
print(i) # string kann nicht als int oder float dargestellt werden
print(j) # string kann nicht als int oder float dargestellt werden


# 11. Beispiel 2


# Beispiel 2.: Datenselektion
f = {’Kern’: [’Marille’, 3515], 3: [42, ’Pflaume’]} 
e = {1: {a: (’Apfel’)}, 2: [’Spar’, ’Billa’, ’Penny Markt’]}
g = (’Semmel’, (’Brot’, ’Toast’))
h = [[’Hallo’, ’Welt’], [[’Schlange’, ’Python’], [’Assembler’, (’Java’, ’C++’)]]] 
# Select and print: ’Semmel’
print(g[0][0]) 
# Select and print: ’Billa’ 
print(e[2][1]) 
# Select and print: 3515 
print(f[’Kern’][1]) 
# Select and print: ’Pflaume’ 
print(f[’Kern’][’Pflaume’])
# Select and print: ’Java’ 
print(h[1][1][0])

# 12. Zu folgenden Problemstellungen, nutze jeweils ein Set, eine Liste und ein Dictionary zur Lösung des Problemes und beschreibe ihre Unterschiede.
# Schreibe anschließend Python-Programme und befülle die Daten mit fiktiven Werten.



# (a) Wir bauen ein Register das Organisationen speichern soll, mit den Einträgen ’Identifikationsnummer’,
# ’Eigentümer’, ’Adresse’, ’Gewerbenummer’ und ’Steuernummer’.



# (b) Man benötigt ein Register der Organisationen zu deren Webauftritten.
# Hierzu nutzt man die Einträge ’Idenfitikationsnummer’ und ’Homepage’.



# (c) Zur Homepage einzelner Organisationen soll man E-Mailadressen indexieren.
# Hierfür verwenden wir die Einträge ’Homepage’ mit einer Liste von eMails variable Länge.



# (d) Zur schnellen Ermittlung finanzieller Anfragen werden ’Steuernummer’ und ’eMail’ gebraucht.
# Diese Daten ändern sich höchstens einmal alle 5 Jahre.



# 13. Was sind Operatoren?

#(a) Schreibe ein Pythonprogramm, welches die arithmetischen Operatoren ’plus’,’minus’,’mal’, ’dividiert’,
# ’modulo’, ’potenzieren’ nutzt. Welche Präzedenz (i.e. Reihenfolge) haben diese Operatoren?

AB = 5
AB + 2
AB - 2
AB * 2
AB / 2
AB ^ 2
AB % 2


#(b) Schreibe ein Pythonprogramm, welches die bitweisen Operatoren ’And’, ’Or’, ’Xor’, ’Shift-left’,
#’Shift-right’, ’Not’ implementiert. Recherchiere kurz wie man diese Operatoren sinngebend nutzen
#kann (z.B. Xor-Swap, Multiplikation/Division mit 2, ...).

BA = 0101


#(c) Schreibe ein Pythonprogramm, das logische Operatoren nutzt. Erkl¨ are f¨ ur die folgenden print
#statements was f¨ ur Werte und Typen ausgegeben wird. Beschreibe die Statements in Umgangssprache.

print([] is not True), print("" == False), print("False" == True),

print(0 != True), print(’0’ != False), print("a" == ’a’),

print(not ((not 5 >= 5) < 2)), print(’a’ in "Hallo!"),

print(int(3) == str(3)), print(int(3) == float(3.00))
