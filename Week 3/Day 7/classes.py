#259 was teaching oop

class wheel:
	#need this tab in
	#define constructor which is auto called
	#unless inheriting- then manual called
	def __init__(self, diameter): #don't have to  write ,"type = "all-weather"
		#those are two underscores 
		#self tells python this method is in and part of this class
		#init is never actually called
		#"init" is the constructor. 
		#this whole thing is a method, method is function part of a class
		#attributes of a class
		self.size = diameter
		#self tells it's part of a class
		self.type = "all-weather" #if added the extra part after ',' jus say = type
class engine:
	def __init__(self, horsepower, cylinders): #torque, 
		self.horsepower = horsepower
		#self.torque = torque
		self.cylinders = cylinders
		#same name is okay since one is in something
		self.is_healthy = True
		#assuming engine is health. 
		self.need_oil_change = False
		#assume new and doesn't need oil change
		#these two are not inputed, they are common assumptions
		self.mileage = 0 #make car = 0
		self.max_mileage = 150000
		#self.odometer= 0
		self.trip_counter = 0

	def check_health(self):	#new method
		#remember, self means it's part of the class
		if self.mileage > self.max_mileage:
			self.is_healthy = False
			print("Our engine is breaking, get a new one")
		
		if self.trip_counter >= 150000:
			self.mileage = self.max_mileage
			print("Died. Bad owner!!! ")
		if self.trip_counter >= 6000:
			print("Change my oil or die! >..< ")			
		if self.trip_counter >= 3000: 
			#else:
			self.is_healthy = False
			self.need_oil_change = True

			print("Change your oil!")
	def change_oil(self):
		#need to reset trip_counter to 0 and alert off
		self.trip_counter = 0
		self.is_healthy = True
		self.need_oil_change = False
		print("All good now- you changed your oil")

class body:
	#pep-8 guidelines v see comment there
	def __init__(self, colour, num_doors=4):#default perameters should be last ones listed#also no space
		self.num_doors = num_doors
		self.colour = colour
		
		if self.num_doors == 0:
			self.boot_size - "tiny"
		elif self.num_doors == 2:
			self.boot_size = "small"
		elif self.num_doors == 4:
			self.boot_size = "med"
		elif self.num_doors >= 5:
			self.boot_size = "large"
		#this code says boot size depends on the number of doors

		

