from PIL import Image
im = Image.open("cat!.jpg")
new_image = Image.new(im.mode, im.size)
new_image.save("output.jpg", "jpeg")

data = im.getdata()
data = list(data)

darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

recolored = [ ]

for elem in data:
    number = elem[0] + elem[1] + elem[2]
    if number < 182:
        elem = darkBlue
        recolored.append(elem)
    elif 182 < number < 364:
        elem = red
        recolored.append(elem)
    elif 364 < number < 546:
        elem = lightBlue
        recolored.append(elem)
    elif number > 546:
        elem = yellow
        recolored.append(elem)
    else:
        recolored.append(elem)

new_image = Image.new("RGB", im.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
