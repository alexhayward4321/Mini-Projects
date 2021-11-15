# -*- coding: utf-8 -*-
"""
Just a quick project I made to 
"""

import winsound
import random
import time

start_time = time.perf_counter()
sound_dict = {"one": "C:/Users/alexh/OneDrive/Documents/Coding/Python/Mini_projects/Exercise routine/Voice_files/One_1.wav",
              "two": "C:/Users/alexh/OneDrive/Documents/Coding/Python/Mini_projects/Exercise routine/Voice_files/Two_1.wav",
              "three": "C:/Users/alexh/OneDrive/Documents/Coding/Python/Mini_projects/Exercise routine/Voice_files/Three_1.wav"}


while time.perf_counter() - start_time < 60:
    number = random.choice(list(sound_dict.values()))
    dur1 = 500
    dur2 = random.randrange(10)+2
    winsound.PlaySound(number, winsound.SND_FILENAME)
    time.sleep(dur2/4)
