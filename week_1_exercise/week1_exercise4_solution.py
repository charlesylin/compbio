#week_1_exercise4.py
#Finding ORFs

'''
Find all ORFs on the sense strand of DNA and print them
'''


#this section of code is cleaned up and taken from exercise1
fastaFileName = ""   #add the name of the file in between the quotes
fastaFileName = '/Users/chazlin/Dropbox/teaching/2013_summer_comp/compbio/week_1_exercise/tubb.fasta'
fastaFile = open(fastaFileName,"r")
fastaFileLines = fastaFile.readlines()
dna = ''
dna = dna + fastaFileLines[1]


#An ORF begins with ATG and ends with a stop codon

stopCodonList = ['TAA','TAG','TGA']

#As you find ORFs, add the sequence of each ORF to this list
orfList = []


#At the end of the script, print all of the ORFs

#The rest is up to you. Remember that a stop codon is only considered a stop if it's in frame!


#First find all of the starts.  This is straight from exercise 3
startSiteList = []
i = 0
while i < (len(dna)-3):
    if dna[i:(i+3)] == 'ATG':
        startSiteList.append(i)
    i = i +1


for start in startSiteList:

    i = start
    while i < (len(dna) -3):
        if stopCodonList.count(dna[i:(i+3)]) == 1:
            orfSequence = dna[start:(i+3)]
            orfList.append(orfSequence)
            break # this exist the loop
                              
        i = i+ 3

for orf in orfList:
    print orf





#BONUS SECTION

#There are two ways to find ORFS in the antisense direction
#You can either create a reverse complement sequence
#Or you can search for the reverse complement of ATG, which is CAT
#And work your way towards the 5' end of the sequence finding ORFs

#By far the easiest way is to simply reverse complement the sequence

#Reverse complement approach


revDNA = dna[::-1]

#This is extended slice syntax. It works by doing [begin:end:step] - by leaving begin and end off and specifying a step of -1, it reverses a string.

revCompDNA = ''

for i in revDNA:

    if i == 'A':
        revCompDNA = revCompDNA + 'T'

    if i == 'T':
        revCompDNA = revCompDNA + 'A'

    if i =='C':
        revCompDNA = revCompDNA + 'G'

    if i =='G':
        revCompDNA = revCompDNA + 'C'


#And now it's just like the sense strand ORF problem


#First find all of the starts.  This is straight from exercise 3
startSiteList = []
revOrfList = []
i = 0
while i < (len(revCompDNA)-3):
    if revCompDNA[i:(i+3)] == 'ATG':
        startSiteList.append(i)
    i = i +1


for start in startSiteList:

    i = start
    while i < (len(revCompDNA) -3):
        if stopCodonList.count(revCompDNA[i:(i+3)]) == 1:
            orfSequence = revCompDNA[start:(i+3)]
            revOrfList.append(orfSequence)
            break # this exist the loop
                              
        i = i+ 3

for orf in revOrfList:
    print orf

  

