# Beispiel-Praxen-Datenbank (kannst du später aus CSV laden)
praxen = {
    "Erkältung": "Hausarztpraxis Dr. Meyer, Berlin",
    "Stress": "Ganzheitliche Praxis Lichtblick, Hamburg",
    "Schlafstörung": "Schlafzentrum Nord, München",
    "Verdauung": "Magen-Darm-Zentrum Süd, Köln",
    "Psychisch": "Psychotherapie Praxis Harmonie, Leipzig",
    "Herz-Kreislauf": "Kardiologie West, Düsseldorf",
    "Orthopädisch": "Orthopädiezentrum Mitte, Stuttgart",
    "Allergie": "Allergiezentrum Rhein, Mainz"
}

def empfehlung_für_kategorie(kategorie):
    return praxen.get(kategorie, "Keine passende Praxis gefunden.")

# Test:
if __name__ == "__main__":
    test_kategorie = "Stress"
    print(f"✅ Empfohlene Praxis für '{test_kategorie}':")
    print(empfehlung_für_kategorie(test_kategorie))