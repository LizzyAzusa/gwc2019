from PIL import Image

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    im= Image.open(filename)
    return im

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(im):
    im.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(im,filename):
    im.save(filename,"jpeg")
    show_img(im)


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(im):
    #load the pixel data
    pixels= im.getdata()
    #print (list(pixels))
    #create a list to hold the new image pixel data
    new_pixels=[]

    #Define the color constants
    darkBlue= (0,51,76)
    red=(217,26,33)
    lightBlue=(112,150,158)
    yellow=(252,227,166)

    for p in pixels:
        intensity=p[0]+p[1]+p[2]

        if intensity<182:
            new_pixels.append(darkBlue)

        elif intensity >= 182 and intensity < 364:
            new_pixels.append(red)

        elif intensity >= 364 and intensity < 546:
            new_pixels.append(lightBlue)

        elif intensity >=546:
            new_pixels.append(yellow)

    #save the modified pixels as a new Image
    newim= Image.new("RGB",im.size)
    newim.putdata(new_pixels)
    return newim
