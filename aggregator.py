# Mohammad Saidur Rahman
# Saidur.Rahman@mail.rit.edu
# Department of Computing Security, Rochester Institute of Technology

print "This program writtedas part of the Cryptography and Authentication Project.\n"
print "The two group members are Saidur and Haani\n\n"

import numpy as np

n = int(input("Enter the number of splits to test: "))

#we are assuming equal probability for all the split.
p_i = np.float(1.00/n)

print "\nProbability of each Split: ",p_i

#The entropy of the system: H(X)


entropy = -(p_i*(np.log2(p_i))*n)

print "\nCalculation of the Entropy of the System: H(X) ",entropy


max_entropy = np.log2(n)

print "\nMaximum Entropy of the System: H(M) ",max_entropy

#print "\nMeasuring Degree of Anonymity: d"

d = 1 - np.float(((max_entropy-entropy)/max_entropy))

print "\nDegree of Anonymity is ",d