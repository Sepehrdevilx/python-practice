
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget



class Touch(Widget):
    def on_touch_down(self, touch):
        print("touch down" , touch)
    
    def on_touch_move(self, touch):
        print("touch move" , touch)
    
    def on_touch_up(self, touch):
        print("touch up" , touch)


class MyApp(App):
    def build(self):
        return Touch()
    

if __name__ == "__main__":

    MyApp().run()
