
# Studylens AI

StudyLens AI is an AI-powered study assistant that helps students understand study questions and uploaded images using Google Gemini. It is designed for students and learners who want quick, simple, and easy-to-understand explanations of difficult study material.


## Features

- Ask study-related questions
- Upload images for AI-powered analysis
- Get simple explanations of difficult concepts
- Uses Google Gemini for AI responses
- Simple and beginner-friendly Streamlit interface
- Deployed using Streamlit Community Cloud

## Tech Stack

**Frontend/UI:** Streamlit

**Backend/AI:** Python, Google Gemini API

**Libraries:** Google GenAI SDK

**Deployment:** Streamlit Community Cloud

**Version Control:** Git, GitHub
## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/studylens-ai.git
cd studylens-ai
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Add your Gemini API key

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "your-api-key-here"
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.
## Environment Variables

To run this project, you need to configure the following secret in Streamlit:

```toml
GEMINI_API_KEY = "your-gemini-api-key"
```

For local development, create:

```text
.streamlit/secrets.toml
```

Then add:

```toml
GEMINI_API_KEY = "your-gemini-api-key"
```
## Run Locally

### 1. Clone the project

```bash
git clone https://github.com/your-username/studylens-ai.git
```

### 2. Go to the project directory

```bash
cd studylens-ai
```

### 3. Create and activate a virtual environment

```bash
python -m venv .venv
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure your Gemini API key

Create the following file:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "your-gemini-api-key"
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser at the local Streamlit address.
## Usage/Examples

1. Run the application:

```bash
streamlit run app.py
```

2. Upload an image of your study material, notes, or question.

3. Enter a question related to the uploaded content.

4. StudyLens AI analyzes the input using the Google Gemini API and provides an AI-generated response.

### Example

**Input:** Upload an image of a question and ask:

```text
Explain this question in simple words.
```

**Output:** StudyLens AI analyzes the image and provides a clear, student-friendly explanation.
## Screenshots

![StudyLens AI](screenshots/Screenshot%202026-10-03%20141841.png)
## Deployment

The project is deployed using Streamlit Community Cloud.

To run the application locally:
```bash
streamlit run app.py

## API Reference
StudyLens AI uses the Google Gemini API to analyze uploaded study material and generate AI-powered responses.
### Gemini API
The application uses the Gemini API through the Google GenAI SDK.
**Required secret:**
```toml
GEMINI_API_KEY = "your-gemini-api-key"

## Roadmap
- Add PDF and document upload support
- Add more AI-powered study tools
- Add quiz and flashcard generation
- Improve image and handwritten-question analysis
- Add conversation history
- Improve UI and user experience
- Deploy the application on Streamlit Community Cloud

## Acknowledgments
- [Google Gemini](https://ai.google.dev/) for providing the generative AI capabilities used in StudyLens AI.
- [Streamlit](https://streamlit.io/) for the framework used to build and deploy the application.
- [GitHub](https://github.com/) for repository hosting and version control.

## Authors
  - Vaibhav Sorte
  - GitHub: [@vaibhavsorte26-source](https://github.com/vaibhavsorte26-source)
  - LinkedIn: [Vaibhav Sorte](https://www.linkedin.com/in/vaibhav-sorte-8753b6350/)

## License
This project is for educational purposes.
