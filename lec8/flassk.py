from flask import Flask
from PyQt5 import QtWidgets
import pyfiglet,termcolor
# my_app=pyfiglet.figlet_format("hello")
my_app=Flask("happy")
app=QtWidgets.QApplication([])


@my_app.route("/")
def home():
    return r'<button> WoW</button>',r'<h1>Hello Moto</h1>'

@my_app.route("/bye")
def hello():
    return "hello vaibhav!!"


if __name__ =="__main__":
    my_app.run( port=8080)