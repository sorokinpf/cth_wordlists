from yaml import safe_load
import re
import itertools
import argparse

def parse(val_name,schema):
    print (val_name)
    vals = schema[val_name]
    result = []
    for v in vals:
        print (type(v))
        sub_vals = re.findall('%([^;]+);',v)
        if len(sub_vals)==0:
            result.append(v)
            continue
        sub_arrays = []
        for sub_val in sub_vals:
            sub_arrays.append(parse(sub_val,schema))

        possible_values = itertools.product(*sub_arrays)
        for x in possible_values:
            generating_v = v
            for sub_val_name,sub_val_value in zip(sub_vals,x):
                generating_v = generating_v.replace('%%%s;'%sub_val_name,sub_val_value)
            result.append(generating_v)
    return result

def save(filename,vectors):
    res_file = open(filename,'wb')
    res_file.write(('\n'.join(vectors)).encode('ascii'))
    res_file.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("source",help="yml file to build")
	parser.add_argument("target",help="yml param name to build")
	parser.add_argument("output",help="output filename")
	args = parser.parse_args()

	all_data = safe_load(open(args.source).read())
	print (all_data)
	target = parse(args.target,all_data)
	save(args.output,target)








