from classes import wheel, engine, body

class vehicle(wheel, engine, body):
	def __init__(self, horsepower, cylinders, colour, num_doors=4, w_size=18):
		#makes engine of vehicle
		self.engine = engine(horsepower, cylinders)
		#makes tires of vehicle
		self.front_right_wheel = wheel(w_size)
		self.front_left_wheel = wheel(w_size)
		self.back_right_wheel = wheel(w_size)
		self.back_left_wheel = wheel(w_size)

		#makes the body of vehicle
		self.body =  body(colour, num_doors)
	def drive(self, num_miles):
		self.engine.mileage += num_miles
		self.engine.trip_counter += num_miles
		print(f"You drove {num_miles}")
	def repair(self):
		self.engine.change_oil()#calls method
		self.engine.max_mileage += 100
		print(f"Thanks for repairing!")
	def check_mileage(self):
		mileage = self.engine.mileage 
		print(f"Your car has {mileage} miles")
camry = vehicle(180, 4, "silver")
santa_fe = vehicle(200, 4, "blue", w_size=20)

#checks mileage of new cars
camry.check_mileage()
santa_fe.check_mileage()

#drives
camry.drive(60)
santa_fe.drive(10)

# second check mileage of cars
camry.check_mileage()
santa_fe.check_mileage()

