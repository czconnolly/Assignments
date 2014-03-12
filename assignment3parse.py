#import glob,os

#outfile = glob.glob(os.path.join('C:/homes/czconnolly/BS32010/assignment3/*.out'))
#	fh=open(outfile,'r')

#fh=open(outfile)

infile='/homes/czconnolly/BS32010/assignment3/ig_pairs.out'

fh = open(infile)

line = fh.readline()
while line != ' 1542   >d4jvpa_/1-132         132 b.1.1.1 (A:) automated matches {Vicugna pacos [TaxId: 30538]         0	0.00	   ':
	line=fh.readline()

header= fh.readline().strip()

colnames = {}

index=0
for title in header.split('\t'):
	colnames[title]=index
	print '%s\t%s'%(title,index)
	index=index+1


igfile=open('ig_file.txt','w')

columns=['I', 'J','ILEN', 'JLEN', 'MATCH', 'NGAPS', 'NALIG', 'NIDENT', '%IDENT', 'NAS', 'NASAL', 'NRANS', 'RMEAN', 'STDEV', 'SCORE']

def buildrow(row, fields):
	newrow=[]
	for f in fields:
		newrow.append(row[int(colnames[f])])
	return '\t'.join(newrow)+'\n'

for line in fh.readlines():
	try:
		if line[0] == 'I':
			continue
		row=line.strip().split('\t')
		igfile.write(buildrow(row, columns))
		rows=rows+1
	except:
		pass

igfile.close()

print '%s rows processed'%rows
