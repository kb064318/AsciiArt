from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder
from kivy.core.image import Image
from plyer import filechooser

class LayoutScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LayoutScreen, self).__init__(**kwargs)
        self.cols = 3
        self.add_widget(Label(text="image1"))
        self.add_widget(Label())
        self.add_widget(Label(text="image2"))
        self.add_widget(Label(text="image3"))
        btn = SelectButton()
        btn.bind(on_press=btn.choose_file)
        self.add_widget(btn)
        self.add_widget(Label(text="image4"))
        self.add_widget(Label(text="image5"))
        self.add_widget(Label())
        self.add_widget(Label(text="image6"))

class SelectButton(Button):
    def choose_file(self, val):
        path = filechooser.open_file(title="Select a Photo", 
                             filters=[("Photos", "*.png")])
        print(path)
        m = Image.load(path, keep_data=True)
        color = m.read_pixel(x, y)
        return color[0] * 255

class ButtonMain(App): 
    def build(self):
        #Builder.load_file('button.kv')
        return LayoutScreen()

ButtonMain().run()
