# create a class named calculator and pass a and b as arguments

class Calculator:
	# key value pairs in class dictionary
	a = 10
	b = 20


c1 = Calculator()
c2 = Calculator()

# to access class dictionary: __dict__
print(Calculator.__dict__)  # {'a': 10, 'b': 20}
print(c1.__dict__)          # {}
print(c2.__dict__)          # {}

########################################################################
# instance dictionary

class Calculator:

	def __init__(self, a, b):
		self.a = a
		self.b = b


c1 = Calculator(1, 2)
c2 = Calculator(38, 52)

# accessing instance dictionary of c1
# instance dictionary - information about object variables
print(c1.__dict__)
print(c2.__dict__)

# class dictionary - information about methods/functions and class variables
print(Calculator.__dict__)

########################################################################
# create a class that can perform addition on a and b
# subtraction, multiplication, division

class Calculator:

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def add(self):
		print(self.a + self.b)


c1 = Calculator(1, 2)
c2 = Calculator(38, 52)

c1.add()
c2.add()
print(Calculator.__dict__)

########################################################################
# create a Person class and check if the person is above 18 years or not
#  name, age, gender

class Person:

	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender

	def is_adult(self):
		if self.age > 18:
			print(f"{self.name} is an adult")
		else:
			print(f"{self.name} is not an adult")


p1 = Person("John", 13, "Male")
p2 = Person("Shyam", 28, "Male")

p1.is_adult()
p2.is_adult()














