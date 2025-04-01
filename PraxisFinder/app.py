import streamlit as st
import tensorflow as tf
import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from praxisempfehlung import empfehlung_für_kategorie

st.set_page_config(page_title="PraxisFinder", page_icon="🌿", layout="centered")

st.markdown("""
    <style>
    html, body {
        background-color: #f2f4f3;
        font-family: 'Helvetica Neue', sans-serif;
        color: #2e2e2e;
    }
    .stTextInput>div>div>input {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 10px;
        font-size: 18px;
        border: 1px solid #cccccc;
    }
    .stButton>button {
        background-color: #6bb586;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        border: none;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #4d9970;
    }
    .result-box {
        background-color: #ffffff;
        border-left: 6px solid #6bb586;
        padding: 1rem;
        margin-top: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

model = tf.keras.models.load_model('../model/symptom_model.h5')
with open('../model/tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)
with open('../model/label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

st.markdown("<h1 style='text-align: center;'>🌿 PraxisFinder</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Finde auf natürliche Weise die passende Praxis – basierend auf deinem Wohlbefinden.</p>", unsafe_allow_html=True)
st.write("")

user_input = st.text_input("Beschreibe deine Symptome:")

if user_input:
    sequence = tokenizer.texts_to_sequences([user_input])
    padded = pad_sequences(sequence, maxlen=20)
    prediction = model.predict(padded)
    kategorie = label_encoder.inverse_transform([np.argmax(prediction)])[0]
    praxis = empfehlung_für_kategorie(kategorie)

    st.markdown(f"""
    <div class="result-box">
        <h4>🧠 Erkannte Kategorie:</h4>
        <p><strong>{kategorie}</strong></p>
        <h4>🏥 Empfohlene Praxis:</h4>
        <p>{praxis}</p>
    </div>
    """, unsafe_allow_html=True)
