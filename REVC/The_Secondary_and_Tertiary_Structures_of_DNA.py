import EasyFiles as ef 

# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.
complement = {'A':'T','C':'G','G':'C','T':'A'}
input = ef.getInput() # get the input list
DNA = input[0]
reverse = ''
for bp in reversed(DNA):
	bpComplement = complement[bp]
	reverse+=bpComplement

ef.writeOutput( reverse ) 