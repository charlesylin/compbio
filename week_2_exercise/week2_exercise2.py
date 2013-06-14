#week2_exercise2.py

'''
In this exercise we will write a function to extract all of the binding sites
for a given factor from chenTF.txt

The easiest way to complete this exercise is to make edits and try running the entire file
in canopy by selecting run from the menu bar
'''

chenFileName = '' #change this to be the complete path of the chenTF.txt file


def parseTable(fileName,sep):

    '''
    Please replace parseTable with your own version from week2_exercise1.py
    '''
    




def getTFSites(fileName,tf):

    '''
    this function will return a list of binding sites for any given factor
    
    e.g. getTFSites(fileName,'Oct4') will return a list containing all Oct4 binding sites
    
    '''

    chenTable = parseTable(fileName,'\t')

    #the first line of the table is a list where each column contains
    #a string with the name of the tf
    header = chenTable[0] 

    #we can use this header to figure out which column corresponds to the tf in tf
    tfColumn = header.index("%s bound loci" % tf)

    print "Data for transcription factor %s is located in column %s" % (tf,tfColumn)

    tfSites  =[]
    
    '''
    fill in the rest of the code
    tfSites should be a list of binding sites for the given factor
    e.g. tfSites = ["chr1:10212250-10212257","chr1:10212250-10212257", etc...]

    note:  the table in chenTF.txt is a ragged array, meaning that each column has a different length
    open up chenTF.txt in excel and scroll to the bottom to see what I mean.

    Please keep this in mind as you code.

    '''

    return tfSites



#Test your function by using it to open up chenTF.txt
#And print the value of the second row first column

oct4Sites = getTFSites(chenFileName,'Oct4')


print "the first oct4 binding site is at %s" % oct4Sites[0]

print "the last oct4 binding site is at %s" % oct4Sites[-1]







#BONUS
#This code is not very fool proof
#For instance try uncommenting and running it with the following lines

#oct4Sites = getTFSites(chenFileName, 'oct4')

#lmycSites = getTFSites(chenFileName,'l-myc')

#Can you fix up the getTFSites function to still give you oct4 sites in the first instance
#And to print an error message like "ERROR: THIS TF IS NOT IN THE DATA SET"
#In the second instance?

#Call this new function getTFSitesFixed







    
