class Company:
	company_name = "ABC"

	def __init__(self, turn_over):
		self.turn_over = turn_over

	def display(self):
		print(f"The company {self.company_name} has a turn over of {self.turn_over}")

class BusinessUnit(Company):

	def __init__(self, name, turn_over):
		self.name = name
		# constructor chaining
		super().__init__(turn_over)

	def display(self):
		print("in business unit display...")
		# method chaining
		super().display()

print(BusinessUnit.__dict__)  # This dictionary will have only the attributes of BusinessUnit class
b = BusinessUnit("HRD", "20 crores")    # b.__init__()
b.display()

########################################################################
class Demo:
	def __init__(self, value):
		self.value = value

	def spam(self):
		print("in demo.spam()")

class Employee:
	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname

	def email(self):
		print(f"{self.fname}.{self.lname}@gmail.com")

class Sample(Demo, Employee):

	def __init__(self, value, fname, lname):
		# constructor chaining
		Demo.__init__(self, value)
		Employee.__init__(self, fname, lname)


s = Sample(12, "steve", "jobs")        # s.__init__()
s.email()
s.spam()

"""
1. Whenever a class is instantiated or object is created, __init__ will be invoked implicitly.
2. __dict__ can only return the dictionary with the attributes native to the calling class
   For ex: BusinessUnit.__dict__  will return only the attributes of BusinessUnit class not the attributes which it has inherited from Company class
3. To see all the attributes(native + inherited), we can use dir(obj)
   For ex: dir(s) -> gives list of attributes of Sample, Demo and Employee classes altogether
4. All python classes by default inherit from object class. So the extra properties/attributes that are present in the class dictionary are actually inherited from object class
5. In multiple inheritance, super() in child class will always be pointing to the first Parent class.
6. It will always be the responsibilty of child class to fulfill the arguments of parent classes.
"""







