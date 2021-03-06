
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

# 3. Write a program to mutate a sequence taken from user. Accept sequence as a input from the user. 
# Take position and mutated base as argument.
#Answer
dna_seq3=input("please enter the DNA sequence: ")
dna_seq3=[dna_seq3]
dna_seq3_mutated=dna_seq3.copy()
dna_seq3_mutated.insert(3, "GCGGCG")
print("The mutated DNA sequence is ", dna_seq3_mutated)# this is adition in the list not inbetween the sequences.

dna_seqM=input("please enter the DNA sequence: ")
Position_of_mutation=int(input("Please enter the position of Mutation: "))
Mutated_character=input("Please enter the Mutated character: ")
Mutated_sequence=dna_seqM[:Position_of_mutation-1]+Mutated_character+dna_seqM[Position_of_mutation:] 
print(Mutated_sequence)

# Addition sequence in list data set.
data_list=input("Please enter the DNA Sequence: ") 
convert_list=list(data_list)
data_list[3]="AAAAAAA"
print(convert_list)
new_list="".join(convert_list)
print(new_list)

# 4. Write a program to slice the sequence in two halves. Print the result. Take the sequence from the user. 
#answer 
dna_seq5=input("please enter the DNA sequence: ")
length=len(dna_seq5)
print("The first half of the sequence is ", dna_seq5[:int(length/2)]) #first half part
print("The second half of the sequence is ",dna_seq5[int(length/2):]) #second half part


# 5. Print position of  the 2nd occurrence of “A”  in the sequence “ATCGATAGATACAA”.
#Answer

dna_seq6="ATCGATAGATACAA"
print("The DNA sequence is ", dna_seq6)
print("The index position of 2nd occurance of A in DNA sequence is=", dna_seq6.find("A", 2))


# 6. Write a program to check which stop codons are present in the sequence  “UAAAAGGCGAGAUAAAUA” .
# Answer

rna_seq="UAAAAGGCGAGAUAAAUA"  
print("There are 3 stop codons are present UAA, UGA and UAG and their presence in this (UAAAAGGCGAGAUAAAUA) sequence")
print("The presence of UAA in sequence is", "UAA" in rna_seq)
print("The presence of UGA in sequence is", "UGA" in rna_seq)
print("The presence of UAG in sequence is",  "UAG" in rna_seq)


#  7. suppose that we have few restriction enzyme recognition sites ["ACGTC","CTAGT","ATGCTA"] 
#  find sites with their frequencies in the DNA sequences of  delta strain of COVID 19.

# Answer

sars_cov2_DNA_sequence= "CAAATGCTAACCAACCTAGTCAACTTTCGATCTCTTGTAGATCTGTTCTCTACGTCAAACGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATCTAGTACGTCGCTTAGTGCACTCACGCAGTATAATTAATAACTAATTACTGTCGTTGACAGGACACGAGTAACTCGTCTATCTTCTGCAGGCTGCTTACGGTTTCGTCCGTTTTGCAGCCGATCATCAGCACATCTAGGTTTTGTCCGGGTGTGACCGAAAGGTAAGATGGAGAGCCTTGTCCCTGGTTTCAACGAGAAAACACACGTCCAACTCAGTTTGCCTGTTTTACAGGTTCGCGACATGCTAGTGCTCGTACGTGGCTATGCTATTGGAGACTCCGTGGAGGAGGTCTTATCAGAGGCCTAGTACGTCAACATCTTAAAGATGGCACTTGTGGCTTAGTAGAAGTTGAAAAAGGCGTTTTGCCTCAACTTGAACAGCCCTATGTGTTCATCAAACGTTCGGATGCTCGAACTGCACCTCATGGTCATGTTATGGTTGAGCTGGTAGCAGAACTCGAAGGCATTCAGTACGGTCGTAGTGGTGAGACACTTGGTGTCCTTGTCCCTCATGTGGGCGAAATACCAGTGGCTTACCGCAAGGTTCTTCTTCGTAAGAACGGTAATAAAGGAGCTGGTGGCCATAGTTACGGCGCCGATCTAAAGTCATTTGACTTAGGCGACGAGCTTGGCACTGATCCTTATGAAGATTTTCAAGAAAACTGGAACACTAAACATAGCAGTGGTGTTACCCGTGAACTCATGCGTGAGCTTAACGGAGGGGCATACACTCGCTATGTCGATAACAACTTCTGTGGCCCTGATGGCTACCCTCTTGAGTGCAT"

print("The COVID 19 delta variant DNA sequence is", 
sars_cov2_DNA_sequence)
acgtc=sars_cov2_DNA_sequence.count("ACGTC")
ctagt=sars_cov2_DNA_sequence.count("CTAGT")
atgcta=sars_cov2_DNA_sequence.count("ATGCTA")

print("The frequency of  restriction enzyme recognition sites ACGTC, CTAGT, ATGCTA in covid delta strains are", acgtc , ctagt, atgcta)


# 8 Write a program to reverse the second half region of a DNA sequence. "ATGATAGATAGATGATATCGATAGTA".

#Answer 
dna_seq7="ATGATAGATAGATGATATCGATAGTA" 
length=len(dna_seq7)
second_half=dna_seq7[int(length/2):]
print("The DNA sequence is", dna_seq7)
print("The second half of DNA sequence is", dna_seq7[int(length/2):])
print("The reverse of second half is", second_half[::-1])
