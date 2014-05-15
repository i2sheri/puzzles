import image

img = Image.open('oxygen.png')
''.join([chr(img.getpixel((x,47))[0]) for x in range(0, 629, 7)])
list = [105, 110, 116, 101, 103, 114, 105, 116, 121]
''.join(map(chr,list))
