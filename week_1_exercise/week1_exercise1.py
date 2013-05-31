#week_1_exercise1.py

#Open up a .fasta sequence file and make a string type ojbect with only the DNA sequence


#Create a string type ojbect with the FULL PATH of the tubb.fasta file
fastaFileName = ""   #add the name of the file in between the quotes

#create an open file type object of the fasta file
fastaFile = open(fastaFileName,"r")

#Check the type of fastaFile
print type(fastaFile)

#Use the .readlines() attribute of a file type object to get all of the lines
fastaFileLines = fastaFile.readlines()

#What type of object is fastaFileLines?
print "fastaFileLines is a %s type of object" %  #complete this line


#How long is fastaFileLines?
print "fastaFileLines has a length of %s" #complete this line


#Lets examine fastaFileLines

#Print the first line
print fastaFileLines[0]


#What type of object is fastaFileLines[0]?
print "fastaFileLines[0] is a %s type of object" % #complete this line

#Print the second line
print fastaFileLines[1]

#That was probably pretty big.  Now print only the first 100 characters in fastaFileLines[1]
print #complete this line

#Now print the last 100 characters of fastaFileLines[1]
print # complete this line



#So what is fastaFileLines
print "fastaFileLines is a %s that contains %s elements that are %s type objects" % (x,y,z) # replace x,y,z with the correct answers 

#Now lets create a variable called dna that is a string type object 
dna = ''

#Then lets add the DNA sequence from the tubb.fasta file to dna

dna = dna + #complete this line

#If all goes well, this should print the DNA sequence of the TUBB gene locus
print(dna)




