import pandas as pd
import tensorflow as tf
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import os

# 📁 Datenpfad (angepasst auf Root-Ordner)
csv_path = os.path.join(os.path.dirname(__file__), '../data/symptome_training.csv')

# 📥 Daten laden
df = pd.read_csv(csv_path)

texts = df['symptom_text'].values
labels = df['label'].values

# 🎯 Labels codieren
le = LabelEncoder()
labels_encoded = le.fit_transform(labels)

# 🔠 Tokenizer
tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
padded = pad_sequences(sequences, maxlen=20)

# 🔀 Split
X_train, X_test, y_train, y_test = train_test_split(padded, labels_encoded, test_size=0.2, random_state=42)

# 🧠 Modell
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(1000, 16, input_length=20),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(len(set(labels_encoded)), activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=30, validation_data=(X_test, y_test))

# 💾 Speichern
os.makedirs('../model', exist_ok=True)
model.save('../model/symptom_model.h5')
with open('../model/tokenizer.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)
with open('../model/label_encoder.pkl', 'wb') as f:
    pickle.dump(le, f)

# 📊 Evaluation
y_pred = model.predict(X_test)
y_pred_labels = np.argmax(y_pred, axis=1)

print("\n📊 Klassifikationsbericht:")
print(classification_report(y_test, y_pred_labels, target_names=le.classes_))

print("\n🧩 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_labels))