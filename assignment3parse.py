#!/usr/bin/python

import re

infile='/homes/czconnolly/BS32010/assignment3/serprot_pairs.out'
fh = open(infile)

output_filename ='/homes/czconnolly/BS32010/assignment3/serprot_pairs_parsed.out'
handle = open(output_filename, 'w')

mydict = {}
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


line = fh.readline()

for line in fh:
	regexp=r'(\d+) +>([^/]+)/'
        m=re.search(regexp,line)
	if m:
		index,identifier = m.group(1), m.group(2)
		mydict[index] = identifier
fh.close		

#for line in fh:
#	I.append(line[0:5].strip())
#	J.append(line[6:10].strip())
#	ILEN.append(line[11:15].strip())
#	JLEN.append(line[16:20].strip())
#	MATCH.append(line[21:30].strip())
#	NGAPS.append(line[31:37].strip())
#	NALIG.append(line[38:44].strip())
#	NIDENT.append(line[45:51].strip())
#	IDENT.append(line[52:61].strip())
#	NAS.append(line[62:71].strip())
#	NASAL.append(line[72:81].strip())
#	NRANS.append(line[82:88].strip())
#	RMEAN.append(line[89:98].strip())
#	STDEV.append(line[99:108].strip())
#	SCORE.append(line[109:119].strip())

fh = open(infile)
#line = fh.readline()
#while line[:5] != '     I':
#	line=fh.readline()
#	if line[:2] ==' T':
	#line=fh.readline()
#		continue


for line in fh:
	try:
		if line[:2]=='  T':
		#for line in fh:
       			continue
	regexp2='(\d{1,5}\D*)+(\d{1,5}\D*)+(\d{1,5}\D*)+(\d{1,5}\D*)+(\d{1,5}\D*)+(\d{1,5}\D*)+(\d{1,5}\D*)+(\d{1,5}\D*)+(\d{1,5}\D*)+(\d{1,5}\D*)+(\d{1,5}\D*)+(\d{1,5}\D*)+(\d{1,5}\D*)+(\d{1,5}\D*)+(\d{1,5}\D*)$'
    	m2=re.search(regexp2,line)
 	if m2:
            	I.append(m2.group(1))
	     	#		J.append(m2.group(2))
	       	#		ILEN.append(m2.group(3))
            	#		JLEN.append(m2.group(4))
              	#		MATCH.append(m2.group(5))
              	#		NGAPS.append(m2.group(6))
            	#		NALIG.append(m2.group(7))
            	#		NIDENT.append(m2.group(8))
             	#		IDENT.append(m2.group(9))
             	#		NAS.append(m2.group(10))
            	#		NASAL.append(m2.group(11))
              	#		NRANS.append(m2.group(12))
              	#		RMEAN.append(m2.group(13))
     		#		STDEV.append(m2.group(14))
		#		SCORE.append(m2.group(15))
               # list.append(m2.group())
		print m2.group(1)
	else:
	     	print 'not found'

#while list[0:5] == index:
#                list[0:5] = identifier
#                print list





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
