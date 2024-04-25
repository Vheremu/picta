import os
from PIL import Image, ImageDraw,ImageFont


def printpromo(image):
    im1=Image.open(image)
    width,height=im1.size
    fontsfolder='C:\Windows\Fonts'
    tahomaFont = ImageFont.truetype(os.path.join(fontsfolder, 'STENCIL.ttf'), width*0.02)
    
    print(width)
    print(height)
    draw1 = ImageDraw.Draw(im1)
    draw1.rectangle((width*0.625, height*0.35, width*0.83,height*0.5), fill='red')
    draw1.text((width*0.63, height*0.36), 'Get 10% Off', fill='blue', font=tahomaFont,fontsize=width*0.03)
    draw1.text((width*0.63, height*0.39), 'PROMO CODE', fill='white', font=tahomaFont)
    draw1.text((width*0.63, height*0.43), 'Your Code', fill='green', font=tahomaFont)
    draw1.text((width*0.63, height*0.47), 'Here!', fill='yellow', font=tahomaFont)
    im1.save('static/images/promo.png')
   
    return im1

def printpromocode(image,promocode):
    im1=Image.open(image)
    width,height=im1.size
    fontsfolder='C:\Windows\Fonts'
    tahomaFont = ImageFont.truetype(os.path.join(fontsfolder, 'STENCIL.ttf'), width*0.02)
    
    print(width)
    print(height)
    draw1 = ImageDraw.Draw(im1)
    draw1.rectangle((width*0.625, height*0.35, width*0.83,height*0.5), fill='red')
    draw1.text((width*0.63, height*0.36), 'Get 10% Off', fill='blue', font=tahomaFont,fontsize=width*0.03)
    draw1.text((width*0.63, height*0.39), 'PROMO CODE', fill='white', font=tahomaFont)
    draw1.text((width*0.63, height*0.43), str(promocode), fill='green', font=tahomaFont)
    draw1.text((width*0.63, height*0.47), 'Now!', fill='yellow', font=tahomaFont)
    im1.save('static/images/promo.png')
    im1.save('promo2.png')
   
    return im1
x=printpromocode('promo.png','hello')
def saveimage(image):
    im1=image
    im1.save('promo2.png')
def printpromo2():
    im1=Image.open('promo.png')
    width,height=im1.size
    fontsfolder='C:\Windows\Fonts'
    tahomaFont = ImageFont.truetype(os.path.join(fontsfolder, 'STENCIL.ttf'), width*0.03)
    
    print(width)
    print(height)
    draw1 = ImageDraw.Draw(im1)
    draw1.rectangle((width*0.625, height*0.35, width*0.83,height*0.5), fill='red')
    draw1.text((width*0.63, height*0.36), 'Get 10% Off', fill='blue', font=tahomaFont,fontsize=width*0.03)
    draw1.text((width*0.63, height*0.39), 'PROMO CODE', fill='white', font=tahomaFont)
    draw1.text((width*0.63, height*0.43), 'Your Code', fill='green', font=tahomaFont)
    draw1.text((width*0.63, height*0.47), 'Now!', fill='yellow', font=tahomaFont)
    im1.save('promo2.png')

print('helloworld'+'how are your guys')