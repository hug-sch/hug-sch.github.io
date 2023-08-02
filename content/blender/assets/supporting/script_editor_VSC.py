# context.area: SEQUENCE_EDITOR
import bpy
import numpy as np
import os
os.system('cls')
animated_samples = np.empty(shape=[0, 1])
strip = bpy.context.scene.sequence_editor.active_strip

def print_strip_parameters(strip):
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print('{:20}:{:2}'.format("start", strip.frame_start))
    print('{:20}:{:2}'.format("duration start", strip.frame_duration))
    print('{:20}:{:2}'.format("<<calculated END>>", strip.frame_start + strip.frame_duration))
    print('{:20}:{:2}'.format("final start", strip.frame_final_start))
    print('{:20}:{:2}'.format("final end", strip.frame_final_end))
    print('{:20}:{:2}'.format("offset start", strip.frame_offset_start))
    print('{:20}:{:2}'.format("offset end", strip.frame_offset_end))
    print('{:20}:{:2}'.format("still start", strip.frame_still_start))
    print('{:20}:{:2}'.format("still end", strip.frame_still_end))
    print("------------------------------------------------------")

print_strip_parameters(strip)
print("Start at frame 1000")
strip.frame_start = 1000
print("Start at frame 1")
print("End at frame 3500")
strip.frame_start = 1
#strip.frame_duration = 3500 --- frame_duration is read-only
strip.frame_final_end = 3500
print_strip_parameters(strip)
print("Start at frame 300")
strip.frame_start = 300
print_strip_parameters(strip)

print("End at frame 500")