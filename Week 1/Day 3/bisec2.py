import math

def f(x):
	return math.sin(X)

def find_root(a, b):
	c = (a + b)/2 #assume c is in the middle
	ans = f(c)
	num_iteration = 0
#	tolerance = 0.001
	while ans != 0 and num_iteration <= 100:# and ans > tolerance:
		num_iteration += 1
		c = (a + b)/2 
		ans = f(c)
		if (f(a)*ans > 0): #ans (ans > 0): #need to account for the sign changes. 
			a = c
		else:
			b = c
	else:
		return c
			#this is 0
#print(math.pi/2)
lower = 2
upper = 4

print(find_root(lower, upper))

# need to finish this one 