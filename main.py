from random import randint
import sys
print("Welcome to Guess the number game!!")
print("Guess the number from 1-10")
print("SO easy! now guess the number!")
def hint(count,number):
    if count == 0:
        if number % 2 == 0:
            print("HINT: The number is an EVEN number")
        else:
            print("HINT: The number is an ODD number")
    elif count == 2:
        print("WRONG again!")
        if number * 2 >= 10:
            print("HINT: if the number was multiplied by 2 the product is a TWO digit number")
        elif number * 2 < 10:
            print("HINT: if the number was multiplied by 2 the product is a ONE digit number")
    elif count == 3:
        print("NO MORE HINTS!!!!")
    elif count >= 5:
        print("YOU ARE TROLLING!!")
count = -1
number = randint(1,11)
while True:
    count += 1
    print(number)
    user_answer = int(input("Your answer is "))
    if user_answer == number:
        print("You are Correct!")
        again = input("Wanna play again? [y/(anyinput)]: ")
        if again == "y":
            count = -1
            number = randint(1, 11)
            continue
        else:
            sys.exit()
    else:
        print("Oppsie, Try Again!")
    hint(count,number)


