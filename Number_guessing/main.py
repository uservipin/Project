import math
import random

lower = int(input("Please input lower limit \n"))
upper = int(input("Please input upper limit \n"))

ran_int= random.randint(lower, upper)
max_chances = int(math.log(upper-lower+1,2))

print(f"you have {max_chances} chanches to guess the No.")

counter= 0


while max_chances > counter:
    counter += 1
    guess_number= int(input("Guess the Number"))
    if guess_number ==ran_int:
        print(f"Congratulation you did it in {counter} no of count")
        break

    elif max_chances > guess_number:
        print("Your guess to small ")
    elif max_chances < guess_number:
        print("Your guess is too high")
if counter >= max_chances:
    print(f" \n The number is {max_chances} \n Better luck Next  Time!")

