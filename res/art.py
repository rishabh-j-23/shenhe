import random
import os
from os import listdir
import discord


class Art:
    def art():
        folder_dir = "res/images/art"
        image = []
        try:
            for images in os.listdir(folder_dir):
                if (images.endswith(".png") or images.endswith(".jpg")
                        or images.endswith(".jpeg")):
                    image.append(images)
        except Exception as e:
            print(e)

        return random.choice(image)
