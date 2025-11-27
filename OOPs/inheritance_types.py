"""
1. single level inheritance
2. multi level
3. hierarchical
4. muliple
5. hybrid
"""

# single level inheritance: child inherits from 1 parent class

# class Person:
#
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
#
# 	def is_adult(self):
# 		if self.age > 18:
# 			print(f"{self.name} is an adult")
# 		else:
# 			print(f"{self.name} is not an adult")
#
#
# class Employee(Person):
#
# 	def emp_details(self):
# 		print(f"Employee name: {self.name}")
# 		print(f"Employee age: {self.age}")
#
#
# e1 = Employee("steve", 28)
# e1.emp_details()
# e1.is_adult()
#
# #######################################################################
# # multi level inheritance: A -> B -> C -> D.....
#
# class A:
# 	pass
#
# class B(A):
# 	pass
#
# class C(B):
# 	pass
#
# class D(C):
# 	pass
#
# #######################################################################
# # hierarchical inheritance: parent -> multiple child classes
#
# class Parent:
#
# 	# create constructor
#
# 	def spam(self):
# 		print("in spam")
#
#
# class Child1(Parent):
# 	def spam(self):
# 		print("Child 1")
# 		super().spam()
#
#
# class Child2(Parent):
# 	def spam(self):
# 		print("Child 2")
# 		super().spam()
#
#
# c1 = Child1()
# c1.spam()
#
# c2 = Child2()
# c2.spam()

#######################################################################
# multiple inheritance: single child inheriting more than 1 parent class

class Parent1:
	a = 10
	b = 20

class Parent2:
	c = 30
	b = 40

class Child(Parent1, Parent2):
	d = 200

# MRO(method Resolution Order) - order in which an attribute is searched for in inheritance
# child -> parent1 -> parent2 -> object
c1 = Child()
print(c1.a)     # 10
print(c1.b)     # 20
print(c1.c)     # 30
print(c1.d)     # 200











