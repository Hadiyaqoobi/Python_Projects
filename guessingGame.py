import random

def computerGuess(lowval, highval, randnum, count=0):
    if highval >= lowval:
        guess = lowval + (highval - lowval) // 2
        # if guess is in the middle, it is found!
        if guess == randnum:
            return count
        # if Guess is greater than the number,
        # it must be found in the lower half of the set of numbers
        #between the lower balue nad the guess.

        elif guess > randnum:
            count = count + 1
            return computerGuess(lowval, guess-1, randnum, count)
        else:
            count = count +1
            return computerGuess(lowval, guess, randnum, count)

    else:
    # Number not found
        return -1
    # Enf of the Function

#Generate a random number between 1 and 100
randnum = random.randint(1, 101)

count = 0
guess = -99

while (guess != randnum):
    #Get the user's guess

    guess = int(input("Enter your guess between 1 and 100:"))



    if guess < randnum:
        print("Higher")
    elif guess > randnum:
        print("Lower")
    else:

        print("you guessed it!")
        break
    count = count + 1
#End of the while loop

print("You took" + str + " steps the guess the number")

print("Computer took" + str(computerGuess(0, 100, randnum))+ "steps!")
