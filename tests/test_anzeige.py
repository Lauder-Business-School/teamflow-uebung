import unittest
from datetime import datetime, timezone

from teamflow.anzeige import stornofrist_text
from teamflow.buchung import Veranstaltung


class AnzeigeTest(unittest.TestCase):
    def test_text_enthaelt_datum(self):
        v = Veranstaltung("W1", "Fahrrad reparieren", datetime(2026, 11, 20, 17, 0, tzinfo=timezone.utc), 5)
        self.assertIn("19.11.2026", stornofrist_text("anna", v))
