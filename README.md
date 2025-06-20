🧠 Empathetic AI Therapist Chatbot (Voice & Emotion Tracking)
Welcome to the Empathetic AI Therapist Chatbot! This project aims to create a supportive and understanding conversational agent designed to listen to users and provide empathetic responses. It features voice interaction and dynamically changes the chat interface color based on the user's inferred emotional state, creating a more soothing and responsive environment.
Disclaimer: This AI chatbot is for emotional support and self-exploration purposes only. It is NOT a substitute for a licensed mental health professional and cannot provide diagnoses, medical advice, or crisis intervention. If you are experiencing a mental health crisis or need urgent help, please contact a qualified professional or emergency services.
✨ Features
Empathetic Responses: Powered by Google's Gemini Pro model, trained to offer compassionate, non-judgmental, and reflective dialogue.
Voice Input (Speech-to-Text): Speak your thoughts directly to the chatbot using your browser's microphone.
Voice Output (Text-to-Speech): The chatbot replies audibly with a calm and soothing voice.
Emotion Tracking via Color: The background color of the chat interface subtly changes based on the sentiment (emotion) detected in your input, providing visual feedback and enhancing the empathetic atmosphere.
Web Interface (Flask): A simple and intuitive web-based chat interface accessible through your browser.
Conversation History: The bot remembers the context of your conversation for more coherent interactions.
Chat Reset: Option to clear the conversation history and start fresh.
🚀 Technologies Used
Python: The core programming language for the backend logic.
Flask: A lightweight Python web framework for building the web application.
Google Gemini API (gemini-1.5-flash-latest): The large language model (LLM) powering the chatbot's conversational abilities and sentiment analysis.
python-dotenv: For securely loading API keys from a .env file.
HTML, CSS, JavaScript: For the interactive and responsive frontend web interface.
Web Speech API (Browser-side): Utilized for Speech-to-Text (microphone input) and Text-to-Speech (voice output).
⚙️ Setup Instructions
Follow these steps to get the chatbot up and running on your local machine.
Prerequisites
Python 3.9+: Download Python
Git: Download Git (often pre-installed on macOS/Linux)
Google Gemini API Key:
Go to Google AI Studio.
Sign in with your Google account.
Click "Get API Key" or "Create new API key."
Copy your API key.
Ensure the "Generative Language API" is enabled in your Google Cloud Console (under "APIs & Services" > "Enabled APIs & services").
Installation Steps
Clone the repository:
If you've already initialized Git locally and linked it, you might just be setting up your local environment. If you're starting fresh (e.g., on another machine), you'd clone:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name # Replace with your actual repository name

(If you are pushing an existing project, you would cd into your project directory and proceed.)
Create a Python Virtual Environment (Highly Recommended):
A virtual environment isolates your project dependencies.
python3 -m venv venv


Activate the Virtual Environment:
macOS/Linux:
source venv/bin/activate


Windows (Command Prompt):
.\venv\Scripts\activate


Windows (PowerShell):
.\venv\Scripts\Activate.ps1


(You'll know it's active when (venv) appears at the beginning of your terminal prompt.)
Install Dependencies:
pip install Flask google-generativeai python-dotenv


Create a .env file:
In the root of your project directory (the same folder as app.py), create a file named .env.
Using Terminal (macOS/Linux): touch .env
Using Terminal (Windows Cmd): type nul > .env
Using Terminal (Windows PowerShell): New-Item -Path .\.env -ItemType File
Using a Code Editor: Most code editors allow you to create files starting with . directly.
Open the .env file and add your Google Gemini API key:GOOGLE_API_KEY="YOUR_GEMINI_API_KEY_HERE"
Replace YOUR_GEMINI_API_KEY_HERE with the actual key you copied from Google AI Studio.
Ensure .gitignore is set up:
Make sure you have a .gitignore file in your project root with at least these entries to prevent sensitive information from being committed to Git:
# Environment variables
.env

# Python bytecode
__pycache__/
*.pyc

# Virtual environment
venv/

# macOS specific
.DS_Store

# Any logs or temporary files
*.log
temp/


Run the Flask Application:
python app.py

You should see output indicating that the Flask development server is running, usually on http://127.0.0.1:5000/.
🤖 Usage
Open your web browser and navigate to the URL provided by the Flask server (e.g., http://127.0.0.1:5000/).
Text Input: Type your message into the text area and click "Send" or press Enter.
Voice Input: Click the "🎙️ Speak" button. Your browser will likely ask for microphone permission. Grant it. Speak your message clearly, and the bot will automatically process it once you stop speaking.
Emotion Tracking: Observe the chat container's background color. It will subtly change based on the sentiment inferred from your last message.
Light Green: Positive emotions
Light Blue: Sadness/Calm
Light Orange/Peach: Anger/Anxious
Very Light Off-White: Neutral
Reset Chat: Click the "Reset Chat" button to clear the conversation history and start a new interaction.
⚠️ Important Considerations
Browser Compatibility for Voice: The voice input (SpeechRecognition) and voice output (SpeechSynthesis) features rely on the Web Speech API, which has varying support across browsers. Google Chrome is highly recommended for the best experience. Safari's support is limited.
Privacy: This application does not store your chat history or audio data on a persistent server. The chat_history is in-memory for the current session, and audio is processed client-side. Your API key is kept secure in the .env file and is not exposed in the frontend or version control.
API Usage: While Google Gemini offers a generous free tier, be mindful of your API usage, especially for high volumes of requests. You can monitor your usage in the Google Cloud Console.
💡 Future Enhancements
More Granular Emotion Detection: Explore advanced sentiment analysis or emotion recognition models for richer emotional understanding.
Dynamic Voice Modulation: If using a paid TTS API, implement dynamic voice modulation to truly match the bot's tone to the inferred user emotion (e.g., a sad voice for a sad user, a reassuring voice for an anxious user).
Session Management: Implement Flask sessions or a small database (e.g., SQLite, Firestore) to store chat history more persistently or for multiple users (with appropriate privacy considerations).
Guided Conversations: Integrate therapeutic techniques (e.g., CBT, DBT elements) to provide more structured guidance.
User Profiles: Allow users to create profiles to personalize the experience over time.
Deployment: Deploy the Flask application to a cloud platform (e.g., Google Cloud Run, Heroku, Render) for public access.
📄 License
This project is open-source and available under the MIT License.
Thank you for exploring the Empathetic AI Therapist Chatbot! We hope it provides a helpful and soothing experience.

