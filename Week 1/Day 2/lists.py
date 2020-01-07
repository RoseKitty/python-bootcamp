#lists: dynamic, so they can change. 

# to declare a list, use "[]"
my_first_list = [2,4, 6, 8]

#printing the first element =  #lists start counting at 0, then 1 , 2 etc. 
#print(my_first_list[0]) #prints 2

#print(my_first_list[2]) #prints 3rd element of list, 6

length = len(my_first_list)
#print("The length of this list is:", length)

#for index in range(0, len(my_first_list)):
#	print(my_first_list[index])
#can also just print the list, instead of the loop. 
#print(my_first_list)

#error here, DNE place
#print(my_first_list[4]) #only 4 places, index 4 is place 5... DNE so error. 
#adding elements, clearing list. 
my_first_list.append(10) #adds 10 to the list. 
print("List after append")
print(my_first_list) 
print("\n\n")
#make a list of even numbers up to 12, include 12.
print("The list of even numbers up to 12: ")
evens_list = []
#blanks list
for number in range(1, 13):
	if number % 2 == 0:
		evens_list.append(number)
#fill
print(evens_list)

#to clear list, 
#evens_list.clear() #or evens_list[] works too.

#pop index, remove an index	
for i in range(0, len(evens_list)-1):
	if evens_list[i] == 10:
		index_of_ten = i
		ten = evens_list.pop(i)
print("The even list:",evens_list)
print("The popped element is:", ten)

evens_list.insert(index_of_ten, ten)
print("Puts the 10 back:", evens_list)

print("sorting the list:")
print(sorted(evens_list))
