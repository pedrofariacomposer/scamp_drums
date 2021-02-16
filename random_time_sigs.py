from scamp import *
import random

s = Session(tempo=140)

drums = s.new_midi_part("drums", 2)

def play_hi_hat(x,hat):
    for _ in range(x):
        i = random.uniform(0,1)
        if i > 0.4:
            drums.play_note(hat,1,0.5)
        else:
            drums.play_note(hat, 1, 0.25)
            drums.play_note(hat, 1, 0.25)


def play_backbeat():
    
    i = random.uniform(0,1)
    if i > 0.4:
        drums.play_note(36,1,1)
    else:
        drums.play_note(36,1,0.75)
        drums.play_note(36,1,0.25)
        
    j = random.uniform(0,1)
    if j > 0.4:
        drums.play_note(38,1,1)
    else:
        drums.play_note(38,1,0.75)
        drums.play_note(38,1,0.25)
 

while True:
    i = random.uniform(0,1)
    if i > 0.3:
        s.fork(play_hi_hat,args=(7,42))
        s.fork(play_backbeat)
        wait(3.5)
    else:
        s.fork(play_hi_hat,args=(9,53))
        s.fork(play_backbeat)
        wait(4.5)