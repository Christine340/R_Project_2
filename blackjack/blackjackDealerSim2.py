#Simulating the dealer in blackjack

## Needs minor modifications
## Triple pounds (###) indicate either:
##      1. that line was altered from the in-class version, or
##      2. you need to change something here for the lab

from random import *

def main():
    #print intro
    printIntro()
    #input num games to be simulated
    totalGames = eval(input("How many dealer hands do you want to simulate for each possible starting card?")) ###
    print ("The percentage of busted games for each possible starting card is as follows." )###
    ### for each possible starting card
    for startCard in range(1,14): ### this loop was not here before
        #simulate the blackjack dealer totalGames times and record how many times the dealer busted
        numBusted = simulateGames(totalGames, startCard) ### we are sending TWO arguments here now!
        #output summary of simulation results
        print ( "For starting card " + str(startCard) + " bust percentage is "  + str(float(numBusted)/totalGames*100))
    
### Simulates the blackjack dealer n times for each possible starting card
### (Fix this function so that it has two parameters, as the call from the main function requires.)
def simulateGames(n,initialCard):
    totalBustedGames = 0
    #do this n times:
    for i in range(n):
        ### Simulate game with the given initial showing card and see if dealer busts
        if dealerBusts(initialCard): ### <-- this function call now needs an argument... what should you pass it?
            #add one to the total number of busted games
            totalBustedGames += 1
    return totalBustedGames

### Deals out one dealer-hand that starts with the given initialCard
# and returns True if dealer busts, False otherwise
total=0
def dealerBusts(initialCard): ### The initialcard parameter has been added
    
    ### This is no longer necessarily the default initial value of hasAce,
    ### because the initialcard might be an Ace!
    hasAce=False
    total=0
    if initialCard==1:### <-- so you need an if statement around this
       hasAce=True
    elif initialCard==11 or initialCard==12 or initialCard==13:
        initialCard=10
    ### This is also no longer initially true,
    ### since we now already have an initial card with some value...
    total = total+initialCard ### <-- so fix it!

    #keep dealing cards until total reaches 17
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
        
def printIntro():
    print ("This is a program that computes how often blackjack dealers bust.")
    print ("You input the number of times you want the simulation to be run.")
    print ("I output the percentage of times the dealer busts, for each initial dealer card. ") ###
    print ()

main()
