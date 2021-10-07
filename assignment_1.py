
#  1. Write a program to calculate the length of DNA Sequence in python. Take the sequence from user.
#  Answer


dna_seq1=input("Please enter the DNA sequence: ")
print("The length of DNA sequence is=",len(dna_seq1))


# 2 Write  a program to calculate the GC percentage of DNA sequence. Take the sequence from the user.
# Answer
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

# 4. Write a program to slice the sequence in two halves. Print the result. Take the sequence from the user. 
#answer 
dna_seq5=input("please enter the DNA sequence: ")
length=len(dna_seq5)
print(dna_seq5[:int(length/2)]) #first half part
print(dna_seq5[int(length/2):]) #second half part

# 5. Print position of  the 2nd occurrence of “A”  in the sequence “ATCGATAGATACAA”.
#answer

dna_seq6="ATCGATAGATACAA"
print("A" in dna_seq6)






# Write a program to check which stop codons are present in the sequence  “UAAAAGGCGAGAUAAAUA” .
# suppose that we have few restriction enzyme recognition sites ["ACGTC","CTAGT","ATGCTA"] find sites with their frequencies in the DNA sequences of  delta strain of COVID 19.
# Write a program to reverse the second half region of a DNA sequence. "ATGATAGATAGATGATATCGATAGTA".
