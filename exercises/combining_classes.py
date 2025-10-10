class Car:
	def __init__(self,model,color,owner):
		self.model = model
		self._color = color
		self.owner = owner

	def vroom_vroom(self):
		print("vroom vroom")



class Owner:
	def __init__(self,name,phone_number):
		self.name = name
		self.phone_number = phone_number
	def introduction(self):
		print(f"hey name is {self.name}")


owner1 = Owner("johnson","09202019708")
car1 = Car("bmw e34","black",owner1)
car1.vroom_vroom()
car1.color = "blue"
print(car1.color)
car1.owner.introduction()
