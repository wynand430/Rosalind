import EasyFiles as ef 

# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.

input = ef.getInput() # get the input list
DNA = input[0]
RNA = DNA.replace("T","U")
ef.writeOutput( RNA ) 