#goal: sum up all numbers between N and M, inclusively. Both are user inputs.
N = int(input("Input a pref. lower number: "))
M = int(input("Input a pref. higher number: "))
sum = 0
for number in range(N, M+1):
	#sum = number + sum #same as next line  
	sum += number 
#stuff
print("The sum is: ", sum)
#/n #new line
#while
print("Using a while loop")
sum2 = 0
while N <= M:
	sum2 = N + sum2
	N += 1
#stuff
print("The sum2 is:", sum2)