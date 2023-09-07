from flask import Flask
app = Flask(__name__)
@app.route('/')
def welcome():
    return "Welcome Devi"
@app.route('/shivam')

def greet():
    retutn  "my name is mohan"

if __name__ == '__main__':
    app.run(debug = True)