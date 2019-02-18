hmc = []
depth = []
children = []
subtree = []
path = []
count = 0
values = open("AUPRC.txt",'r').readlines()
for value in values:
	value = value.rstrip()
	if count == 0:
		path.append(value)
	elif count == 1:
		subtree.append(value)
	elif count == 2:
		children.append(value)
	elif count == 3:
		depth.append(value)
	elif count == 4:
		hmc.append(value)
	count = count + 1
	if count == 5:
		count = 0

with open("AUPRC.csv", 'w') as output:
	output.write("Path,Subtree,Children,Depth,HMC\n")
	for i in range(0,len(hmc)):
		output.write(path[i]+','+subtree[i]+','+children[i]+','+depth[i]+','+hmc[i]+'\n')


