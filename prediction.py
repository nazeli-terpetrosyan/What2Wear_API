from PIL import Image
from io import BytesIO
import numpy as np
import array as arr
import math
import requests
import cv2

def predict(img_front, img_side, height):
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': img_front},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'wUwxPYmeSjBD7853HAcoPcj5'},
    )
    if response.status_code == requests.codes.ok:
        with open('no-bg.png', 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)

    img = cv2.imread("no-bg.png")

    boy = height
    chap_front = arr.array('i',[0,0,0])

    s = 1
    for i in range(len(img)):
        s = np.sum(img[i] != 0)
        if s != 0:
            chap_front.append(s)


    mekichap_frontt = round((1 / (boy / (len(chap_front)-3))) * 100) / 100

    bust_fr = round(round((chap_front[round(boy * 17.3 / 100 * mekichap_frontt)] * ((boy / (len(chap_front) -3)) / 3)) * 100) / 100)
    waist_fr = round(round((chap_front[round(boy * 38.2 / 100 * mekichap_frontt)] * ((boy / (len(chap_front) -3)) / 3)) * 100) / 100 - 25)
    hip_fr =round(round((chap_front[round(boy * 52.3 / 100 * mekichap_frontt)] * ((boy / (len(chap_front) -3)) / 3)) * 100) / 100 - 10)

    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': img_side},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'wUwxPYmeSjBD7853HAcoPcj5'},
    )
    if response.status_code == requests.codes.ok:
        with open('no-bg.png', 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)

    img = cv2.imread("no-bg.png")

    chap_prof = arr.array('i',[0,0,0])

    s = 1
    for i in range(len(img)):
        s = np.sum(img[i] != 0)
        if s != 0:
            chap_prof.append(s)

    mekichap_proff = round((1 / (boy / (len(chap_prof)-3))) * 100) / 100

    bust_pr = round(round((chap_prof[round(boy * 17.3 / 100 * mekichap_proff)] * ((boy / (len(chap_prof) -3)) / 3)) * 100) / 100)
    waist_pr = round(round((chap_prof[round(boy * 38.2 / 100 * mekichap_proff)] * ((boy / (len(chap_prof) -3)) / 3)) * 100) / 100 - 10)
    hip_pr = round(round((chap_prof[round(boy * 52.3 / 100 * mekichap_proff)] * ((boy / (len(chap_prof) -3)) / 3)) * 100) / 100 - 20)

    bust = round(2 * 3.14 * math.sqrt((math.pow((bust_fr/2), 2) + math.pow((bust_pr/2), 2))/2))
    waist = round(2 * 3.14 * math.sqrt((math.pow((waist_fr/2), 2) + math.pow((waist_pr/2), 2))/2))
    hip = round(2 * 3.14 * math.sqrt((math.pow((hip_fr/2), 2) + math.pow((hip_pr/2), 2))/2))

    return {"bust": bust, "waist": waist, "hip": hip }