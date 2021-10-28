#!/usr/bin/python3
"""
Title: most_similar.py
Date: 2021-10-27
Author: Yueqi Gong

Description:
    This script take the input of user and output corresponding results.
    The input file is a similarity matrix based on alignment scores.
    When user input 'ALL', the program will output all the similarities between all individuals
    When user input one individual name, the program will output the most similar individual.
    When user input any other things, it will output an warning 'Please input the correct name!'

List of functions:
    No user defined fuctions are used.

List of modules:
    No "non-standard" modules are used.

Procedure:
    1. make the header line a name list
    2. start with the second row, make the first column(name) as keys, all the alignment
        scores with other people are stored in a list and make this list as values
    3. when user input 'ALL', it prints out all results
    4. when user input one person's name from the name list, it finds the maximum score
        in the value list and finds which column the score is located and output the resut.
    
    
usage:
    python most_similar.py input_file ALL/Name output_file [optional]
"""


import sys
input_file = sys.argv[1]
input = sys.argv[2]
output_file = sys.argv[3]

# open files
with open(input_file,'r') as matrix, open(output_file,'w') as output:
    # take header line
    header = matrix.readline().strip('\n')
    # make a name list from the header line
    listid = header.split('\t')[1:] # strip the first tab in the file

    dict = {} # make a dictionary
    for line in matrix:
        id = line.split('\t')[0] # make the name in the first column as keys
        # make the entire row of scores as values
        value = line.strip('\n').split('\t')[1:]
        dict[id] = value

    input_value = input # input ALL/Name
    # print the header
    print('SampleA'+'\t'+'SampleB'+'\t'+'Score[alignment score]',file = output)
    
    # if the user input ALL
    if input_value =='ALL': # output all the comparisons
        i = 0
        while (i< len(listid)): # take one sequence
            for k in range(i+1,len(listid)): 
                print(listid[i]+'\t'+listid[k]+'\t'+dict[listid[i]][k],file = output)
            i = i + 1
    # if the user input other stuff        
    elif input_value in listid: # if the input is one of the names included
        SA = listid.index(input_value) #find the row of the input name
        max_value = max(dict[input_value]) #find the maximum score in that row
        SB = dict[input_value].index(max_value) #find the column of the maximum score
        print(listid[SA]+'\t'+listid[SB]+'\t'+max_value, file = output)
        # output the result
    # if the user input something that is not included in the name list
    else:
        print('Please input the correct name!')
            

            
        
                
            


