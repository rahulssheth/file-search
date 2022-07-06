import os
import re

def search_file(path, input_file, search_term):
	with open(input_file, 'r') as f:
		try:
			buffer = f.read()
		except:
			return
	res = [_.start() for _ in re.finditer(search_term, buffer)]	
	for r in res:
		print(f'File is: {input_file}, string is "{buffer[r-5:r+5]}"')

def search_dir(file_path):
	for f in os.listdir(file_path):
		if os.path.isfile(f):
			search_file(file_path, f, 'hello')
		elif os.path.isdir(f):
			path = f'{file_path}/{f}'
			search_dir(path)

search_dir('.')
