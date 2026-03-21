# Mobilomat Freiburg

## Website

https://www.mobilomat-freiburg.de/ -> Ausprobieren

## Entwicklung

1. Github-Repo klonen
2. Webserver starten: `python3 -m http.server 8080`
3. Auf `localhost:8080` ansehen

Live-Version ist auf `localhost:8080`.
Entwicklungsstand ist auf `localhost:8080/index.wip.html`.

## Mobilomat und DSGVO

- Alle **Verarbeitungen** passieren **innerhalb des Browsers** des Nutzers
- **keine Datenerhebung auf dem Server** (nur optional für eine Statistik - Ausnahme: Standardmäßige Erfassung der Zugriffe durch den Webhosting-Anbieter, z.B. IP-Adresse und Uhrzeit)
- kein Aufruf von externen Dateien (z.B. Content Delivery Network / CDN, Bootstrap, jQuery, kein Social Media-Plugin) - alles inklusive 

## LIZENZ

GPL 3 (siehe Verzeichnis /SYSTEM oder http://choosealicense.com/licenses/gpl-v3/)
- Quellcode, Lizenz und größere Änderungen müssen kenntlich gemacht werden.
- Änderungen, Weitergabe, sowie kommerzielle und private Nutzung erlaubt.
- Keine Garantie für Softwareschäden. 
