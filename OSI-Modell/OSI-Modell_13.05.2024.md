# OSI-Modell (2.Schicht) (13/05/2024)

##	Erkläre die Aufgabe der zweiten OSI-Schicht!

Die zweite OSI-Schicht hat die Aufgabe die Kommunikation zwischen zwei informationsverarbeitenden Systemen (Computersysteme), die über ein Übertragungsmedium verbunden sind, ermöglichen. Sie ist auch zuständig für die physikalische Adressierung (MAC-Adressen) der Geräte.
Die Aufgaben der Schicht werden von mehreren Protokollen ausgeführt.

##	Welche 2 Sublayer gibt es auf der zweiten OSI-Schicht?

Das sind die: Das MAC-Sublayer, die regelt wie ein gemeinsam genutztes Übertragungsmittel reibungslos genutzt wird, und das LLC-Sublayer, die für die logische Verbindung zwischen zwei Kommunikationsteilnehmern zuständig ist.

##	Was ist die Aufgabe des MAC-Sublayers?

Das MAC-Sublayer (Media Access Control) ist für die Aufgaben zuständig, die näher am physikalischen Übertragungsmedium liegen. 

Die Aufgabe des MAC-Sublayer ist, zu regeln wie, Computersystemen auf einen gemeinsam genutztes Übertragungsmedium, zugreifen. 
Es erkennt und gar ganz verhindert Kollisionen von Datenpaketen. Das wird durch verschiedenen Zugriffsverfahren geregelt.

## Was ist die Aufgabe des LLC-Sublayers?

Das LLC-Sublayer (Logical Link Control) ist für Aufgaben zuständig die näher an der Vermittlungsschicht liegen.

Die Aufgabe des LLC-Sublayer ist es, eine logische Verbindung zwischen zwei Kommunikationsteilnehmern zuständig. 
Es hat auch die Aufgabe der Flow Control (Daten- Flusskontrolle) das gezielte Anhalten des Datenstroms, um eine Überlastung eines Systems zu verhindern. 
Und die Aufgabe der Fehlererkennung infalle eines Bitübertragungsfehlers auf der Leitung (z.B. durch externe Störeinflüsse)

##	Was ist ein Zugriffsverfahren?

Zugriffsverfahren sind verfahren die Kollisionen von Daten erkennen und vermeiden wie z.B.: CSMA

##	Was ist Flusskontrolle?

Eine gezielte Anhaltung des Datenstroms, um eine Überlastung eines Systems durch eine Unmenge von Daten zu verhindern.

##	Wofür braucht man Fehlererkennung?

In Falle eines Bitübertragungsfehlers auf der Leitung springt die Fehlererkennung ein und versucht den Fehler der Leitung zu erkennen.

##	Was ist eine MAC-Adresse und wofür wird sie benötigt?



##	Was ist Protocol Multiplexing?

Protocol Multiplexing ermöglicht das verschiedene Schicht-2-Protokolle gleichzeitig arbeiten können und wird auf der Sicherungsschicht gehandhabt. 

##	Erkläre den Begriff “Frame”!

Die Sicherungsschicht verpackt die Daten der anderen Schichten schlussendlich in den sogenannten „Frame“. Das Frame stellt die Datenübertragungseinheit dar, die in Bits auf dem Übertragungsmedium ausgegeben wird.

##	Welche Protokolle findet man auf der 2. OSI-Schicht?

Ethernet, Wifi, Token Ring, Spanning Tree Protocol, ATM (Asynchronous Transfer Mode), uvm.
