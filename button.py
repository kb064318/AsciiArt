from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder
from kivy.core.image import Image
from kivy.config import Config
from plyer import filechooser

# Front-End Design. - Lets us organize the GUI.
class LayoutScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LayoutScreen, self).__init__(**kwargs)
        self.cols = 3                   # Creates three columns for the widgets to occupy.
        self.add_widget(Label(text="")) 
        self.add_widget(Label())
        self.add_widget(Label(text=""))
        self.add_widget(Label(text=""))
        btn = SelectButton()
        btn.bind(on_press=btn.choose_file)
        self.add_widget(btn)
        self.add_widget(Label(text=""))
        self.add_widget(Label(text=""))
        self.add_widget(Label())
        self.add_widget(Label(text=""))

# Returns pixel RGB value of an image at specified coordinates
def get_pixel(img, x, y):
    color = img.read_pixel(x, y)
    return color[0] * 255, color[1] * 255, color[2] * 255

# Back-end for file browse button.
class SelectButton(Button):
    def choose_file(self, val):
        # Opens file chooser
        filePath = filechooser.open_file(title="Select a Photo to convert", 
                             filters=[("Photos", "*.png")])
        # Declares img as the image picked
        print(*filePath)
        img = Image.load(*filePath, keep_data=True)
        # Prints all pixel RGB values in file
        for i in range(0, img.size[0]):
            for j in range (0, img.size[1]):
                print(i, j, get_pixel(img, i, j))

class ASCIIArt(App): 
    def build(self):
        #Builder.load_file('button.kv')
        return LayoutScreen()

ASCIIArt().run()
