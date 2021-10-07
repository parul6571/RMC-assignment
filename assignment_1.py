
#  1. Write a program to calculate the length of DNA Sequence in python. Take the sequence from user.
#  Answer


dna_seq1=input("Please enter the DNA sequence: ")
print("The length of DNA sequence is=",len(dna_seq1))


# Write  a program to calculate the GC percentage of DNA sequence. Take the sequence from the user.

dna_seq2=input("please enter the DNA sequence: ")
no_of_Gs=dna_seq2.count("G")
no_of_Cs=dna_seq2.count("C")
gc_percentage=100*(no_of_Gs + no_of_Cs) /len(dna_seq2)
print("The GC percentage of the sequence is= ", gc_percentage )

# Write a program to mutate a sequence taken from user. Accept sequence as a input from the user. 
# Take position and mutated base as argument.
#Answer
dna_seq3=input("please enter the DNA sequence: ")
dna_seq3=[dna_seq3]
dna_seq3_mutated=dna_seq3.copy()
dna_seq3_mutated.insert(3, "GCGGCG")
print(dna_seq3_mutated)

# dna_seq4="ATTCCGTGTGGTGTG"
# dna_seq4_mutated=dna_seq4[:4]+"GGTTCGT"+[5:] # need to ask about string mutation is is not happening

