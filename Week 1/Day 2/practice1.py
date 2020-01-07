# practicing with lists and functions

#example: define a function that returns a list of even numbers between N and M, inclusively

def find_evens(N,M):
	evens = []
	for numbers in range(N, M + 1):
		if (numbers % 2 == 0):
			evens.append(numbers)
	return evens

print(find_evens(2,20))

#print a list of even numbers that are multples of 3. 
print("even multplies of 3 list")
def even_muls(A,B):
	muls = []
	for number in range(A, B + 1):
		if (number % 3 == 0) and (number % 2 == 0): #can shorten to % 6 == 0... 
			muls.append(number)
	return muls
#fill
print(even_muls(2,20))

