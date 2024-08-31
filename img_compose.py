#处理图片的工具 pillow
#pip install pillow
from PIL import Image
import os

im = Image.open('./图片合成/imag_f/1.jpg') #1用图片名替换
w,h = im.size

image_row = 4
image_col = 4

names = os.listdir('./图片合成/imag_f'):

#新的画布大小
new_img = Image.new('RGB', (w*image_col, h*image_row))

for y in range(image_row):
    for x in range(image_col):
        #打开图片
        o_img = Image.open('./图片合成/imag_f'+names[image_col*y+x])
        new_img.paste(o_img, (w*x, h*y))
new_img.save('new_img.jpg')