PraxisFinder Chatbot

Der PraxisFinder Chatbot ist eine Anwendung, die Benutzern dabei hilft, medizinische Praxen und Heilpraktiker zu finden, insbesondere solche mit ganzheitlichem Ansatz wie Ayurveda und Traditionelle Chinesische Medizin (TCM).

Projektstruktur

Die Hauptverzeichnisse und -dateien des Projekts sind wie folgt organisiert:
	•	backend/: Enthält die Backend-Komponenten des Projekts, einschließlich des Modells und der Trainingsskripte.
	•	train_model.py: Skript zum Trainieren des Modells mit den bereitgestellten Daten.
	•	data/: Beinhaltet die Datensätze für das Training und die Tests.
	•	symptome_training.csv: CSV-Datei mit den Trainingsdaten.
	•	model/: Speichert das trainierte Modell.
	•	symptom_model.h5: Die gespeicherte Modelldatei nach dem Training. ￼
	•	app.py: Hauptskript für die Ausführung der Streamlit-Anwendung.
	•	requirements.txt: Liste der Python-Abhängigkeiten für das Projekt.

Installation und Einrichtung
	1.	Repository klonen:

git clone <repository-url>
cd Praxis-Finder-Chatbot


	2.	Virtuelle Umgebung erstellen und aktivieren:
	•	Mit venv: ￼

python3 -m venv venv
source venv/bin/activate


	•	Mit pyenv und pyenv-virtualenv:

pyenv virtualenv 3.10.11 praxisfinder-env
pyenv activate praxisfinder-env


	3.	Abhängigkeiten installieren:

pip install -r requirements.txt


	4.	Modell trainieren:
Stellen Sie sicher, dass die Datei symptome_training.csv im Verzeichnis data/ vorhanden ist. Führen Sie dann das Trainingsskript aus:

python backend/train_model.py

Das trainierte Modell wird im Verzeichnis model/ als symptom_model.h5 gespeichert.

Anwendung ausführen

Starten Sie die Streamlit-Anwendung mit folgendem Befehl:

streamlit run app.py

Die Anwendung wird im Standard-Webbrowser geöffnet und ermöglicht es Benutzern, durch Eingabe von Symptomen passende Praxen zu finden.

Fehlerbehebung
	•	Modul nicht gefunden (ModuleNotFoundError):
Stellen Sie sicher, dass alle Abhängigkeiten installiert sind und die virtuelle Umgebung aktiviert ist.
	•	Datei nicht gefunden (FileNotFoundError):
Überprüfen Sie, ob die erforderlichen Dateien, insbesondere symptome_training.csv und symptom_model.h5, im entsprechenden Verzeichnis vorhanden sind.

Kontakt

Für Fragen oder Unterstützung wenden Sie sich bitte an charlotte@jeroma.com


