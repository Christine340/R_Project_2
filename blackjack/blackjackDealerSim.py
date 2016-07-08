#COM110 blackjack simulation
#This program simulates the dealer in blackjack

from random import *

def main():
    #print intro
    printIntro()
    #ask user for input
    totalGames = eval(input("How many blackjack dealer hands shall I simulate? "))
    #simulate the blackjack dealer totalGames times and record how many times the dealer busts
    numBusted = simulateGames(totalGames)
    #output summary of simulation results
    print ("The percentage of hands the dealer busted is " +str(round(numBusted/totalGames*100,2)))

#Deal out n hands following dealer rules to see how often the dealer busts.
#Returns the number of times the dealer busts out of n games
 
def simulateGames(n):
    totalBustedGames = 0
    #do this n times:
    for i in range(n):
        #simulate a game to see if the dealer busts
        if dealerBusts():
            totalBustedGames = totalBustedGames + 1
            #if so, add one to the total number of busted games
    return totalBustedGames


#Deals out one dealer-hand,
#returning True if dealer busts, and False otherwise
def dealerBusts():
    hasAce = False #flag that indicates whether dealer has an ace in their hand
    total = 0
    #(so far, no ca ds dealt, so ace flag is "down" and point total of dealer is 0)
    #deal cards until "soft 17" is reached
    while total < 17:
        num=randrange(1,14)
        #generate a random number between 1 and 13 to simulate dealing a card
        #(a 1 will represent ace, 11 - jack, 12 - queen, and 13 - king)
        
        #if card is a face card, adjust it's value to 10
        if num==11 or num==12 or num==13:
             num=10
        #else, if card is an Ace, then
            #raise that boolean ace flag
        elif num==1:
            hasAce=True
        
        #add the value of the card to total
        total=total+num

        #if there is an ace in the hand and the total with ace as 11 is between 17 and 21
            #adjust total so ace counts as 11
        if hasAce and total+10<=21:
            total=total+10
            hasAce=False
          
    #return true if dealer busted, false otherwise
    if total<=21:
        return False
    else:
        return True
#Prints introduction to program, explains to the user what will happen                                                        
def printIntro():
    print ("This is a program that computes the percentage of time blackjack dealer has busted.")
    print ("The input is the number of times the simulation should be run")
    print ("The output is the percentage of time the dealer busted ")
    print ()

main()
