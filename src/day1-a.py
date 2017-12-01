import sys

DAY = '1'
PUZ = 'a'
infile_name = "./dat/day" + DAY + "-" + PUZ + "-in.dat"
outfile_name = "./res/day" + DAY + "-" + PUZ + "-out.dat"

infile = open(infile_name, 'r')

result = 0
#BEGIN:


first_num = infile.read(1)
last_num = first_num

while True:
	next_num = infile.read(1)
	if next_num is "":
		break
	if(next_num == last_num):
		result += int(next_num)
	last_num = next_num
if(last_num == first_num):
	result += int(last_num)

outfile = open(outfile_name, 'w')
outfile.write(str(result))
outfile.close()