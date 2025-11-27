l = [1, 2, 3, 4]

print(len(l))
print(l.__len__())
l.__dir__()             # dir(l)

######################################################################
class Demo:

	def __init__(self):
		print("in constructor")

d = Demo()          # d.__init__()

######################################################################
# addition
a = 10
b = 20

print(a + b)
print(a.__add__(b))

print(a - b)
print(a.__sub__(b))

######################################################################
# in operator
s = "hello world"

print("e" in s)
print(s.__contains__("e"))

######################################################################
# comparison operators
print(a > b)
print(a.__gt__(b))

print(a < b)
print(a.__lt__(b))

#######################################################################
a = enumerate("hello")

print(next(a))      # (0, 'h')
print(a.__next__()) # (1, 'e')

#######################################################################
class Sample:

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def display(self):
		print("in display")


s = Sample(1, 2)            # s.__init__(1, 2)
print(s.a)                  # s.__getattribute__("a")
s.display()                 # s.__getattribute__("display")

s.b = 12                    # s.__setattr__("b", 12)

######################################################################

s = "hello"
print(s.count("h"))
print(s.__getattribute__("count"))
print(s.__getattribute__("count")("h"))

########################################################################
class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __len__(self):
		return 2

	def __add__(self, other):
		return self.x + other.x, self.y + other.y


p1 = Point(1, 2)
p2 = Point(3, 4)
print(len(p1))           # p.__len__()
print(p1 + p2)          # p1.__add__(p2)















