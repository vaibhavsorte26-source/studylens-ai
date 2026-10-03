import streamlit as st
from gemini_service import ask_gemini


st.title("StudyLens AI")

# Normal question
question = st.text_input(
    "Ask your question:",
    "Explain the difference between supervised learning and unsupervised learning?"
)

# Upload textbook image
uploaded_image = st.file_uploader(
    "Upload your textbook page or question",
    type=["jpg", "jpeg", "png"]
)

# Question about the uploaded image
image_question = st.text_input(
    "Ask a question about the image",
    "Explain the main concept on this page in simple words."
)

# Ask Gemini
if st.button("Ask Gemini"):

    if uploaded_image is not None:
        # Send image + image question to Gemini
        answer = ask_gemini(image_question, uploaded_image)
    else:
        # Send normal text question to Gemini
        answer = ask_gemini(question)

    st.subheader("AI Response")
    st.write(answer)