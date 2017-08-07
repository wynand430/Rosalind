import EasyFiles as ef

# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate

input = ef.getInput() # get the input list

# k = homozygous dominant = homoD
# m = heterozygous = hetero
# n = homozygous recessive = homoR
K, M, N = input[0].split(' ')
K, M, N= float(K), float(M), float(N)
L = K+M+N # total organisms

Kx = 1 # probability of getting a dominant allele offspring with K involved is 1
MN = .5 # Xx crossed xx wil have .5 dominant
MM = .75 # Xx crossed Xx will have .75 dominant
NN = 0 # xx crossed xx will have 0 dominant

K_K = ( (K/L) * ((K-1)/(L-1)) ) * (Kx) # K cross K
K_M = ( (K/L) * (M/(L-1)) ) * (Kx) # K cross M
K_N = ( (K/L) * (N/(L-1)) ) * (Kx) # K cross N
M_K = ( (M/L) * (K/(L-1)) ) * (Kx) # M cross K
M_M = ( (M/L) * ((M-1)/(L-1)) ) * (MM) # M cross M
M_N = ( (M/L) * (N/(L-1)) ) * (MN) # M cross N
N_K = ( (N/L) * (K/(L-1)) ) * (Kx) # N cross K
N_M = ( (N/L) * (M/(L-1)) ) * (MN) # N cross M
N_N = ( (N/L) * ((N-1)/(L-1)) ) * (NN) # N cross N
ans = K_K + K_M + K_N + M_K + M_M + M_N + N_K + N_M + N_N # Add up all posibilities

# Denom = (1/L) * (1/(L-1))
# ans = Denom * (K*((K-1)+(M)+(N))+(M*((K)+(M-1)*(MM)+(N)*(MN)))+(N*((K)+M*(MN)+(N-1)*(NN) )))
# print ans
ef.writeOutput( str(ans) ) # write the output

# homo = alleles the same
# heter = alleles diff