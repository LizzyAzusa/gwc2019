import filters

def main():
    filename = input("Enter the name of the image file")
    #load image from the file
    img = filters.load_img(filename)
    #save the modified image
    obamicon=filters.obamicon(img)

    filters.show_img(obamicon)

    filters.save_img(obamicon,"recolored.jpeg")


main()
