import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Laden
model = tf.keras.models.load_model('model/symptom_model.h5')
with open('model/tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)
with open('model/label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

# Chatbot-Funktion
def chatbot_input(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=20)
    prediction = model.predict(padded)
    predicted_label = label_encoder.inverse_transform([prediction.argmax()])[0]
    return predicted_label

# Test
while True:
    user_input = input("Welche Symptome hast du? ")
    if user_input.lower() in ['exit', 'quit']:
        break
    kategorie = chatbot_input(user_input)
    print(f"Empfohlene Kategorie: {kategorie}")