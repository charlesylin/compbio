#week_1_exercise2.py
#Finding nucleotide composition

#open up a .fasta file and create a string type object of the DNA sequence
#make a dictionary showing the mononucleotide and dinucleotide composition

#this section of code is cleaned up and taken from exercise1
fastaFileName = ""   #add the name of the file in between the quotes
fastaFile = open(fastaFileName,"r")
fastaFileLines = fastaFile.readlines()
dna = ''
dna = dna + fastaFileLines[1]


#we want to figure out how many times A,T,C,G occur in this sequence.
#to do this, we can use the .count attribute of string type objects.


aCount = dna.count('A')
tCount = #complete the rest of these lines
cCount =
gCount =


#the count doesn't tell us the frequency.  to do that, we have to divide by the
#length of the dna
dnaLength = len(dna)
aFreq =   #complete this line

print aFreq

#Does aFreq equal 0?  If so, it's because of integer division!
#we need to change the object type of aCount and dnaLength the from an integer into a float
aCount = float(aCount)
dnaLength = float(dna)

#now try to calculate aFreq again. better?

aFreq = #complete this line

print "aFreq is now a %s type object" % type(aFreq)
print aFreq

#Write similar lines of code to calculate tFreq,cFreq,gFreq






print "the frequencies of A,T,C,G in dna are %s,%s,%s,%s" % (aFreq,tFreq,cFreq,gFreq)

#it's more useful to have this information in the form of a dictionary?
#dictionaries allow you to quickly look up information


#For instance, want to know the number of times people in the bradner lab have
#dunked a basketball? We can create a dictionary keyed by individuals with integer values
#of number of dunks (n.b. our hoop is 6 feet tall)

#create dunks a dictionary type object
dunks = {}

#we can fill in the dictionary one key at at time
dunks['charles'] = 100
dunks['rhamy'] = 15
dunks['fed'] = 50
dunks['ott'] = 7  #predominantly a jump shooter
dunks['joanna'] = 20
dunks['jay'] = 999
dunks['dan'] = 70

print dunks
print "jay has dunked %s times" % dunks['jay']

#dictionaries also allow you to change values by key

dunks['charles'] = 0 

print "charles has dunked %s times on a real hoop... sad :(" % dunks['charles']

#now lets make a dictionary of mononucleotide composition keyed by each nucleotide

#start with an empty dictionary
monoComp = {}

monoComp['A'] = #complete the rest of the lines




print monoComp



#Now lets do the same thing for dinucleotides
#Unfortunately there are 16 possible dinucleotide combinations, which makes
#it rather tedious to do this manually
#we can use loops to help us automate the process...

#lets take a brief detour and learn about for loops

#for loops follow the basic format

#for x in y:
#y needs to be defined before hand and must be an iterable object
#x does not need to be defined before hand

#for example
y = 'abcdefg'
for x in y:   #all loop statements must end in a :
    print "x is of type %s" % type(x)
    print "x has a value of %s" % x
    
#We will most commonly iterate through two kinds of objects, strings and lists
y = [0,1,2,3,4,5,6,7,8,9]
for x in y:
    print "x is of type %s" % type(x)
    print "x has a value of %s" % x
    
#notice how the type of x changes depending on y



#Lets first use a for loop to help us make a list of all possible 
#dinucleotides

#We need to start with something to iterate through
nucList = ['A','T','C','G']

#we also need to create a list type variable dinucList to store dinucleotides
dinucList = []

#now use a loop and string operations to make a list of all dinucleotides
#this is a bit tricky so collaborate with others to reach a solution.
for nuc in nucList:
    #complete the rest of the code
    
    
#at the end of the day, dinuclist should look like this

    
dinucList = ['AA',  #in python you can break up big lists like this to make them easier to read
 'AT',
 'AC',
 'AG',
 'TA',
 'TT',
 'TC',
 'TG',
 'CA',
 'CT',
 'CC',
 'CG',
 'GA',
 'GT',
 'GC',
 'GG']
 
 
 #once we have the dinuclist, we need to calculate the frequency of each one
 #and fill out a dictionary dinucComp 
 dinucComp = {}
 
 #again this is a bit tricky, so collaborate with others.
 
 for dinuc in dinucList:
     
     
     #complete the rest of the code
     dinucComp[dinuc] = #complete this too
     
     
#at the end of the day you should be able to calculate the CG composition of this sequence

print dinucCom['CG']



 










