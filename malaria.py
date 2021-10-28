#!/usr/bin/python3
"""
Title: Running Exercise 1
Date: Mon Oct 11 2021
Author: Yueqi Gong

Description: 
    This program will output the sequence file with protein description from blastx results accrodingly.    
    
Procedure:
    1.make dictionary1 with the fasta sequence file
    2.make dictionary2 with the blastx results file, same keys with dictionary1
    3.join values from two dictionaries accroding to the keys
    4.output file

Usage: To insert the information about the protein description from the blastx results to the fasta file
    
"""
dic1={}#create a new dictionary
f1 = open('malaria.fna','r').readlines()#read fasta file
for i in f1:
    if i.startswith('>'):#for the header line
        id = i.split()[0]#take first position in the list as keys for the dictionary
        fa = ''
    else:
        fa = fa + i.strip("\n")#take sequences as the values
        dic1[id]=fa
        
dic2={}#create a dictionary
f= open('malaria.blastx.tab','r').readlines() #read blastx results file
for a in f:
    if a.startswith('#'):#skip the header line
        pass
    else:
        name = '>'+a.split()[0]#take first position in the list as keys for the fictionary
        pro= a.split()[9:]#take information after protein name
        pros=' '.join(pro)#join all elements in list to a string
        dic2[name]=pros

#map two dictionaries with same keys and merge them into one dictionary
final_dic = {key: ", ".join([dic2[key], dic1[key]]) for key in dic1 if key in dic2}
out = open('output.txt','w')#write in output file
for key in final_dic:
    out.write(key + ' protein= '+ final_dic[key]+'\n')#print keys and values
out.close()#close the file
       

            
         
            