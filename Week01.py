import csv # imports the csv module
import sys # imports the sys module

f = open('TB_burden_countries_2014-09-29.csv') # opens the csv file
	
# Excercise Part 1 - 1
reader = csv.reader(f)
lines=len(list(reader))
print(lines)

# Count of row without header

count_of_rows = 0
with open('TB_burden_countries_2014-09-29.csv') as f:
	csv_reader_object = csv.reader(f)
	if csv.Sniffer().has_header:
		next(csv_reader_object)
	for row in csv_reader_object:
		count_of_rows += 1
print(count_of_rows)

# Excercise Part 1 - 2

total_e_prev_num = 0

row_index_e_prev_num = 10
count_missing_rows = 0
with open('TB_burden_countries_2014-09-29.csv', newline = '') as f:
	csv_reader_object = csv.reader(f)
	if csv.Sniffer().has_header:
		next(csv_reader_object)
	for row in csv_reader_object:
		if len(row[row_index_e_prev_num]) == 0:
			count_missing_rows +=1
			continue
		float_e_prev_num = float(row[row_index_e_prev_num])
		total_e_prev_num += float_e_prev_num
print(total_e_prev_num)
print(total_e_prev_num / (count_of_rows - count_missing_rows))

# Excercise Part 1 - 3

count_of_rows_1990 = 0
count_of_rows_2011 = 0
with open('TB_burden_countries_2014-09-29.csv') as f:
	csv_reader_object = csv.reader(f)
	if csv.Sniffer().has_header:
		next(csv_reader_object)
	for row in csv_reader_object:
		if int(row[5]) == 1990:
			count_of_rows_1990 += 1
		elif int(row[5]) == 2011:
			count_of_rows_2011 += 1
print(count_of_rows_1990)
print(count_of_rows_2011)


total_e_prev_num_1990 = 0
total_e_prev_num_2011 = 0

row_index_e_prev_num = 10
count_missing_rows_1990 = 0
count_missing_rows_2011 = 0
with open('TB_burden_countries_2014-09-29.csv', newline = '') as f:
	csv_reader_object = csv.reader(f)
	if csv.Sniffer().has_header:
		next(csv_reader_object)
	for row in csv_reader_object:
		if int(row[5]) == 1990:
			if len(row[row_index_e_prev_num]) == 0:
				count_missing_rows_1990 +=1
				continue
			float_e_prev_num = float(row[row_index_e_prev_num])
			total_e_prev_num_1990 += float_e_prev_num
		elif int(row[5]) == 2011:
			if len(row[row_index_e_prev_num]) == 0:
				count_missing_rows_2011 +=1
				continue
			float_e_prev_num = float(row[row_index_e_prev_num])
			total_e_prev_num_2011 += float_e_prev_num
print(total_e_prev_num_1990 / (count_of_rows_1990 - count_missing_rows_1990))
print(total_e_prev_num_2011 / (count_of_rows_2011 - count_missing_rows_2011))
	
# The difference the average number of 2011 is much lower than the number of 1990 and much lower when compares with the total average

# Excercise Part 2 - 1 

import numpy as np

# Create an array of int ranging from 5-15
a = np.array([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], dtype=int)

# Create an array containing 7 evenly spaced numbers between 0 and 23
b = np.arange(7, 23, 2)

# Numpy has several routines for generating artificial data following a particular structure. 
# Check this page for different types. And generate an artificial numpy array with values between -1 and 1 that follow a uniform data distribution.
c = np.random.uniform(-1,1,1000)

# Visualise the array in an histogram in matplotlib
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 15, density=True)
plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
plt.show()

#Create two random numpy arrays with 10 elements. Find the Euclidean distance between the arrays using arithmetic operators, hint: numpy has a sqrt function
c = np.arange(10)
d = np.arange(10)
Euclidean_distance = np.sqrt(np.sum(((c - d) ** 2)))
