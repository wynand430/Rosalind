def writeOutput(output):
	f = open("output.txt","w+")
	f.write(str(output))
	f.close()

def getInput():
	f = open("input.txt", "r")
	contents = f.read()
	contentsArray = contents.split("\n")
	return contentsArray