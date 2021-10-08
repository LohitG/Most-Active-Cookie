#!/usr/bin/env python
import argparse

# parse through arguments and store them in args as an iterable
parser = argparse.ArgumentParser(description = 'Process arguments')
parser.add_argument('filename')
parser.add_argument('-d')
args = parser.parse_args()

# open file
cookie_file = open(args.filename, "r")

# skip first line
cookie_file.readline()

cookies_from_date = []

# iterate through each line of csv
for line in cookie_file:
	# split up data and keep only relevant information
	components = line.split(',')
	components[1] = components[1][:10]
	# if the date matches the input, add cookie to list
	if components[1] == args.d:
		cookies_from_date += [components[0]]

# helper function to find mode
def find_mode(cookies):
	# create a dictionary to store cookies and their frequencies
	dict_of_cookies = {}
	# iterate through cookies
	for cookie in cookies:
		# add cookie to dictionary or update its frequency
		if cookie in dict_of_cookies:
			dict_of_cookies[cookie] += 1
		else:
			dict_of_cookies[cookie] = 1
	mode_values = []
	# determine max frequency of a cookie
	max_frequency = max(dict_of_cookies.values())
	# iterate through all cookie/frequency pairs and add cookie to list of
	# modes if its frequency matches max frequency
	for cookie, frequency in dict_of_cookies.items():
		if frequency == max_frequency:
			mode_values += [cookie]
	return mode_values

# handle a situation where there are no cookies from the specified data
if len(cookies_from_date) == 0:
	quit()

# find_mode of the cookies from the given data
list_of_modes = find_mode(cookies_from_date)

# print each the most frequent cookie/cookies
for cookie in list_of_modes:
	print(cookie)