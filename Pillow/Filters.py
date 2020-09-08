from PIL import Image
from PIL import ImageFilter
from matplotlib import pyplot as plt
from PIL import ImageDraw

# 242 79 298 148
img = Image.open('../codevita/data\\smarties.png')
# img.show()
# img2 = img.copy()
# img2.show()
# img2.save("smarties2.jpg")
rgb_img = img.convert('RGB')
blurred = rgb_img.filter(ImageFilter.BLUR)
blurred1 = rgb_img.filter(ImageFilter.GaussianBlur)
emboss = rgb_img.filter(ImageFilter.EMBOSS)
box_blur = rgb_img.filter(ImageFilter.BoxBlur(1))
sharp = rgb_img.filter(ImageFilter.SHARPEN)
median = rgb_img.filter(ImageFilter.MedianFilter)
cropped = rgb_img.crop((242, 79, 298, 148))
drawing = ImageDraw.Draw(rgb_img)
drawing.rectangle((242, 79, 298, 148), fill=None, outline='blue')
names = ['Default', 'RGB', 'Normal Blur', 'Gaussian Blur', 'Box Blur', 'Emboss', 'Sharpen', 'Median Filter', 'Cropped']
pics = [img, rgb_img, blurred, blurred1, box_blur, emboss, sharp, median, cropped]

for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.imshow(pics[i])
    plt.title(names[i])
    plt.xticks([]), plt.yticks([])

plt.show()
