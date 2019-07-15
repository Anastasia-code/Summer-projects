# Rename this file to be "filters.py"
# Add commands to import modules here.
import PIL
from PIL import Image
import os



# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(name):
    image1 = Image.open('dogPic.jpg')
    return image1

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(image1):
    image1.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(image1, name):
    image1.save()

# # Define your obamicon() function here.
# #       Parameters: The image object to apply the filter to.
# #       Returns: A New Image object with the filter applied.
# def obamicon():


load_img(input())
