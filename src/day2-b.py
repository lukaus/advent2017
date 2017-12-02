import sys

DAY = '2'
PUZ = 'b'
infile_name = "./dat/day" + DAY + "-" + "a" + "-in.dat"
outfile_name = "./res/day" + DAY + "-" + PUZ + "-out.dat"

infile = open(infile_name, 'r')
#BEGIN:

result = 0
for line in infile:
	nums = line.split()
	numerator = 0
	denominator = 0  # Don't try this at home
	for x in range(len(nums)):
		for y in range(len(nums)):
			if x == y: 
				continue
			if int(nums[x]) % int(nums[y]) == 0:
				numerator = nums[x]
				denominator = nums[y]

	result += (int(numerator) / int(denominator))

outfile = open(outfile_name, 'w')
outfile.write(str(int(result)))
outfile.close()