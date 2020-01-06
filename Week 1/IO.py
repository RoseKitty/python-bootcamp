# input output functions
#input() takes from user
name = input("Enter your name:") #name is your variable here. 
print("Hello", name, "you are awesome.")
#says hello to the input name

#TYPE CONVERSION EX
#python easily converts input data types. 
age = input("Enter your age: ")
#if you want min age, ie input is greater than something 
minimum_age = 5;
age = int(age)
print(age > minimum_age)
#if you want age to become an int, use int function 
#last line there prints a true or false statement 
#can go to string to int always, etc.. see site for notes, note characters 0-9 only

#error_line = int(name) #prints error since words aren't ints.



