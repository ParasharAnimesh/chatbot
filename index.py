from flask import Flask,request,render_template
from dotenv import load_dotenv
import os
import requests
import openai

app = Flask(__name__)
load_dotenv()

openai.api_key=os.environ.get('API_KEY')

@app.route('/', methods=['GET','POST'])
def form_handler():
    return render_template('index.html')
    
@app.route('/form', methods=['POST'])
def input_form():
      input_value = request.form.get('input_value')
      print(input_value)
      response = openai.ChatCompletion.create(
            model ="gpt-3.5-turbo",
            temperature=0,
            messages =[
                {"role": "user", "content": f'{input_value}'}
            ]
      )
      return render_template('index.html', output=response['choices'][0]['message']['content'], question=input_value)         
  
if __name__ == '__main__':
    app.run(debug=True)