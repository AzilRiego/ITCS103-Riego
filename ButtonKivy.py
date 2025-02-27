import kivy
from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        btn = Button(text="Button", font_size="20sp", background_color=(1, 1, 1, 1), color =(1, 1, 1, 1), size =(100, 60), size_hint=(None, None), pos =(300, 250))
        btn.bind(on_press = self.callback)
        return btn
    def callback(self, event):
        print("Someone Pressed The Button")
    
root = ButtonApp()
root.run()