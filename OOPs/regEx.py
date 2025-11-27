import re   # inbuilt module

string = "Hello world, Hello everyone, Hello"

words = string.split()
for word in words:
	if word == "Hello":
		print(word)

"""
methods of re
1. re.findall(pattern, string): list of matches
2. re.finditer()
3. re.search()
4. re.sub(old, new, string)
"""

string = "Hello world, Hello everyone, Hello"
pattern = "Hello"

result = re.findall(pattern, string)
print(result)           # ['Hello', 'Hello', 'Hello']
print(len(result))      # 3

result = re.finditer(pattern, string)
print(result)           # <callable_iterator object at 0x000001B5AA3BF490>

for item in result:
	print(item)
	print(item.start(), item.end())

"""
<re.Match object; span=(0, 5), match='Hello'>
0 5
<re.Match object; span=(13, 18), match='Hello'>
13 18
<re.Match object; span=(29, 34), match='Hello'>
29 34
"""

########################################################################
string = "Hello world, Hello everyone, Hello"
pattern = "Hello"

result = re.search(pattern, string)
print(result)
print(result.start(), result.end())

# <re.Match object; span=(0, 5), match='Hello'>

########################################################################
string = "Hello world, Hello everyone, Hello"

result = re.sub("Hello", "Hai", string)
print(result)

result = string.replace("Hello", "Hai")
print(result)

########################################################################
# count the number of times "e" is present in sentence
sentence = "The Theory of relativity"

# for loop
count = 0
for char in sentence:
	if char == "e":
		count += 1
print(count)

# regEx
result = re.findall("e", sentence)
print(result)           # ['e', 'e', 'e']
print(len(result))

########################################################################
# character set- [ae]

# find "e" and "a"
sentence = "The Theory of relatIvity"

matches = re.findall("[ae]", sentence)
print(matches)          # ['e', 'e', 'e', 'a']

# al the vowel characters
matches = re.findall("[aeiouAEIOU]", sentence)
print(matches)          # ['e', 'e', 'o', 'o', 'e', 'a', 'I', 'i']

matches = re.findall("[aeiou]", sentence, re.IGNORECASE)
print(matches)          # ['e', 'e', 'o', 'o', 'e', 'a', 'I', 'i']

# match the word "theory" ignoring the case
sentence = "The Theory of relatIvity"

result = re.findall(r"theory", sentence, re.IGNORECASE)
print(result)

result = re.findall(r"[tT]heory", sentence)
print(result)

# range( - )
# match only lowercase characters
sentence = "The Theory of relatIvity"

count = 0
for char in sentence:
	if "a" <= char <= "z":      # if char.islower():
		count += 1
print(count)

# regEx
result = re.findall(r"[a-z]", sentence)
print(len(result))

# match only uppercase characters
result = re.findall(r"[A-Z]", sentence)
print(len(result))

########################################################################
sentence = "The cost of this book is Rs.100"

# count only the alphabets
matches = re.findall(r"[a-zA-Z]", sentence)
print(len(matches))

# count only numbers
matches = re.findall(r'[0-9]', sentence)
print(matches)      # ['1', '0', '0']

matches = re.findall(r'[\d]', sentence)
print(matches)      # ['1', '0', '0']

# match all the non-special characters
pattern = r'[a-zA-Z0-9]'
matches = re.findall(pattern, sentence)
print(matches)

matches = re.findall(r'[\w]', sentence)
print(matches)

#######################################################################
# matching special characters
sentence = "Hello! How are you, doing today:)"

matches = re.findall(r'[^a-zA-Z0-9 ]', sentence)
print(matches)

# matching whitespaces
matches = re.findall(r' ', sentence)
print(matches)

matches = re.findall(r'\s', sentence)
print(matches)

#######################################################################
sentence = "The cost of this book is Rs.100"

# matching only alphabets
matches = re.findall(r"[a-zA-Z]", sentence)
print(matches)          # ['T', 'h', 'e', 'c', 'o', 's', 't', 'o', 'f', 't', 'h', 'i', 's', 'b', 'o', 'o', 'k', 'i', 's', 'R', 's']

# matching words
matches = re.findall(r"[a-zA-Z]+", sentence)
print(matches)          # ['The', 'cost', 'of', 'this', 'book', 'is', 'Rs']

# matching digits
matches = re.findall(r"[0-9]", sentence)
print(matches)          # ['1', '0', '0']

matches = re.findall(r"\d", sentence)
print(matches)          # ['1', '0', '0']

# matching numbers
matches = re.findall(r"[0-9]+", sentence)
print(matches)          # ['100']

matches = re.findall(r"\d+", sentence)
print(matches)          # ['100']

# match non-special characters
matches = re.findall(r"[a-zA-Z0-9]", sentence)
print(matches)  # ['T', 'h', 'e', 'c', 'o', 's', 't', 'o', 'f', 't', 'h', 'i', 's', 'b', 'o', 'o', 'k', 'i', 's', 'R', 's', '1', '0', '0']

matches = re.findall(r"\w", sentence)
print(matches)  # ['T', 'h', 'e', 'c', 'o', 's', 't', 'o', 'f', 't', 'h', 'i', 's', 'b', 'o', 'o', 'k', 'i', 's', 'R', 's', '1', '0', '0']

matches = re.findall(r"[a-zA-Z0-9]+", sentence)
print(matches)  # ['The', 'cost', 'of', 'this', 'book', 'is', 'Rs', '100']

matches = re.findall(r"\w+", sentence)
print(matches)  # ['The', 'cost', 'of', 'this', 'book', 'is', 'Rs', '100']

########################################################################
string = "sony16pvt923ltd87"        # 16 + 923 + 87

nums = re.findall(r"\d", string)
print(nums)         # ['1', '6', '9', '2', '3', '8', '7']

nums = re.findall(r"\d+", string)
print(nums)         # ['16', '923', '87']

total = 0

for num in nums:
	total += int(num)
print(total)

#######################################################################
# /b - boundaries







