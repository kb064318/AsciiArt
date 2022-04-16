from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.core.image import Image
from kivy.config import Config
from kivy.resources import resource_add_path, resource_find
from plyer import filechooser
from pixelConversionAlgorithm import algorithm, text_to_image
import os
import sys
import threading

'''
Front-End Design. - Lets us organize the GUI.
'''
class LayoutScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LayoutScreen, self).__init__(**kwargs)
        # finds button object and binds the choose_file function to the on_press event
        btn = self.ids.selectbtn # selectbtn is the id of the button object in the .kv file
        btn.bind(on_press=SelectButton.choose_file)

'''
Returns pixel RGB value of an image at specified coordinates
'''
def get_pixel(img, x, y):
    color = img.read_pixel(x, y)
    return color[0] * 255, color[1] * 255, color[2] * 255



#class Title(TitleImage):


'''
Back-end for file browse button.
'''
class SelectButton(Button):
    def choose_file(self):
        # Tells the user the image is loading
        App.get_running_app().root.ids.label_loading.text = "Loading Image..."
        # Runs choose_file_threaded on another thread. Without this, the label is not updated until after the function is complete.
        threading.Thread(target=self.choose_file_threaded).start()
        
    def choose_file_threaded(self):
        # Opens file chooser
        file_path = filechooser.open_file(title="Select a Photo to convert", 
                    filters=[("Photos", "*.jpg", "*.png")])
        if len(file_path) != 0:
            # Runs the algorithm from pixelConversionAlgorithm
            ascii_string = algorithm(*file_path)
            # Path to save image to
            photo_name = "ASCII_art.png"
            # Converts ASCII to image. text_to_image is imported from pixelConversionAlgorithm
            text_to_image(*file_path, ascii_string, photo_name)
            # Opens created image
            os.system(photo_name)
            # Removes label_loading text
        App.get_running_app().root.ids.label_loading.text = ""

class ASCIIArt(App): 
    def build(self):
        self.title = "ASCII Art Generator"
        return LayoutScreen()

'''
Helps this app be converted into a standalone executable
'''
if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    ASCIIArt().run()
