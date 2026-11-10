# TeamFlow: Übungs-Repository für Innovieren mit KI

Fiktiver Unterrichtsfall: Anmeldung zu Reparaturworkshops. Alle Namen und Daten sind erfunden.

## So starten Sie (5 Minuten)

1. Einladung zu diesem Repository per E-Mail annehmen.
2. Oben auf **Code**, dann **Codespaces**, dann **Create codespace on main**. Der Editor öffnet sich im Browser, Copilot ist dabei, wenn Ihr Konto Copilot hat. Alternativ in Visual Studio Code klonen.
3. Eigenen Branch anlegen: `team-1` bis `team-6`. Nie direkt auf `main` arbeiten.
4. Copilot-Chat öffnen und testen: `Fasse produktkontext.md in drei Sätzen zusammen. Ändere keine Dateien.`

## Was hier liegt

| Datei | Wofür |
|---|---|
| `produktkontext.md` | Worum es bei TeamFlow geht |
| `geschaeftsregeln.md` | Verbindliche Buchungsregeln BR01 bis BR08 |
| `quellen.md`, `quellenregister.csv` | Welche Quelle wie belastbar ist |
| `daten/` | Interviews, Meeting- und PRD-Export, Funnel- und Prioritätsdaten, Kundenfeedback |
| `teamflow/buchung.py` | Buchungslogik in Python (Übungscode, enthält absichtlich Fehler) |
| `tests/test_buchung.py` | Tests, die nur die einfachen Fälle abdecken |
| `tickets/` | Ein vages Ticket und ein Fehlerbericht |

Tests ausführen (Python 3, keine Installation nötig):

```bash
python3 -m unittest discover -s tests -t .
```

Pull Request #1 „Stornofrist in der Bestätigung anzeigen“ ist für die Review-Übung gedacht. Nicht mergen.

Regeln: keine echten Personen- oder Kundendaten eintragen. Ergebnisse kommen ins gemeinsame Dokument des Kurses, nicht nach `main`.

Kurs: https://ai-literacy.disrupt.company/#tag-11-11-bausteine
