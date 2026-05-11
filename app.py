from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

number_to_guess = random.randint(1, 100)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():

    user_guess = int(request.form['guess'])

    if user_guess < number_to_guess:
        result = "Enter a higher number"

    elif user_guess > number_to_guess:
        result = "Enter a lower number"

    else:
        result = "Congrats! You've won the game!"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)