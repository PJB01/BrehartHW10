'''
Created by Phil Brehart
This program takes two txt files and converts their contents to a list. The contents are then merged right to left,
first txt file's word and then second txt files word.

Example Invocation: python3 reconstructSentence.py input1.txt input2.txt
'''

import sys

inputList1 = []
inputList2 = []
f1 = open(sys.argv[1], "r")
f2 = open(sys.argv[2], "r")
f3 = open("output.txt", "w")

def checkLine():
    global l  # global variables
    global curWordCount
    w = l.split()
    curWordCount += len(w)
    return w

def reconstructSentence(arr1, arr2, totLen):
    output = []
    for i in range(int(totLen / 2) + 1):
        if arr1 != []:
            output.append(arr1[-1]) # append last element of list1 to output
            arr1 = arr1[:-1] # delete last element of list1
        if arr2 != []:
            output.append(arr2[-1]) # append last element of list2 to output
            arr2 = arr2[:-1] # delete last element of list2
    return output

totWordCount = 0

#Create list from first file, calculate word count
curWordCount = 0
lines = f1.readlines()
linecount = len(lines) # len()
for l in lines:
    inputList1 += checkLine()
print ("List 1 is: ", inputList1)
print ("List1Length: ", curWordCount, "\n")
totWordCount += curWordCount

#Create list from second file, calculate word count
curWordCount = 0
lines = f2.readlines()
for l in lines:
    inputList2 += checkLine()
print ("List 2 is: ", inputList2)
print ("List2Length: ", curWordCount, "\n")

#Create final list, print results
totWordCount += curWordCount
out = reconstructSentence(inputList1, inputList2, totWordCount)
print ("The list out is: ", out)

#write resulting out list to file called output.txt
for i in range(len(out)):
    f3.write(out[i])
    f3.write(' ')




