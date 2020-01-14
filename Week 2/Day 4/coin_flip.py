import random 

def flip_coin():
	'''
	returns a coin flip, random int between 0 and 1; 
	1 = heads
	0 = tails
	'''
	return random.randint(0,1)
#result = random.randint(0,1))

#every number has the same chance of coming up

#if result == 1: 
#	print("heads")
#else: 
#	print("tails")

def monte_carlo(n):
	'''
	performs monte carlo sim of coin flip 
	[PARAM]\t n (int) - number of samples
	[RETURN]\t None - prints ot the result of the sim 
	'''
	head_count = 0
	tail_count = 0
	exp_count = 0 
	while exp_count < n:
		result = flip_coin()
		if result == 1:
			head_count += 1
		else: 
			tail_count += 1
		exp_count += 1
	print(f"There were {n} sims performed.")
	msg = f"There were {head_count} heads" #format and message
	print(msg)
	msg = f"There were {tail_count} tails"
	print(msg)
	msg = f"There were {(head_count)/n *100} % heads" #format and message
	print(msg)


	#this is how to print without the print("stuff")
monte_carlo(100)
#in your cmd, you can start up python, you'll get >>>> and to quit, you can write quit()
#we used to check how to see helps


#help(flip_coin)

