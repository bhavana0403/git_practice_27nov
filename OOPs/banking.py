"""
1. withdraw
2. deposit
3. check balance
"""

class Banking:

	def __init__(self, balance):
		self.balance = balance

	def deposit(self, amount):
		self.balance += amount
		print(f"Rs {amount} has been credited to your account")

	def withdraw(self, amount):
		self.balance -= amount
		print(f"Rs {amount} has been debited from your account")

	def check_balance(self):
		print(f"The current balance is {self.balance}")


customer1 = Banking(10000)
customer1.deposit(-1000)
customer1.withdraw(5000)
customer1.check_balance()

customer2 = Banking(2000)
customer2.deposit(5000)
customer2.check_balance()

