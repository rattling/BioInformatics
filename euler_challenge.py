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
edgeCount = 0
graph = {}
with open(myfile) as f:
    for line in f:
       #(key, val) = line.split()
       #d[int(key)] = val
       line=line.rstrip()
       x=line.split(" -> ")
       y=x[1].split(",")  
       graph[x[0]]=y     
       edgeCount = edgeCount + len(y)
       
check1=graph.get("2181", "none")
       

#print (graph.get("952", "none"))

#fo = open(fout, "w")
#
#for k, v in graph.items():
#    fo.write(str(k) + ' >>> '+ str(v) + '\n\n')
#
#fo.close()

#first go is just to let it wend its way back to start.  So its cycle0 from the 
#example.  And can just use first outnode rather than randomize!

#LOOP TO DO ONE ATTEMPT AT A PATH

def buildPath(euler, graphLeft, currNode):    
    myLen = len(graphLeft[currNode])    
    while myLen > 0:    
        #Print the out nodes for the first node
        #print (graphLeft.get(currNode, "none"))        
        #2. Take the first outnode from current node as the next node
        nextNode = graphLeft.get(currNode, "none")[0]       
        check3=graphLeft.get("2181", "none")
        #Remove the edge to the out node from the current node;
        graphLeft[currNode] = graphLeft[currNode][1:]    
        myLen = len(graphLeft[nextNode])
        euler.append(nextNode)
        currNode = nextNode
    return euler, graphLeft

def changeStart(euler, graphLeft):
    for idx, key in enumerate(euler):
        if len (graphLeft.get(key, "none"))> 0:
            newStart = key
            newIndex = idx
            break
    #euler = shift(euler, idx)
    return newStart, newIndex

def arb(dictionary):
    return next(iter(dictionary))

def shift(l, n):
    return l[n:] + l[:n]


#Program Start
euler=[]
use=[]

graphLeft = graph.copy()
print ("Goal is to traverse this many edges:" + str(edgeCount))
startNode = arb(graph)
euler.append(startNode)
euler, graphLeft = buildPath(euler, graphLeft, startNode)
counter = 1

print ("Eulerian Path now contains this many edges:" + str(len(euler)))
print("Eulerian Path")
print (', '.join(euler)) 

check2=graph.get("2181", "none")

while len(euler) < edgeCount:
    counter = counter + 1
    print ("Counter = " + str(counter))  
    startNode, startIndex = changeStart(euler, graphLeft)
    del euler[-1]    
    euler = shift(euler, startIndex) 
    euler.append(startNode)        
    euler, graphLeft = buildPath(euler, graphLeft, startNode)     
    print ("Eulerian Path now contains this many edges:" + str(len(euler)))
    print("Eulerian Path")
    print    

fo = open(fout, "w")
fo.write('->'.join(euler)) 
fo.close()
 









