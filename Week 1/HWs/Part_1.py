#problem 1
#a
x = 14.5
print(type(x))
#b
My_name = "Bob"
print(My_name); #note this ";" had no effect
#c
My_name = "Bob"
print(type(My_name))
#d
My_name = "Mike" + str(49) #note, this prints the number as a string, not dealing with mem here. <..<''
print(type(My_name))

#problem 2
print("\nProblem 2")
#a
x,y = 8,2
ans = x^y
print(ans, "\n")
#b
x,y = 8,2
ans = x**y
print(ans, "\n")
#c
#x,y = "2", 5
#ans = x + y
#print(ans, "\n")
#d 
x, y = 18, 4
ans = x % y
print(ans, "\n")
#e
x, y = 18, 4
ans = (x % y) >= 3
print(ans)