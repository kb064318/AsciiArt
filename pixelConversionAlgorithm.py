from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder
from PIL import Image, ImageDraw, ImageFont
import os

def algorithm(path):
    im = Image.open(path,  'r')
    width, height = im.size
    pix_val = list(im.getdata())
    for pix in pix_val:
        pix = get_pixel_gray(pix)
    ascii_list = []
    ascii_string = ""
    print("Converting photo to ascii... (May take a while)")
    for x in range(len(pix_val)):
        if(x % width == 0):
            # Adds each string as a separate element in ascii_list. Used to set the space between each line of text in text_to_image()
            ascii_list.append(ascii_string)
            ascii_string = ""
        if (pix_val[x][0] < 17):
            #black
            ascii_string += "A"
        elif (pix_val[x][0] < 34):
            #black
            ascii_string += "B"
        elif (pix_val[x][0] < 51):
            #black
            ascii_string += "C"
        elif (pix_val[x][0] < 68):
            #black
            ascii_string += "D"
        elif (pix_val[x][0] < 85):
            #black
            ascii_string += "E"
        elif (pix_val[x][0] < 102):
            #black
            ascii_string += "F"
        elif (pix_val[x][0] < 119):
            #black
            ascii_string += "G"
        elif (pix_val[x][0] < 136):
            #black
            ascii_string += "H"
        elif (pix_val[x][0] < 153):
            #black
            ascii_string += "I"
        elif (pix_val[x][0] < 170):
            #black
            ascii_string += "J"
        elif (pix_val[x][0] < 187):
            #black
            ascii_string += "K"
        elif (pix_val[x][0] < 204):
            #black
            ascii_string += "L"
        elif (pix_val[x][0] < 221):
            #black
            ascii_string += "M"
        elif (pix_val[x][0] < 238):
            #black
            ascii_string += "N"
        elif (pix_val[x][0] < 255):
            #black
            ascii_string += "O"
        else:
            #white
            ascii_string += " "
    im.close()
    return ascii_list
        
'''
Returns the grayscale value of a pixel (white = 0, black = 1)
'''
def get_pixel_gray(pixel):
    return (pixel[0]*0.299) + (pixel[1]*0.587) + (pixel[2]*0.114)

'''
Converts text to png file and saves it to photo_name. Having this in the same
file as a function that uses kivy.core.image causes namespace problems.
'''
def text_to_image(path, ascii_list, photo_name):
    print("Saving image...")
    
    # Gets width and height of image
    im = Image.open(path,  'r')
    width, height = im.size
    im.close()

    # Gets font path and size
    this_file_path = os.path.dirname(__file__)
    font_path = os.path.join(this_file_path, 'Font/DeferralSquare.ttf')
    font_size = 8 # Currently, only size 8 font works correctly
    
    # Generates an image based on the contents of ascii_string and saves it
    ascii_font = ImageFont.truetype(font_path, font_size) # Deferral Square is the base font
    ascii_image = Image.new(mode="RGB", size=(width*font_size, height*font_size), color=(255, 255, 255))
    draw_ascii = ImageDraw.Draw(ascii_image)
    for x in range(len(ascii_list)): # Draws every ascii_string in ascii_list, with a y position that makes each character equally spaced
        draw_ascii.text(xy=(0, x*font_size), text=ascii_list[x], font=ascii_font, fill=(0, 0, 0))

    ascii_image.save(photo_name)
    return ascii_image
