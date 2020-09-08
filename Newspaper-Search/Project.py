import zipfile as zip
import pytesseract as tess
import cv2
import PIL.Image as Img
import numpy as np

images = {}
img__names = []
face_cascade = cv2.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')


def final(img_names, name):
    for img_name in img_names:
        faces = []
        img = images[img_name][0]
        text = tess.image_to_string(img).replace('\n', '')
        if name in text:
            print(f'Results found in {img_name}')
            face = face_cascade.detectMultiScale(np.array(img), 1.35, 4)
            for (x1, y1, w, h) in face:
                face_pic = np.array(img)[y1: y1 + h, x1: x1 + w]
                faces.append(Img.fromarray(np.uint8(face_pic)))
            if len(faces) == 0:
                print("But there were no faces in that file!")
            else:
                rem = len(faces) % 5
                temp = 5 - rem
                lines = int((len(faces) + temp) / 5)
                contact_sheet = Img.new(img.mode, (110 * 5, 110 * lines))
                x = 0
                y = 0
                for person in faces:
                    person.thumbnail((110, 110))
                    contact_sheet.paste(person, (x, y))
                    if x + 110 == contact_sheet.width:
                        x = 0
                        y = y + 110
                    else:
                        x = x + 110

                cv2.imshow('Contact Sheet', contact_sheet)


zip_files = zip.ZipFile('readonly/small_img.zip')
for file in zip_files.infolist():
    file_name = file.filename
    temp_img = zip_files.open(file_name)
    images[file_name] = [Img.open(temp_img)]
    img__names.append(file_name)

final(img__names, 'Mark')
