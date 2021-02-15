#!/bin/python3

import pygame as py
import sys, player, data

py.init()

screen = py.display.set_mode(data.screensize)

fall_tick = 0

#Game Loop
while 1:
    for event in py.event.get():
        if event.type == py.QUIT: sys.exit()

    player.jump, player.pos, player.jump_timer = player.movement()
    player.pos, jump_tick = data.gravity(player.pos, player.size, player.vel, fall_tick)

    
    p_model = py.Rect(player.p_pos, player.p_size)

    cube_model = py.Rect(100, 0, 80, 40)

    screen.fill(data.black)
    py.draw.rect(screen, data.blue, cube_model)
    py.draw.rect(screen, data.red, p_model)
    py.display.flip()
