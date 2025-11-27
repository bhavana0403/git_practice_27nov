# property decorators - restrict the access to any attribute inside a class

# create salary as property: getter, setter, deleter
"""
1. decorate getter method with @property
2. all getters, setters and deleter methods must have the same name
3. for setter: @prop_name.setter
4. for deleter: @prop_name.deleter
5. the property name and the variable name must be different
	always keep variable as _variablename (_salary)
	always keep property as variable (salary)

"""
class Employee:

	def __init__(self, name, salary):
		self.name = name
		self._salary = salary

	# getter method
	@property
	def salary(self):
		print("getting salary....")
		return self._salary

	# setter method
	@salary.setter
	def salary(self, new_value):
		print("setting salary to a new value....." )
		if new_value > 0:
			self._salary = new_value

	# deleter method
	@salary.deleter
	def salary(self):
		print("deleting salary....")
		del self._salary


# emp1 = Employee("John", 5000)
# print(emp1.salary)
# emp1.salary = -1000
# print(emp1.salary)
# del emp1.salary

# print(emp1.get_salary())
# emp1.set_salary(-1000)
# print(emp1.get_salary())

#######################################################################
class Employee:

	def __init__(self, name, salary):
		self.name = name
		self._salary = salary

	# getter method
	@property
	def salary(self):
		print("getting salary....")
		return self._salary

	# setter method
	@salary.setter
	def salary(self, new_value):
		raise Exception("cannot set value to salary")

	# deleter method
	@salary.deleter
	def salary(self):
		raise Exception("Cannot delete the salary")


# emp1 = Employee("John", 5000)
# print(emp1.salary)
# emp1.salary = -1000
# print(emp1.salary)
# del emp1.salary

########################################################################
class BankAccount:

	def __init__(self, name, balance):
		self.name = name
		self._balance = balance

	@property           # getter method
	def balance(self):
		pass

	@balance.getter
	def balance(self):
		print("fetching balance....")
		raise Exception

	@balance.setter
	def balance(self, new_value):
		print("setting new_value to balance...")
		raise Exception("Cannot update balance")


cust1 = BankAccount("Bob", 20000)
print(cust1.name)
print(cust1.balance)        # property getter

cust1.balance = -800        # property setter
print(cust1.balance)        # property getter














