#finding the roots of a function between a specific region

def f(x):
	return 2*x + 1

def find_root(a, b):
	c = (a + b)/2 #assume c is in the middle
	ans = f(c)
	num_iteration = 0
	while ans != 0 and num_iteration < 100:
		num_iteration += 1
		c = (a + b)/2 
		ans = f(c)
		if ans (ans > 0):
			b = c
		elif (ans < 0):
			a = c
	if (num_iteration == 100 annd f(c) != 0):
		print("No 0s in region")
		return none	
	else:
		return c
			#this is 0
lower = -5
upper = 0
print(find_root(lower, upper))

#####
#trying with x^2 +1 
def f(x):
	return 2**x + 1

def find_root(a,b):
	c = (a + b)/2 #assume c is in the middle
	ans = f(c)
	num_iteration = 0
	while ans != 0 and num_iteration <= 100:
		num_iteration += 1
		c = (a + b)/2 
		ans = f(c)
		if ans (ans > 0):
			b = c
		elif (ans < 0):
			a = c
	return c
			#this is 0
upper = 16
lower = 0
