from PIL import Image
from PIL import ImageEnhance
import matplotlib.pyplot as plt

img = Image.open('smarties2.jpg')
enhancer = ImageEnhance.Brightness(img)
images = []
for i in range(1, 10):
    temp = enhancer.enhance(i / 10)
    images.append(temp)

# for i in range(9):
#     plt.subplot(3, 3, i + 1)
#     plt.imshow(images[i])
#     plt.xticks([]), plt.yticks([])

plt.show()

frame = images[0]
contact_sheet = Image.new(frame.mode, (frame.width * 3, frame.height * 3))

x = 0
y = 0
for i in images:
    contact_sheet.paste(i, (x, y))
    if x + frame.width == contact_sheet.width:
        x = 0
        y += frame.height
    else:
        x += frame.width

contact_sheet = contact_sheet.resize((int(contact_sheet.width / 2), int(contact_sheet.height / 2)))
contact_sheet.show()
