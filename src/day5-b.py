DAY = '5'
PUZ = 'b'
infile_name = "./dat/day" + DAY + "-" + 'a' + "-in.dat"
outfile_name = "./res/day" + DAY + "-" + PUZ + "-out.dat"

infile = open(infile_name, 'r')
#BEGIN:
instructions = []

for num in infile.read()[:-1].split('\n'):
	instructions.append(int(num))

location = 0
steps = 0
while location >= 0 and location < len(instructions):
	next_location = location + instructions[location]
	
	if instructions[location] >= 3:
		instructions[location] -= 1
	else:
		instructions[location] += 1

	location = next_location
	steps += 1

result = steps

infile.close()
outfile = open(outfile_name, 'w')
outfile.write(str(result))
outfile.close()