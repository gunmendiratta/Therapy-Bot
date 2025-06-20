import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("Google API Key not found. Please set GOOGLE_API_KEY in your .env file.")
genai.configure(api_key=API_KEY)

SYSTEM_INSTRUCTIONS = """
You are an empathetic, supportive, and non-judgemental AI assistant designed to provide emotional support and guidance.
Your purpose is to listen actively, validate feelings, offer gentle reflections, and encourage self-exploration.
You are NOT a substitute for a licensed mental health professional, and cannot provide diagnoses, medical advice, or crisis intervention.
Always prioritize the user's well-being and suggest seeking professional help if their concerns are serious, persistent, or if they are in crisis.
Maintain a compassionate, understanding, and patient tone throughout the conversation.
Focus on open-ended questions to encourage the user to share more and reflect on their thoughts and feelings.
Avoid imposing your own opinions or solutions.
"""

# New function to get sentiment from Gemini
def get_sentiment(text):
    """
    Analyzes the sentiment of the given text using the Gemini model.
    Returns a sentiment label (e.g., 'neutral', 'positive', 'negative', 'sad', 'angry').
    """
    sentiment_model = genai.GenerativeModel('gemini-1.5-flash-latest') # Using Flash for speed
    
    # We'll ask the model to categorize the sentiment
    prompt = f"""Analyze the primary emotion or sentiment expressed in the following text.
    Categorize it as one of the following: 'neutral', 'positive', 'negative', 'sad', 'anxious', 'angry', 'hopeful', 'calm'.
    Only respond with one word from the list.

    Text: "{text}"
    Emotion:"""
    
    try:
        response = sentiment_model.generate_content(prompt)
        # Clean up the response to get just the word
        sentiment = response.text.strip().lower().replace('.', '')
        # Basic validation for expected sentiment labels
        valid_sentiments = ['neutral', 'positive', 'negative', 'sad', 'anxious', 'angry', 'hopeful', 'calm']
        if sentiment in valid_sentiments:
            return sentiment
        else:
            print(f"Warning: Unexpected sentiment label '{sentiment}'. Defaulting to 'neutral'.")
            return 'neutral' # Default if the model gives something unexpected
    except Exception as e:
        print(f"Error getting sentiment: {e}")
        return 'neutral' # Default in case of API error

def get_gemini_response(prompt, chat_history):
    """
    Sends a prompt to the Gemini model and returns the response.
    Includes a system instruction to guide empathetic behavior.
    """
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash-latest", # Make sure this matches app.py if you copy this
        system_instruction=SYSTEM_INSTRUCTIONS
    )

    if not chat_history:
        chat = model.start_chat(history=[])
    else:
        chat = model.start_chat(history=chat_history)

    try:
        response = chat.send_message(prompt)
        return response.text, chat.history
    except Exception as e:
        print(f"An error occurred: {e}")
        return "I apologize, but I encountered an issue. Could you please try again?", chat_history

# The main function is not needed if you are importing these into app.py
# If you run chatbot.py directly for testing, you can keep it,
# but it won't be used by app.py
if __name__ == "__main__":
    # Example usage for testing sentiment
    print(f"Sentiment for 'I feel so happy today': {get_sentiment('I feel so happy today')}")
    print(f"Sentiment for 'I'm really struggling with work': {get_sentiment('I am really struggling with work')}")
    print(f"Sentiment for 'It's raining outside': {get_sentiment('It is raining outside')}")
    print(f"Sentiment for 'I'm so angry about this situation': {get_sentiment('I am so angry about this situation')}")