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

record = SeqIO.read(r"D:\Python for bioinformatics\python\RMC-assignment\Projects\project1\wuhan_variant.gb", "genbank")

gd_diagram = GenomeDiagram.Diagram(record.id)
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
gd_feature_set = gd_track_for_features.new_set()

for feature in record.features:
    if feature.type=="mat_peptide":
        if len(gd_feature_set) % 2 == 0:
            color = colors.blueviolet
        else:
            color = colors.orangered
        gd_feature_set.add_feature(
            feature, sigil="ARROW", color=color, label=True, label_size=20, label_angle=25
        )


import os
os.chdir(r"D:\Python for bioinformatics\python\RMC-assignment\Projects\project1")

gd_diagram.draw(format="linear", pagesize="A4", fragments=4, start=0, end=len(record))
gd_diagram.write("wuhan_plasmid.pdf", "PDF")


# plot the restriction map sites on plasmid
restriction_record = SeqIO.read(r"D:\Python for bioinformatics\python\RMC-assignment\Projects\project1\wuhan_variant.gb", "genbank")

gd_diagram = GenomeDiagram.Diagram(restriction_record.id)
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
gd_feature_set = gd_track_for_features.new_set()



restriction_map_data=[
    ("GAATTC", "EcoRI", colors.green),
    ("CCCGGG", "SmaI", colors.orange),
    ("AAGCTT", "HindIII", colors.red),
    ("GGATCC", "BamHI", colors.purple),
]
for feature in restriction_record.features:
    if feature.type=="mat_peptide":
        if len(gd_feature_set) % 2 == 0:
            color = colors.blue
        else:
            color = colors.yellow
        gd_feature_set.add_feature(
            feature, sigil="ARROW", color=color, label=True, label_size=20, label_angle=10
        )
    for site, name, color in restriction_map_data:
      index = 0
      while True:
        index = restriction_record.seq.find(site, start=index)
        if index == -1:
            break
        feature = SeqFeature(FeatureLocation(index, index + len(site)))
        gd_feature_set.add_feature(
            feature,
            color=color,
            name=name+" "+str(index),
            label=True,
            label_size=15,
            label_color=color,
            label_position=index
        )
        index += len(site)



import os
os.chdir(r"D:\Python for bioinformatics\python\RMC-assignment\Projects\project1")

gd_diagram.draw(
    format="circular",
    circular=True,
    pagesize=(40 * cm, 40 * cm),
    start=0,
    end=len(record),
    circle_core=0.5,
)
gd_diagram.write("wuhan_restriction_gd_circular.pdf", "PDF")


# Plot all the CDS regions on plasmid
# Mark the CDS regions having GC value>50 
