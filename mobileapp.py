import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.graphics import Rectangle
from kivy.graphics import * 

class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch,self).__init__(**kwargs)
        with self.canvas:
            Line(points = (20,30,400,500,60,500))
            Color (1., 0, 0)
            self.rect = Rectangle(pos=(0,0), size=(50,50))



    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        #print('move', touch)
    
    def on_touch_down(self, touch):
        self.rect.pos = touch.pos
        #print('down', touch)
class MyApp(App):
    def build(self):
        return Touch() # Label(text = "for fun")


if __name__ == "__main__":
    MyApp().run()
