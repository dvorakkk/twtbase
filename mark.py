from PIL import Image, ImageDraw, ImageFont
caption = 'jawafess'
img = Image.open('temp2.jpg')
d = ImageDraw.Draw(img)
font = ImageFont.truetype('upakarti.ttf', size=40)
d.text((60, 60), caption, fill='green', font=font, spacing=3, align = 'center', stroke_width=3, stroke_fill= 'white')
img.save('temp3.jpg')