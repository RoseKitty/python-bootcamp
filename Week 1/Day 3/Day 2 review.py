#make a function that takes in 2 inputs, a lower and upper limit. 
#return multiples of 5 in a list. inclusively. 

def mul5(lower, upper ):
	#N = int(input("Lower bound: "))
	#M = int(input("Upper bound: "))
	mults = []
	for number in range(lower, upper + 1):
		if number % 5 == 0:
			mults.append(number)
	return mults
print(mul5(0,10))

# function that takes integer as a list as input
#return index from the list
#### Linear search 
#ie if you have a list given, search and return index
list_1 = [10,8,7,19,42,2]
def searching(x, list):
	"""
	This is a multi line string.. but under a function definition, it is called a dot string
	\tparam : x - the element you're searching for
	\tparam : list - the list you're searching through
	\treturns : the index of where the element was found (if applicable)
	"""
	pass
	#search(2, list_1)
	#note returns stop loops without breaking them... heh
	for i in range(0, len(list)):
		if list[i] == x:
			return i
#typing help(searching) prints out that dot string, and the name of the function
#this print is here and then run
print(searching(2,list_1))
#note the list isn't specific to just ints, you can use any data type

def find_max(list):
	"""
	returns max element from list
	\treturns : the max value in list
	\tparam : list - a list of numerical elements
	"""
	pass

	max = list[0]
	#another way to write the first line
	#for element in list:
	for i in range(0, len(list)):
		if list[i] >= max:
			max = list[i]
	return max
print (find_max(list_1))

#help(searching) #these tell how to use the code without testing


def find_min(list):
	"""
	returns min element from list
	\treturns : the min value in list
	\tparam : list - a list of numerical elements
	"""
	pass
	min = list[0]
	for i in range(0, len(list)):
		if list[i] <= min:
			min = list[i]
	return min

#
