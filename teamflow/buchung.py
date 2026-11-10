"""TeamFlow: Buchungslogik für Reparaturworkshops (Übungscode, fiktiv).

Setzt die Regeln aus geschaeftsregeln.md um. Zeitpunkte sind immer UTC (BR07).
Der Code enthält absichtlich Fehler für die Übungen. Nicht in Produktion verwenden.
"""
from dataclasses import dataclass, field
from datetime import datetime, timedelta

AKTIV = {"pending_approval", "confirmed", "waitlisted"}  # BR01
STORNO_FRIST = timedelta(hours=24)  # BR03


class BuchungsFehler(Exception):
    """Unzulässige Aktion: Zustand und Belegung bleiben unverändert."""


@dataclass
class Veranstaltung:
    id: str
    titel: str
    beginn: datetime  # UTC
    kapazitaet: int
    genehmigungspflichtig: bool = False


@dataclass
class Buchung:
    person: str
    veranstaltung_id: str
    status: str
    seq: int


@dataclass
class Buchungsbuch:
    buchungen: list = field(default_factory=list)
    _seq: int = 0

    def _naechste_seq(self):
        self._seq += 1
        return self._seq

    def belegte_plaetze(self, v):
        """Anzahl belegter Plätze einer Veranstaltung (BR02)."""
        return sum(
            1
            for b in self.buchungen
            if b.veranstaltung_id == v.id and b.status in ("confirmed", "waitlisted")
        )

    def frei(self, v):
        return self.belegte_plaetze(v) < v.kapazitaet

    def aktive_buchung(self, person, v):
        for b in self.buchungen:
            if b.person == person and b.veranstaltung_id == v.id and b.status in AKTIV:
                return b
        return None

    def buchen(self, person, v, jetzt):
        if jetzt >= v.beginn:
            raise BuchungsFehler("Die Veranstaltung hat bereits begonnen.")
        if self.aktive_buchung(person, v):
            raise BuchungsFehler("Es gibt schon eine aktive Buchung für diese Veranstaltung.")
        if v.genehmigungspflichtig:
            status = "pending_approval"  # BR05: reserviert noch keinen Platz
        else:
            status = "confirmed" if self.frei(v) else "waitlisted"
        b = Buchung(person, v.id, status, self._naechste_seq())
        self.buchungen.append(b)
        return b

    def genehmigen(self, b, v, jetzt):
        if b.status != "pending_approval" or jetzt >= v.beginn:
            raise BuchungsFehler("Nur offene Anfragen vor Beginn können genehmigt werden.")
        b.status = "confirmed" if self.frei(v) else "waitlisted"
        return b

    def ablehnen(self, b, v, jetzt):
        if b.status != "pending_approval" or jetzt >= v.beginn:
            raise BuchungsFehler("Nur offene Anfragen vor Beginn können abgelehnt werden.")
        b.status = "rejected"  # BR08: keine Warteliste
        return b

    def stornieren(self, b, v, jetzt):
        if b.status not in AKTIV:
            raise BuchungsFehler("Nur aktive Buchungen können storniert werden.")
        if v.beginn - jetzt > STORNO_FRIST:
            b.status = "cancelled"
            return b
        raise BuchungsFehler("Stornierung ist nur bis 24 Stunden vor Beginn möglich.")

    def warteliste(self, v):
        """Wartende in Eintrittsreihenfolge (BR04)."""
        return sorted(
            (b for b in self.buchungen if b.veranstaltung_id == v.id and b.status == "waitlisted"),
            key=lambda b: b.seq,
        )
