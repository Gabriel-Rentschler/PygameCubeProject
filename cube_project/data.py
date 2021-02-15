#!/bin/python3

import pygame as py

screensize = width, height = 720, 480

clock = py.time.Clock()
dt = clock.tick(60)

g = 9.806 / 100

black = 0, 0, 0
red = 255, 0, 0
blue = 0, 0, 255
green = 0, 255, 0

def gravity(position, size, vel, tick):
    gforce = 0
    TerminalVelocity = lambda g, ming, maxg: max(min(maxg, g), ming)

    if position[1] < (height - size[1]):
        tick += 0.001
        gforce = (g*pow(tick, 2)) * dt
        gforce = TerminalVelocity(gforce, 0, 0.3)
        position[1] += gforce
    elif position[1] >= (height - size[1]):
        tick = 0

    return position, tick
