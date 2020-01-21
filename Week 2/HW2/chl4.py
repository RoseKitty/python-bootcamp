#sum of smallest odd nums and largest odd nums
#if small == large, ans = num * 2 
#if no odd, = 0 

def odd_num(list1):
	odd_nums = [0] #list of odds are 0 unless there are odd numbers
	for number in range(len(list1)):
		if list1[number] % 2 == 1:
			odd_nums.append(list1[number])	
	return odd_nums

def odd_mins(odd_nums):
	odd_min = odd_nums[0]
	for numbers in range(0, len(odd_nums)):
		if odd_nums[numbers] < odd_min:
			odd_min = odd_nums[numbers]
		elif odd_nums[numbers] == 1:#since 0 is smaller, odd min is 1 if 1 exists in list
			odd_min = 1
		elif (len(odd_nums) == 2): #if list has only 2 numbers, list is only 0 and one odd number
			odd_min = odd_nums[1] #sets oddmin as the only other odd number in list
			#append function puts new number at end of list, since size = 2, i = 1
	return odd_min

def odd_maxs(odd_nums):
	odd_max = odd_nums[0]
	for numbers in range(len(odd_nums)):
		if odd_nums[numbers] > odd_max: 
			#if list has odd numbers, any number is greater than 0 else 0 + 0
			odd_max = odd_nums[numbers]
	return odd_max
lista = [1,3,5,7,9]
#num1 = (odd_mins(odd_num(lista)))
#num2 = (odd_maxs(odd_num(lista)))

def odd_sums(list2):
	num1 = (odd_mins(odd_num(list2)))
	num2 = (odd_maxs(odd_num(list2)))
	odd_sum = num1 + num2
	return odd_sum

print(odd_sums(lista))

listb = [1,2,3,4,5]
#num1 = (odd_mins(odd_num(listb)))
#num2 = (odd_maxs(odd_num(listb)))
print(odd_sums(listb))

listc = [2,4,6,8,10,3]
#num1 = (odd_mins(odd_num(listc)))
#num2 = (odd_maxs(odd_num(listc)))
print(odd_sums(listc))

listd = [2,4,10,28,32]
#num1 = (odd_mins(odd_num(listd)))
#num2 = (odd_maxs(odd_num(listd)))
print(odd_sums(listd))
