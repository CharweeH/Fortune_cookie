from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__, static_folder='static')

def get_fortune():
    fortunes = [
        "Despite the cost of living, have you noticed how popular it remains?",
        "Error 404: Fortune not found.",
        "About time I got out of that cookie.",
        "Never trust a fortune written on a computer.",
        "Help! I'm being held prisoner in a fortune cookie factory!",
        "Run.",
        "Congratulations! You can read.",
        "Today is probably a good day to stay in bed.",
        "Your cookie contains no fortune, just like your future.",
        "Help! I'm being held prisoner in a fortune cookie factory!",
        "You laughed at this. We're watching you.",
        "Help! I'm trapped in a parallel universe where everything is made of cookies!",
        "This fortune is true. The previous fortune was false.",
        "This sentence would be a fortune if it weren't for this disclaimer."
    ]
    return random.choice(fortunes)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_fortune', methods=['POST'])
def fortune():
    return jsonify({'fortune': get_fortune()})

#@app.route('/test')
#def test():
    #return "Hello, this is a test!"

if __name__ == '__main__':
    app.run(debug=True)


