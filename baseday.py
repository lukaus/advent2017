DAY = ''
PUZ = ''
infile_name = "./dat/day" + DAY + "-" + 'a' + "-in.dat"
outfile_name = "./res/day" + DAY + "-" + PUZ + "-out.dat"

infile = open(infile_name, 'r')
#BEGIN:




infile.close()
print(result)
outfile = open(outfile_name, 'w')
outfile.write(str(result))
outfile.close()