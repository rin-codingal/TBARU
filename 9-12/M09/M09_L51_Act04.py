# Merge two files into a third file

# Reading data from file1
with open('test2.txt') as fp:
	data1 = fp.read()

# Reading data from file2
with open('test3.txt') as fp:
	data2 = fp.read()
	
# Merging 2 files to add the data of file2 from next line
data1 += "\n"
data1 += data2

print("Merging two files....")

with open ('MergedFile.txt', 'w') as fp:
	fp.write(data1)

