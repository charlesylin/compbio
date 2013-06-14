#week2_exercise2_solution.py

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
    
    openFile = open(fileName,'r')

    table = []

    fileLines = openFile.readlines()

    for line in fileLines:
        line = line.rstrip() # this removes the end of line characters at the end of each line
        line = line.split(sep)
        table.append(line)

    return table




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

    '''
    for line in chenTable[1:]:  #we don't need to get information from the header
        
        site = line[tfColumn]
        if len(site) > 0: #we only want entries that actually have data
            tfSites.append(line[tfColumn])
        

    return tfSites



#Test your function by using it to open up chenTF.txt
#And print the value of the second row first column

oct4Sites = getTFSites(chenFileName,'Oct4')


print "the first oct4 binding site is at %s" % oct4Sites[0]

print "the last oct4 binding site is at %s" % oct4Sites[-1]




#BONUS
#This code is not very fool proof
#For instance try uncommenting and running it with the following lines

def getTFSitesFixed(fileName,tf):

    '''
    this function will return a list of binding sites for any given factor
    
    e.g. getTFSites(fileName,'Oct4') will return a list containing all Oct4 binding sites
    
    '''

    chenTable = parseTable(fileName,'\t')

    #the first line of the table is a list where each column contains
    #a string with the name of the tf
    #to solve the capitlization problem, we need to make everything uppercase

    header = []
    for tfHeader in chenTable[0]:
        header.append(tfHeader.upper())
    
    #we can use this header to figure out which column corresponds to the tf in tf
    tf = tf.upper()
    
    #now the header.index attribute function is case invariant

    #now we need to check if the header actually has the TF
    
    if header.count("%s BOUND LOCI" % tf) == 0:
        print "ERROR: THIS TF %s IS NOT IN THE DATA SET" % tf
        return #this exist the function prematurely
    
    tfColumn = header.index("%s BOUND LOCI" % tf)

    print "Data for transcription factor %s is located in column %s" % (tf,tfColumn)

    tfSites  =[]
    
    '''
    fill in the rest of the code
    tfSites should be a list of binding sites for the given factor
    e.g. tfSites = ["chr1:10212250-10212257","chr1:10212250-10212257", etc...]

    '''
    for line in chenTable[1:]:  #we don't need to get information from the header
        
        site = line[tfColumn]
        if len(site) > 0: #we only want entries that actually have data
            tfSites.append(line[tfColumn])
        

    return tfSites



oct4Sites = getTFSitesFixed(chenFileName, 'oct4')

lmycSites = getTFSitesFixed(chenFileName,'l-myc')










    
