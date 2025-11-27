""" This is module level documentation string """

# a = 10
# # callable
# print(callable(a))
# b = a
#
# # accessing integer object "10" through a and b
# print(a)    # 10
# print(b)    # 10
#
# l1 = [1, 2, 3]
# l2 = l1
#
# # accessing list object [1, 2, 3] through l1 and l2
# print(l1)
# print(l2)
#
# d1 = {1: 2, 2: 3}
# d2 = d1
#
# # accessing dictionary object {1: 2, 2: 3} through d1 and d2
# print(d1)
# print(d2)
#
# ##################################################################################
# def add(a, b):
# 	print(a + b)
#
# # add and a both references points to the memory address of function add
# print(add)          # <function add at 0x000001B3C7CC3E20>
# a = add
# print(callable(a))
# print(callable(add))
#
# # invoking add function using a and add
# add(1, 2)           # 3
# a(1, 2)             # 3
#
#
# def sub(a, b):
# 	print(a - b)
#
# s = sub
# sub(1, 2)           # -1
# s(1, 2)             # -1
#
# ####################################################################################
# data = []
#
# data.append(10)
# data.append(20)
# data.append(30)
# data.append(add)
# data.append(sub)
#
# print(data) # [10, 20, 30, <function add at 0x000001E1AA3DADD0>, <function sub at 0x000001E1AA3DAE60>]
#
# for item in data:
# 	if callable(item):
# 		item(1, 2)
#
# ####################################################################################
# # storing function references in a dictionary
#
# operations = {
# 	"add": add,
# 	"sub": sub
# }
#
#
# def calculator(operand, value1, value2):
# 	if operand in operations:
# 		operations[operand](value1, value2)     # operations.get(operand)(v1, v2)
# 	return "unknown operation"
#
#
# calculator("add", 1, 2)
# calculator("sub", 1, 2)
# print(calculator("mul", 1, 2))
#
# ######################################################################################
# def dummy(some_thing):
# 	print(some_thing)
#
#
# # passing integer into dummy function
# dummy(10)
#
# # passing a list object
# dummy([1, 2, 3])
#
# # passing a dictionary object
# dummy({"a": 1, "b": 2})
#
# # passing function references into dummy function
# dummy(add)      # some_thing -> add (callback function)
# dummy(sub)      # some_thing -> sub (callback function)

#######################################################################################
# function taking function references/ memory address as argument and invoking it

def spam(some_func, *args, **kwargs):     # add, (1, 2)
	print(some_func)
	some_func(*args, **kwargs)     # add(1, 2)

def greet():
	print("hello world")

# spam(greet)

def display():
	print("in display function")

# spam(display)

def add(a, b):
	print(a + b)

# spam(add, a=1, b=2)

#######################################################################################
import time

def delay(some_func, *args, **kwargs):
	time.sleep(5)
	result = some_func(*args, **kwargs)
	return result


def greet():
	return "helloooo"

# print(delay(greet))
#######################################################################################
# functions -> first class objects
def delay(some_func):
	def inner(*args, **kwargs):
		time.sleep(5)
		result = some_func(*args, **kwargs)
		return result
	return inner


@delay      # greet = delay(greet)
def greet(message):
	return message


# greet = delay(greet)
# print(greet)       # inner address
# print(greet("hello world"))

@delay
def add(a, b):
	return a + b

# add = delay(add)
# print(add(1, 2))        # 3

####################################################################################
# log decorator - log the function's name
# __name__ - name of any programmable entity
def log(some_func):
	def wrapper(*args, **kwargs):
		print("The decorated function is", some_func.__name__)
		result = some_func(*args, **kwargs)     # spam()
		return result
	return wrapper


@log        # spam = log(spam)  = wrapper
def spam():
	return "executing spam...."


# print(spam())           # wrapper()

@log        # greet = log(greet) = wrapper
def greet():
	return "Good morning"

# print(greet())

######################################################################################
# positive decorator

def positive(func):
	def wrapper(*args, **kwargs):
		result = abs(func(*args, **kwargs))
		return result
	return wrapper

@positive
def sub(a, b):
	return a - b

# print(sub(1, 2))

