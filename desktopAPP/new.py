import kivy
kivy.require("1.10.0")
from kivy.app import App
from kivy.uix.button import Label
class HelloKivy(App):
    def build(self):
        return Label(text="hello there")
hel=HelloKivy()
hel.run()