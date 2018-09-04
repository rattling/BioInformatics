# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 21:32:47 2018

@author: John
"""
#https://www.python.org/doc/essays/graphs/
myfile = 'C:/Users/John/Documents/GitHub/BioInformatics/euler_challenge.txt'

#OK, this is nice.  Reads the file into a dict and stores multiple values as a list
#This allows duplication of key value pairs

graph = {}
with open(myfile) as f:
    for line in f:
       #(key, val) = line.split()
       #d[int(key)] = val
       line=line.rstrip()
       x=line.split(" -> ")
       y=x[1].split(",")  
       graph[x[0]]=y       

print (graph.get("952", "none"))

#first go is just to let it wend its way back to start.  So its cycle0 from the 
#example.  And can just use first outnode rather than randomize!


#pick a node randomly
#pick the next node from that value list randomly
#that value randomly for that node
#and so on until return home 

#so each time need to save the path 
#and note which nodes in the path have unused edges