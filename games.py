import random

money = 100



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

print(cho_han(25, "even"))