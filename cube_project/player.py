#!/bin/python3

import pygame as py
import data

pos = [0, 0]
size = [40, 40]
vel = 1 / 100

jump_timer = 0
jump = False

def movement():
    keys=py.key.get_pressed()

    if pos[1] >= (data.height - size[1]):

        if keys[py.K_UP] or keys[py.K_w]:
            if jump == False and jump_timer == 0:
                jump = True
        
        elif jump == True:
            jump = False
            jump_timer = 500

    if keys[py.K_RIGHT] or keys[py.K_d]:
        pos[0] += vel * data.dt
    elif keys[py.K_LEFT] or keys[py.K_a]:
        pos[0] -= vel * data.dt

    if jump == True:
        pos[1] -= vel * data.dt

    if jump_timer > 0:
        jump_timer -= 1
