from graphics import *
from random import *
import math 

def printIntro(win):
    #create a title
    title=Text(Point(300,20),"Welcome to word cloud")
    #size size of title to be bigger
    title.setSize(36)
    #draw title
    title.draw(win)
    #prompt user to click anywhere to close
    prompt=Text(Point(300,300),"Click anywhere to begin")
    #set size to 25
    prompt.setSize(25)
    #display the prompt
    prompt.draw(win)
    #get user mouse click
    win.getMouse()
    #undraw title and prompt
    title.undraw()
    prompt.undraw()
    #print an introduction
    intro=Text(Point(300,100),"This program calcualtes word frequency and display as word cloud\nyou can enter text file and number of words you want to display in word cloud\nwords with larger frequency appear bigger")
    intro.setSize(15)
    intro.draw(win)
    #prompt user to enter name of text file he/she wants to work with
    prompt=Text(Point(100,200),"Enter name of text file:")
    prompt.draw(win)
    #give user example of text file he/she should enter
    example=Text(Point(100,220),"(Example: poem.txt,MarkTwain.txt)")
    example.draw(win)
    #prompt user to enter number of words he/she wants to display in the word 
    prompt2=Text(Point(100,300),'Enter number of words:')
    prompt2.draw(win)
    #give user example of number to enter
    example2=Text(Point(100,320),"(Example: 20,50)")
    example2.draw(win)

#define function to calculate frequency
def freq(text,usernumword):
    #remove punctuation
    for p in '!\"#$%()&*+-,./;:<=>?@[\\]^_{|}~\'':
        text=text.replace(p,"")
        
    

    #open stop words file
    inputfile=open("stopwords.txt","r")
    #read stop words
    stopword=inputfile.read()
    #split stop words into a list
    stopwordList=stopword.split()
    #split original file into a list
    wordlist=text.split()

    #create a newlist
    newlist=[]
    #loop
    for word in wordlist:
        #convert all words to lower case
        #so that it does not generate case-sensitive problem
        #for example:computer and Computer will count as same word now
        word=word.lower()
        #if word is in stopword,ignore it
        #if word is not in stopword, append it to the newlist
        if word not in stopword:
            newlist.append(word)
    #create a count dictionary
    counts={}
    maxcount=0
    #loop to count occurence of words and store occurence in dictionary
    for w in newlist:
        counts[w]=counts.get(w,0)+1
        #find the maximum count in this file
        #this maxcount will be used later when display words size
        if counts[w]>maxcount:
            maxcount=counts[w]
    #add words into a list
    items=list(counts.items())
    #sort these words by occurence
    items.sort(key=byFreq,reverse=True)
    #return the list of words and maximum-count word
    return items,maxcount

#create a function to display word cloud
def display(listofWords,usernumword,win,text):
    #calculate freq function returns items and maxcount 
    items,maxcount = freq(text,usernumword)
    #avoid overlap of the words function
    listofPoints=avoidOverlap(usernumword)
    #if user input num word is greater than the num of different words in file
    #reset the value of user num to length of items
    if usernumword>len(items):
        usernumword=len(items)
    #loop
    for i in range(usernumword):
        word,count=items[i-1]
        displayword=Text(listofPoints[i],word)
        displayword.draw(win)
        #make word randomly displayed on screen
        r=randrange(255)
        g=randrange(255)
        b=randrange(255)
        #dispaly word and set color randomly
        displayword.setTextColor(color_rgb(r,g,b))
        #set word size based on occurence
        #the bigger the count, the bigger the word size
        if count>0.8*maxcount:
                displayword.setSize(50)
 
        elif count>0.5*maxcount:
                displayword.setSize(35)                                                       
        elif count>0.2*maxcount:
                displayword.setSize(25)
        else:
                displayword.setSize(10)

#create draw button function
def drawButton(gwin,pt1,pt2,words):
    #set the rectangle
    button1=Rectangle(pt1,pt2)
    #set the button to be blue
    button1.setFill("blue")
    #draw button in the window
    button1.draw(gwin)
    #put word in the middle of button
    midx=(pt1.getX()+pt2.getX())/2
    midy=(pt1.getY()+pt2.getY())/2
    button1Label=Text(Point(midx,midy),words)
    #set the text in button color to be white 
    button1Label.setFill("white")
    button1Label.draw(gwin)
    return button1,button1Label

#this function retunrs freq for each word freq pair
def byFreq(pair):
        return pair[1]


#create a white rectangular to cover everything
#so that everything is undrawed(including prompts,buttons)
#except two inputboxes(where i undraw them in main function)
def undraw(win):
    rectangle=Rectangle(Point(0,0),Point(600,650))
    rectangle.draw(win)
    rectangle.setFill("white")

#this function avoid overlap between words
#this function make square grids for each word
def avoidOverlap(usernumword):
    #store x,y and coords
    y=[]
    x=[]
    coords=[]
    #square root of user-enter words
    w=math.sqrt(usernumword)
    #round up square root to whole integer
    w2=math.ceil(w)
    #the width/height of window divide by number of words user want to dispaly
    #make space for grids
    division=int(580/w2)
    #loop
    for i in range(w2):
        #pick x and y coordinate for each word into a grid
        #i*division: which row/line to go
        #division/2: put point in the center of grid section
        x.append(int((division/2)+(i*division)))
        y.append(int((division/2)+(i*division)))
        
    #loop x list and y list of positions
    for i in range(w2):
        for j in range(w2):
            #create a list of each x,y pair coordinate
            coords.append(Point(x[i],y[j]))

    #randomness the positions of the list
    shuffle(coords)
    return coords

#define main function
def main():
    #create graphical window
    win=GraphWin("Word Frequency",600,650)
    #set background to pink
    win.setBackground("pink")
    #call printintro function
    printIntro(win)
    #create entry box for entering text file
    inputbox=Entry(Point(300,200),30)
    inputbox.draw(win)
    inputbox.setText("MarkTwain.txt")
    #create entry box for entering num of words user wants to display
    inputbox2=Entry(Point(300,300),30)
    inputbox2.draw(win)
    inputbox2.setText("30")
    #set default to be marktwain
    #get user mouse click
    #create an enter button
    enterbutton=drawButton(win,Point(450,200), Point(500,300),"Enter")
    click=win.getMouse()
    x=click.getX()
    y=click.getY()
    
    #get text from inputbox
    text1=inputbox.getText()
    #get value from entry box
    usernumword=int(inputbox2.getText())
    #while user not click enter button,continue on clicking
    #until user click enter button
    while not (450<=x<=500 and 200<=y<=300):
        click=win.getMouse()
        x=click.getX()
        y=click.getY()
    #read the text file from that user enter
    inputfile=open(str(text1),"r",encoding="utf-8")
    #read the file
    text=inputfile.read()
    #undraw two inputboxes
    undraw(win)
    inputbox.undraw()
    inputbox2.undraw()
        
    #call freq function to calculate occurence of words
    listofWords=freq(text,usernumword)
    #call display function to display words in window
    display(listofWords,usernumword,win,text)

    #create exit button
    exitbutton=drawButton(win,Point(250,610), Point(325,650),"Exit")
    #get user mouse click
    click=win.getMouse()
    x=click.getX()
    y=click.getY()
    #while user not click exit button,continue clicking
    #untile user click exit button
    while not (250<=x<=325 and 610<=y<=650):
        click=win.getMouse()
        x=click.getX()
        y=click.getY()
    #close the window
    win.close()
       
main()
