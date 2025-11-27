# encapsulation - hide the data
# abstraction - hide the implementation

"""
1. import AbstractBaseClass(ABC)
	from abc import ABC

2. create a class by inheriting ABC
	class Demo(ABC):
		pass

3. the class can have 2 types of methods
	1. abstract method
	2. concrete method

4. You can never create an object of abstract class directly when it has
   atleast one abstract method

5. create a child class which inherits the abstract class

6. child class must give implementation to all the abstract methods of parent class


"""
# abstract class with only concrete methods

from abc import ABC

class Demo(ABC):     # abstract class

	# concrete methods in ABC
	def greet(self):
		print("hellooo")

	def add(self, a, b):
		print(a + b)

	def spam(self):
		print("in spam")


d = Demo()
d.add(1, 2)
d.spam()
d.greet()

# --------------------------------------------------------------------
# abstract class with abstract and concrete method

from abc import ABC, abstractmethod

class Demo(ABC):  # abstract class

	@abstractmethod
	def greet(self):
		pass

	def add(self, a, b):
		print(a + b)

	def spam(self):
		print("in spam")

class Derived(Demo):

	def greet(self):
		print("in derived greet")

d = Derived()
d.add(1, 2)
d.greet()
# ---------------------------------------------------------------------

class Banking(ABC):

	def __init__(self, bank_name):
		self.bank_name = bank_name

	@abstractmethod
	def deposit(self):
		pass

	@abstractmethod
	def withdraw(self):
		pass

	@abstractmethod
	def check_balance(self):
		pass


class ICICI(Banking):

	def deposit(self):
		print("in icici deposit")

	def withdraw(self):
		print("in icici withdraw")

	def statement(self):
		print("printing the last 5 transactions....")

	def check_balance(self):
		print("the balance is XXXX.XX ")

acc1 = ICICI("icici")















