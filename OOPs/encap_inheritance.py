# public members can be accessed anywhere inside the child class
# they can be accessed directly outside the class as well
class Demo:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def display(self):
		print("In parent class", self.a, self.b)


class DerivedDemo(Demo):
	def greet(self):
		print("In child class", self.a, self.b)


d1 = DerivedDemo(10, 20)
# d1.greet()
# d1.display()
# print(d1.a, d1.b)

######################################################################
# protected members: can be accessed anywhere inside the child class
# but should not be accessed outside the class
class Demo:
	def __init__(self, a, b):
		self._a = a
		self._b = b

	def display(self):
		print("In parent class", self._a, self._b)


class DerivedDemo(Demo):
	def greet(self):
		print("In child class", self._a, self._b)


d2 = DerivedDemo(96, 97)
# d2.greet()

#####################################################################
# private variables: cannot be accessed inside the child class
# cannot be accessed outside the class as well

class Demo:
	def __init__(self, a, b):
		self.__a = a
		self.__b = b

	def display(self):
		print("In parent class", self.__a, self.__b)    # _Demo__a , _Demo__b

# d = Demo(13, 65)
# d.display()

class DerivedDemo(Demo):
	def greet(self):
		print("In child class", self.__a, self.__b)     # _DerivedDemo__a


# d3 = DerivedDemo(1, 2)
# d3.greet()


