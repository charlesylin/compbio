#week_1_exercise3.py
#Finding start sites

'''
In this exercise, we will scan the DNA sequence from exercise 1 and 2 for potential start sites
on the sense strand and then print a list where each element is a position of a start site.
'''


#this section of code is cleaned up and taken from exercise1
fastaFileName = ""   #add the name of the file in between the quotes
fastaFile = open(fastaFileName,"r")
fastaFileLines = fastaFile.readlines()
dna = ''
dna = dna + fastaFileLines[1]

#First use the .count() attribute of string type objects to count 
#the number of potential start sites in dna
#If you are having trouble here, please go to
#http://www.tutorialspoint.com/python/string_count.htm
#or watch the video here http://www.youtube.com/watch?v=cFfOOSMLEIE

nStartSites = #complete this line
print "There are %s potential start sites in this sequence" % nStartSites

#Create an empty list object called startSiteList
startSiteList = [] 

#We will fill up startSiteList with the positions of all starts
#e.g. if start sites occur at positions 100,125, and 150 in dns
#then startSiteList will be [100,125,150]

#To do this we need to first learn how to figure out if a string = 'ATG'

#this can be accomplished using an if statemnt.
#Learn Python The Hard Way exercise 29 is useful here
#http://learnpythonthehardway.org/book/ex29.html

#Let's see an if statement in action
#play with the value of 'a' here and examine the output
a = 1
if a == 1:
    print 'a is equal to 1'

if a != 1:
    print 'a does not equal to 1'

if a > 1:
    print 'a is greater than 1'

if a >= 1:
    print 'a is greater than or equal to 1'

if a < 1:
    print 'a is less than 1'

if a <= 1:
    print 'a is less than equal to 1'


#If statements can also test whether or not strings are equal

a = 'ATG'

if a == 'ATG':
    print 'a is equal to ATG'

if a != 'ATG':
    print 'a is not equal to ATG'

if a != 'atg':
    print 'a is not equal to atg'

#Notice here how case matters for string if tests.

#Now let's start examining a DNA sequence
#We start with a string called sequence

sequence = 'CCATGCCC'

#we want to test each 3mer starting with CCA to see if it equals ATG

if sequence[0:3] == 'ATG':
    print 'sequence[0:3] equals ATG' 

if sequence[1:4] == 'ATG':
    print 'sequence[1:4] equals ATG'

if sequence[2:5] == 'ATG':
    print 'sequence[2:5] equals ATG'

#You should be able to see that this gets fairly tedious.
#We can automate this with a while loop

#This is a good resource to learn about while loops
#http://www.tutorialspoint.com/python/python_while_loop.htm
#Learn Python The Hard Way exercise 33 is also good
#http://learnpythonthehardway.org/book/ex33.html


#a while loop acts like a repeating if test.  
#for instance
i = 0  
while i < 10:
    print i
    i = i+1

#as long as i is less than 10, the loop will keep looping.
#notice how we add 1 to i during each loop.
#this means after the 10th loop, i is no longer less than 10 and the loop stops

#You have to be very careful with while loops because they can go on forever

#for instance try this loop
#note, to break out of an infinite loop, 
#you have to typ ctrl + c at the same time to manually break out of your code
#this is a very good trick to learn as you will likely make many accidental infinite loops
#during your coding


#use ctrl + c to break out of this infinite loop
#save everything first in case things go haywire
i = 0
while i < 10:
    print i



#now lets use a while loop to loop through a stirng sequence
sequence = 'CCATGCCC'
i = 0
while i < (len(sequence)-3):
    if sequence[i:(i+3)] == 'ATG':
        print i


#While loops can take some time to understand intuitively so play with them and use the resources above

#now lets go back to the original problem


#Create an empty list object called startSiteList
startSiteList = [] 

#We will fill up startSiteList with the positions of all starts
#e.g. if start sites occur at positions 100,125, and 150 in dna
#then startSiteList will be [100,125,150]



'''
fill in the code to do the rest!
'''



#If all works, this list will print the location of start sites in DNA
print startSiteList





















