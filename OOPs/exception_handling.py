"""
1. try: includes any statements/expressions which throws error
2. except: takes the control when try block has some exceptions
3. finally: mandatorily gets executed even if there is an exception or not

4 types of exception blocks
1. default:  try -- except:
2. specific : try -- except <exception_name> as msg:
3. multiple : try -- except
					except
4. Generic: try --- except <Exception/BaseException> as msg:
"""
# default exception block

try:
	print("in try block")
	print(name)         # NameError

except:
	print("in except block")

a = 10
print(a)

# #####################################################################

a = 10
b = 0

try:
	c = a / b       # ZeroDivisionError
	print(c)

except:
	b = 1
	c = a / b
	print(c)

#####################################################################
l = [1, 2, 3]
num = 10

try:
	l.remove(num)           # ValueError

except:
	print("The number is not present please try with a different number")

print(l)

# #######################################################################
# Specific exception block
l = [1, 2, 3]
num = 10

try:
	# l.remove(num)           # ValueError
	print(string1)              # NameError

except ValueError:
	print("The number is not present please try with a different number")

print(l)

########################################################################
# multiple exception block

l = [1, 2, 3]
num = 10

try:
	l.remove(num)           # ValueError
	# print(string1)              # NameError

except ValueError as error_msg:
	print(error_msg)
	print("The number is not present please try with a different number")

except NameError as err:
	print(err)
	print("handling Name error")

print(l)

###################################################################
# Generic exception block: Exception or BaseException

try:
	list().append(1, 2)       # TypeError
	print(list2)            # NameError

except Exception as msg:
	print(msg)
	print("in except block")

######################################################################
# finally

try:
	print("in try block")
	list().append(1, 2)       # TypeError

except Exception as msg:
	print(msg)
	print("in except block")

finally:
	print("in finally block")
	print(1 + 2)

######################################################################
# raise: keyword which helps in raising any exception anywhere

a = 10
b = 20

print(a + b)
# raise ValueError("Raising value error")

amount = -1000

if amount < 0:
	raise ValueError("Amount cannot be negative")

# login scenario
username = "admin"
password = "pwd"

if username == "User1" and password == "pwd":
	print("Login successful")
else:
	raise Exception("invalid username or password")

print("Home page funtionalities")
######################################################################
# custom exceptions

class InvalidCredentials(Exception):
	pass

# login scenario
username = "admin"
password = "pwd"

if username == "User1" and password == "pwd":
	print("Login successful")
else:
	raise InvalidCredentials("invalid username or password")

print("Home page funtionalities")




