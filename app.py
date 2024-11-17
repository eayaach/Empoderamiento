from flask import Flask, render_template, request, jsonify
from credentials import CREDENTIALS
import os
from dotenv import load_dotenv
from flask_cors import CORS
from openai import OpenAI

load_dotenv()
app = Flask(__name__)
cors = CORS(app)

# Load API keys from environment variables
# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
# client = OpenAI(api_key=OPENAI_API_KEY)


""" #Optional - But for specific tasks you need a system role to get refined responses
system_message = {
    "role": "system",
    "content": (
        "You're a Helpful assistant, and your task is to handle the user's query and provide Answers"
    )
}

messages = [system_message]

def generate_text(query):
    if query is None:
        return jsonify({"error": "No query provided"}), 400
    # Add the user's query to the conversation
    messages.append({"role": "user", "content": query})
    print("Hola")
    try:
        # Get the assistant's response using GPT-4o
        response = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=messages,
            temperature=0.6,
            top_p=0.9,
            max_tokens=256
        )
        assistant_message = response.choices[0].message.content
        # Append the assistant's response to messages
        messages.append({"role": "assistant", "content": assistant_message})
        print(messages)
        return assistant_message
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500 """

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/subir')
def subir():
    return render_template('subir.html')




if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)