import EasyFiles as ef 

# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

def createTrackingList(matrixLength):
	tracking = []
	outputTracking = {"A":[],"G":[],"C":[],"T":[]}
	# each list is 4 long
	# A:0, G:1, C:2, T:3
	# [0,0,0,0] and create one for each length of the dna
	for x in range(0,matrixLength):
		tracking.append([0,0,0,0])
		outputTracking["A"].append(0)
		outputTracking["G"].append(0)
		outputTracking["C"].append(0)
		outputTracking["T"].append(0)
	return tracking, outputTracking


input = ef.getInput() # get the input list
DNALength = 0

endLine = -1
x = 0
while endLine < 1:
	DNALength += len(input[x])
	print "len(input[x]): %s" % (len(input[x]))
	print "input[x+1][0] %s" % (input[x+1][0])
	if input[x+1][0] == '>':
		endLine = 1
	x+=1
print DNALength

consensus = ""
output = ""

tracking, outputTracking = createTrackingList(DNALength)
reference = {"A":0, "G":1, "C":2, "T":3}
referenceList = ["A","G","C","T"]
'''
# For line in input:
for line in input:
# 	Is it not a name?
	if line[0] != '>':
		for index, bpName in enumerate(line):
			subIndex = reference[bpName]
			tracking[index][subIndex]+=1

for index, subSet in enumerate(tracking):
	subSetMaxBP = ""
	subSetMaxCount = 0
	for subIndex, count in enumerate(subSet):
		outputTracking[referenceList[subIndex]][index]=count
		if count > subSetMaxCount:
			subSetMaxCount = count
			subSetMaxBP = referenceList[subIndex]
	consensus += subSetMaxBP

output += consensus
output += "\n"
for bpName in referenceList:
	output += "%s:" % (bpName)
	for val in outputTracking[bpName]:
		output += " %s" % str(val)
	output += "\n"
ef.writeOutput( output ) '''