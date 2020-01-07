#todo: write a script that prints out multiples of 3 between 0 and N, include N, N = user input

N = int(input("Input a number: "))

#for number in range(N+1):
#	if (number % 3 == 0):
#		print(number)
#stuff
#print("With a while loop")
count = 0
#while count <=N:
#	if (count % 3 == 0):
#		print(count)
#	count += 1
#stuff
#NOTE: ALL ABOVE WAS MUTED FOR TERMINAL SPACE
#write a scipt that prints out common multiplies of 3 and 5 between 0 and N (inclusive), N is a user input. 

for number2 in range(N+1):
	if (number2 % 3 == 0):
		if (number2 % 5 == 0):
			print(number2)
#stuff
#alternatively, you can write if (numer2 % 3 == 0) and (number2 % 5 == 0)
print("With a while loop")
count2 = 0
while count2 <= N:
	if (count2 % 3 == 0):
		if (count2 % 5 == 0):
			print(count2)
	count2 += 1	
#stuff
