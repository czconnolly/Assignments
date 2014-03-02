#python script that smooths data by calculating a moving average

#define the names of the files and set up an output handle
input_file = '/homes/czconnolly/BS32010/datastructures/signal.txt'
output_file = '/homes/czconnolly/BS32010/datastructures/smoothsignal.txt'
output_handle = open(output_file, 'w')

#opens signal.txt
data_file = open(input_file)

#creates an array called data
data = []

#reads in each line in the file and casts them to a float
for line in data_file.readlines():
	line = line.strip()
	for number in line.split():
		data.append(float(number))	

#closes signal.txt
data_file.close()

#sets the size of the buffer to 70, as this gives a sine graph when plotting the data 
buffersize = 70

#defines the variables 
buffer = []
buffertotal = 0
position = 0
result = []

#if the length of the current buffer is smaller than the specified buffer size
#then it will increase the buffer to fill it 
while len(buffer)<buffersize:
	buffer.append(data[position])
	buffertotal = buffertotal + data[position]
	position = position + 1

#calculates the average
result.append(float(buffertotal)/buffersize)

#works through the rest of the data calculating the moving average
for v in range(position, len(data)):
	buffertotal = buffertotal - buffer[v%buffersize]
	buffer[v%buffersize]=data[v]
	buffertotal = buffertotal + buffer[v%buffersize]
	result.append(float(buffertotal)/buffersize)

#write the results to the output text file with one floating point value per line
for r in result:
	output_handle.write('%s\n' %r)
output_handle.close()



