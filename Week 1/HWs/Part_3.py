#if n is your input, list all odd numbers from 0-> n 
#include n

def print_nums(N):
	counter = 0
	odd_list = [] 
	while counter <= N: 
		if counter % 2 == 1:
			odd_list.append(counter)
		counter += 1
	return odd_list #without this, it returned a "none" in console
	print(odd_list)

print(print_nums(1), "\n")

print(print_nums(5), "\n")

print(print_nums(2), "\n")

print(print_nums(19), "\n")

#testing edgecase
#print(print_nums(0), "\n")
