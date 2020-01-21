#write a function that finds min of a list
def find_min_num(list1):
	if (list1 == []):
		return None
	else:
		min_num = list1[0]
		for number in range(len(list1)):
			if (min_num >= list1[number]):
				min_num = list1[number]
		return min_num
lista = [1,2,3]
print(find_min_num(lista))
listb = [1,2,19,22]
print(find_min_num(listb))
listc = [1,1]
print(find_min_num(listc))
listd = [2.5,6.2, 3.14]
print(find_min_num(listd))
liste = []
print(find_min_num(liste))