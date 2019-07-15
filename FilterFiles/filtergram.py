import filters




def main():
    while True:
        filters.load_img("dogPic.jpg")
        filters.show_img(image1)
        filters.save_img(image1, "dogPic.jpg")


main()
