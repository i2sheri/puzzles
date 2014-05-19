"""first and second are available in Level 9"""

import Image, ImageDraw

img = Image.open('good.jpg')
draw = ImageDraw.Draw(img)
draw.polygon(first, 'red')
draw.polygon(second, 'red')
img.save('super.png', 'png')
