#!/bin/env python3

from record import start, finish
from leaf import draw
import turtle

L = 400
N = 3
LL = L/N*(N+1)

start(LL, LL, 0, -LL/2, 50, __file__)

turtle.speed('fast')
turtle.left(90)
draw(L, N)

finish()