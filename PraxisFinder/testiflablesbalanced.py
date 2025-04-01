import pandas as pd
from sklearn.model_selection import train_test_split

# Lade den Datensatz
df = pd.read_csv('data/symptome_training.csv')

# Verteilung der Labels anzeigen (um Unbalance zu erkennen)
print("📊 Klassenverteilung:")
print(df['label'].value_counts())

# Fehlende Daten anzeigen
print("\n🧼 Fehlende Werte pro Spalte:")
print(df.isnull().sum())

# Zufällige Stichprobe anzeigen
print("\n🔍 Zufällige 5 Beispiele:")
print(df.sample(5))

# Beispielhafter Train/Test-Split
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
print(f"\n📈 Trainingsdaten: {len(train_df)} Beispiele")
print(f"📉 Testdaten: {len(test_df)} Beispiele")