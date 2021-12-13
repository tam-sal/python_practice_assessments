# -*- coding: utf-8 -*-

### Standalone Project
'''1 -The purpose of this project is to take a gif image and create 9 copies of this image concatenated in a contact sheet taking into consideration that the color channel should be adjusted for each image and a label should be added specifying the color channel and intensity'''

import PIL
from PIL import Image, ImageFilter, ImageDraw, ImageEnhance, ImageFont

image = Image.open("readonly/msi_recruitment.gif").convert("RGB")
im_x, im_y = image.width, image.height
intensity = [0.1, 0.5, 0.9]
font = ImageFont.truetype('readonly/fanwood-webfont.ttf', 40)
colors = ["red", "green", "blue"]
images = []
for color in colors:
    for intensity_level in intensity:
        created_image = Image.new(image.mode, (im_x, int(im_y*1.1)))
        for x_pixel in range(im_x):
            for y_pixel in range(im_y):
                red, green, blue = image.getpixel((x_pixel,y_pixel))
                if color == "red":
                    red = int(red*intensity_level)
                    created_image.putpixel((x_pixel, y_pixel), (red,green,blue))
                    
                elif color == "green":
                    green = int(green*intensity_level)
                    created_image.putpixel((x_pixel, y_pixel), (red,green,blue))
                    
                else:
                    blue = int(blue*intensity_level)
                    created_image.putpixel((x_pixel, y_pixel), (red,green,blue))
            
            n_red, n_green, n_blue = created_image.getpixel((im_x/2, im_y/2))
            txt_box = ImageDraw.Draw(created_image)
            txt_box.rectangle((im_x,im_y,0,int(im_y*.999)), fill = "black")
            txt_box.text((im_x*0,int(im_y)), f"channel {colors.index(color)} intensity {intensity_level}", font = font, fill = (n_red, n_green, n_blue))
        images.append(created_image)

first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
contact_sheet.show()
display(contact_sheet)


################# Final Project for the program ###
'''The Project
This is a project with minimal scaffolding. Expect to use the the discussion forums to gain insights! It’s not cheating to ask others for opinions or perspectives!
Be inquisitive, try out new things.
Use the previous modules for insights into how to complete the functions! You'll have to combine Pillow, OpenCV, and Pytesseract
There are hints provided in Coursera, feel free to explore the hints if needed. Each hint provide progressively more details on how to solve the issue. This project is intended to be comprehensive and difficult if you do it without the hints.
The Assignment
Take a ZIP file) of images and process them, using a library built into python that you need to learn how to use. A ZIP file takes several different files and compresses them, thus saving space, into one single file. The files in the ZIP file we provide are newspaper images (like you saw in week 3). Your task is to write python code which allows one to search through the images looking for the occurrences of keywords and faces. E.g. if you search for "pizza" it will return a contact sheet of all of the faces which were located on the newspaper page which mentions "pizza". This will test your ability to learn a new (library), your ability to use OpenCV to detect faces, your ability to use tesseract to do optical character recognition, and your ability to use PIL to composite images together into contact sheets.

Each page of the newspapers is saved as a single PNG image in a file called images.zip. These newspapers are in english, and contain a variety of stories, advertisements and images. Note: This file is fairly large (~200 MB) and may take some time to work with, I would encourage you to use small_img.zip for testing.

Here's an example of the output expected. Using the small_img.zip file, if I search for the string "Christopher" I should see the following image:Christopher SearchIf I were to use the images.zip file and search for "Mark" I should see the following image (note that there are times when there are no faces on a page, but a word is found!):Mark Search

Note: That big file can take some time to process - for me it took nearly ten minutes! Use the small one for testing.'''

import zipfile
import PIL
from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

# the rest is up to you!

images = {}
name_list = []

zf = zipfile.ZipFile('readonly/images.zip')
info = zf.infolist()
for item in info:
    file_name = item.filename
    images[file_name] = [Image.open(zf.open(file_name))]
    name_list.append(file_name)

for name in name_list:
    img = images[name][0]    
    images[name].append(pytesseract.image_to_string(img).replace('\n',' '))
    
    if 'Mark' in images[name][1]:
        print('Results found in file', name)
        
        try:
            faces = (face_cascade.detectMultiScale(np.array(img), 1.3, 5)).tolist()
            images[name].append(faces)
            faces_in_image = []
            
            for x,y,w,h in images[name][2]:
                faces_in_image.append(img.crop((x,y,x+w,y+h)))
            
            contact_sheet = Image.new(img.mode, (550,110*int(np.ceil(len(faces_in_image)/5))))
            x = 0
            y = 0
        
            for face in faces_in_image:
                face.thumbnail((110,110))
                contact_sheet.paste(face, (x,y))
                
                if x+110 == contact_sheet.width:
                    x=0
                    y = y + 110
                else:
                    x= x + 110
            display(contact_sheet)
        except:
            print('But there were no faces in that file!')
