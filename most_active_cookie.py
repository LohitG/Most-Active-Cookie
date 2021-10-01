#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(description = 'Process arguments')
parser.add_argument('filename')
parser.add_argument('-d')
args = parser.parse_args()
def test_function(test):
	return test

print(args.d)