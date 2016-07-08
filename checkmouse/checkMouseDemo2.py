from graphics import *
import time
from random import randrange

win = GraphWin("Demo of Zelle's win.checkMouse() method", 600,600)

prompt = Text(Point(300,100),"Click below the time to exit.  Click above it to change its color")
prompt.draw(win)

output = Text(Point(300,300), time.ctime())
output.draw(win)

pt = None #set initial value for the Point object to null, or "None" since no clicks yet


oldTime=time.time()#returns the time in total seconds that have elapsed since the start of the epoch.
print(oldTime)
#if no new clicks or if new click just taken in this loop was above the output text, keep the loop going
while pt == None or pt.getY() < 300: 
    output.setText(time.ctime()) #update the output field with the current time
    #(note it is looping so fast that usually just outputting the same time again and we can't see it change)
    #print(time.ctime())  #add this line back in if you want to see how fast we're looping in the shell!
    pt = win.checkMouse() #check if mouse was clicked since last check.
    #(usually not b/c we're looping so fast, so usually the checkMouse returns None.)
    #print(pt) #add this line back in for proof of my claim!
    if pt != None and pt.getY() < 300: #if a new click was made and it was above the text
        #change the text color
        output.setFill(color_rgb(randrange(0,256), randrange(0,256), randrange(0,256))) 
    
win.close()
