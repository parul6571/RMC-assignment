# Download a sequence of COVID Geneome(NC_045512) by using Entrez module
from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq
import matplotlib.pyplot as plt
from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio.SeqFeature import SeqFeature, FeatureLocation

Entrez.email = "parul.bhatt@mirandahouse.ac.in"
handle = Entrez.efetch(db="nucleotide", id="NC_045512", rettype="gb", retmode="text")
save_covid_sequence=open("wuhan_variant.gb","w")
save_covid_sequence.write(handle.read())
save_covid_sequence.close()


# Get informations about gene features.
path=r"D:\Python for bioinformatics\python\RMC-assignment\Projects\project1\wuhan_variant.gb"

wuhan_record=SeqIO.read(path,"genbank")
path=r"D:\Python for bioinformatics\python\RMC-assignment\Projects\project1\wuhan-genes.txt"
wuhan_gene=open(path,"w")
wuhan_gene.writelines("Wuhan variant gene sequences"+"\n")
for gene_features in wuhan_record.features:
    if gene_features.type=="gene":
        print(gene_features.type)
        print(gene_features.extract(wuhan_record).seq)
        print(len(gene_features.extract(wuhan_record.seq)))
        wuhan_gene.writelines("\n"+str(gene_features.id)+"\n" )
        wuhan_gene.writelines("\n"+str(gene_features.type)+"\n" )
        wuhan_gene.writelines((str(gene_features.extract(wuhan_record.seq))+"\n"))
        wuhan_gene.writelines(str(len(str(gene_features.extract(wuhan_record.seq))+ "\n")))
wuhan_gene.close()

# Get informations about CDS features
path=r"D:\Python for bioinformatics\python\RMC-assignment\Projects\project1\wuhan_variant.gb"

wuhan_record=SeqIO.read(path,"genbank")
path=r"D:\Python for bioinformatics\python\RMC-assignment\Projects\project1\wuhan-CDS.txt"
wuhan_cds=open(path,"w")
wuhan_cds.writelines("Wuhan variant CDS sequences"+"\n")
for gene_features in wuhan_record.features:
       if gene_features.type=="CDS":
        print(gene_features.type)
        print(gene_features.extract(wuhan_record).seq)
        print(len(gene_features.extract(wuhan_record.seq)))
        wuhan_cds.writelines("\n"+str(gene_features.type)+"\n" )
        wuhan_cds.writelines((str(gene_features.extract(wuhan_record.seq))+"\n"))
        wuhan_cds.writelines(str(len(str(gene_features.extract(wuhan_record.seq))+ "\n")))
wuhan_cds.close()


# Translate the gene regions

path=r"D:\Python for bioinformatics\python\RMC-assignment\Projects\project1\wuhan_variant.gb"

wuhan_record=SeqIO.read(path,"genbank")
path=r"D:\Python for bioinformatics\python\RMC-assignment\Projects\project1\wuhan-genes-translation.txt"
wuhan_gene_translation=open(path,"w")
wuhan_gene_translation.writelines("Wuhan Genes  sequence Translation "+"\n")
for gene_features in wuhan_record.features:
    if gene_features.type=="CDS":
        gene=gene_features.extract(wuhan_record).seq
        rna_seq=gene.transcribe()
        protein_p=str(rna_seq.translate())
        wuhan_gene_translation.writelines("\n"+"Translated gene product")
        wuhan_gene_translation.writelines("\n"+(str(protein_p)+"\n"))
        wuhan_gene_translation.writelines("Length of the gene product="+(str(len(protein_p))+"\n"))
wuhan_gene_translation.close()



# Create the plasmid

# plot the restriction map sites on plasmid
# Plot all the CDS regions on plasmid
# Mark the CDS regions having GC value>50 
