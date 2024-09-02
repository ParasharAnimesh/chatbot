from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)
load_dotenv()

groq_api_key = os.environ.get('API_KEY')
groq_url = "https://api.groq.com/v1/generate"

@app.route('/', methods=['GET', 'POST'])
def form_handler():
    return render_template('index.html')

@app.route('/form', methods=['POST'])
def input_form():
    input_value = request.form.get('input_value')
    print(input_value)

    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": input_value,
        "max_tokens": 2048,
        "temperature": 0
    }

    response = requests.post(groq_url, headers=headers, json=payload)
    response.raise_for_status()

    output = response.json()["output"]

    return render_template('index.html', output=output, question=input_value)

if __name__ == '__main__':
    app.run(debug=True)
