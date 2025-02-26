import random
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
#puska
print(answer)
print("A random number has been choosen (1-100) try and guess it! ")
print("Goodluck")

guesses = 0
isrunnung = True


"""for answer in guess:
    if guess == guesses:
        print("YOU WIN")
    elif guess != guesses:
        print("INCORRECT, TRY AGAIN")
    """
while isrunnung:
    
    guess = input("Your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses =+ 1

        if guess > highest_num or guess < lowest_num:
            print("PLEASE SELECT A NUMBER (1-100) that was out of the range")
        elif guess == answer:
            print("CORRECT, YOU WON")
            break
        elif guess > answer:
            print("TRY LOWER")
        elif guess < answer:
            print("TRY HIGHER")
    else:
        print("PLEASE SELECT A NUMBER (1-100) that was not a number")