from graphics import *
import time
from random import randrange

win = GraphWin("Demo of Zelle's win.checkMouse() method", 600,600)

prompt = Text(Point(300,100),"Click below the time to exit.  Click above it to change its color")
prompt.draw(win)

output = Text(Point(300,300), time.ctime())
output.draw(win)

while True:
    output.setText(time.ctime())
    pt = win.checkMouse()
    if pt != None:
        if pt.getY() > 300:
            break
        else:
            output.setFill(color_rgb(randrange(0,256), randrange(0,256), randrange(0,256)))

win.close()
