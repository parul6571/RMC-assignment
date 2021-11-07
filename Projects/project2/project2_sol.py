# Download two sequences of COVID Geneome(Delta, Wuhan) by using Entrez module
from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq
import matplotlib.pyplot as plt
from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.SeqUtils import GC
# wuhan variant accession no is NC_045512, 
Entrez.email = "parul.bhatt@mirandahouse.ac.in"
handle = Entrez.efetch(db="nucleotide", id="NC_045512", rettype="gb", retmode="text")
save_wuhan_sequence=open("D:\Python for bioinformatics\python\RMC-assignment\Projects\project2\wuhan_variant.gb","w")
save_wuhan_sequence.write(handle.read())
save_wuhan_sequence.close()

# The accession no of delta variant is MZ571142.1 published in the following paper 
# Genome Sequences of the Delta Variant (B.1.617.2) and the Kappa Variant (B.1.617.1) Detected in Morocco
# Marouane Melloula,b, Taha Chouatia, Mouhssine Hemlalia,b, Sanaa Alaoui Aminea,b, Nadia Touilb, Hicham Elannazc, Khalid Ennibic, Mohammed Youbid, Mouad Merabetd, Abdelkrim Meziane Bellefquihd, Jalal Nourlile, Abderrahmane Maaroufif, and Elmostafa El Fahime
Entrez.email = "parul.bhatt@mirandahouse.ac.in"
handle = Entrez.efetch(db="nucleotide", id="MZ571142.1", rettype="gb", retmode="text")
save_delta_sequence=open("D:\Python for bioinformatics\python\RMC-assignment\Projects\project2\delta_variant.gb","w")
save_delta_sequence.write(handle.read())
save_delta_sequence.close()



# Find a comparison informations about CDS features.
# Reading of CDS region of delta variant into file.
path1=r"D:\Python for bioinformatics\python\RMC-assignment\Projects\project2\delta_variant.gb"
delta_record=SeqIO.read(path1,"genbank")
path=r"D:\Python for bioinformatics\python\RMC-assignment\Projects\project2\delta-CDS.txt"
delta_cds=open(path,"w")
delta_cds.writelines("Delta variant CDS sequences"+"\n")
for gene_features in delta_record.features:
       if gene_features.type=="CDS":
        print(gene_features.type)
        print(gene_features.extract(delta_record).seq)
        print(len(gene_features.extract(delta_record.seq)))
        delta_cds.writelines("\n"+str(gene_features.type)+"\n" )
        delta_cds.writelines("\n"+(str(gene_features.extract(delta_record.seq))+"\n"))
        delta_cds.writelines(str(len(str(gene_features.extract(delta_record.seq))+ "\n")))
delta_cds.close()

# Reading of CDS region of wuhan variant into the file.
path2=r"D:\Python for bioinformatics\python\RMC-assignment\Projects\project2\wuhan_variant.gb"

wuhan_record=SeqIO.read(path2,"genbank")
path=r"D:\Python for bioinformatics\python\RMC-assignment\Projects\project2\wuhan-CDS.txt"
wuhan_cds=open(path,"w")
wuhan_cds.writelines("Wuhan variant CDS sequences"+"\n")
for gene_features in wuhan_record.features:
       if gene_features.type=="CDS":
        print(gene_features.type)
        print(gene_features.extract(wuhan_record).seq)
        print(len(gene_features.extract(wuhan_record.seq)))
        
        wuhan_cds.writelines("\n"+str(gene_features.type)+"\n" )
        wuhan_cds.writelines("\n"+(str(gene_features.extract(wuhan_record.seq))+"\n"))
        wuhan_cds.writelines(str(len(str(gene_features.extract(wuhan_record.seq))+ "\n")))
wuhan_cds.close()


# Find a comparison informations about gene features.
# Reading the genebank file fo wuhan gene
path3=r"D:\Python for bioinformatics\python\RMC-assignment\Projects\project2\wuhan_variant.gb"

wuhan_record=SeqIO.read(path3,"genbank")

path=r"D:\Python for bioinformatics\python\RMC-assignment\Projects\project2\wuhan-genes.txt"
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
# Getting the gene sequence of delta variant.
path4="D:\Python for bioinformatics\python\RMC-assignment\Projects\project2\delta_variant.gb"

delta_record=SeqIO.read(path4,"genbank")

path=r"D:\Python for bioinformatics\python\RMC-assignment\Projects\project2\delta-genes.txt"
delta_gene=open(path,"w")
delta_gene.writelines("Delta variant gene sequences"+"\n")
for gene_features in delta_record.features:
    if gene_features.type=="gene":
        print(gene_features.type)
        print(gene_features.extract(delta_record).seq)
        print(len(gene_features.extract(delta_record.seq)))
        
        delta_gene.writelines("\n"+str(gene_features.id)+"\n" )
        delta_gene.writelines("\n"+str(gene_features.type)+"\n" )
        delta_gene.writelines((str(gene_features.extract(delta_record.seq))+"\n"))
        delta_gene.writelines(str(len(str(gene_features.extract(delta_record.seq))+ "\n")))
delta_gene.close()

# Translate the gene regions and compare the products
# Create the plasmid for both the varient
# plot the restriction map sites on both the plasmid and analyse the result
# Plot all the CDS regions on plasmid for both the variants and analyze the result