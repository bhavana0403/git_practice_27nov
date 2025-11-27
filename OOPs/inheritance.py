"""
Inheritance - deriving the properties from a base class into derived class
"""
class A:
	num1 = 20
	num2 = 27


class B(A):
	def display(self):
		print("in display method")


b = B()
print(b.num1)
print(b.num2)
b.display()

a = A()
print(a.num1)
print(a.num2)
a.display()         # AttributeError

#######################################################################
class Demo:

	def __init__(self, value):
		self.value = value

	def greet(self):
		print("in Demo greet()", self.value)

	def display(self):
		print("in Demo display")

# d = Demo(10)

class Demo1(Demo):
	pass


d1 = Demo1(10)
print(d1.value)         # 10
d1.greet()
d1.display()

########################################################################
# Child class with completely independent property
class Demo:

	def __init__(self, value):
		self.value = value

	def greet(self):
		print("in Demo greet()", self.value)

	def display(self):
		print("in Demo display")


class Demo2(Demo):

	def spam(self):
		print("Demo2.spam")

d2 = Demo2(16)
print(d2.value)
d2.greet()
d2.display()
d2.spam()

########################################################################
# completely overriding the parent method(display)
class Demo:

	def __init__(self, value):
		self.value = value

	def display(self):
		print("in Demo display")


class Demo3(Demo):

	def display(self):
		print("in Demo3 display.....")


d3 = Demo3(20)
print(d3.value)
d3.display()

# child -> parent

######################################################################
# partially overriding the parent class' method
# super() -> gives the access to the parent class' attribute

class Demo:

	def __init__(self, value):
		self.value = value

	def display(self):
		print("in Demo display")


class Demo3(Demo):

	def display(self):
		print("in Demo3 display.....")
		super().display()               # method chaining

d3 = Demo3(12)
d3.display()

#######################################################################






