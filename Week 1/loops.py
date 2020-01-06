#while loops and for loops
#while expression is true:
# (tab) do something

#ie counting for 0-9

counter = 0
while counter < 5: #or != 5, this is more dangerous esp bc inf loops heh... ; can also do <= 5
	print(counter)
	counter += 1

#range function
#range(start, stop, increment), only stop is required.. default increment is 1. stop is also default 0 
for number in range(0,5): #does not include stopping number. 
	print(number)
#proof of stop only
for number in range(3): #does not include stopping number. 
	print(number)
# stops

