#ref , http://marco79423.twbbs.org/articles/%E6%B7%BA%E8%AB%87-regex-%E5%8F%8A%E5%85%B6%E6%87%89%E7%94%A8/

import re
import sys


def readFile():
	data = []
	with open("data.ex", "r") as fr:
		for line in fr.readlines():
			data.append(line.strip())
	return data	


def select(line):
	matchObj = re.match( r'this is a pencil', line, re.M|re.I)	
	if matchObj:
		print matchObj.group(0)

def select_or(line):
	matchObj = re.match( r'this is a (p|b)', line, re.M|re.I)	
	if matchObj:
		print line

	matchObj = re.match( r'this is a [pb]', line, re.M|re.I)	
	if matchObj:
		print line

def select_un(line):
	matchObj = re.match( r'this is a [^c]', line, re.M|re.I)	
	if matchObj:
		print line

def count_star(line):
	matchObj = re.match( r'this is a (p*)encil', line, re.M|re.I)	
	if matchObj:
		print line
	
def count_plus(line):
	matchObj = re.match( r'this is a (p+)encil', line, re.M|re.I)	
	if matchObj:
		print line

def count_num(line):
	matchObj = re.match( r'this is a (p){2,3}encil', line, re.M|re.I)	
	if matchObj:
		print line

def position_start(line):
	matchObj = re.match( r'^tthis is a (p){2,3}encil', line, re.M|re.I)	
	if matchObj:
		print line

def position_end(line):
	matchObj = re.match( r'this is a (p){2,3}encil$', line, re.M|re.I)	
	if matchObj:
		print line

def extract_dup(line):
	matchObj = re.match( r'(this){2} is a (p){2,3}encil$', line, re.M|re.I)	
	if matchObj:
		print line

def extract_num(line):
	matchObj = re.match( r'this is a (\d+)cm pencil', line, re.M|re.I)	
	if matchObj:
		print line
		print matchObj.group(0)
		print matchObj.group(1)

def extract_insert(line):
	matchObj = re.match( r'this is a (\d+)cm (\1) type pencil', line, re.M|re.I)	
	if matchObj:
		print line
		print matchObj.group(0)
		print matchObj.group(1)

def main():
	data = readFile()
	func = getattr(sys.modules[__name__], sys.argv[1])
	for line in data:
		func(line)
		print
		'''
		matchObj = re.search( r'his is a pen.', line, re.M|re.I)	
		if matchObj:
			print matchObj.group(0)
		'''

if __name__ == "__main__":
	main()
