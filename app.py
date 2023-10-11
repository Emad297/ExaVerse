from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# Initialize OpenAI API with your secret key from the Azure environment
openai.api_key = os.environ.get('OPENAI_SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html')

# Generate text from prompt from gpt-3.5-turbo model
@app.route('/generate', methods=['POST'])
def generate_text():
    user_message = request.json.get('prompt')
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages = [{"role": "system", "content" : "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible."},
        {"role": "user", "content" : user_message}]
    )
    return jsonify({'text': completion.choices[0].message['content']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
