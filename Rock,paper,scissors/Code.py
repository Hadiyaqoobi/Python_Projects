import random
i=0
print("Hi There ^_^")
while (i<3):
	print("\n")
	print("Rock, Paper or Scissors")
	userInput = input("Choose your weapon: [R]ock, [P]aper or [S]cissors: ")
	choices = ['R', 'S','P']
	computerChoice = random.choice(choices)
	if userInput == computerChoice :
		print("Tie")
		i=i+1
	elif userInput == 'R' and computerChoice == 'P':
		print("You choose Rock and I choose Paper, I win")
		i=i+1
	elif userInput == 'R' and computerChoice == 'S':
		print("You choose Rock and I choose Scissors, You win")
		i=i+1
	elif userInput == 'S' and computerChoice == 'P':
		print("You choose Scissors and I choose Paper, You win")
		i=i+1
	elif userInput == 'S' and computerChoice == 'R':
		print("You choose Scissors and I choose Rock, I win")
		i=i+1
	elif userInput == 'P' and computerChoice == 'R':
		print("You choose Paper and I choose Rock, You win")
		i=i+1
	elif userInput == 'P' and computerChoice == 'S':
		print("You choose Paper and I choose Scissors, I win")
		i=i+1
	else:
		print("invalid input")
		userInput = input("Choose again, [R]ock, [P]aper or [S]cissors: ")
