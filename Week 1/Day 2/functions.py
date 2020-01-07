#writing define f(x) = x + 1
def f(x):
	ans = x + 1
	return ans
#fill

my_solution = f(1)
print (my_solution)

##########
# with operators:
print("Operators, g(x) = x^4 + x^2 +1")
def g(x): 
	stuff = x**4 + x**2 + 1
	return stuff
#fill

print (g(1), g(2), "\n\n") #this bothers me so much... ugghh... I pref. endl or cout::endl 

#####
#functions with multiple returns
def get_first_two():
	return 2,4
#can have multiple returns

even1, even2 = get_first_two()
print(even1)
print(even2, "\n\n")

#with no returns

def print_evens(N):
	for number in range(1, N+1):
		if number % 2 == 0:
			print(number)
#note there is no return
#this calls the prev. and plugs in N for (10*) and prints
print_evens(10)

# write a fuction that takes N as input and prints all common multiplies of 3 and 7. 

def print_func():
	NN = int(input("Give a number: "))
	for number2 in range(1, NN + 1):
		if number2 % 3 == 0:
			if number2 % 7 == 0:
				print(number2)
##alternatively you can write if (number2 % 3 == 0) and (number2 % 7 == 0)
print_func() #this calls the function... 
#otherwise, nothing happens to the defined funcntion even if it says print or whatever... 
##other note: if you defined NN first outside, you have to call it in the def print_func(here) and in the print_func(here)

#define a function to take 3 inputs, and get all common multplies of 2 of the inputs, the last being the stopper. 
def print_common_multiplies():
	stopper = int(input("Input stopper: "))
	mul1 = int(input("Input first multiple: "))
	mul2 = int(input("Input second multiple: "))
	for number3 in range(1, stopper + 1):
		if number3 % mul1 == 0:
			if number3 % mul2 == 0:
				print(number3)
#fill
print_common_multiplies()

##alt: 
#def find_stuff(x,y,N):
#	for num in range(1,N):
#		if (num % x == 0) and (num % y == 0):
#			print(num)
#call function
#find_stuff(3,7,100)

