# from pygame import mixer
# from datetime import datetime
# from time import time
# def musicloop(file,stopp):
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.play()
#     while True:
#         a = input()
#         if (a == stopp):
#             mixer.music.stop()
#             break
# def log(mm):
#     with open ("mylog.txt","a") as f:
#         f.write(f"{mm}{datetime.now()}\n")
# if __name__=='__main__':
#     # musicloop("Four More Shots Please Yaara Teri Yaari Full Song Darshan Raval.mp3","stop")
#     init_water= time()
#     init_eyes= time()
#     init_break= time()
#     watersecs=5
#     eyesec=10
#     breaksec=20
#     while True:
#         if time() - init_water > watersecs:
#             print("drinking time .enter s to stop song")
#             musicloop("river-1.mp3","s")
#             init_water=time()
#             log("drank water at ")
#         if time() - init_eyes > eyesec:
#             print("eye excercice time .enter s to stop song")
#             musicloop("salamisound-5682726-mountain-spring-gushes.mp3","s")
#             init_eyes=time()
#             log("done excercise at ")
#         if time() - init_break > breaksec:
#             print("break time .enter s to stop song")
#             musicloop("Four More Shots Please Yaara Teri Yaari Full Song Darshan Raval.mp3","s")
#             init_break=time()
#             log("break over at ")


















import time
import datetime
import pygame
from pygame import mixer

# current_time=time.strftime("%H:%M:%S")
# startt='08:00:00'
# endss='05:00:00'

#for drinking water
drinking_time=5
water_mp3="water.mp3"

#for relaxing eyes
# eyes_time=10
# eye_mp3="eye.mp3"

#for excercise
# excer_time=15
# excer_mp3="excer.mp3"

def play_musicon(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

def waterrem():
    i=''
    while(i != "drank"):
        play_musicon(water_mp3)
        i=input("did u drank water?if YES type drank").lower()
        if (i=="drank"):
            print("thank you!!")
            mixer.music.stop()
            time.sleep(drinking_time)
            break


# def eyerem():
#     i=" "
#     while(i != "eyedone"):
#         play_musicon(eye_mp3)
#         i=input("did u drank water?if YES type eyedone").lower()
#         if (i=="eyedone"):
#             print("thank you!!")
#             mixer.music.stop()
#             break
#
# def excerrem():
#     i=" "
#     while(i != "exdone"):
#         play_musicon(water_mp3)
#         i=input("did u drank water?if YES type exedone").lower()
#         if (i=="exedone"):
#             print("thank you!!")
#             mixer.music.stop()
#             break
