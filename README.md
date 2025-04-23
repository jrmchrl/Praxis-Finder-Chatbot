
# 🌿 PraxisFinder Chatbot

Der **PraxisFinder Chatbot** ist ein intelligenter KI-gestützter Chatbot, der Nutzer:innen hilft, passende ganzheitliche medizinische Praxen wie Ayurveda-, TCM- oder Heilpraktikerpraxen zu finden – basierend auf ihren Symptomen.

---

## 📁 Projektstruktur

```
PraxisFinder-Chatbot/
├── backend/
│   └── train_model.py          # Training des KI-Modells
├── data/
│   └── symptome_training.csv   # Trainingsdatensatz
├── model/
│   ├── symptom_model.h5        # Trainiertes Modell
│   ├── tokenizer.pkl           # Tokenizer für Texteingaben
│   └── label_encoder.pkl       # Label-Encoder für Klassennamen
├── PraxisFinder/
│   └── app.py                  # Streamlit Frontend
├── praxisempfehlung.py         # Logik für passende Praxen
├── testiflablesbalanced.py     # Datensatzprüfung
├── plot_label_distribution.py  # Visualisierung der Labelverteilung
└── README.md                   # Diese Datei
```

---

## ⚙️ Setup & Installation

### 1. Repository klonen

```bash
git clone <REPOSITORY_URL>
cd PraxisFinder-Chatbot
```

### 2. Python-Umgebung erstellen

```bash
pyenv virtualenv 3.10.11 praxisfinder-env
pyenv activate praxisfinder-env
```

> Alternativ mit `venv`:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

### 4. Modell trainieren (optional, falls nicht vorhanden)

```bash
python backend/train_model.py
```

---

## 🚀 Anwendung starten

```bash
cd PraxisFinder
streamlit run app.py
```

---

## 💡 Nutzung

- Gib deine Symptome im Textfeld ein
- Das KI-Modell erkennt die passende medizinische Kategorie
- Eine passende ganzheitliche Praxis wird dir vorgeschlagen

---

## 🧠 Verwendete Technologien

- Python 3.10
- TensorFlow / Keras
- Streamlit (Frontend)
- Pandas, NumPy, Scikit-Learn

---

## 📌 Hinweise

- Die App basiert auf einem lokal trainierten KI-Modell (keine API-Kosten!)
- Daten sind anpassbar über `symptome_training.csv`
- Praxenvorschläge kannst du in `praxisempfehlung.py` pflegen

---

## 🧘 Autorin

Charlotte Jeroma 
