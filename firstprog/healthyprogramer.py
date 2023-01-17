from pygame import mixer
from datetime import datetime
from time import time
def musicloop(file,stopp):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if (a == stopp):
            mixer.music.stop()
            break
def log(mm):
    with open ("mylog.txt","a") as f:
        f.write(f"{mm}{datetime.now()}\n")
if __name__=='__main__':
    # musicloop("Four More Shots Please Yaara Teri Yaari Full Song Darshan Raval.mp3","stop")
    init_water= time()
    init_eyes= time()
    init_break= time()
    watersecs=5
    eyesec=10
    breaksec=5
    while True:
        if time() - init_water > watersecs:
            print("drinking time .enter s to stop song")
            musicloop("river-1.mp3","s")
            init_water=time()
            log("drank wayer at ")
        if time() - init_eyes > eyesec:
            print("drinking time .enter s to stop song")
            musicloop("eye.mp3","s")
            init_eyes=time()
            log("drank wayer at ")
        if time() - init_break > breaksec:
            print("drinking time .enter s to stop song")
            musicloop("Four More Shots Please Yaara Teri Yaari Full Song Darshan Raval.mp3","s")
            init_break=time()
            log("drank wayer at ")
