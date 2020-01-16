#functions are defined at the top so ... 
#finding avg year 

#returned a list of years^
def avg_year(car_yr):
	avg_tot = 0
	for i in range(len(car_years)):
		avg_tot += int(car_years[i]) 
	div_avg = int(avg_tot/len(car_years))
	return div_avg
#def avg2(years):
	#return int(sum(years/len(years)))
	#this one is the shortest possible one


list_of_cars = ["toyta","ford","BMW","Audi","Benz"]
list_of_models = ["Camry","F150","i8","A4","S550"]
car = {
	"make" : list_of_cars,
	"model" : list_of_models,
	"years" : [2010, 2017, 2020, 2006, 2020]#can also define in here
}

car_years = car["years"]

for key in car:
	#print(key)
	pass
for lists in car.values():
	#print(lists)
	pass

#note, this needs to be written down here after car_years is defined... 
#guess python reads down but function is defined up there... ?
avg_yr = avg_year(car_years)
#print(avg_yr)

#adding a key and val to dictionary 
car_colours = ["red","blue","black","blue","silver"]
car["colour"] = car_colours
for key in car:
	#print(key)
	pass
for values in car.values():
	#print(values)
	pass
#tested with printing the above and then the after of this adding placed in the code- yeah
#it reads down... c++ is smarter.. it reads everything at once. 
inv_count = [3,5,6,1,3]
stock_car = []
c = 0
#for i in range(len(inv_count)):
while len(car["make"]) == len(inv_count) and len(inv_count) > c:
	for x in range(len(car["make"])):
	#	print(inv_count[x], car["make"][x]) #this print works
		#need to have it go into the empty list
		c += 1
		stock_car.append(str(inv_count[x]) + " " + car["make"][x])
		#added space.. heh works! 
#print(stock_car)
#		if i == x:
#			stock_car[c] = str(inv_count[i]) + car["make"][x]
#			i += 1	
#			c += 1
#		return stock_car
#print(stock_car)
#so basically, you were thinking in c++, we need to think python here. 

car["inv"] = inv_count #+ car["make"]
for key in car:
	#print(key)
	pass
for values in car.values():
	#print(values)
	pass
car["inv"] = stock_car
del car["make"]
for values in car.values():
	print(values)
	pass

#number of stock 
#sum_stock = (sum(car["inv"]))	#inserting this line into print doesn't work
#print(f"We have {sum_stock} cars in stock.")

car["Dealers"] = ["Amy","Bob","Charlie","Dylan","Elephant"]
for key in car:
	#print(key)
	pass
for values in car.values():
	#print(values)
	pass
#essentially, the keys are lists. so they can do list things
#firing dealers 
#car.pop("Dealers")
#for key in car:
#	print(key)
#car["Dealers"].clear() #clears list
#print(car)
#print("\n we're going to close out dealership")
#car.clear() #clears dictionary contents
#print(car)
#del car #deletes the whole dictionary

