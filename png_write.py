import datetime
from datetime import timedelta
from PIL import Image, ImageFont
from PIL import ImageDraw
def get_date():
	#return date of most recent Monday
	today = datetime.datetime.today()

	if today.weekday() == 0:
		the_date = today
	else:
		the_date = today - timedelta(days=today.weekday())

	return the_date.strftime("%m/%d/%Y")

def find_v_border(png):
	h = png.height
	png_ims = png.load()
	x = 250
	for y in range(h-1,0,-1):
		v = png_ims[x,y]
		sum_v = sum(v)
		if sum_v < 1010:
			print("IT IS HERE: " + str(y))
			return y	
def find_right_border(png,bottom_border):
	png_ims = png.load()
	for x in range(1,250):
		v = png_ims[x,bottom_border]
		if sum(v) < 1010:
			print("x is " + str(x))
			return x

def draw_on_image(raw_img, new_img,date_text):
	
	font_size = 16
	png = Image.open(raw_img)
	offset = font_size + 3
	bottom_border = find_v_border(png) - offset
	right_border = find_right_border(png,bottom_border) + 3

	fg="#000000"
	fnt = ImageFont.truetype('OpenSans-Bold.ttf',font_size)
	
	draw = ImageDraw.Draw(png)
	draw.text((right_border,bottom_border), date_text,font=fnt, fill=fg)
	del draw
	png.save(new_img, "PNG",quality=100)

img_text = get_date() + " Server Vulnerabilities"
raw_img = "summaryImage.png"
new_img = "final_image.png"
draw_on_image(raw_img,new_img,img_text)
