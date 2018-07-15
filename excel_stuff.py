"""Programmaticaly create an excel file that has:
 - 200 random numbers on column A
 - 200 random words from a small pool on column B(edited)
Output a new file that has:
 - All columns between 20-30 removed
 - All columns that have EXCACTLY three vowels removed
STEP 1: what is a random number?
STEP 2: How to choose a random word from a list?
STEP 3: How do I read/write .csv files?
we aint fuck with no XML right now(edited)
"""

import xlswriter
import random

#Create a workbook and add a worksheetself.
workbook = xlswriter.Workbook('Rando.xlsx') #This constructor creates the Workbook
worksheet = workbook.add_worksheet() #Adds a new worksheet to the Workbook

# Start from the first cell. Rows and columns are zero indexedself.
row = 0
col = 0

list_of_numbers = []  #Creates an empty list

random.randint(numLow, numHigh)
for x in range (0, n):
    list_of_numbers.append(random.randint(numLow, numHigh))

list_of_numbers.sort() # Sorts the random list of numbers, because we can.

#Iterate over the above list and write it out row by row
for item in (list_of_numbers):
    worksheet.write(row, col, item)
    row += 1

word_list = [] #Create empty list to store words

row_1 = 1
col_1 = 1

with open('word_list.txt') as f:
    for line in f.readlines():
        index, word = line.strip().split('\t')
        word_list.append(word)
        worksheet.write(row_1, col_1, line)

workbook.close() #Close Excel file
