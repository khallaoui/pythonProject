from kivy.app import App
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
from kivy.uix.button import Button

Window.clearcolor = (89 / 255.0, 7 / 255.0, 45, 3)
Window.size = (370, 600)


class Name(App):
    s = SoundLoader.load('Anne.mp3')

    if s: s.play()


if __name__ == '__main__':
    Name().run()
