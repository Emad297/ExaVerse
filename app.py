from flask import Flask, request, jsonify, render_template, session
from flask_session import Session
import openai
import os

app = Flask(__name__)

# Initialize OpenAI API with your secret key from the Azure environment
openai.api_key = os.environ.get('OPENAI_SECRET_KEY')
# Configuration for the session
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def index():
    return render_template('index.html')

# Generate text from prompt from gpt-3.5-turbo model
@app.route('/generate', methods=['POST'])
@app.route('/generate', methods=['POST'])
def generate_text():
    user_message = request.json.get('prompt')
    
    # Get previous messages from session or initialize an empty list if not found
    messages = session.get('messages', [])
    messages.append({"role": "user", "content": user_message})
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    # Append the model's response to messages
    messages.append({"role": "assistant", "content": completion.choices[0].message['content']})
    
    # Update the session with the modified messages
    session['messages'] = messages
    
    return jsonify({'text': completion.choices[0].message['content']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
