import sys

DAY = '2'
PUZ = 'a'
infile_name = "./dat/day" + DAY + "-" + PUZ + "-in.dat"
outfile_name = "./res/day" + DAY + "-" + PUZ + "-out.dat"

infile = open(infile_name, 'r')
#BEGIN:

result = 0
for line in infile:
	nums = line.split()
	min = -1
	max = -1
	for val in nums:
		if int(val) < int(min) or int(min) == -1 :
			min = val
		if int(val) > int(max) or int(max) == -1:
			max = val
	result += int(max) - int(min)

outfile = open(outfile_name, 'w')
outfile.write(str(result))
outfile.close()