from scamp import *
import random

s = Session(tempo=130)

drums = s.new_midi_part("drums", 2)

def play_hat():
    for _ in range(8):
        p = random.uniform(0,1)
        if p > 0.3:
            drums.play_note(42, 1, 0.5)
        else:
            drums.play_note(42, 1, 0.25)
            drums.play_note(42, 1, 0.25)
        
def play_backbeat():
    for i in range(4):
        if i in [0,2]:
            pb = random.uniform(0,1)
            if pb > 0.3:
                drums.play_note(36, 1, 1)
            else:
                drums.play_note(36, 1, 0.5)
                drums.play_note(36, 1, 0.5)
                
        else:
            ps = random.uniform(0,1)
            if ps > 0.5:
                drums.play_note(38, 1, 1)
            else:
                drums.play_note(38, 1, 0.75)
                drums.play_note(38, 1, 0.25)
                
                
while True:
    s.fork(play_hat)
    s.fork(play_backbeat)
    s.wait_for_children_to_finish()