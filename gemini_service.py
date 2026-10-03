import base64
from google import genai
import streamlit as st


# Get Gemini API key
api_key = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=api_key)


def ask_gemini(question, uploaded_image=None, study_mode="Explain"):

    # Study mode instructions
    if study_mode == "Explain":

        mode_instruction = """
Explain the concept in simple, student-friendly language.

Include:
📌 Topic
🧠 Simple Explanation
🔑 Key Points
📝 Exam Tip
"""

    elif study_mode == "Summarize":

        mode_instruction = """
Summarize the study material.

Include:
📌 Topic
📝 Short Summary
🔑 5-7 Key Points
💡 Important Terms
"""

    elif study_mode == "Quiz":

        mode_instruction = """
Create a short quiz based ONLY on the provided study material.

Create 5 multiple-choice questions.

For each question provide:
Question
A)
B)
C)
D)

Then provide:
✅ Correct Answer
📖 Short Explanation
"""

    elif study_mode == "Exam Prep":

        mode_instruction = """
Help the student prepare for an exam.

Include:
📌 Topic
🔑 Important Concepts
❓ Possible Exam Questions
📝 Important Definitions
⭐ Exam Tips
"""

    # Common prompt
    prompt = f"""
You are StudyLens AI, an AI study assistant for college students.

The student's question is:

{question}

The selected study mode is:

{study_mode}

{mode_instruction}

Keep the response clear, concise and easy to understand.
Do not invent information that is not supported by the provided study material.
"""

    # Image input
    if uploaded_image is not None:

        image_bytes = uploaded_image.getvalue()

        image_data = base64.b64encode(image_bytes).decode("utf-8")

        interaction = client.interactions.create(
            model="gemini-3.8-flash",
            input=[
                {
                    "type": "text",
                    "text": prompt
                },
                {
                    "type": "image",
                    "data": image_data,
                    "mime_type": uploaded_image.type
                }
            ]
        )

    # Text-only input
    else:

        interaction = client.interactions.create(
            model="gemini-3.8-flash",
            input=prompt
        )

    return interaction.output_text