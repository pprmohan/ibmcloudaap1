from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/login1', methods = ['POST',"GET"])
def login1():
    NAME = request.form['NAME']
    EMAIL = request.form['EMAIL']
    if NAME == "srikanth" and EMAIL == "srikanth@gmail.com":
        return " Welcome to portal"
    else:
        return render_template("register.html")

@app.route('/register1', methods = ['POST','GET'])
def register1():
    NAME = request.form['NAME']
    EMAIL = request.form['EMAIL']
    PASSWORD = request.form['PASSWORD']
    return render_template("login.html")
    

if __name__ == "__main__":
    app.run(debug = True,port = 5000,host ='0.0.0.0')