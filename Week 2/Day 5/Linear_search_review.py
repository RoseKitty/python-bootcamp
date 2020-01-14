#linear search, take every element and check to see if 
#that's the right one you want
## searching and sorting = most of it; object orientated, classes, meaning of classes etc 

def linsearch(x,list1):
	for i in range(0, len(list1)):
		if (x == list1[i]):
			location_i= i
			return i

		#else:
			#print(f"{x}Not found")
	return none
try_list = [0,3,2,1]
print(linsearch(1,try_list))
