#import #in C++, you did #include
#import the random module
import random

winning_number = random.randint(0,10)
print(winning_number)

#simple version
#guess = int(input("Enter your guess: "))
#if guess == winning_number:
#	print("Congrats, you win")
#else:
#	print("Nope")

num_guesses = 2 
user_won = False
while num_guesses != 0 and user_won == False:
	user_guess = int(input("Enter your guess: "))
	if user_guess == winning_number:
		user_won = True
		print("You win!")
	else:
		num_guesses -= 1
		if num_guesses == 0:
			print("Nope, you lose. T..T!!!")
		else:
			print("Nope, try again")
#fill

#range of numbers is 0-100. randint makes both inclusive, num_of_guesses = 10 
#if user is within 5, print "hot", if 10, print "warm". else print "cold"
#also keep track of the user guesses in a list. #when the game is over, output the number of tries and their guesses

winning_number2 = random.randint(0,100)
print(winning_number2)

num_guesses2 = 2 
count = 0
user_won2 = False
while num_guesses2 != 0 and user_won2 == False:
	user_guess2 = int(input("Enter your guess: "))
	if user_guess2 == winning_number:
		user_won2 = True
		print("You win!")
	else:
		num_guesses2 -= 1
		if num_guesses2 == 0:
			print("Nope, you lose. T..T!!!")
		else:
			print("Nope, try again")
			count += 1
