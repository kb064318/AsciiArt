from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.lang.builder import Builder
from kivy.core.image import Image
from plyer import filechooser

class LayoutScreen(Widget):
    pass

class SelectButton(Widget):
    def choose_file(self):
        path = filechooser.open_file(title="Select a Photo", 
                             filters=[("Photos", "*.png")])
        print(path)
        m = Image.load(path, keep_data=True)
        color = m.read_pixel(x, y)
        return color[0] * 255

class ButtonMain(App): 
    def build(self):
        Builder.load_file('button.kv')
        return SelectButton()

ButtonMain().run()
