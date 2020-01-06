# goal: print even numbers between 1 and N, N = user input, include 1 and N
N = int(input("Enter upper limit: "))
for number in range(1,N+1):
	if (number % 2 == 0):
		print(number)
#stuff
#same ut different
print("With a While loop")
count = 1;
while count <= N: 
	if (count % 2 == 0):
		print(count)
	elif (count == 1):
		print(count)
	count += 1
#stuff