######################################################################################
def positive(func):
	def wrapper(value1, value2):
		if value1 > value2:
			result = func(value1, value2)
			return result
		raise ValueError("value1 must be greater than value2")

	return wrapper


@positive
def sub(a, b):
	return a - b

# print(sub(3, 1))        # 2
# print(sub(1, 3))        # ValueError

###################################################################################
# count the numbers of arguments passed to a decorated function

def count_arguments(func):
	def wrapper(*args, **kwargs):
		print(f"arguments passed to {func.__name__} are {len(args) + len(kwargs)}")
		result = func(*args, **kwargs)
		return result
	return wrapper


def count_arguments(func):
	def wrapper(*args, **kwargs):
		count = 0
		for _ in args:
			count += 1              # print(add(1, 2, 3))

		for _ in kwargs:
			count += 1

		print(f"arguments passed to {func.__name__} are {count}")
		result = func(*args, **kwargs)
		return result
	return wrapper


@count_arguments    # add = count_arguments(add)
def add(a, b, c):
	return a + b + c

@count_arguments
def sub(a, b):
	return a - b

# print(add(1, 2, 3))
# print(add(1, b=2, c=3))

#####################################################################################
# decorator that does not allow a function to take more than 3 arguments

def limit_arguments(func):

	def wrapper(*args, **kwargs):
		if len(args) + len(kwargs) <= 3:
			result = func(*args, **kwargs)
			return result
		raise ValueError("Arguments cannot be more than 3")

	return wrapper

@limit_arguments
def add(a, b, c, d):
	return a + b + c + d

# print(add(1, 2, 3, 4))

######################################################################################
# decorator to reverse the function's result only if it is a string

def reverse(func):
	def wrapper(*args, **kwargs):

		result = func(*args, **kwargs)
		if isinstance(result, str):
			return result[::-1]
		return result

	return wrapper

@reverse
def convert_to_lower(string):
	if string[0] in "aeiouAEIOU":
		return string.lower()
	return string

# print(convert_to_lower("Email"))


@reverse
def add(a, b):
	return a + b


# print(add("hai", "hello"))
# print(add(1, 2))

######################################################################################
#  count the time of execution of decorated function

