#!/usr/bin/python

import re

infile='/homes/czconnolly/BS32010/assignment3/ig_pairs.out'
fh = open(infile)

output_filename ='/homes/czconnolly/BS32010/assignment3/ig_pairs_parsed.out'
handle = open(output_filename, 'w')

line = fh.readline()

while line[:6] !='     I':
	line=fh.readline()
colnames=['I', 'J', 'ILEN', 'JLEN', 'MATCH', 'NGAPS', 'NALIG', 'NIDENT', '%IDENT', 'NAS', 'NASAL', 'NRANS', 'RMEAN', 'STDEV', 'SCORE', 'NUMBER']
for c in colnames:
	handle.write(c+'\t')
for line in fh:
	try:
		if line[:2]==' T':
			continue
		I=line[1:6]
		J=line[7:11]
		ILEN=line[12:16]
		JLEN=line[17:21]
		MATCH=line[22:31]
		NGAPS=line[32:38]
		NALIG=line[39:45]
		NIDENT=line[46:52]
		IDEN=line[53:62]
		NAS=line[63:72]
		NASAL=line[73:82]
		NRANS=line[83:89]
		RMEAN=line[90:99]
		STDEV=line[100:109]
		SCORE=line[110:119]
		NUMBER=line[120:126]
		handle.write('\n' + I + '\t' + J + '\t' + ILEN + '\t' + JLEN + '\t' + MATCH + '\t' + NGAPS + '\t'+ NALIG + '\t' + NIDENT + '\t' +IDEN + '\t' + NAS + '\t' + NASAL + '\t' + NRANS + '\t' + RMEAN + '\t' + STDEV + '\t' + SCORE)
	except:
		pass 
handle.close()
