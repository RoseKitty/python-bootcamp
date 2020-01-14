#Challenge 1 
#create a funcntion that takes an array or list of int or floats as input
#output of funcntion is sum of all elements in array 
#print to console
#####
#list_1 = [1, 2, 3]
#what if...
#have in the user create list. 

N = int(input("Number of elements: "))

#have a blank list and append
try_list = []
while N > 0:
	N -= 1
	M = int(input("Input an element: "))
	try_list.append(M)
print(try_list)	#testing line
#try_list = [1,2,3]
def input_list(try_list):
	L = len(try_list)
	sum_1 = 0
	for number in range(L):
		sum_1 += try_list[number]
	return sum_1 	
print(input_list(try_list)) #something wrong... prints location intead of sum

#print(type(len(try_list))) #since len list is an int number  

#repeat for all except the float one 

N2 = int(input("Number of elements: "))

#have a blank list and append
try_list2 = []
while N2 > 0:
	N2 -= 1
	M2 = float(input("Input an element: "))
	try_list2.append(M2)
print(try_list2)	#testing line
def input_list(try_list2):
	L2 = len(try_list2)
	sum_2 = 0
	for number2 in range(L2):
		sum_2 += try_list2[number2]
	return sum_2 	
print(input_list(try_list2)) 
#this one is for float

