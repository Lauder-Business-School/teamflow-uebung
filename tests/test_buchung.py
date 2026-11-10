"""Tests für die Buchungslogik. Sie decken nur die einfachen Fälle ab (Übung: Grenzfälle ergänzen)."""
import unittest
from datetime import datetime, timedelta, timezone

from teamflow.buchung import Buchungsbuch, BuchungsFehler, Veranstaltung

JETZT = datetime(2026, 11, 11, 9, 0, tzinfo=timezone.utc)


def workshop(kapazitaet=2, genehmigung=False, in_tagen=7):
    return Veranstaltung("W1", "Fahrrad reparieren", JETZT + timedelta(days=in_tagen), kapazitaet, genehmigung)


class BuchenTest(unittest.TestCase):
    def test_bestaetigt_bei_freiem_platz(self):
        buch, v = Buchungsbuch(), workshop()
        self.assertEqual(buch.buchen("anna", v, JETZT).status, "confirmed")

    def test_keine_zweite_aktive_buchung(self):
        buch, v = Buchungsbuch(), workshop()
        buch.buchen("anna", v, JETZT)
        with self.assertRaises(BuchungsFehler):
            buch.buchen("anna", v, JETZT)

    def test_genehmigungspflicht_startet_offen(self):
        buch, v = Buchungsbuch(), workshop(genehmigung=True)
        self.assertEqual(buch.buchen("ben", v, JETZT).status, "pending_approval")

    def test_ablehnung_fuehrt_nicht_zur_warteliste(self):
        buch, v = Buchungsbuch(), workshop(genehmigung=True)
        b = buch.buchen("ben", v, JETZT)
        buch.ablehnen(b, v, JETZT)
        self.assertEqual(b.status, "rejected")
        self.assertEqual(buch.warteliste(v), [])


class StornierenTest(unittest.TestCase):
    def test_stornierung_eine_woche_vorher(self):
        buch, v = Buchungsbuch(), workshop()
        b = buch.buchen("anna", v, JETZT)
        self.assertEqual(buch.stornieren(b, v, JETZT).status, "cancelled")

    def test_stornierung_kurz_vor_beginn_abgelehnt(self):
        buch, v = Buchungsbuch(), workshop(in_tagen=0.5)
        b = buch.buchen("anna", v, JETZT)
        with self.assertRaises(BuchungsFehler):
            buch.stornieren(b, v, JETZT)


if __name__ == "__main__":
    unittest.main()
