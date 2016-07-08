from graphics import *
import time
from random import randrange

win = GraphWin("Demo of time", 600,600)

output = Text(Point(300,300), time.ctime())
output.draw(win)

while True:
    output.setText(time.ctime())
    print(time.ctime())
