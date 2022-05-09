
import os
import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter
from PIL import ImageFont

size = 1080, 1080
filter_choice = input('Filters (BLUR, CONTOUR, DETAIL, EMBOSS)')
png_images = [image for image in os.listdir() if image.endswith('.png')]
for png_image in png_images:
    try:
        im = Image.open(png_image)
        im = im.resize((1080, 1080))
        if filter_choice == 'BLUR':
            im = im.filter(ImageFilter.BLUR)
        elif filter_choice == 'CONTOUR':
            im = im.filter(ImageFilter.CONTOUR)
        elif filter_choice == 'DETAIL':
            im = im.filter(ImageFilter.DETAIL)
        elif filter_choice == 'EMBOSS':
            im = im.filter(ImageFilter.EMBOSS)

        width, height = im.size

        draw = ImageDraw.Draw(im)
        text = "THEBEST"
        font = ImageFont.truetype("arial.ttf", 82)

        textwidth, textheight = draw.textsize(text, font)

        # calculate the x,y coordinates of the text
        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin

        # draw watermark in the bottom right corner
        draw.text((x, y), text, fill=(0, 0, 255), font=font)
        im.save('resized'+png_image)
        print(im.size)

    except IOError as error:
        print('Error')
