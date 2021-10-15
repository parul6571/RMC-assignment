# We have a DNA Sequence ATGCTGATAGATAGTAAAATATAAGCA
# There are few features present in this sequence 

# 1> Exon: location 3..9
#Answer
dna_seq="ATGCTGATAGATAGTAAAATATAAGCA" # to find location of the sequence we need to apply slicing. 
exon_seq=dna_seq[2:9]
print("The Exon location is 3...9 and the sequence of exon is",exon_seq)


# 2> Intron: location  10..12
#Answer     ATG CTG ATA  GAT     AGT      AAA      ATA     TAA      GCA
# indexing  012 345 678 91011  121314   151617   181920  212223   242526
# nos.      123 456 789 101112 131415    161718  192021  222324   252627 
dna_seq="ATGCTGATAGATAGTAAAATATAAGCA" # to find intron location of the sequence we need to apply slicing. 
intron_seq=dna_seq[9:12]
print("The Exon location is 3...9 and the sequence of exon is",intron_seq)


# 3> Gene: In right half part
#Answer
dna_seq="ATGCTGATAGATAGTAAAATATAAGCA"
length=int(len(dna_seq)/2)
print("The right half of the gene is",dna_seq[:length])


# 4> CDS: In Left half part
dna_seq="ATGCTGATAGATAGTAAAATATAAGCA"
length=int(len(dna_seq)/2)
print("The left half of the gene having CDS is",dna_seq[length:])


# 5> Mutation: 7th position
#Answer
dna_seq="ATGCTGATAGATAGTAAAATATAAGCA"
mutation=dna_seq[:6]+"NN"+dna_seq[7:]
print("The mutation on the 7th position is 'NN' of the dna sequence",mutation)


# 6> find index of every occurance of AT
seq="ATGCTGATAGATAGTAAAATATAAGCA"
index=0
list_result=[]
last_found_domain_index=-1
while index<len(seq):
    found_result=seq.find("AT",last_found_domain_index+1)
    if found_result!=-1:
        list_result.append(found_result)
        last_found_domain_index=found_result
        index+=last_found_domain_index
    index+=1
print("The index value of every occurence of AT is",list_result)   # need to understand from sir. while loop body functioning and for loop functioning.
    
# Kindly find the sequences for every features and print them. 
# Also calculate the length of Gene and CDS regions.
dna_seq="ATGCTGATAGATAGTAAAATATAAGCA"
length=int(len(dna_seq)/2)
dna_seqn=dna_seq[:length]
length_of_gene=len(dna_seqn)
print("The right half of the gene is",dna_seqn, "and length is", length_of_gene)
#CDS calculation
dna_seq_cds=dna_seq[length:]
length_of_cds=len(dna_seq_cds)
print("The left half of the gene having CDS is",dna_seq_cds, "and length is", length_of_cds)