# Grundbegriffe der Datentechnik

## Daten & Informationen

Daten sind Informationen die ohne Kontext weniger und aussagen als Informationen die mit Kontext sind. Das bedeutet: Daten sind z.B. "Diese Woche wird es wahrschenlich nicht Regnen." und als Information mit Kontext wäre das "Es wird nicht Regnen." Ich verstehe den Unterschied selbst nicht gut genug um ihn in Wörter auszudrucken zu können.

## Signale & Signalverarbeitung

 Es gibt Kabelgebundene Signale (Elektrische, Optische) und nicht Kabelgebundene Signale (Funk). Für Kabelgebundene Signale werden Kabel wie TP-Kabel (Kupfer) und LWL-Kabel (Glassfaser, Kunststoff,...) benutzt um Netzwerke zu erstellen und ein austausch von Daten zu erlauben. Für nicht Kabelgebundene Signale werden die Daten mit Funk durch WLAN oder sogar Bluetooth ausgetauscht und so ein kabelloses Netzwerk erstellt. 
 
 Signale werden vom Rechner des Empfängers als Bits (Datenspeichersystem mittels 1 und 0) und Bytes (8 Bits) zum nutzbaren Daten verarbeitet und interpretiert. Diese Daten werden dann je nach dem für was sie benutzt werden sollten vom Rechner verarbeitet.

 Bei LWL-Kabel (Optische Signale) werden die Lichtwellen in elektrische Signale umgewandelt und dann vom Rechner als Bits verarbeitet.

 Signale können Analog (immer an und unterschiedliches Wert) und Digital (immer nur ein und aus) 

## Datencodierung

Computer nutzen das Binärsystem um Daten zu verarbeiten und interpretieren. Computer benutzen dafür Datencodierungen wie z.B. ASCII oder UTF-8 bzw. UTF-16. Ohne einer Datencodierung würden Texte so ausschauen: 01000001 (in ASCII: A)
 Deshalb ist die Datencodierung wichtig für Computer und die Benutzer des Computers. In UTF-8 und UTF-16 (und UTF-32) werden die Daten durch dem Hexadecimalsystem encodiert. Auch Befehle werden mit UTF encodiert.

## Datenformate

Datenformate sind Formate wie CSV (Comma-seperated Values), XML (Extensible markup language) und JSON (Javascript object notation) die Daten standardmäßig strukturieren. Diese Datenformate werden benutzt um eine menge von Daten zu speichern, zu verändern und zu verwalten. Alle der Datenformate können vom Spreadsheet-Programmen als Daten interpretiert werden.

CSV (Comma-seperated Values) speichert die Daten indem sie die Daten durch einfache kommastellen separiert. Z.B.: Andraz,Robin,30.04.2024,bfi,... Spreadsheet-Programme wie MS Excel und Libreoffice Calc können CSV Dateien aus Tabellen erstellen und CSV Dateien interpretieren und eine Tabelle daraus erstellen.

XML (Extensible markup language) speichert die Daten indem sie die Daten in "Objekte" speichert. Dies erlaubt den Benutzer nach daten rasch zu suchen. Z.B.: ... <Arbeiter>Andraz Robin</Arbeiter> ...

JSON (Javascript object notation) speichert die Daten in Blöcken ähnlich wie XML. JSON ist übersichtlicher als XML da man die Daten leichter sehen kann. Bei JSON müssen die Blöcke mit Kommas getrennt werden. Z.B.: ... "Vorname": "Andraz", ...

## Netzwerktechnik

Netzwerktechnik ist die Technik der vernetzung von Geräten und ihre zusammenarbeit. Unter Netzwerktechnik gibt es folgenden Begriffe wie: Netzwerkarchitektur, Server, Client, Endgeräte, Zwischengeräte und mehr...

Netzwerkarchitektur (oder Netzwerkstrukturen) wie Peer-to-Peer (P2P) und Server-Client Strukturen.

Netzwerkgrößen werden durch PAN, LAN, MAN, WAN und GAN unterschieden. 
PAN ist der kleinste netz mit einer reichweite von 10m und wird mit z.B. Funk oder Bluetooth erstellt. 
LAN ist der zweit kleinste Netz und umspannt ein Raum, mehrere Räume, ein Stockwerk, mehrere Stockwerke, ein Gebäude, mehrere Gebäude und sogar ein ganzes Standort. LAN wird mit Kabel erstellt. 
MAN umspannt eine ganze Stadt oder mehrere Städte, sie regelt Ampeln und verbindet die Blaulicht-Organisationen miteinander. MAN wird mit LWL-Kabel erstellt.
WAN umspannt ein Land, mehrere Länder und ein Kontinent oder mehrere Kontinente. WAN wird mit LWL-Kabel erstellt.
GAN umspannt die ganze Welt. GAN wird mit LWL-Kabel erstellt

Endgeräte sind Geräte die Daten Senden und Empfängern am ende der ganzen Netzwerkes. Endgeräte sind Computer, Handys, Drucker, eventuell Fax-Maschinen, Smart-TVs und mehr.

Zwischengeräte leiten Daten weiter zum Empfängern. Zwischengeräte sind Server, Switches, Router und mehr.

## Datenschutz

Der Schutz der Daten und ihre rechtsgemäße verwaltung und verarbeitung.

### Verschlüsselung & Entschlüsselung

Daten werden vom Sender verschlüsselt um sie sicher zu halten und dann vom Empfänger entschlüsselt um auf die Daten zuzugreifen.

Daten können Synchronisch und Asynchronisch verschlüsselt werden. Bei der Synchronischen verschlüsselung können die Daten nur mit einem einzigen Schlüssel. Bei der Asynchronischen verschlüsselung können die Daten mit mehreren Schlüsseln entschlüsselt werden.

### Rechtslage von Datennutzung

Webseiten und Applikationen können deine Daten (je nach Datenschutzrechtlinien) verwalten, verarbeiten, weitergeben und speichern. Sie dürfen das nur tun wenn du deine einwillingung gibst. 
Als EU-Bürger kannst du auffordern, das die Webseite, die Daten die sie gespeichert haben dir zu verschicken. Du darfst auch anfordern das alle deine Daten gelöscht werden.
