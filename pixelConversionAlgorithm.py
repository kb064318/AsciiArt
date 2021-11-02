from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder
from PIL import Image, ImageDraw, ImageFont

def algorithm(path):
    im = Image.open(path,  'r')
    width, height = im.size
    pix_val = list(im.getdata())
    ascii_string = ""
    print("Converting photo to ascii... (May take a while)")
    for x in range(len(pix_val)):
        if(x % width == 0):
            ascii_string += "\n"
        if (pix_val[x][0] < 126):
            #black
            ascii_string += "M"
        else:
            #white
            # This amount of spaces is required to make the photo look normal
            ascii_string += "    "
    im.close()
    return ascii_string
        
'''
Converts text to png file and saves it to photo_name. Having this in the same
file as a function that uses kivy.core.image causes namespace problems.
'''
def text_to_image(path, ascii_string, photo_name):
    print("Saving image...")
    
    # Gets width and height of image
    im = Image.open(path,  'r')
    width, height = im.size
    im.close()

    # Generates an image based on the contents of ascii_string and saves it
    ascii_font = ImageFont.truetype('calibri.ttf', 10)
    ascii_image = Image.new(mode="RGB", size=(width*9, height*12), color=(255, 255, 255))
    draw_ascii = ImageDraw.Draw(ascii_image)
    draw_ascii.text(xy=(0, 0), text=ascii_string, font=ascii_font, fill=(0, 0, 0))
    ascii_image.save(photo_name)
    return ascii_image
