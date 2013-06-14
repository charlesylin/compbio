#week3_exercise1.py

'''
In this exercise we will write and use  a function
that tests the overlap of any two genomic regions
'''
        
def testOverlap(chrom1,start1,end1,chrom2,start2,end2):

    '''
    this function tests any two sets of coordinates for overlap
    and returns true/false
    '''
    #make sure start/end values are integers
    start1 = int(start1)
    end1 = int(end1)
    start2 = int(start2)
    end2 = int(end2)
    
    #first check the chromosomes for matching
    if chrom1 != chrom2:
        return False

    #then check the coordinates
    if start1 <= end2 and end1 >= start2:
        return True
    else:
        return False
    

print testOverlap('chr1',50,100,'chr1',75,150) #True

overlap = testOverlap('chr1',50,100,'chr1',75,150)
print overlap #True

print testOverlap('chr1',50,100,'chr1',150,200) 

print testOverlap('chr1',50,100,'chr1',25,75)

print testOverlap('chr1',50,100,'chr1',60,80)

print testOverlap('chr1',50,100,'chr1','60','80')

print testOverlap('chr2',50,100,'chr1',60,80)

print testOverlap('chr1',50,100,'chr1',25,50)

print testOverlap('chr1',50,100,'chr1',25,49)



print "Correct answers should be as follows:\nTrue\nTrue\nFalse\nTrue\nTrue\nTrue\nFalse\nTrue\nFalse\n"

