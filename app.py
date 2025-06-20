import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Import the chatbot logic and the new get_sentiment function
from Bot import get_gemini_response, get_sentiment, SYSTEM_INSTRUCTIONS

load_dotenv()

app = Flask(__name__)

chat_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    if not user_message:
        return jsonify({"response": "Please enter a message."}), 400

    global chat_history

    # Get sentiment of the user's message
    user_sentiment = get_sentiment(user_message)

    # Get response from the Gemini model
    bot_response_text, updated_chat_history = get_gemini_response(user_message, chat_history)
    chat_history = updated_chat_history

    # Include sentiment in the JSON response
    return jsonify({
        "response": bot_response_text,
        "sentiment": user_sentiment # <--- NEW: Send sentiment to frontend
    })

@app.route("/reset", methods=["POST"])
def reset_chat():
    global chat_history
    chat_history = []
    return jsonify({"status": "Chat history reset."})

if __name__ == "__main__":
    app.run(debug=True)