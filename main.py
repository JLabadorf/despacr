#this is a flask app which will display a text area to the user. This webiste will take the input, remove all enter keys and then return the text to the user.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/remove', methods=['POST'])
def remove():
    if request.method == 'POST':
        text = request.form['text-input']
        text = text.replace('\n', ' ')
        while '  ' in text:
            text = text.replace('  ', ' ')
        return render_template('index.html', text=text)
