import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Daten laden
df = pd.read_csv('data/symptome_training.csv')

# Text & Labels vorbereiten
texts = df['symptom_text'].values
labels = df['label'].values

# Labels codieren
le = LabelEncoder()
labels_encoded = le.fit_transform(labels)

# Texte tokenisieren
tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
padded = pad_sequences(sequences, maxlen=20)

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(padded, labels_encoded, test_size=0.2)

# Modell bauen
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(1000, 16, input_length=20),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(len(set(labels_encoded)), activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=30, validation_data=(X_test, y_test))

# Modell & Tokenizer speichern
model.save('model/symptom_model.h5')
import pickle
with open('model/tokenizer.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)
with open('model/label_encoder.pkl', 'wb') as f:
    pickle.dump(le, f)