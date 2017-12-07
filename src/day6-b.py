DAY = '6'
PUZ = 'b'
infile_name = "./dat/day" + DAY + "-" + 'a' + "-in.dat"
outfile_name = "./res/day" + DAY + "-" + PUZ + "-out.dat"

infile = open(infile_name, 'r')
#BEGIN:
#
def get_state_string(banks):
	state = ""
	for num in banks:
		state += chr(num + 60)
	return state

states = {}

banks = []
for num in infile.readline().split():
	banks.append(int(num) )

result = 0
state = get_state_string(banks)
states[str(state)] = 0

unique_flag = True
while unique_flag == True:
	result += 1
	max = -1
	max_index = -1
	# Find bank
	for x in range(0, len(banks)):
		if banks[x] > max:
			max = banks[x]
			max_index = x
	#distribute
	to_distribute = max
	dist_index = max_index
	if(dist_index >= len(banks) - 1):
		dist_index = 0
	else:
		dist_index += 1

	banks[max_index] = 0
	while to_distribute > 0:
		banks[dist_index] += 1
		to_distribute -= 1

		if(dist_index >= len(banks) - 1):
			dist_index = 0
		else:
			dist_index += 1
	cur_state = get_state_string(banks)
	if str(cur_state) in states:
		unique_flag = False
		break
	else:
		states[str(cur_state)] = result
	
result = result - states[cur_state]

infile.close()
outfile = open(outfile_name, 'w')
outfile.write(str(result))
outfile.close()