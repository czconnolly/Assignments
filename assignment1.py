#a python script that uses the BioPython library to return the sequence in FASTA format 
#of the 3 longest genes from a bacterial genome sequence.

from Bio import SeqIO

#define the names of the files
input_filename = 'NC_000913.faa'
output_filename = 'NC_000913_longest_genes.fasta'

#create a handle to output the result into
output_handle = open(output_filename, 'w')

#load in the file as a list
records = list(SeqIO.parse(input_filename, 'fasta'))
#order the list from large to small
records.sort(cmp = lambda x,y: cmp(len(y),len(x)))
#write the longest 3 results to the output handle file
SeqIO.write(records[0:3], output_handle, 'fasta')
#close the handle
output_handle.close()

