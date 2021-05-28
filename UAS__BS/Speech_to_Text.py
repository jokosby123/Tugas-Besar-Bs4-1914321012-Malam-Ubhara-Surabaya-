# -*- coding: utf-8 -*-
"""
Created on Fri May 28 11:19:29 2021

@author: Joko Susilo
"""

import speech_recognition as sr
r = sr.Recognizer()

with sr.AudioFile("edison.wav") as source:
    audio = r.record(source)
try:
    s = r.recognize_google(audio)
    print("Text: "+s)
except Exception as e:
    print("Exception: "+str(e))