TOP DOWN DESIGN

first version
def main():
    #print out introduction and title
    printIntro()
    #calculate freq of each word
    freq()
    #display word cloud in window
    display()
    #undraw irrelavant things in the window
    undraw()
    #avoid overlaps between different words in word cloud
    avoidOverlap()

main()


second version
def main():
    win=GraphWin("Word Frequency",600,600)
    win.close()      
main()
def printIntro(win):
    #print intro
    #print title
    #create inputbox
    #create entry button
def freq(listofWord with frq,textfile,numofwordEnter):
    #loop through textfile
    #loop through stopword file
    #remove punctuation
    #remove stop words
    #if word is not in stopword
    #append it to newlist
    #sort word dictionary by frequency

def display(textfile,numofwordEnter):
    #loop through every word in wordlist(after removing irrelavant things)
    #find the maxcount(the word exist most)
    #loop through each word
    #font size varies depend on the freq of word
def avoidOverlap(numofwordEnter):
    #create a list
    #create grid
    #generate random points
    #check if that point is the same as others
    #append the word to list
def undraw():
    #create a white rectangle covers everything
    #draw the rec
    
third version:
    third version is the final code
    it is in this folder(file: proj4_jyi)
    

    
       


    
    
    
    


