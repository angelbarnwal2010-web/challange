import random 
secret_number=random.randint(1,100)
attemps=7

print("Guess the number between 1 and 100")
print("You have 7 attemps.")

while attemps>0:
    guess=int(input("Enter your guess: "))

    if guess==secret_number:
        print("🎉Correct! you won!")
        break
    elif guess<secret_number:
        print("Too Low!")
    else:
        print("Too high!")

    attemps=-1
    print("Remaining attemps:",attemps)    

if attemps==0:
    print("😢Game Over!The number was:" ,secret_number)