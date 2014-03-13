#!/usr/bin/python

#import glob,os

#outfile = glob.glob(os.path.join('C:/homes/czconnolly/BS32010/assignment3/*.out'))
#	fh=open(outfile,'r')

#fh=open(outfile)





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
		my.dict = {'index':index, 'identifier':identifier}
	print mydict		



	



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
