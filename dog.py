class Dog:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	
	
	def sit(self):
		print(f'{self.name} is siting')
		
	def roll(self):
		print(f'{self.name} is rolling')
		
 
my_dog = Dog('gengiqngfeng',18)
print(f"My dog name is {my_dog.name}") 				
print(f"My dog age is {my_dog.age}") 	
my_dog.sit()
my_dog.roll()