def execution_time(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		func(*args, **kwargs)
		end = time.time()
		print(f"Time of execution of function {func.__name__} is {end - start}")

	return wrapper


@execution_time
def make_list(num):
	l = []
	for i in range(num):
		l.append(i)

	print("list is created")


# make_list(10000000)
# make_list(10000000)

#####################################################################################
# count the number of function calls for each function
d = {}

def function_calls_count(func):
	count = 0
	def wrapper(*args, **kwargs):
		nonlocal count
		count += 1
		d[func.__name__] = count        # {add: 4, div: 2}
		result = func(*args, **kwargs)
		print(d)
		return result

	return wrapper


count = {}
def function_calls_count(func):
	def wrapper(*args, **kwargs):
		if func.__name__ not in count:
			count[func.__name__] = 1
		else:
			count[func.__name__] += 1

		result = func(*args, **kwargs)
		return result

	return wrapper

@function_calls_count
def add(a, b):
	return a + b

@function_calls_count
def div(a, b):
	return a // b


add(1, 2)           # wrapper
add(1, 2)
add(1, 2)
add(1, 2)

div(1, 2)
div(1, 2)
# print(count)


# limit the number of function calls to 3 for each function

d = {}
def function_calls_count(func):
	def wrapper(*args, **kwargs):
		if func.__name__ not in d:
			d[func.__name__] = 1
		else:
			d[func.__name__] += 1

		count = d[func.__name__]

		if count <= 3:
			result = func(*args, **kwargs)
			return result
		raise TypeError("Cannot call a function more than 3 times")

	return wrapper


@function_calls_count
def add(a, b):
	return a + b

@function_calls_count
def div(a, b):
	return a // b


# add(1, 2)           # wrapper
# add(1, 2)
# add(1, 2)
# add(1, 2)

# print(div(1, 2))
# print(div(1, 2))

######################################################################################
# cache decorator

def cache(func):
	d = {}
	def wrapper(*args, **kwargs):
		if args not in d:               # (1, 2)
			d[args] = func(*args, **kwargs)     # {(1, 2): 3}
		return d[args]
	return wrapper


@cache
def add(a, b):
	print("executing add function")
	return a + b


# print(add(1, 2))        # 3
# print(add(1, 2))
# print(add(1, 2))

@cache
def make_list(num):
	l = []
	for i in range(num):
		for j in range(2, i // 2):
			if i % j == 0:
				break
		else:
			l.append(i)

	print("list is created")
	return l


# print(make_list(10000000))
# print(make_list(10000000))
# print(make_list(10000000))

#######################################################################################
# Decorator that executes a function for 3 times

def retry(func):
	def wrapper(*args, **kwargs):
		count = 3

		while count > 0:
			try:
				result = func(*args, **kwargs)
				return result

			except ValueError:
				count -= 1              # 2, 1, 0
				if count == 0:
					return "Account is blocked"

	return wrapper


@retry
def login():
	username = input("enter the username: ")        # admin
	password = input("enter the password: ")        # admin

	if username == "admin" and password == "manager":
		return "login successful"

	raise ValueError("Invalid credentials")


# print(login())

######################################################################################
# Decorator that re-executes the function until the number is even/ until there
# is no ValueError

def re_execute(func):
	def wrapper(*args, **kwargs):

		while True:
			try:
				result = func(*args, **kwargs)
				return result

			except ValueError:
				print("number must be even")

	return wrapper


@re_execute
def even():
	number = int(input("enter a number: "))         # 3
	if number % 2 == 0:
		return number

	raise ValueError


# print(even())

#######################################################################################
# memory usage
import tracemalloc


def memory(func):
	def wrapper(*args, **kwargs):
		tracemalloc.start()
		result = func(*args, **kwargs)
		print(tracemalloc.get_traced_memory())
		tracemalloc.stop()
		return result

	return wrapper

@memory
def add(a, b):
	return a + b

# print(add(1, 2))

@memory
def make_list(num):
	l = []
	for i in range(num):
		l.append(i)

	print("list is created")

# print(make_list(10000000))
######################################################################################
# decorator that handles any exception

def handle_exception(func):
	def wrapper(*args, **kwargs):

		try:
			result = func(*args, **kwargs)

		except Exception as message:            # generic exception block
			return message

		else:
			return result

	return wrapper


@handle_exception
def login():
	username = input("enter the username: ")        # admin
	password = input("enter the password: ")        # admin

	if username == "admin" and password == "manager":
		return "login successful"

	raise ValueError("Invalid credentials")

# print(login())


@handle_exception
def div(a, b):
	return a / b


# print(div(1, 0))

####################################################################################
# parameterized decorators

# delay decorator

def outer(n):       # n -> 3, 5
	def delay(func):
		def wrapper(*args, **kwargs):
			time.sleep(n)
			result = func(*args, **kwargs)
			return result
		return wrapper
	return delay


@outer(3)      # @delay     => display = delay(display)
def display():
	return "in display"

# print(display())


@outer(5)       # @delay        => spam = delay(spam)
def spam():
	return "in spam"

# print(spam())

######################################################################################
# log decorator

def log_decorator(message="Execution started..."):
	def log(func):
		def wrapper(*args, **kwargs):
			print(message)
			func(*args, **kwargs)
		return wrapper
	return log


@log_decorator("Executing display....")
def display():
	print("in display")

# display()


@log_decorator()
def spam():
	print("in spam")

# spam()

#####################################################################################
# to execute a function n number of times

def execute_n_times(n):
	def n_times(func):
		def wrapper(*args, **kwargs):

			for _ in range(n):
				result = func(*args, **kwargs)
				print(result)

		return wrapper
	return n_times


@execute_n_times(2)
def display():
	return "in display"

# display()


@execute_n_times(5)
def spam():
	return "in spam"

# spam()

#######################################################################################
# function annotations
def add(a: int, b: int) -> int:
	return a + b


def add(a: int, b: int) -> None:
	print(a + b)


# print(add(1, 2))
# print(add("hai", "world"))


def palindrome(value: str):
	if value == value[::-1]:
		print("palindrome")
	else:
		return "not palindrome"


# palindrome("1221")

####################################################################################
# type validator decorator

def type_validator(*types):         # (int, int),   (str,)
	def type_check(func):           # func -> add
		def wrapper(*args):         # args -> ("1", 2)
			data = zip(args, types)        # [("1", int), (2, int)]

			for value, expected_type in data:       # value-> "1",  exp_type -> int
				if not isinstance(value, expected_type):
					raise TypeError(f"{value} is not an instance of {expected_type}")

			result = func(*args)
			return result
		return wrapper
	return type_check


@type_validator(int, int)
def add(a, b):
	return a + b


# print(add(1, "2"))
# print(add([1, 2], [3, 4]))
# print(add(1, 2))

@type_validator(str)
def palindrome(value):
	if value == value[::-1]:
		return "palindrome"
	else:
		return "not palindrome"


# print(palindrome("hello"))
# print(palindrome(111))

#######################################################################################
def type_validator(*types):         # (int, int)
	def type_check(func):           # func -> add
		def wrapper(*args, **kwargs):         # args -> (1, )  kwargs -> {b: 2}
			arguments = args + tuple(kwargs.values())

			data = zip(arguments, types)        # [(1, int), (2, int)]

			for value, expected_type in data:       # value-> "1",  exp_type -> int
				if not isinstance(value, expected_type):
					raise TypeError(f"{value} is not an instance of {expected_type}")

			result = func(*args, **kwargs)
			return result
		return wrapper
	return type_check


@type_validator(int, int)
def add(a, b):
	return a + b


# print(add("1", b=2))

######################################################################################


def type_validator(**types):         # {name: str, id: int, pay: int}
	def type_check(func):           # func -> emp_details
		def wrapper(*args, **kwargs):         # args -> ("John", 12)  kwargs -> {pay: 10000}
			arguments = args + tuple(kwargs.values())
			data = zip(arguments, types.values())        # [("John", str), (12, int), (10000, int)]

			for value, expected_type in data:       # value-> "1",  exp_type -> int
				if not isinstance(value, expected_type):
					raise TypeError(f"{value} is not an instance of {expected_type}")

			result = func(*args, **kwargs)
			return result
		return wrapper
	return type_check


@type_validator(name=str, id=int, pay=int)
def emp_details(name, id, pay):
	return name, id, pay


# print(emp_details("John", "12", pay=10000))

#######################################################################################

def decorator1(func):
	def wrapper(*args, **kwargs):

		print("starting decorator 1.......")
		func(*args, **kwargs)
		print("ending decorator 1.......")

	return wrapper


def decorator2(func):
	def wrapper(*args, **kwargs):
		print("decorator 2 started!!!!!!!!")
		func(*args, **kwargs)
		print("decorator 2 ended!!!!!!!!")

	return wrapper


@decorator1             # spam = decorator1(decorator2(spam))
@decorator2
def spam():
	print("in spam")

# spam()

######################################################################################
def hike_salary(func):
	def wrapper(*args, **kwargs):
		print("in hike salary")
		result = func(*args, **kwargs)
		return result + 5000

	return wrapper

def check_salary(func):
	def wrapper(*args, **kwargs):

		result = func(*args, **kwargs)
		print("in check salary")
		if result >= 10000:
			return result

	return wrapper


@hike_salary
@check_salary
def details(pay):
	print("in details")
	return pay

# print(details(1000))


##################################################################################
def convert_to_upper(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		return result.upper()
	return wrapper


def check_palindrome(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		if result == result[::-1]:
			return result
		else:
			return result[::-1]
	return wrapper


@convert_to_upper
@check_palindrome
def get_name(fname, lname):
	return fname + " " + lname


# print(get_name("John", "doe"))
# print(get_name("bob", "bob"))

#######################################################################################
# functools
from functools import wraps


def log(some_func):
	@wraps(some_func)
	def wrapper(*args, **kwargs):
		""" This decorator logs a message before executing the function """
		print(f"executing {some_func.__name__}....")
		result = some_func(*args, **kwargs)
		return result
	return wrapper


@log
def spam():
	""" This is a spam function """
	return "in spam"


# print(spam())       # wrapper
# print(spam.__doc__)
# print(spam.__name__)        # spam

# print(__name__)
# print(__doc__)
######################################################################################


