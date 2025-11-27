# raise Exception_name

class Banking:

	def __init__(self, name, balance):
		self.name = name
		self.balance = balance
		self.transactions = []

	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			self.transactions.append(f"Rs.{amount} has been credited and available balance is {self.balance}")
		else:
			raise ValueError("Invalid amount")

	def withdraw(self, amount):
		if amount < self.balance:
			self.balance -= amount
			self.transactions.append(f"Rs.{amount} has been debited and available balance is {self.balance}")
		else:
			raise Exception("Amount to be withdrawn exceeds balance")

	def statement(self):
		print("*" * 50)
		print(f"The statement for {self.name} account is,")
		for transaction in self.transactions:
			print(transaction)

# cus1 = Banking("Steve", 10000)
# cus1.deposit(1000)
# cus1.deposit(3000)
# cus1.withdraw(7000)
# cus1.statement()

#######################################################################
# Amount to be deposited must exceed 1000
# amount to be withdrawn must not exceed 5000

class SavingsAccount(Banking):

	def deposit(self, amount):
		if amount >= 1000:
			super().deposit(amount)
		else:
			raise Exception("Minimum amount for deposit : RS.1000")

	def withdraw(self, amount):
		if amount <= 5000:
			super().withdraw(amount)
		else:
			raise Exception("Amount cannot exceed Rs.5000")


# s = SavingsAccount("John", 10000)
# s.deposit(1000)
# s.withdraw(3000)
# s.statement()

########################################################################
# depositing should be allowed, minimum of 1000 rupees should be deposited
# withdrawing should not be possible.

class SukanyaSamruddhiAccount(Banking):

	def deposit(self, amount):
		if amount > 1000:
			super().deposit(amount)
		else:
			raise Exception("Amount should be at least 1000")

	def withdraw(self, amount):
		raise Exception("Cannot withdraw from Sukanya Samruddhi Account")


s = SukanyaSamruddhiAccount("Sita", 10000)
# s.deposit(200)
s.withdraw(3000)
s.statement()

#####################################################################

a = 10
b = 20

# print(a)
# # print("Cannot execute further")
# raise Exception("Cannot execute further")
# print(b)















