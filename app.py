from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# Initialize OpenAI API with your secret key from the Azure environment
openai.api_key = os.environ.get('OPENAI_SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_text():
    user_message = request.json.get('prompt')
    
    # Use conversation method
    messages = [{"role": "user", "content": user_message}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    response_message = response["choices"][0]["message"]["content"]
    
    return jsonify(response_message.strip())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
