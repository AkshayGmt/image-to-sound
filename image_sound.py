# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 22:05:33 2021

@author: Lenovo
"""

from PIL import Image
from gtts import gTTS
from pytesseract import image_to_string


def image_to_sound(path_to_image):
    """
    Function for converting an  image to sound
    """
    try:
        loaded_image = Image.open(path_to_image)
        decoded_text = image_to_string(loaded_image)
        cleaned_text = " ".join(decoded_text.split("\n"))
        print(cleaned_text)
        sound = gTTS(cleaned_text, lang="en")
        sound.save("sound.mp3")
        return True
    except Exception as bug:
        print("The bug thrown while executing the code\n", bug)
        return


if __name__ == "__main__":
    image_to_sound("C:/Users/Lenovo/OneDrive/Desktop/insta/anmika_9634/111.jpg")
    input()