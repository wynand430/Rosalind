import EasyFiles as ef 

# Given: A DNA string s of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s

counts = {'A':0,'C':0,'G':0,'T':0} # set up my dictionary
input = ef.getInput() # get the input list
DNA = input[0]
for nt in DNA:
	counts[nt]+=1
ans = "%d %d %d %d" % (counts['A'], counts['C'], counts['G'], counts['T'])
ef.writeOutput( ans ) 