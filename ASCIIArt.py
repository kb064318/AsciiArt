from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.core.image import Image
from kivy.config import Config
from plyer import filechooser
from pixelConversionAlgorithm import algorithm, text_to_image
import os

# Front-End Design. - Lets us organize the GUI.
class LayoutScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LayoutScreen, self).__init__(**kwargs)
        # finds button object and binds the choose_file function to the on_press event
        btn = self.ids.selectbtn # selectbtn is the id of the button object in the .kv file
        btn.bind(on_press=SelectButton.choose_file)

# Returns pixel RGB value of an image at specified coordinates
def get_pixel(img, x, y):
    color = img.read_pixel(x, y)
    return color[0] * 255, color[1] * 255, color[2] * 255

# Returns the grayscale value of a pixel (white = 0, black = 1)
def get_pixel_gray(img, x, y):
    gray = img.read_pixel(x, y)
    return (gray[0]*0.299) + (gray[1]*0.587) + (gray[2]*0.114)

# Back-end for file browse button.
class SelectButton(Button):
    def choose_file(self):
        # Opens file chooser
        file_path = filechooser.open_file(title="Select a Photo to convert", 
                             filters=[("Photos", "*.jpg")])
        #print(*filePath)
        # Declares img as the image picked
        img = Image.load(*file_path, keep_data=True)
        # Runs the algorithm from pixelConversionAlgorithm
        ascii_string = algorithm(*file_path)
        # Path to save image to
        photo_name = "ASCII_art.png"
        # Converts ASCII to image. text_to_image is imported from pixelConversionAlgorithm
        ascii_image = text_to_image(*file_path, ascii_string, photo_name)
        # Opens created image
        os.system(photo_name)
        # Prints all pixel RGB values in file
        #for i in range(0, img.size[0]):
        #    for j in range (0, img.size[1]):
        #        print(i, j, get_pixel(img, i, j))

class ASCIIArt(App): 
    def build(self):
        return LayoutScreen()

ASCIIArt().run()
