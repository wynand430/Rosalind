import EasyFiles as ef # Given: Two positive integers a and b, each less than 1000.

# Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.

input = ef.getInput() # get the input list
a,b = str(input[0]).split(" ") # split 0th line on space
sum = int(a) + int(b) # add a and b
ef.writeOutput(str(sum)) # print out the sum string