#week2_exercise1.py

'''
In this exercise we will write and use a function that can parse delimited tables
We will use it to parse the table of ChIP-Seq peaks from chen et al., 2008

The easiest way to complete this exercise is to make edits and try running the entire file
in canopy by selecting run from the menu bar
'''

chenFileName = '' #change this to be the complete path of the chenTF.txt file


def parseTable(fileName,sep):

    '''
    write a function parseTable that takes each line of a file
    and splits it into a table.
    In python, tables are lists made up of lists
    
    e.g.
    the table
    1    2    3
    4    5    6
    7    8    9
    
    is represented as
    table = [[1,2,3],[4,5,6],[7,8,9]]
    
    where the first row is table[0]

    the first column of the first row is table[0][0]
    
    etc...
    
    We can make tables from delimited text files by breaking apart each row of the file into
    a list of elements using the delimiter defined in the variable sep
    e.g. for a tab delimited file, parseTable(fileName,'\t') will separate each line
    by the \t tab character
    '''
    
    openFile = open(fileName,'r')

    table = []

    fileLines = openFile.readlines()

    for line in fileLines:
        line = line.rstrip() # this removes the end of line characters at the end of each line
        line = line.split(sep)
        table.append(line)

    return table






#Test your function by using it to open up chenTF.txt
#And print the value of the second row first column




chenTable = parseTable(chenFileName,'\t')


print chenTable[1][0] 





    