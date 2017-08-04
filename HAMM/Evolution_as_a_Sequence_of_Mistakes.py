import EasyFiles as ef 

# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t).

input = ef.getInput() # get the input list
s,f = input[0],input[1]
hd = 0 #Hammin distance = 0

for index in range(0,len(s)):
	if s[index] != f[index]:
		hd+=1
#print hd
ef.writeOutput(hd) 