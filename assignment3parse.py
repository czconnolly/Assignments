#!/usr/bin/python

import re

infile='/homes/czconnolly/BS32010/assignment3/ig_pairs.out'
fh = open(infile)

output_filename ='/homes/czconnolly/BS32010/assignment3/ig_pairs_parsed.out'
handle = open(output_filename, 'w')

index = []
identifier= []
mydict = {}

line = fh.readline()

for line in fh:
	regexp=r'(\d+) +>([^/]+)/'
	m=re.search(regexp,line)
	if m:
		group1 = m.group(1)
		group2 = m.group(2)
		
		index.append(group1)
		identifier.append(group2)
		mydict = {'index':index, 'identifier':identifier}
#print mydict		



I = line[0:5].strip()
#J = line[6:10].strip()
#ILEN =line[11:15].strip()
#JLEN = line[16:20].strip()
#MATCH = line[21:30].strip()
#NGAPS = line[31:37].strip()
#NALIG = line[38:44].strip()
#NIDENT = line[45:51].strip()
#IDENT = line[52:61].strip()
#NAS = line[62:71].strip()
#NASAL = line[72:81].strip()
#NRANS = line[82:88].strip()
#RMEAN = line[89:98].strip()
#STDEV = line[99:108].strip()
#SCORE = line[109:119].strip()

#I = line.strip([0:5])	
print I


#line = outfile.readline()
#while line = regex
#	line=fh.readline()
#index = m.group(1)
#identifier = m.group(2)



#header= fh.readline().strip()

#colnames = {}

#index=0
#for title in header.split('\t'):
#	colnames[title]=index
#	print '%s\t%s'%(title,index)
#	index=index+1


#igfile=open('ig_file.txt','w')

#columns=['I', 'J','ILEN', 'JLEN', 'MATCH', 'NGAPS', 'NALIG', 'NIDENT', '%IDENT', 'NAS', 'NASAL', 'NRANS', 'RMEAN', 'STDEV', 'SCORE']

#def buildrow(row, fields):
#	newrow=[]
#	for f in fields:
#		newrow.append(row[int(colnames[f])])
#	return '\t'.join(newrow)+'\n'

#for line in fh.readlines():
#	try:
#		if line[0] == 'I':
#			continue
#		row=line.strip().split('\t')
#		igfile.write(buildrow(row, columns))
#		rows=rows+1
#	except:
#		pass

#igfile.close()

#print '%s rows processed'%rows
