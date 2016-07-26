#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Date: 2016/7/26
# Author: Acceml

from PIL import Image, ImageFont, ImageDraw


def add_num(img):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    color = "#ff0000"
    width, height = img.size
    draw.text((width - 40, 0), '100', font=font, fill=color)
    img.save('ans.jpg', 'jpeg')


if __name__ == '__main__':
    im = Image.open('no_num.png')
    add_num(im)
