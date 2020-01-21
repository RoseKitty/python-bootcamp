#write a function that extracts numbers from string
#return as list of int 

def find_dig(strings):
	digits = []
	for stuff in strings:
		if stuff.isdigit() is True:
			digits += stuff
	return digits

stringa = ("Bob has 1 donut and 16 coffees")
print(find_dig(stringa))
stringb = "Oh my! You have 18 keys!"
print(find_dig(stringb))
stringc = "Hey look, there are 4 coffees and 5 donuts on the table"
print(find_dig(stringc))
stringd = "Pi is approx 3.1415926"
print(find_dig(stringd))
stringe = "Amy has no absences in this class!"
print(find_dig(stringe))

