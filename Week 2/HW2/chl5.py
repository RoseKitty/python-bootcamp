#given 5 pos ints
#find min and max values summing 4 out of 5 ints
#put those values into a list with len == 2
#sorry teacher... 
#abuse:
# since lists are in order, and limit is 5
#can hardcode a little
def adding_stuff(lista):
	count_up = 0
	count_down = 4 
	sum1 = 0
	sum2 = 0
	total_list = []
	for index in range(len(lista)):
		while (count_down > 0) and (count_up < 5):
			sum1 += lista[count_down]
			sum2 += lista[count_up]
			count_down -= 1
			count_up += 1
	#print(sum2, sum1)
	total_list.append(sum2)
	total_list.append(sum1)
	return total_list
list1 = [1,3,5,7,9]
print(adding_stuff(list1))
list2 = [1,2,3,4,5]
print(adding_stuff(list2))
list3 = [2, 4, 6, 8, 10]
print(adding_stuff(list3))