import os
import json
DIR = input("Enter path:")
DIR += "/"
output_path = DIR
file_count = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
name = input("Enter input file basename: ")
out_name = input("Enter output file base:")
max_size = input("Enter the max size in bytes")
max_size = int(max_size)
DIR += name
ext = ".json"
base_num = 1 
w_num = 1;


with open(DIR + "1.json") as json_file:
	S = json.load(json_file)

res = json.dumps(S)
i = 2
key = ""
while(res[i] != '"'):
	key += res[i]
	i += 1
print("Key: ", key)

json_file.close()



file_count = int(file_count)
# print("Number of json files: ", file_count)

result = {}
result[key] = []

for i in range(file_count):
	str_num = str(base_num)
	open_path = DIR + str_num + ext
	base_num += 1
	with open(open_path) as json_file:
		data = json.load(json_file)
	for s in data[key]:
		# print("writing :",s['name'])
		result[key].append(s)
	if(i == 0):
		continue
	write_name = out_name
	write_name += str(w_num)
	write_name += ext

	with open(output_path + write_name,'w',) as outfile:
		json.dump(result,outfile)
	length = os.path.getsize(output_path + write_name)
	if(length > max_size):
		os.remove(output_path + write_name)
	w_num += 1
	outfile.close()
	json_file.close()

