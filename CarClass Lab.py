class Car(object):

	 # created the class car and define the constructor for the class car 

	def __init__(self,Car_name='General',Car_model='GM',Type = 'saloon'):

		self.name = Car_name
		self.model = Car_model
		self.car_type = Type
		self.speed = 0

		if (self.name == 'Porshe' or self.name == 'Koenigsegg'):
			self.num_of_doors=2
		else:
			self.num_of_doors=4

		if self.car_type == "trailer":
			self.num_of_wheels=8
		else:
			self.num_of_wheels=4
	# created the method saloon to establish if car is saloon 		
	def is_saloon(self):
		if self.car_type != "trailer":
			return True
		else:
			return False
	def drive(self, desired_speed):
		if (self.car_type == 'trailer'):
			self.speed = desired_speed * 11
			return self
		else:
			if(desired_speed !=0):
				self.speed = 10 ** desired_speed
			else:
				self.speed = 10 * desired_speed
				return self