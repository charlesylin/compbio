#week_1_exercise4.py
#Finding ORFs

'''
Find all ORFs on the sense strand of DNA and print them
'''


#this section of code is cleaned up and taken from exercise1
fastaFileName = ""   #add the name of the file in between the quotes
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


for orf in orfList:
    print orf



#SUPER AWESOME BONUS.  FIND ALL OF THE ORFS IN THE ANTISENSE STRAND
#hint: try to reverse complement the dna sequence
#hint: use extended slice syntax http://docs.python.org/release/2.3.5/whatsnew/section-slices.html
