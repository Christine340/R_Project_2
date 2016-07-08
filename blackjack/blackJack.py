 #black jack

def main():
    printIntro()
    #input num games to be simulated
    totalGames=eval(input("How many simulations of the dealer shall I run? "))
    #simulate that many deals,counting how many were busts
    numBusts=simDeals(totalGames)
    #output summary
    print("The percentage of busted games is "+str(numBusted/totalGames*100))
    
    
def printIntro():
    #outline
def simDeals(n):
    #outline
