import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 24)

imageFile = "nico.jpg"
im1 = Image.open(imageFile)

draw = ImageDraw.Draw(im1)
draw.text((160,0),"4", (255,0,0),font=font) #设置文字位置/内容/颜色/字体
draw = ImageDraw.Draw(im1)

im1.save("nico_new.jpg")