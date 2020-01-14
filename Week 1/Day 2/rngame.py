#import #in C++, you did #include
#import the random module
import random

#winning_number = random.randint(0,10)
#print(winning_number)

#simple version
#guess = int(input("Enter your guess: "))
#if guess == winning_number:
#	print("Congrats, you win")
#else:
#	print("Nope")

#num_guesses = 2 
#user_won = False
#while num_guesses != 0 and user_won == False:
#	user_guess = int(input("Enter your guess: "))
#	if user_guess == winning_number:
#		user_won = True
#		print("You win!")
#	else:
#		num_guesses -= 1
#		if num_guesses == 0:
#			print("Nope, you lose. T..T!!!")
#		else:
#			print("Nope, try again")
#fill

#range of numbers is 0-100. randint makes both inclusive, num_of_guesses = 10 
#if user is within 5, print "hot", if 10, print "warm". else print "cold"
#also keep track of the user guesses in a list. #when the game is over, output the number of tries and their guesses

winning_number2 = random.randint(0,100)
print(winning_number2)
#Don't print this later if you want to play the game 4real
num_guesses2 = 5
count = 0
guess_list = []
user_won2 = False
while num_guesses2 != 0 and user_won2 == False:
	user_guess2 = int(input("Enter your guess: "))
	guess_list.append(user_guess2) 
	#putting append here instead of after logic statements because then you write less
	if user_guess2 == winning_number2:
		user_won2 = True
		print("You win!")
		count += 1
	else:
		num_guesses2 -= 1
		if num_guesses2 == 0:
			print("Nope, you lose. T..T!!!")
			print("The winning number was:", winning_number2)
			count += 1
		else:
			if user_guess2  >= winning_number2 - 5 and user_guess2 <= winning_number2 + 5:
				print("Hot")
			elif user_guess2  >= winning_number2 - 10 and user_guess2 <= winning_number2 + 10:
					print("Warm")
			#note my prior had and else there^ and always print the nopes. 
			#elseif is for secondary and takes out some words 
			else:
				print("Cold")
			count += 1
print("The number of guesses:", count)
print("You guessed:", guess_list)
