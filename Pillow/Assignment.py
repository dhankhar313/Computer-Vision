from PIL import Image, ImageFont, ImageDraw
from IPython.display import display

image = Image.open("smarties2.jpg")
image = image.convert('RGB')
images = []
labels = []
for i in range(3):
    for j in range(1, 10, 4):
        bands = image.split()
        mid = bands[i].point(lambda m: m * (j / 10))
        bands[i].paste(mid)
        im = Image.merge(image.mode, bands)
        labels.append(f'channel {i} intensity {j / 10}')
        images.append(im)
frame = images[0]
contact_sheet = Image.new(frame.mode, (frame.width * 3, (frame.height + 75) * 3))
x = 0
y = 0
data = ImageDraw.Draw(contact_sheet)
i = 0
font = ImageFont.truetype("readonly/fanwood-webfont.ttf", 75)
for img in images:
    contact_sheet.paste(img, (x, y))
    data.text((x, y + frame.height + 5), labels[i], font=font)
    i += 1
    if x + frame.width == contact_sheet.width:
        x = 0
        y = y + frame.height + 75
    else:
        x = x + frame.width

contact_sheet = contact_sheet.resize((int(contact_sheet.width / 2), int(contact_sheet.height / 2)))
display(contact_sheet)
