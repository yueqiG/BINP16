#!/usr/bin/python3
"""
Title: build_similarity_matrix.py
Date: 2021-10-27
Author: Yueqi Gong

Description:
    This script converts the identity scores and alignment scores of pairwise sequences
        from part 1 to two similarity matrices.
    This program will output two similarity matrices into two tab-delimited files.
    The program will output the matrix based on identity scores into the first output
        file and output matrix based on alignment scores into the second one.
    The user must specify the name of two output file.

List of functions:
    1.NOR(list)
    2.NUMList(column)
    3.MakeList(column)
    4.MAT(list)
    5.OUTList(matrix,row)

List of "non-standard" modules:
    No "non-standard" modules are used.

Procedure:
    1. normalize alignment scores
    2. put identity scores and normalized alignment scores separately in two lists
    3. put the two names of sequences aligned in a small list
    4. put the small lists in a new list in order
    5. make a unrepeated name list of all sequences
    6. use the small lists to determine which position that the score belong to
    7. output the matrices
    

Usage:
    python build_similarity_matrix.py input_file output1_file output2_file
"""

import sys
input_file = sys.argv[1]
output1_file = sys.argv[2]
output2_file = sys.argv[3]

#open files
with open(input_file,'r') as data, open(output1_file,'w') as out1, open(output2_file,'w') as out2:

    #function 1 : normalize the alignment score
    def NOR(list): 
        maxl = max(list) # take the maximum value of the list
        minl = min(list) # take the minimal value of the list
        a = maxl - minl # calculate the difference
        nor_list = [] #make a empty list
        for i in range(len(list)): 
            nor_score =(float(list[i]) - float(minl))/ a
        #convert the values to floats and normalize them
        #put the nomalized scores in the empty list
            nor_list.append(round(nor_score,2))# round the score before append it
        return nor_list # output the normalized list
    #function 2 : put all values in the same column to a list
    def NUMList(column):    
        listscr = [] # make an empty list
        data = open(input_file,'r') # open file
        for line in data:
            read_line = line.split('\t') #split by tabs
            score = read_line[column].strip('\n') # find value in the same column
            listscr.append(float(score)) # convert them to floats and append them to the list
        return listscr # output the list
    
    #number list for identity scores
    numlist_id = NUMList(2)
    #number list for alignment score
    numlist_align = NUMList(3)  
    # normalized list for alignment score
    nor_alignment = NOR(numlist_align)
    
    listid = [] # new list for ids
    data = open(input_file,'r')
    for line in data:
        read_line = line.split('\t') # split by tabs
        ids =read_line[0:2] 
        # take the first two columns in the same row, which are the names of two compared sequences
        listid.append(ids) # put them in a list
   
    #function 3 : put the names in the same column to a list
    def MakeList(column):
        list = [] # make a list
        data = open(input_file,'r')
        for line in data:
            read_line = line.split('\t') #split by tabs
            id = read_line[column] # find names in the same column
            list.append(id) # put them in the list
        return list #output the name list
#header for the matrix
    list1 = MakeList(0) # names in the first column
    list2 = MakeList(1) # names in the second column

    con_list = list1 +list2 #put list1 and list2 together

    new_list = [] # make a new list
    # organize the name list by deleting the repeated names
    for i in con_list:
        if not i in new_list:
            new_list.append(i)
    
    num = len(new_list) # count the number of names

    #function 4 : put the values in the matrix
    def MAT(list):
        num = len(new_list)
        import numpy
        A = numpy.zeros((num,num)) # create matrix full of zeros
        for i in range(len(list)):
            m1 = listid[i][0] # the first name of compared sequences
            n1 = listid[i][1] # the second name of compared sequences
            m = new_list.index(m1) # find the position of the first name in the organized name list
            n = new_list.index(n1) # find the position of the second name in the organized name list 
            A[(m,n)] = list[i] # put the score in the right place in the matrix
            for m in range(num): 
                for n in range(num):
                    A[(n,m)] = A[(m,n)]
            # copy the matrix in a diagonal position
        return A # output matrix
    mat_id = MAT(numlist_id) # matrix based on identity scores
    mat_align = MAT(nor_alignment) # matrix based on aligment scores
    
    #function 5 : output one row of the matrix
    def OUTList(matrix,row):
        list = []
        for i in range(num):
            value = str(matrix[(row,i)]) 
            # output the values in the same row, take one value each time, convert float to string
            list.append(value)
        return '\t'.join(list) #output the values in one row separated by tabs

    print('\t'+'\t'.join(new_list),file = out1)
    # print the name list for the header line 
    for i in range(num):
        print(new_list[i]+'\t'+OUTList(mat_id,i),file = out1)
    # output the identity score matrix line by line
    
    print('\t'+'\t'.join(new_list),file = out2)
    # print the name list for the header line
    for i in range(num):
        print(new_list[i]+'\t'+OUTList(mat_align,i),file = out2)
    # output the alignment score matrix line by line

