import os
import re
import sys

def search_file(full_file_path, search_term):
	try:
		with open(full_file_path, 'r') as f:
			buffer = f.read()
	except:
		return
	res = [_.start() for _ in re.finditer(search_term, buffer)]	
	for r in res:
		print(f'File is: {full_file_path}, string is "{buffer[r-5:r+5]}"')

def search_dir(file_path, search_term):
	for f in os.listdir(file_path):
		path = f'{file_path}/{f}'
		if os.path.isfile(path):
			search_file(path, search_term)
		elif os.path.isdir(path):
			search_dir(path, search_term)

starting_directory = sys.argv[1]
search_term = sys.argv[2]
search_dir(starting_directory, search_term)

