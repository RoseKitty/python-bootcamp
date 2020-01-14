
import random
def dice_roll():
	'''
	returns a coin flip, random int between 0 and 1; 
	1 = 1
	2 = 2
	3 = 3
	4 = 4
	5 = 5 
	6 = 0
	'''
	return random.randint(0,5)


def dice_roll_results(n):
	'''
	performs monte carlo sim of coin flip 
	[PARAM]\t n (int) - number of samples
	[RETURN]\t None - prints ot the result of the sim 
	'''
	count1 = 0
	count2 = 0
	count3 = 0
	count4 = 0
	count5 = 0
	count6 = 0
	
	exp_count = 0 
	#for exp in range(0,n):
	#	if roll_dice(dice_max) == 1:
	#		one_counter += 1
	while exp_count < n:
		result = dice_roll()
		if result == 1:
			count1 += 1
		elif result == 2: 
			count2 += 1
		elif result == 3: 
			count3 += 1
		elif result == 4: 
			count4 += 1
		elif result == 5: 
			count5 += 1
		else: 
			count6 += 1
		exp_count += 1
	print(f"There were {n} sims performed.")
	
	msg = f"There were {count1} 1s"  #format and message
	print(msg)
	
	msg = f"There were {count2} 2s"
	print(msg)
	
	msg = f"There were {count3} 3s"
	print(msg)
	
	msg = f"There were {count4} 4s"
	print(msg)
	
	msg = f"There were {count5} 5s"
	print(msg)
	
	msg = f"There were {count6} 6s"
	print(msg)


	msg = f"There were {(count1)/n *100} % 1" #format and message
	print(msg)
	msg = f"There were {(count2)/n *100} % 2"
	print(msg)
	msg = f"There were {(count3)/n *100} % 3"
	print(msg)
	msg = f"There were {(count4)/n *100} % 4"
	print(msg)
	msg = f"There were {(count5)/n *100} % 5"
	print(msg)
	msg = f"There were {(count6)/n *100} % 6"
	print(msg)

dice_roll_results(10)


#can also use:
def roll_dice(highest_n):
	return random.randint(1,highest_n)
#def roll_choice():
#this one needs a list
#	sides = [1,2,3,4,5,6]
#	return random.choice(sides)

#monte carlo with lists
def monte_carlos_w_lists(N, die_max=6): #die_max = optional for user, default is 6
	results = []
	for exp in range(0,N):
		results.append(roll_dice(die_max))
	print(f"{N} experiments were made")
	for outcome in range(1,die_max +1):
		count = results.count(outcome)
		msg = f"The probability of result of {outcome} is = {(count/N *100)} % "
		print(msg)
monte_carlos_w_lists(10)

#or 
#monte_carlos_w_lists(10,10)#10 sided die! 


