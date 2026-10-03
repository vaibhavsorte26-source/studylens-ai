import streamlit as st
from gemini_service import ask_gemini


# Page configuration
st.set_page_config(
    page_title="StudyLens AI",
    page_icon="📚",
    layout="centered"
)


# Header
st.title("📚 StudyLens AI")
st.caption("Your AI-powered study assistant")

st.markdown(
    "Upload your study material, choose a study mode, "
    "and let AI help you learn smarter."
)


# Sidebar
st.sidebar.title("📚 StudyLens AI")

st.sidebar.markdown("### Study Mode")

study_mode = st.sidebar.selectbox(
    "Choose how you want to study:",
    [
        "Explain",
        "Summarize",
        "Quiz",
        "Exam Prep"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "💡 Tip: Upload a textbook page, diagram, "
    "or question and ask StudyLens to explain it."
)


# Question
st.subheader("💬 Ask StudyLens")

question = st.text_input(
    "Your question",
    placeholder="e.g. Explain supervised learning in simple words."
)


# Image upload
st.subheader("📷 Upload Study Material")

uploaded_image = st.file_uploader(
    "Upload a textbook page, diagram, or question",
    type=["jpg", "jpeg", "png"]
)


# Image preview
if uploaded_image is not None:

    st.image(
        uploaded_image,
        caption="Uploaded study material",
        use_container_width=True
    )


# Analyze button
if st.button("🚀 Analyze with StudyLens", use_container_width=True):

    if not question and uploaded_image is None:

        st.warning(
            "Please enter a question or upload study material."
        )

    else:

        with st.spinner("🤖 StudyLens is thinking..."):

            if uploaded_image is not None:

                answer = ask_gemini(
                    question if question else
                    "Explain the main concepts in this image.",
                    uploaded_image,
                    study_mode
                )

            else:

                answer = ask_gemini(
                    question,
                    None,
                    study_mode
                )

        st.success("Analysis complete!")

        st.subheader("🤖 StudyLens Response")

        st.markdown(answer)


# Footer
st.markdown("---")

st.caption(
    "StudyLens AI • Built with Python, Streamlit & Gemini"
)
