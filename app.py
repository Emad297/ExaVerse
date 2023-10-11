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
    prompt = request.json.get('prompt')
    response = openai.Completion.create(model="gpt-3.5-turbo", prompt=prompt, max_tokens=100, temperature=0.7, top_p=1, frequency_penalty=0, presence_penalty=0.3, stop=["\n"])
    return jsonify(response.choices[0].text.strip())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
