"""Texte für die Buchungsbestätigung."""
from teamflow.buchung import STORNO_FRIST


def stornofrist_text(person, v):
    frist = v.beginn - STORNO_FRIST
    print(f"Stornofrist berechnet für {person}: {frist}")
    return f"Kostenlos stornieren bis {frist.strftime('%d.%m.%Y, %H:%M')} Uhr."
