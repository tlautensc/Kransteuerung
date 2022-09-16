# Kransteuerung
 Steuerung für Kamerakran
 Hier entsteht die Steuerung für einen Kamera-Kran.
 9 Achsen werden von Nema 23 und Nema 17 Schrittmotoren bewegt, die über 2 Bigtreetec Octopus Stepptecontroller angesteuert werden.

 Achsen:
 - XU: Pan Kran
 - YU: Tilt Kran
 - ZU: Tele Kran
 - ZU: Tele Kran
 - AO: Winkleaugleich Tilt

 - XO: Pan Kamera
 - YO: Tilt Kamera
 - AO: Zoom
 - BO: Focus

Der Motorcontroller erhält seine Steuerdaten in Form von G-Code über die Serielle Schnittstelle eines Raspberry-Pi auf welchem auch die hier entwickelte Steuersoftware läuft.

# Anforderunge Backend
 - G-Code generieren
 - Statusüberblick aller Achsen
 - 16 Speichermöglichkeiten für Positionen
 - Import/Export von Presets in Form von XML- oder json-Dateien
 - Interplation zwischen zwei Positionen um weiche Fahrten zu ermöglchen

# Anforderungen Web-Frontend
 - Verfahren jeder Einzelnen Achse
 - Einstellen Fahrzeit
 - Einstellen Weichheit
 - Abrufen und Speichern von Presets
 - Import und Export der Presets
 - Desktop und Mobil
 - Reset des Krans

# Weitere Frontends:
 - DMX
 - Visca-IP
 - Streamdeck-Companion

# Zukünftige Features:
 - Komplexe Fahrten über mehrere Punkte

