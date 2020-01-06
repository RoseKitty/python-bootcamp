#goal: to print all odd numbers between 0 and N, N is a user input
print("Using a for loop")
N = int(input("Enter upper limit: "))
for number in range(1,N+1):
	if (number % 2 != 0):#or == 1
		print(number)

print("Using while loop")
count = 1;
while count <= N: 
	if (count % 2 != 0):
		print(count)
	#probably don't need this since 1 is odd
	#elif (count == 1):
#		print(count)
	count += 1