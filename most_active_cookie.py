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

dict_of_dates = {}

for line in cookie_file:
	components = line.split(',')
	components[1] = components[1][:10]
	if components[1] in dict_of_dates:
		dict_of_dates[components[1]] += [components[0]]
	else:
		dict_of_dates[components[1]] = [components[0]]

cookies_from_date = dict_of_dates[args.d]

def find_mode(lst):
	dict_of_cookies = {}
	for cookie in lst:
		if cookie in dict_of_cookies:
			dict_of_cookies[cookie] += 1
		else:
			dict_of_cookies[cookie] = 1
	mode_values = []
	max_frequency = max(dict_of_cookies.values())
	for cookie, frequency in dict_of_cookies.items():
		if frequency == max_frequency:
			mode_values += [cookie]
	return mode_values

list_of_modes = find_mode(cookies_from_date)

for cookie in list_of_modes:
	print(cookie)