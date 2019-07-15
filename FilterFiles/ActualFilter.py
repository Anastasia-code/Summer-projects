from PIL import Image

def filterFunc(image1):


def main():
    image1 = Image.open('dogPic.jpg')
    image1.show()
    image1.save()
    filterFunc(image1)


main()



#Below is code from internet:

# Imported PIL Library
from PIL import Image, ImageDraw


# Open an Image
def open_image(path):
    newImage = Image.open(path)
    return newImage


# Save Image
def save_image(image, path):
    image.save(path, 'png')


# Create a new image with the given size
def create_image(i, j):
    image = Image.new("RGB", (i, j), "white")
    return image


# Get the pixel from the given image
def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
        return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel
