from flask import Flask, render_template, request
import random

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
    app.run(debug=True, port=8000)