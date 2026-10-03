import base64
from google import genai
import streamlit as st

api_key = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=api_key)


def ask_gemini(question, uploaded_image=None):

    if uploaded_image is not None:

        image_bytes = uploaded_image.getvalue()

        image_data = base64.b64encode(image_bytes).decode("utf-8")

        interaction = client.interactions.create(
            model="gemini-3.8-flash",
            input=[
                {
                    "type": "text",
                    "text": question
                },
                {
                    "type": "image",
                    "data": image_data,
                    "mime_type": uploaded_image.type
                }
            ]
        )

    else:

        interaction = client.interactions.create(
            model="gemini-3.8-flash",
            input=question
        )

    return interaction.output_text