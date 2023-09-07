from flask import Flask

app=Flask(__name__)

@app.route('/')

def welcome():
    return "Welcome to IBM Faculty Development Program"

@app.route('/shivam')

def greet():
    return "Shivam Shivhare Working in SB"

if __name__=='__main__':
    app.run(debug=True)