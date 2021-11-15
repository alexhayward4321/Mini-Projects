# -*- coding: utf-8 -*-
"""
A project I never got to that was planning to use the gtts library to set out
an exercise routine.
"""

from playsound import playsound
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play


sound = AudioSegment.from_file("C:/Users/alexh/OneDrive/Documents/Coding/Python/Mini_projects/Exercise routine/Voice_files/One_1.wav", format="wav")

# simple export
file_handle = sound.export("C:/Users/alexh/OneDrive/Documents/Coding/Python/Mini_projects/hello.wav", format="wav")

tts = gTTS('hello')
tts.save("hello.mp3")

playsound("C:/Users/alexh/OneDrive/Documents/Coding/Python/Mini projects/hello.mp3")
