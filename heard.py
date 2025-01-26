import turtle
import math
import time

def xt(t):
    return 16 * math.sin(t) ** 3

def yt(t):
    return 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)

t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)
screen = turtle.Screen()
screen.bgcolor(0, 0, 0)
"""whle True:
    t.penup()
    t.goto(0, 0)
    t.pendown()
    for i in range(300)"""
while True:
    t.penup()
    t.goto(0, 0)
    t.pendown()
    for i in range(2550):
        t.goto(xt(i) * 20, yt(i) * 20)
        t.pencolor(255 - i % 255, i % 255, (255 + i) // 2 % 255)
        t.goto(0, 0)
    t.clear()
    time.sleep(0.5)
