#write a function that finds max of a list
def find_max_num(list1):
	if (list1 == []):
		return None
	else:
		max_num = 0
		for number in range(len(list1)):
			if (max_num <= list1[number]):
				max_num = list1[number]
		return max_num
lista = [1,2,3]
print(find_max_num(lista))
listb = [1,2,19,22]
print(find_max_num(listb))
listc = [1,1]
print(find_max_num(listc))
listd = [2.5,6.2, 3.14]
print(find_max_num(listd))
liste = []
print(find_max_num(liste))