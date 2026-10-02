import streamlit as st
from gemini_service import ask_gemini

st.title("📚 StudyLens AI")
st.write("Your Multimodal AI Study Assistant")

st.subheader("Ask your question:")

question = st.text_input("")

if st.button("Ask Gemini"):
    if question:
        with st.spinner("Gemini is thinking..."):
            response = ask_gemini(question)

        st.subheader("AI Response")
        st.write(response)
    else:
        st.warning("Please enter a question.")