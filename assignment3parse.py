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


I = []
J = []
ILEN = []
JLEN = []
MATCH = []
NGAPS = []
NALIG = []
NIDENT = []
IDENT = []
NAS = []
NASAL = []
NRANS = []
RMEAN = []
STDEV = []
SCORE = []

for line in fh:
	I.append(line[0:5].strip())
	J.append(line[6:10].strip())
	ILEN.append(line[11:15].strip())
	JLEN.append(line[16:20].strip())
	MATCH.append(line[21:30].strip())
	NGAPS.append(line[31:37].strip())
	NALIG.append(line[38:44].strip())
	NIDENT.append(line[45:51].strip())
	IDENT.append(line[52:61].strip())
	NAS.append(line[62:71].strip())
	NASAL.append(line[72:81].strip())
	NRANS.append(line[82:88].strip())
	RMEAN.append(line[89:98].strip())
	STDEV.append(line[99:108].strip())
	SCORE.append(line[109:119].strip())







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
