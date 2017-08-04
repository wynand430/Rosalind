import EasyFiles as ef 

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

organisms = {} # organisms tracker
current = '' # current working organism
GCcount = 0 # initialize GC counter
Totalcount = 0 # initialize total counter
maxGC = 0 # so I don't have to run through dict again
maxOrg = '' # no need to run through again

		
input = ef.getInput() # get the input list
for line in input:
	if line[0] == '>':
		if current !='':
			GCPercent = float(GCcount)/Totalcount
			organisms[current] = GCPercent
			if maxGC < GCPercent:
				maxGC = GCPercent
				maxOrg = current
		current = line[1:] # new organism name!
		GCcount = 0 # init the GCcount
		Totalcount = 0 # init the Totalcount
	else: # if it's not a new organism
		for bp in line: # run through each bp
			if bp == "G" or bp == "C": # if it's a G or C
				GCcount+=1 # add to the counter
			Totalcount+=1 # for all bp's, add to total counter
GCPercent = float(GCcount)/Totalcount
organisms[current] = GCPercent
if maxGC < GCPercent:
	maxGC = GCPercent
	maxOrg = current

ans = "%s\n%f" % (maxOrg,(maxGC*100))

ef.writeOutput(ans) 