# car class
class Car(object):

	 # created the class car and define the constructor for the class car 

	def __init__(self,Car_name='General',Car_model='GM',Type = 'saloon'):

		#initialized all the variables in class
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
	# this is the method for driving
	def drive(self,speeds):
		if (self.car_type != 'trailer'):
			if(speeds !=0):
				speeding = (10 ** speeds)
			else:
				speeding = 10 * speeds
				return self
			self.speed = speeding
			return self
		else:
			self.speed = speeds * 11
			return self
