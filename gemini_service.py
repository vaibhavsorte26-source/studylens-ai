import streamlit as st
from google import genai

api_key = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=api_key)


def ask_gemini(question):
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=question
    )

    return interaction.output_text