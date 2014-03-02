#script to plot the smoothed data in R
data = scan('/homes/czconnolly/BS32010/datastructures/smoothsignal.txt')

#creates a pdf file for the graph and plots it
pdf('/homes/czconnolly/BS32010/dataplot70.pdf')
plot(data)
#closes the pdf file
dev.off()


