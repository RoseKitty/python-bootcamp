# function that compares two lists of ints; output should be a list containing differences of both lists. 
#list only if element is unique to one list

#part 1
ina = [1, 2, 3]
inb = [1, 2, 3]
#def diff_finder(list_a,list_b):
#	temp_in = list_a
#	for i in range(len(list_b)):
#		for element in range(len(list_a)):
#			if list_b[i] == list_a[element]:
#				temp_in.pop[list_a[element]]#doesn't like this one
#			else:
#				temp_in.append[list_b[i]]
#	return temp_in
#print(diff_finder(ina,inb))



###############
#someone else's example
#def diff(list1, list2)
#	output1 = []
#	if(len(list1) == 0 and len(list2) == 0):
#		print(output)
#	else:
#		for num1 in range(len(list1)):
#			


#####
#without using sets

def find_diffs(a, b):
	difference = []
	for elements in a:
		if elements not in b:
			difference.append(elements)
	for elements in b:
		if elements not in a:
			difference.append(elements)
	
	return difference
print(find_diffs(ina,inb))
#change for ina and inb to give for each of your test cases
#using python's sets


