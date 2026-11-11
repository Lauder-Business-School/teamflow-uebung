# Geschäftsregeln TeamFlow (Referenzstand)

Fiktiver Unterrichtsfall für Innovieren mit KI (AI x Human, DISRUPT). Teams dürfen andere fachliche Entscheidungen begründen, passen dann aber Regeln, Code und Prüfungen konsistent an.

| ID | Regel |
| --- | --- |
| BR01 | Pro Person und Veranstaltung gibt es höchstens eine aktive Buchung. pending_approval, confirmed und waitlisted zählen als aktiv. |
| BR02 | Nur confirmed belegt einen Platz. Die Anzahl bestätigter Buchungen überschreitet die Kapazität auch bei gleichzeitigen Anfragen nicht. |
| BR03 | Stornierung ist erlaubt, wenn bis zum Veranstaltungsbeginn mindestens 24 Stunden verbleiben. Die exakte Grenze ist eingeschlossen. |
| BR04 | Wartelisten werden nach Eintrittsreihenfolge angezeigt; bei gleichem Zeitpunkt entscheidet eine stabile Sequenz. Automatisches Nachrücken gehört nicht zum Kern. |
| BR05 | Eine genehmigungspflichtige Anfrage beginnt als pending_approval und reserviert noch keinen Platz. Eine Genehmigung bestätigt bei freier Kapazität, sonst entsteht waitlisted. |
| BR06 | Die Anwendung prüft die vorgesehenen Ansichten und Aktionen je Demorolle. Diese Rollenlogik ersetzt keine produktive Authentifizierung. |
| BR07 | Zeitpunkte werden eindeutig in UTC gespeichert und für Europe/Vienna angezeigt. Zeitvergleiche erfolgen anhand des tatsächlichen Zeitpunkts. |
| BR08 | cancelled und rejected belegen keinen Platz und sind nicht aktiv. rejected führt nicht automatisch zur Warteliste. |

Eine stornierte oder abgelehnte Anfrage wird bei einem erneuten ausdrücklichen Buchungsversuch als neuer Vorgang behandelt. Er ist nur vor Veranstaltungsbeginn zulässig und durchläuft die üblichen Kapazitäts- und Genehmigungsregeln. BR01 verhindert parallele aktive Vorgänge; die Historie darf erhalten bleiben.

## Zustandswechsel

| Auslöser | Vorbedingung | Ergebnis |
| --- | --- | --- |
| Neue Buchung ohne Genehmigungspflicht | Veranstaltung noch nicht begonnen; keine aktive Buchung derselben Person | confirmed bei freiem Platz, sonst waitlisted |
| Neue genehmigungspflichtige Anfrage | Veranstaltung noch nicht begonnen; keine aktive Buchung derselben Person | pending_approval ohne Belegung |
| Genehmigung | Zugeordnete genehmigende Rolle; Status pending_approval; Veranstaltung noch nicht begonnen | confirmed bei freiem Platz, sonst waitlisted |
| Ablehnung | Zugeordnete genehmigende Rolle; Status pending_approval; Veranstaltung noch nicht begonnen | rejected ohne Wartelistenaufnahme |
| Stornierung | Eigener aktiver Vorgang; mindestens 24 Stunden bis Beginn | cancelled; gegebenenfalls belegter Platz wird frei |
| Unzulässige Aktion | Falsche Rolle, unpassender Status oder nicht erfüllte Zeitgrenze | Verständlicher Fehler; Zustand und Belegung bleiben unverändert |

Die erste Fassung zeigt frei gewordene Kapazität, versendet aber keine Angebote und bestätigt Wartende nicht automatisch. Angebotsfristen, Benachrichtigungen und automatische Nachbuchung sind eigene Produktoptionen.
