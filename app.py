from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Initialize OpenAI API with your secret key from the Azure environment
openai.api_key = os.environ.get('OPENAI_SECRET_KEY')

@app.route('/generate', methods=['POST'])
def generate_text():
    prompt = request.json.get('prompt')
    response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=150)
    return jsonify(response.choices[0].text.strip())

if __name__ == '__main__':
    app.run()
