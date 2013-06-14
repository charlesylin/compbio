#week2_exercise3_solution.py

'''
In this exercise we will write a function that describes the overlap between
two transcription factor binding sites
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
    Please replace getTFSites with your own version from week2_exercise2.py
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



def getTFOverlap(fileName,tf1,tf2):

    '''
    This function should give the overlap statistics for any two transcription factors
    in chenTF.txt

    For example if you ran getTFOverlap(chenFileName,'Oct4','Nanog')

    The output should look like this:
    
    "TRANSCRIPTION FACTOR OCT4 HAS 100000 BINDING SITES"
    "TRANSCRIPTION FACTOR NANOG HAS 200000 BINDING SITES"
    "THERE ARE 5000 SITES WHERE OCT4 AND NANOG OVERLAP"

    
    A pair of binding sites are considered overlapping if they are on the same chromosome
    and their coordinates overlap.

    e.g.
    chr1:1000-2000 overlaps with chr1:1500-3000

    use the .split() attribute of string objects to help you extract this information from the binding
    sites in chenTF.txt

    '''

    tf1SiteList = getTFSites(fileName,tf1)

    tf2SiteList = getTFSites(fileName,tf2)

    overlapCount = 0

    for tf1Site in tf1SiteList:

        #Extracting the coordinate information from tf1Site
        tf1Chrom = tf1Site.split(':')[0]
        tf1Start = int(tf1Site.split(':')[1].split('-')[0]) #make sure coordinates are always integers
        tf1End =int(tf1Site.split(':')[1].split('-')[1])
        
        
        '''
        complete the rest of the code
        '''
        
        #Check each tf1Site against each tf2Site one at a time for overlap
        for tf2Site in tf2SiteList:

            #Extracting the coordinate information from tf2Site
            tf2Chrom = tf2Site.split(':')[0]
            tf2Start = int(tf2Site.split(':')[1].split('-')[0])
            tf2End =int(tf2Site.split(':')[1].split('-')[1])


            if tf1Chrom != tf2Chrom:
                #save time here by checking first that the sites are on the same chrom
                #if they are not, continue advances the loop one iteration
                continue
            
            #overlap occurs if the coordinates of one site can be contained by the other
            #this occurs if tf1Start is <= tf2End and tf1End >= tf2Start 

            if tf1Start <= tf2End and tf1End >= tf2Start:
                overlapCount += 1 #add 1 to the overlap count
                continue

    print "TRANSCRIPTION FACTOR %s HAS %s BINDING SITES" % (tf1,len(tf1SiteList))
    print "TRANSCRIPTION FACTOR %s HAS %s BINDING SITES" % (tf2,len(tf2SiteList))
    print "THERE ARE %s SITES WHERE %s AND %s OVERLAP" % (overlapCount,tf1,tf2)




getTFOverlap(chenFileName,'Oct4','Nanog')




    
