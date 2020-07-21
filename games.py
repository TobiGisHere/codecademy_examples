import random

money = 100


#----------------------------------------------------------
#---------COINFLIP-----------------------------------------
#----------------------------------------------------------

def coinflip(bet, guess):

    if guess == "heads": #change string to integer
        guess_nr = 1
    elif guess == "tails":
        guess_nr = 2
    else:
        print("Wrong input")
        return 0

    if bet > money: #check, if enough money is left
        print("You only have " +str(money) +" left")
        return 0
    
    print("---------------------------") #information for user
    print("You guessed: " +str(guess))
    print("Coin is flipping, aaaaaand it's:")
    print("...")
    result = random.randint(1,2) #flip coin
    if result ==1:
        print("heads")
    else:
        print("tails")

    if result == guess_nr: #print win or loss
        print("You won " +str(bet) +" dollars")
        return bet
    else:
        print("You lost " +str(bet) +" dollars")
        return -bet



#----------------------------------------------------------
#---------CHO-HAN------------------------------------------
#----------------------------------------------------------

def cho_han(bet, guess):
   
    if bet > money:
        return "You only have " +str(money) +" Dollars"

    else:
        print("-------------------------------------")
        print("You've placed " +str(bet) +" Dollars")
        print("Your guess was " +str(guess))
        print("...")
        result1 = random.randint(1,6)
        result2 = random.randint(1,6)
        result = result1 + result2

        if result%2 == 0:
            even_odd = "even"
        else:
            even_odd = "odd"
        print("Dices say " +str(result1) +" and " +str(result2) +". So it's " +str(even_odd))
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        
        if even_odd == guess:
            return "Hey you're right. You won " +str(bet) +" Dollar!"
        else:
            return "... you lost " +str(bet) +" Dollar"


#----------------------------------------------------------
#---------CARD GAME----------------------------------------
#----------------------------------------------------------

def card_game(bet):
    if bet > money:
        print("You only have " +str(money) +" Dollars")
    else:
        player1 = random.randint(1,10)
        player2 = random.randint(1,10)
        if player1 == player2:
            player2 = random.randint(1,10)
        print("Your card is " +str(player1) +" and your oppenents card is " +str(player2))
        
        if player1 > player2:
            print("You won " +str(bet) +" Dollars")
            return bet
        elif player1 < player2:
            print("You lost " +str(bet) +" Dollars")
            return -bet
        else:
            print("It's a tie, try again")
            return 0
    



#----------------------------------------------------------
#---------ROULETTE-----------------------------------------
#----------------------------------------------------------




#----------------------------------------------------------
#---------PRINT FUNCTIONS----------------------------------
#----------------------------------------------------------


#coinflip(10,"heads")
#print(cho_han(25, "even"))
card_game(10)