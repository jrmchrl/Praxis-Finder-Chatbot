import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/symptome_training.csv')
label_counts = df['label'].value_counts()

plt.figure(figsize=(10, 6))
label_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Verteilung der Klassen (Labels)")
plt.xlabel("Kategorie")
plt.ylabel("Anzahl Beispiele")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
