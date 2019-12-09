import sys

sys.argv[5] #Fastq for total numbr of reads, Coutn, Count2, (assembly stats 1 and 2 for error rate) transcriptome 1, transcriptome 2 IN THIS ORDER

Array_of_file = ['']

x = open("Select_Transcriptome_Report.txt",'w')

for eachArg in sys.argv:
	Array_of_file.append(eachArg)
	
j=2
fastq = Array_of_file[j] #has an arguement of a fastq file 
i = 0
with open(fastq, 'r') as f:
    reads = []
    for line in f:
     i+=1
print("The total number of reads is: ", (i/4))

number_of_reads = (i/4)
writer = "The Total Number of Reads is: "
x.write(writer)
writer = str(number_of_reads)
x.write(writer)
writer = '\n'
x.write(writer)

j +=1 
count = Array_of_file[j]
count1 = open(count, 'r')
count_1 = (count1.read())
#print (count_1)


j +=1
count = Array_of_file[j]
count2 = open(count, 'r')
count_2 = (count2.read())
#print (count_2)

percent_map1 = (((float(count_1)/number_of_reads)))
percent_map2 = (((float(count_2)/number_of_reads)))

pt1 = 0 
pt2 = 0

#f = open("Chosen_Transcriptome.txt",'w')
#f.write(chosen_transcriptome)

j +=1
stats1 = Array_of_file[j]
with open(stats1, 'r') as f:
    for line in f:
    	if 'error rate' in str(line):
     		#print (line)
     		#print ('length is: ',len(line))
     		#print ('this is line[15:28]:', line[15:28])
     		index_start = (line.find(':')+2)
     		index_end = line.find('#')
     		#print('Error Rate of transcriptome1: ', line[index_start:index_end])
     		er1 = line[index_start:index_end]

    	if 'reads mapped and' in str(line):
    		#print (line)
    		#print ('length is: ',len(line))
    		#print ('this is line [27:37]:',line[27:37]) #index can go out of range depenting on result
    		#print ('this is line [27:38]:',line[27:38]) #value starts at the 28
    		#print ('index of :',line.find(':'))
    		#print ('index of #',line.find('#'))
    		index_start = (line.find(':')+2)
    		index_end = line.find('#')
    		mp1 = line[index_start:index_end]
    		#print('Reads mapped and paired of transcriptome1: ', line[index_start:index_end])


j +=1
stats2 = Array_of_file[j]
with open(stats2, 'r') as f:
    for line in f:
    	if 'error rate' in str(line):
     		#print (line)
     		#print ('length is: ',len(line))
     		#print ('this is line[15:28]:', line[15:28])
     		index_start = (line.find(':')+2)
     		index_end = line.find('#')
     		#print('Error Rate of transcriptome1: ', line[index_start:index_end])
     		er2 = line[index_start:index_end]

    	if 'reads mapped and' in str(line):
    		#print (line)
    		#print ('length is: ',len(line))
    		#print ('this is line [27:37]:',line[27:37]) #index can go out of range depenting on result
    		#print ('this is line [27:38]:',line[27:38]) #value starts at the 28
    		#print ('index of :',line.find(':'))
    		#print ('index of #',line.find('#'))
    		index_start = (line.find(':')+2)
    		index_end = line.find('#')
    		mp2 = line[index_start:index_end]
    		#print('Reads mapped and paired of transcriptome1: ', line[index_start:index_end])

print()
print ("The percent mapped back of transcriptome1: ", percent_map1)
print('Error rate of transcriptome1: ',er1)
print('Reads mapped and paired of transcriptome1: ', mp1)
print()
print()
print ("The percent mapped back of transcriptome2: ", percent_map2)
print('Error rate of transcriptome2: ',er2)
print('Reads mapped and paired of transcriptome2: ', mp2)
print()

writer = '\n'
x.write(writer)
writer = "The percent mapped back of transcriptome1: "
x.write(writer)
writer = str(percent_map1)
x.write(writer)
writer = '\n'
x.write(writer)
writer = 'Error rate of transcriptome1: '
x.write(writer)
writer = str(er1)
x.write(writer)
writer = '\n'
x.write(writer)
writer = 'Reads mapped and paired of transcriptome1: '
x.write(writer)
writer = str(mp1)
x.write(writer)
writer = '\n'
x.write(writer)
x.write(writer)
writer = "The percent mapped back of transcriptome2: "
x.write(writer)
writer = str(percent_map2)
x.write(writer)
writer = '\n'
x.write(writer)
writer = 'Error rate of transcriptome2: '
x.write(writer)
writer = str(er2)
x.write(writer)
writer = '\n'
x.write(writer)
writer = 'Reads mapped and paired of transcriptome2: '
x.write(writer)
writer = str(mp2)
x.write(writer)
writer = '\n'
x.write(writer)

if float(er1) < float(er2):
	pt1 +=1
	print ('winner er: p1')
if float(er2) < float(er1):
	pt2 +=1
	print ('winner er: p2')

if int(mp1) > int(mp2):
	pt1 +=1
	print ('winner mp: p1')
if int(mp2) > int(mp1):
	pt2 +=1
	print ('winner mp: p2')

if percent_map1 > percent_map2 :
	#chosen_transcriptome = Array_of_file[j+1]
	#print ("Chosen Transcriptome: ", chosen_transcriptome)
	pt1 +=1 
	print ('winner %: p1')

if percent_map2 > percent_map1:
	#chosen_transcriptome = Array_of_file[j+2]
	#print ("Chosen Transcriptome: ", chosen_transcriptome)
	pt2 +=2
	print ('winner %: p2')

chosen_transcriptome = ''
print()
if pt1 > pt2:
	chosen_transcriptome = Array_of_file[j+1]
	print ("Chosen Transcriptome: ", chosen_transcriptome)

if pt2 > pt1:
	chosen_transcriptome = Array_of_file[j+2]
	print ("Chosen Transcriptome: ", chosen_transcriptome)

writer = '\n'
x.write(writer)
writer = 'Chosen Transcriptome: '
x.write(writer)
writer = (chosen_transcriptome)
x.write(writer)

v = open("Chosen_Transcriptome.txt",'w')

with open(chosen_transcriptome, 'r') as f:
    for line in f:
    	v.write(line)