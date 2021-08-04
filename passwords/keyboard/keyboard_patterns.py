import itertools
import string
import argparse

main_patterns=[
'1qaz','2wsx','3edc','4rfv','5tgb','6yhn','7ujm','8ik,','9ol.','0p;/'
]
second_patterns=[
'4esz','5rdx','6tfc','7ygv','8uhb','9ijn','0okm','-pl,','=[;.'
]
patterns_list = [main_patterns,second_patterns]
upper_table={
	'1':'!','2':'@','3':'#','4':'$','5':'%','6':'^','7':'&','8':'*','9':'(','0':')','-':'_','=':'+',
	'[':'{',']':'}',';':':','\'':'"','\\':'|',',':'<','.':'>','/':'?'
}

def up(pattern):
	r = ''
	for c in pattern:
		if c in string.ascii_lowercase:
			r += c.upper()
		else:
			r += upper_table[c]
	return r

def neibors(l,i):
	#print (l,i)
	if i==0:
		return [0,1]
	if i == l-1:
		return [l-2,l-1]
	return [i-1,i,i+1]

def generate_ids(length,number):
	l=length
	n=number
	start = [(i,) for i in range(l)]
	current = start
	for i in range(n-1):
		new = []
		for elem in current:
			new += [(*elem,neib) for neib in neibors(l,elem[-1])]
		current = new
	return (current)

def make_all_patterns(pattern,inverse,upper):
	result = []
	for p in pattern:
		el = [p]
		if inverse:
			el = el+[x[::-1] for x in el]
		if upper:
			el = el+[up(x) for x in el]
		result.append(el)
	return result


def main():
	parser = argparse.ArgumentParser(description='Build password keyboard template list')
	parser.add_argument('pattern', type=int,
	                    help='1 -> 1qaz ...; 2->4esz ...',default=1)
	parser.add_argument('length', type=int,
	                    help='number of templates in each password')
	parser.add_argument('-i','--inverse',action='store_false',
						help='no inverse templates')
	parser.add_argument('-u','--up',action='store_false',
						help='no shift-transform')

	args = parser.parse_args()


	pattern = main_patterns
	if args.pattern == 1:
		pattern = main_patterns
	elif args.pattern == 2:
		pattern = second_patterns
	else:
		parser.print_help()
		return -1



	all_patterns = make_all_patterns(pattern,args.inverse,args.up)

	ids = generate_ids(len(pattern),args.length)
	for elem in ids:
		target_patterns = [all_patterns[i] for i in elem]
		for subs in itertools.product(*target_patterns):
			print(''.join(subs))

if __name__ == '__main__':
	main()

