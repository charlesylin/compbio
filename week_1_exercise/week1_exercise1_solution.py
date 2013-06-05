#week_1_exercise1.py
#NOTE:  These exercises are intended to be complete line by line using the interactive python in canopy.
#To do these exercises, copy them one line at a time into the python interactive window and hit return.  This will run that line of code interactive. Make changes to lines that say "complete this line"
# Lines beginning with # are comments and don't need to be run

#Open up a .fasta sequence file and make a string type ojbect with only the DNA sequence


#When you download and unzip the files, please place the week 1 folder on the desktop in the folder named comp_bio
#The FULL PATH will be something like /Users/Desktop/USERNAME/Desktop/comp_bio/week_1_exercise/tubb.fasta
#on a mac, to deterime the full path of a file, right click a file, select get info and look at the "WHERE" field
#this will tell you the path of the file
#on windows this is a little harder.  try going to http://technet.microsoft.com/en-us/magazine/ff678296.aspx

#Create a string type ojbect with the FULL PATH of the tubb.fasta file
fastaFileName = ""   #complete this line by adding the name of the file in between the quotes


#create an open file type object of the fasta file
fastaFile = open(fastaFileName,"r")

#The type function allows you to determine the type of any object
#e.g. type(object)

#Check the type of fastaFile
print type(fastaFile)

#Use the .readlines() attribute of a file type object to get all of the lines
fastaFileLines = fastaFile.readlines()


#use the type function to figure out the object type of fastaFileLines
print type(fastFileLines)  #complete this line

#What type of object is fastaFileLines?
print "fastaFileLines is a %s type of object" % "list"  #complete this line by changing OBJECT TYPE into the actual object type of fastaFileLines

#The len function allows you to find out the length of an object
#e.g. len(object)

#use the len function to figure out how long fastaFileLines is
print len(fastaFileLines)

#How long is fastaFileLines?
print "fastaFileLines has a length of %s" % "2" #complete this line by replacing LENGTH with a string with the correct answer


#Now that we know fastaFileLines is a list type object, Lets examine its elements
#A list is composed of multiple elements.
#for instance, l = ['a','b','c'] then l is a list type object with 3 elements that are string type objects

#Print the first element of fastaFileLines
print fastaFileLines[0]


#What type of object is fastaFileLines[0]?
print type(fastaFileLInes[0])
print "fastaFileLines[0] is a %s type of object" % "string" #complete this line

#Print the second element
print fastaFileLines[1]

#That was probably pretty big.  Now print only the first 100 characters in fastaFileLines[1]
#Check the lecture notes on slicing an iterable object if you are confused here
print fastaFileLines[1][0:100] #complete this line


#Now print the last 100 characters of fastaFileLines[1]
print fastaFileLInes[1][-100:] # complete this line


#So what is fastaFileLines
print "fastaFileLines is a %s that contains %s elements that are %s type objects" % ("list","2","string") # replace x,y,z with strings containing the correct answers 

#Now lets assign the DNA sequence to a variable dna
dna = fastaFileLines[1]#complete this line


#If all goes well, this should print the DNA sequence of the TUBB gene locus
print(dna)




