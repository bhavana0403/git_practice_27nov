class Demo:

	def __init__(self, value):
		self.value = value

	def add(self):
		print(self.value + 10)

	# static method - independent functions enclosed within classes
	@staticmethod
	def is_even(number):
		if number % 2 == 0:
			print("number is even")
		else:
			print("number is odd")

	@staticmethod
	def display():
		print("hello world")


d = Demo(963)
d.add()             # Demo.add(obj_name)
d.is_even(37)
d.display()

Demo.display()
Demo.is_even(12)

# we cannot call instance methods directly using class name like below
# Demo.add()
# But we can call it using, class_name.method(any_obj_name)
Demo.add(d)

###################### instance methods ################################
class Bank:
	roi = 0.4

	def __init__(self, name, account):
		self.name = name
		self.account = account

	def details(self):          # self --> objects address
		self.roi = 1.5


acc1 = Bank("John", "Account 1")
acc2 = Bank("Steve", "Account 2")

print(Bank.roi)         # 0.4
print(acc1.roi)         # 0.4
print(acc2.roi)         # 0.4

acc1.details()
acc2.details()

print(Bank.roi)         # 0.4
print(acc1.roi)         # 1.5
print(acc2.roi)         # 1.5

# ------------------- class methods -------------------------------
# updating the existing class variable using classmethod

class Bank:
	roi = 0.4

	def __init__(self, name, account):
		self.name = name
		self.account = account

	@classmethod
	def details(cls):              # cls -> class' address
		cls.roi = 1.5

acc1 = Bank("John", "Account 1")
acc2 = Bank("Steve", "Account 2")

print(Bank.roi)         # 0.4
print(acc1.roi)         # 0.4
print(acc2.roi)         # 0.4

acc1.details()

print(Bank.roi)         # 1.5
print(acc1.roi)         # 1.5
print(acc2.roi)         # 1.5

# --------------------------------------------------------------------
# creating a class variable using classmethod
class Bank:

	def __init__(self, name, account):      # self -> instance address
		self.name = name
		self.account = account

	@classmethod
	def details(cls):               # cls --> class'address
		cls.bank_name = "HDFC"


acc3 = Bank("John", "Account 1")
acc4 = Bank("Steve", "Account 2")

# print(Bank.bank_name)             # AttributeError
# print(acc3.bank_name)             # AttributeError
# print(acc4.bank_name)             # AttributeError

Bank.details()          # acc3.details() or acc4.details()

print(Bank.bank_name)           # HDFC
print(acc3.bank_name)           # HDFC
print(acc4.bank_name)           # HDFC

