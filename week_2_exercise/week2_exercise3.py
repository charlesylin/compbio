#week2_exercise3.py

'''
In this exercise we will write a function that describes the overlap between
two transcription factor binding sites
'''

chenFileName = '' #change this to be the complete path of the chenTF.txt file


def parseTable(fileName,sep):

    '''
    Please replace parseTable with your own version from week2_exercise1.py
    '''
    





def getTFSites(fileName,tf):

    '''
    Please replace getTFSites with your own version from week2_exercise2.py
    '''








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
        tf1Start = tf1Site.split('-')[1][0]
        tf1End =tf1Site.split('-')[1][1]
        

        '''
        complete the rest of the code
        '''

    

    print "TRANSCRIPTION FACTOR %s HAS %s BINDING SITES" % (tf1,len(tf1SiteList))
    print "TRANSCRIPTION FACTOR %s HAS %s BINDING SITES" % (tf2,len(tf2SiteList))
    print "THERE ARE %s SITES WHERE %s AND %s OVERLAP" % (overlapCount,tf1,tf2)




getTFOverlap(chenFileName,'Oct4','Nanog')




    
