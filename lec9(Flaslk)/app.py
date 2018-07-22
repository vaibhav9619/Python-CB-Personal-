from flask import Flask,request,render_template
from people import user
app = Flask(__name__)

@app.route("/users/<name>")
def prof(name):
    return render_template("home.html",name=user[name]["name"],hobby=user[name]["hobby"])

@app.route("/")
def home():
    return "Hello world"

@app.route("/action",methods=["POST"])#to hit on /action in html page (name will be same in both for hitting)
def login():
    print(request.form.get("email"))
    print(request.form.get("pwd"))
    return "Now you are login as"+request.form.get("email")

@app.route("/ok")
def house():
    return "bbye"
# debugger mode on while hititng
# app.run(port=8080,debug=True)#for different port


@app.after_request# for clearing previous cache
def add_header(response):

    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

app.run(debug=True)