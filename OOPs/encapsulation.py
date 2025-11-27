# classes -> encapsulation

class Sample:
	a = 10
	b = 20


s_obj = Sample()
print(s_obj.a)
print(s_obj.b)

######################################################################
"""
access specifiers or access modifiers : allow us to restrict the access
to any attributes inside a class

3 types
-------
1. public
2. protected: (_AttrName)
3. private

"""

# protected and public members
class Employee:

	def __init__(self, name, salary):
		self.name = name            # public member
		self._salary = salary       # protected member

	def _email(self):               # protected member
		print(f'{self.name}123@company.com')


emp1 = Employee("John", 2000)
print(emp1.__dict__)
print(emp1.name)
print(emp1.salary)
emp1._email()

#######################################################################
# private members: __AttributeName

class Employee:

	def __init__(self, name, salary):
		self.name = name
		self.__salary = salary      # _classname__salary

	def email(self):
		print(f'{self.name}123@company.com')


emp2 = Employee("Steve", 5000)
print(emp2.__dict__)
print(emp2.name)
print(emp2.salary)

"""
NOTE: We should be accessing protected and private variables outside
of the class in global space
"""

######################################################################
# create a class BankAccount : customer_name, balance, rate of interest
# balance -> private
# rate of interest -> protected
# deposit, withdraw, statement(public)

class BankAccount:

	def __init__(self, name, balance, roi):
		self.name = name
		self.__balance = balance
		self._roi = roi


	def _deposit(self):
		pass

	def __withdraw(self):
		pass

	def statement(self):
		pass


