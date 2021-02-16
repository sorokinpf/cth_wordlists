#!/usr/bin/env python
from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
	if len(sys.argv)!=3:
		print ('remove_duplicate.py <dictionary> <new_dictionary>')
		exit(1)
	data = open(sys.argv[1],'rb').read().split(b'\n')
	new_data = []
	for s in data:
		if s not in new_data:
			new_data.append(s)
		else:
			#eprint ('removing: %s' % s)
			pass
	target = open(sys.argv[2],'wb')
	target.write(b'\n'.join(new_data))
	target.close()


if __name__ == '__main__':
	main()