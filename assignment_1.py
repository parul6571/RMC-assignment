
#  1. Write a program to calculate the length of DNA Sequence in python. Take the sequence from user.
#  Answer


seq=input("Please enter the DNA sequence: ")
print("The length of DNA sequence is=",len(seq))


# Write  a program to calculate the GC percentage of DNA sequence. Take the sequence from the user.

dna_seq=input("please enter the DNA sequence: ")
no_of_Gs=dna_seq.count("G")
no_of_Cs=dna_seq.count("C")
gc_percentage=100*(no_of_Gs + no_of_Cs) /len(dna_seq)
print("The GC percentage of the sequence is= ", gc_percentage )

# Write a program to mutate a sequence taken from user. Accept sequence as a input from the user. Take position and mutated base as argument.
#Answer
