from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder
from kivy.core.image import Image
from plyer import filechooser

from PIL import Image

class algorithm():
    im = Image.open('octopus.jpg',  'r')
    width, height = im.size
    pix_val = list(im.getdata())
    for x in range(len(pix_val)):
        if(x % width == 0):
            print("")
        if (pix_val[x][0] < 126):
            #black
            print('M',end="")
        else:
            #white 
            print(" ", end="") 
        
        