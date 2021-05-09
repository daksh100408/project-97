import random
number = random.randint(1,9)
chance = 0
print("Guess a number between 1-9")
while(chance < 5):
    guess = int(input("Enter your guess "))
    if(guess == number):
        print("Congrats you won")
        break

    elif( guess < number):
        print("Why are you thinking so low numbers, think high")
    else:
        print("You are thinking so high")

        chance = chance + 1
if not chance < 5:
    print("You lose the number is ", number)      