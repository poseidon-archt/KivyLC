from kivy.app import App
from kivy.uix.label import Label
import os

class MyApp(App):
    def build(self):
        current_dir = os.getcwd()
        label = Label(text=current_dir)
        return label

if __name__ == '__main__':
    MyApp().run()
