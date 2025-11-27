"""
classnames follow pascal case

class ClassName:
	pass

obj_name = class_name()
"""

# class is a blueprint
class Simple:
	pass


# creating an instance or object --> physical entity/form of the class
object1 = Simple()
print(object1)

object2 = Simple()
print(object2)

#######################################################################
class Building:
	# class variables
	dimension = "60 * 40"
	no_of_halls = 2
	no_of_rooms = 5
	facing = "north"


building_1 = Building()
print(building_1)       # <__main__.Building object at 0x00000262FC36FA90>

building_2 = Building()
print(building_2)       # <__main__.Building object at 0x00000262FC36FA60>

# accessing class variables through an instance building_1
print(building_1.dimension)     # 60 * 40
print(building_1.no_of_halls)   # 2
print(building_1.no_of_rooms)   # 5
print(building_1.facing)        # north

# accessing class variables through an instance building_2
print(building_2.dimension)     # 60 * 40
print(building_2.no_of_halls)   # 2
print(building_2.no_of_rooms)   # 5
print(building_2.facing)        # north

# accessing class variable through class name
print(Building.dimension)       # 60 * 40
print(Building.no_of_halls)     # 2
print(Building.no_of_rooms)     # 5
print(Building.facing)          # north

#######################################################################
# creating instance/object variables
class Building:

	# constructor -> construct objects with their own properties
	# self -> address of the object which is invoking/calling __init__
	def __init__(self, dimension, halls, rooms, facing):       # function
		self.dimension = dimension       # "30 * 40"
		self.halls = halls               # 1
		self.rooms = rooms               # 2
		self.facing = facing             # East


building_1 = Building("30 * 40", 1, 2, "East")
# building_1.__init__("30 * 40", 1, 2, "East")

building_2 = Building("60 * 40", 2, 4, "North")
# building_2.__init__("60 * 40", 2, 4, "North")

# # accessing the object variables using object address
print(building_1.dimension)     # 30 * 40
print(building_1.halls)         # 1
print(building_1.rooms)         # 2
print(building_1.facing)        # East

# accessing the object variables using class name
# print(Building.dimension)       # AttributeError

#######################################################################
# create a class Employee with 3 emp objects, each object should have different
# name, age, pay, phone_no

class Employee:

	def __init__(self, name, age, pay, phone_no):
		self.name = name
		self.age = age
		self.pay = pay
		self.phone_no = phone_no


emp1 = Employee("steve", 25, 2000, 123456776)
emp2 = Employee("Tom", 30, 5000, 47479875)

print(emp1.name)
print(emp2.pay)








