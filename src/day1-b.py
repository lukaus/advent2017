DAY = '1'
PUZ = 'b'
infile_name = "./dat/day" + DAY + "-" + "a" + "-in.dat"
outfile_name = "./res/day" + DAY + "-" + PUZ + "-out.dat"

infile = open(infile_name, 'r')
indata = infile.read()
infile.close()
#BEGIN:

result = 0
list_length = len(indata)
for x in range(list_length):

	if(x >= int(list_length/2)):
		to_check = x - int(list_length/2)
	else:
		to_check = x + int(list_length/2)
	
	if(indata[x] == indata[to_check]):
		result += int(indata[x])

outfile = open(outfile_name, 'w')
outfile.write(str(result))
outfile.close()