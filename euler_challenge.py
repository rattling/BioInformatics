# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 21:32:47 2018

@author: John
"""
#https://www.python.org/doc/essays/graphs/
myfile = 'C:/Users/John/Documents/GitHub/BioInformatics/euler_challenge.txt'
fout='C:/Users/John/Documents/GitHub/BioInformatics/out.txt'

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

#print (graph.get("952", "none"))

#fo = open(fout, "w")
#
#for k, v in graph.items():
#    fo.write(str(k) + ' >>> '+ str(v) + '\n\n')
#
#fo.close()

#first go is just to let it wend its way back to start.  So its cycle0 from the 
#example.  And can just use first outnode rather than randomize!
euler=[]
use=[]

def arb(dictionary):
    return next(iter(dictionary))

#Gotta start somewhere
startNode = arb(graph)
#Add the first node to the euler path
euler.append(startNode)

#Print the out nodes for the first node
print (graph.get(startNode, "none"))

#Take the first outnode from start node as the current node
currNode = graph.get(startNode, "none")[0]
#Add it to the euler path
euler.append(currNode)
print(currNode)
#Remove the out node from the start node;
graph[startNode] = graph[startNode][1:]
#Print its out nodes
#print (graph.get(currNode, "none"))

#REPEAT THIS
#Take the first outnode from current node as the current node
nextNode = graph.get(currNode, "none")[0]
#Add it to the euler path
euler.append(nextNode)
#print(nextNode)
#Remove the out node from the current node;
graph[currNode] = graph[currNode][1:]
#Print its out nodes
#print (graph.get(currNode, "none"))

#REPEATING
#Take the first outnode from current node as the current node
currNode = nextNode
nextNode = graph.get(currNode, "none")[0]
#Add it to the euler path
euler.append(nextNode)
#print(nextNode)
#Remove the out node from the current node;
graph[currNode] = graph[currNode][1:]
#Print its out nodes
#print (graph.get(currNode, "none"))

print ("Values Left for Nodes already traversed")
print (graph.get("0", "none"))
print (graph.get("2180", "none"))
print (graph.get("2179", "none"))
print (graph.get("2181", "none"))
print("Eulerian Path So Far")
print (', '.join(euler))


