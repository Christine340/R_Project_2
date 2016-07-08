def main():
    #open the file for reading
    #starting the reading cursor before
    #the very first character of the file
    inputFile=open('collosus.txt',"r")

    
    #print the next line in the file
    print(inputFile.readline())
    #print the whole file
    print(inputFile.read())

    #if you want to read the file again
    #close the file and open it again
    inputFile.close()
    #
    inputFile=open('collosus.txt',"r")
    
   
main()

def main():
      inputFile=open('collosus.txt',"r")
      listofLines=inputFile.readlines()
      # how many lines are in this poem?
      lineCount=0
      for line in listofLines:
          lineCount=lineCount+1
      print(lineCount)

main()

#another way to count
def main():
      inputFile=open('collosus.txt',"r")
      poem=inputFile.read()
      lineCount=0
      for x in poem:
          if char=='\n':
             lineCount=lineCount+1
      print(lineCount)
    
main()

# if statement
# if 3<4
# its a true statement

#
if age<21:
   print('sorry')
else:
   print('Welcome')
   
