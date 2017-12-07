DAY = '7'
PUZ = 'b'
# Unfinished and incorrect
infile_name = "./dat/day" + DAY + "-" + 'a' + "-in.dat"
outfile_name = "./res/day" + DAY + "-" + PUZ + "-out.dat"

infile = open(infile_name, 'r')
#BEGIN:

# I think part 1 can be solved by finding the one name only mentioned
# once, but I doubt part 2 can so I'm going to build the tree

class Node:
	name = ""
	weight = -1
	children = []
	parent = None

tree = {}		 # store nodes
id_for_node = {} # returns id for node name
parent_for_node = {} # returns parent node

#Build tree
for line in infile:
	# Load node name and weight, save to object
	line = line[:-1]
	raw_node = line.split(" ")
	node = Node()
	node.name = raw_node[0]
	node.weight = int(str(raw_node[1])[1:-1])
	# Has this node been mentioned? If so, find its parent
	if node.name in id_for_node:
		parent_id = parent_for_node[str(node.name)]
		node.parent = tree[parent_id] # get parent
		node.parent.children.append(node) 	# record this as child
	# Otherwise, save its ID
	id_for_node[node.name] = id(node) # save reference to name dict
	tree[id(node)] = node # save object to tree
	# Check if it has children and record their mention
	if len(raw_node) > 2: # this means it has -> children
		for x in range(3, len(raw_node)): # for each child
			raw_node[x] = str(raw_node[x]).replace(",", "") # trim commas
			if raw_node[x] in id_for_node:
				child = tree[id_for_node[str(raw_node[x])]]
				child.parent = node
			else:
				id_for_node[raw_node[x]] = -1 # record -1 because they have no id
			parent_for_node[str(raw_node[x])] = id(node)
	root_node = node

infile.close()
#Check up tree
while root_node.parent != None:
	root_node = root_node.parent



print(result)
outfile = open(outfile_name, 'w')
outfile.write(str(result))
outfile.close()