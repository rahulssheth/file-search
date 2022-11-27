import os
import re
import sys
import pydoc


def search_file(full_file_path, search_term):
	try:
		with open(full_file_path, 'r') as f:
			buffer = f.read()
	except Exception:
		return ''
	res = [_.start() for _ in re.finditer(search_term, buffer)]
	output_str = ''
	buffer_len = len(buffer)
	for r in res:
		buffer_start = max(0, r-5)
		buffer_end = min(buffer_len, r+5)
		output_str += f'File is: {full_file_path}, string is "{buffer[buffer_start:buffer_end]}"\n'
	return output_str

def search_dir(file_path, search_term):
	output_str = ''
	try:
		for f in os.listdir(file_path):
			f = f.lstrip("/")
			path = f'{file_path}/{f}'
			if os.path.isfile(path):
				output_str += search_file(path, search_term)
			elif os.path.isdir(path):
				output_str += search_dir(path, search_term)
	except Exception as e:
		print(e)
		return output_str
	return output_str

starting_directory = sys.argv[1]
search_term = sys.argv[2]
output_str = search_dir(starting_directory, search_term)
pydoc.pager(output_str)
