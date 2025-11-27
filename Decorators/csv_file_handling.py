# inbuilt module - csv

import csv

# opening a csv file
ex_path = r"C:\Users\Vidyashree M C\PycharmProjectspython_new\files\csv_files\example.csv"


# reading from csv file
with open(ex_path) as file:
	reader_obj = csv.reader(file)       # list of values

	for line in reader_obj:
		print(line)

print()
# DictReader
with open(ex_path) as file:
	reader_obj = csv.DictReader(file)

	for data in reader_obj:
		print(data)

####################################################################################
# writing into csv file

path = r"C:\Users\Vidyashree M C\PycharmProjectspython_new\files\csv_files\\"

# with open(path+"sample.csv", "w") as csv_file:
# 	writer_obj = csv.writer(csv_file)
#
# 	data = ["name", "emp_id", "email"]
#
# 	writer_obj.writerow(data)
# 	writer_obj.writerows(["abcdef", "def", "xyz"])

# DictWriter()

with open(path+"saqmple.csv", "w") as csv_file:
	writer_obj = csv.DictWriter(csv_file, ["name", "email", "e_id"])

	writer_obj.writeheader()
	writer_obj.writerow({"name": "John", "email": "john@abc.com", "e_id": 10})
	writer_obj.writerows([{"name": "John", "email": "john@abc.com", "e_id": 10},
	                      {"name": "John", "email": "john@abc.com"}])


"""
reading csv
-----------
1. reader(file_obj)       --> list of rows
2. DictReader(file_obj)   --> dictionary of rows

writing into csv
----------------
1. writer(file_obj)
	-   writerow(list of data)
	-   writerows(list of iterables)
	
2. DictWriter(file_obj, keys/fieldnames)
	-   writeheader()
	-   writerow(dictionary)
	-   writerows(list of dictionaries)
"""

##################################################################################
emp_file = r"./files/csv_files/employees.csv"

# list of employee names
# reader()
with open(emp_file) as file:
	reader_obj = csv.reader(file)
	header = next(reader_obj)

	names = [row[0] for row in reader_obj]
	# print(names)


# DictReader
with open(emp_file) as file:
	reader_obj = csv.DictReader(file)

	data = [row["name"] for row in reader_obj]
	# print(data)

#######################################################
# group all the male and female employees

# reader()
with open(emp_file) as file:
	r_obj = csv.reader(file)

	header = next(r_obj)
	d = {}
	for row in r_obj:
		name, gender = row[0], row[1]
		if gender not in d:
			d[gender] = [name]
		else:
			d[gender] += [name]

	print(d)

# DictReader()
with open(emp_file) as file:
	r_obj = csv.DictReader(file)

	d = {}

	for row in r_obj:
		# gender, name = row["gender"], row["name"]
		if row["gender"] not in d:
			d[row["gender"]] = [row["name"]]
		else:
			d[row["gender"]] += [row["name"]]

	# print(d)

#####################################################
# extract names of the employees who earn more than 70000

with open(emp_file) as file:
	r_obj = csv.DictReader(file)

	for row in r_obj:
		if int(row["pay"]) > 70000:
			print(row["name"])

#############################################################
# count the number of countries in vaccination_data.csv

vac_file = r"C:\Users\Vidyashree M C\PycharmProjectspython_new\files\csv_files\vaccination_data.csv"

# dictreader

with open(vac_file) as file:
	reader = csv.DictReader(file)
	count = 0
	for row in reader:
		count += 1

	# print(count)

# calculate the sum of total_vaccinations
with open(vac_file) as file:
	reader = csv.DictReader(file)
	total = 0

	for row in reader:
		if row["TOTAL_VACCINATIONS"]:
			total += int(row["TOTAL_VACCINATIONS"])

	# print(total)

# extract the latest updated data
with open(vac_file) as file:
	reader = csv.DictReader(file)

	date_updated = []
	for row in reader:
		date_updated.append(row["DATE_UPDATED"])

	# print(date_updated)
	oldest, *rest, latest_date = sorted(date_updated)
	print(latest_date)


date1 = '2022-08-15'
date2 = '2021-08-15'
date3 = '2021-12-30'

print(date1 > date2)
print(date1 > date3)







