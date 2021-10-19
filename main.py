from random import randint

# add player 
playerLives = 5
computerLives = 5

# Save the player as a variable called player
# the value of player will be one of three choices to type (input)
player =input("chosse rock, paper or scissors: ")

print("player chose: " + player)

# an array is just a container. It bholds multiple values in a 0-based index
# you can store anything in an array and retrieve it later. Arrays have square bracket notation
choices = ["rock", "paper", "scissors"]

computer = choices[randint(0,2)]

print("computer chose: " + computer)

if (computer == player):
	print("Tie! Try egain")

elif (player == "rock"):
	if (computer == "paper"):
		print("you lose!")
		playerLives = playerLives - 1
	else:
		print("you win!")
		computerLives = computerLives - 1

elif (player == "paper"):
	if (computer == "scissors"):
		print("you lose!")
		playerLives = playerLives - 1
	else:
		print("you win!")
		computerLives = computerLives - 1

elif (player == "scissors"):
	if (computer == "rock"):
		print("you lose!")
		playerLives = playerLives - 1
	else:
		print("you win!")
		computerLives = computerLives - 1

print("computer Lives: " + str(computerLives))
print("player Lives " + str(playerLives))