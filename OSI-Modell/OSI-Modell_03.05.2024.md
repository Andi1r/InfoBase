# OSI-Modell (03/05/2024)

## Header

Informationen die von den Computern benötigt wird um zu wissen wass man mit dem Daten den man versendet (Nutzdaten) machen muss (wo & wie schicken usw...). 

### Overhead

Wenn man eine geringe menge an Nutzdaten verschickt und die Daten der Header ist größer als die Nutzdaten dann spricht man von Overhead.
Beim Overhead braucht der Computer länger die Daten zu entpacken als es braucht die Daten zu benutzen.

## Nutzdaten

Sind die eigentliche Daten die verschickt und verpack werden. Der Empfänger des Datenpaketes entpackt dieses Packet und weis dann genaus wass es mit dem Nutzdaten machen sollte.

## Kommunikation im OSI-Modell

Es gibt die Transport und die Anwendungsorientierten Schicht. Um etwas zu versenden, durchlaufen die Datenpakete jede einzelne Schicht des OSI Modells. Von der ersten bis zur siebten Schicht.

Die Schichten werden beim Versenden von 7 nach 1 durchlaufen, wo die Informationen schlussendlich physikalisch übertragen werden. Beim Empfänger läuft dieser Vorgang dann umgekehrt hab, die Daten werden von der 1. Schicht bis zur 7. durchgereicht.

Kopiert vom Hedgedoc da meine antwort schlect war. 

## Einkapselung

Nutzdaten werden in jeder Schicht eingekapselt um die Daten zu verschicken zu können.

Vom Hedgedoc:

Einkapselung bedeutet, dass auf jeder Schicht des OSI Modells bei der Verarbeitung der Informationen der Header der jeweiligen Schicht angehängt wird.