import sys
import random
import copy
#import networkx as nx
import numpy as np
sys.setrecursionlimit(10**6)
global varFrequency 
global minLevel 
global maxLevel 
global size 
global var 
global graph
from swap import *
from cluster import *
from generateTree import *
from cut import *
from shift import *

class tree:
    def __init__(self,root = None,nodeUnderCut = None):
        self.root = root
        self.nodeUnderCut = nodeUnderCut

class node:
    def __init__(self, variable = None, notOp = None,label = None,parent = None,k = None):
        self.right = None
        self.left = None
        self.variable = variable                #initializes a node
        self.notOp  = notOp
        self.parent = parent
        self.label =  [False,False,False,False,False,False,False,False]  # label not necessary
        self.subTreeSequence = []
        self.k = k

def printTree(root):
    if root == None:
        return
    print("(",end = "")
    printTree(root.left)
    if (root.notOp == '!'):
        print("!",end = "")
    print(root.variable ,end = "")
    printTree(root.right)
    print(")",end = "")
    return 


def printLabel(root):
    if root == None:
        return
    
    printLabel(root.left)
    print(root.label )
    printLabel(root.right)
    return 


#def addEdgesToGraph():
 #   for i in range(len(var)):
  #      for j in range(i+1,len(var)):       #creates a graph with all variables as nodes and adds a zero weight 
   #         Graph.add_edge(var[i],var[j],weight=1)


#def weightUpdatesForNodes(root,nodeFirst,nodeSecond,level):
 #   if root == None:            
  #      return 0
   # level = level + 1
    #flagLeft = weightUpdatesForNodes(root.left,nodeFirst,nodeSecond,level)
    #flagRight = weightUpdatesForNodes(root.right,nodeFirst,nodeSecond,level)       #flagLeft and right tells us if the nodes under the subtree have particular variables or not
    #if (root.label[ord(nodeFirst)-65] == True and root.label[ord(nodeSecond)-65] == True) and (flagLeft == 0 and flagRight ==0):
     #   Graph.add_edge(nodeFirst,nodeSecond,weight = level*1+Graph[nodeFirst][nodeSecond]['weight']) #update weights
        #print(level)
      #  return 1
    #if flagRight == 1 or flagLeft == 1:
     #   return 0
    #else:
    #    return 0
    #return 0

#def updateWeights(root):
    #for i in range(len(var)):
    #    for j in range(i+1,len(var)):
    #        level = 0                   #initial level will be 0
    #        weightUpdatesForNodes(root,var[i],var[j],level) 
 
    
def printSequence(root): #prints sequence of leaf nodes under a node
    if root == None:
        return
    print(root.subTreeSequence)
    printSequence(root.left)
    printSequence(root.right)

#def desirableSequence(vector): #arranges the list of nodes according to fielder vector
 #   mini = vector[0]
  #  minPos = 0
   # seq = []
    #varCopy = var.copy()
    #vectorCopy = np.copy(vector)
    #for j in range(len(var)):
     #   mini = 99999
      #  minPos = -1
       # for i in range(len(varCopy)):
        #    if vectorCopy[i] <= mini:
         #       mini = vectorCopy[i]
          #      minPos = i
        #print(mini)
        #seq.append(varCopy[minPos])
        #varCopy.pop(minPos)
        #print(varCopy)
        #vectorCopy=np.delete(vectorCopy,[minPos])
        #print(vectorCopy)
    #return seq

var = ['A','B','C','D','E','F','G','H']
minLevel = 3
maxLevel = 5
size =8

for i in range(1):
    level = 0
    #Graph = nx.Graph()
    #Graph.add_nodes_from(var)
    root = node()
    root = generateTree(root,level)
    printTree(root)
    print()
    rootNew = copy.deepcopy(root)
    #addEdgesToGraph()
    #updateWeights(root)
    #vector = nx.fiedler_vector(Graph,weight="weight")
    #sequence = desirableSequence(vector)
    k = 3
    #findSwappableNodes(root,root,sequence,k)
    #root=findCluster(root,root,sequence)
    nodesUnderCut = []
    count = 0 # no of luts initially zero
    flag = 0
    nodesUnderCut  = []
    nodesUnderCut,count,var,flag = cut(root,root,k,nodesUnderCut,count,var) 
    Tree = tree()
    Tree.root = root
    Tree.nodeUnderCut = nodesUnderCut
    while root != Tree.nodeUnderCut[len(nodesUnderCut)-1]:
        nodesUnderCut,count,var,flag = cut(root,root,k,nodesUnderCut,count,var) #does the cutting in the graph inititaly no of new variables =0
    if root != Tree.nodeUnderCut[len(nodesUnderCut)-1]:
        printTree(root)
        print()
    else:
        print("finalLut : ",end = " ") # in case one lut is made
        print("Z"+str(count-1))
    for i in range(len(Tree.nodeUnderCut)):
        print("Z"+str(i)," = ",end = " ")
        printTree(Tree.nodeUnderCut[i])
        print()
        print(Tree.nodeUnderCut[i].subTreeSequence)
    print(var)
    var = ['A','B','C','D','E','F','G','H']
    shiftHeavy(rootNew,rootNew,var)
    printTree(rootNew)
    print()
    nodesUnderCut = []
    count = 0 # no of luts initially zero
    flag = 0
    nodesUnderCut,count,var,flag = cut(rootNew,rootNew,k,nodesUnderCut,count,var) #does the cutting in the graph inititaly no of new variables =0
    Tree = tree()
    Tree.root = rootNew
    Tree.nodeUnderCut = nodesUnderCut
    while rootNew != Tree.nodeUnderCut[len(nodesUnderCut)-1]:
        nodesUnderCut,count,var,flag = cut(rootNew,rootNew,k,nodesUnderCut,count,var) #does the cutting in the graph inititaly no of new variables =0
    if rootNew != Tree.nodeUnderCut[len(nodesUnderCut)-1]:
        printTree(rootNew)
        print()
    else:
        print("finalLut : ",end = " ") # in case one lut is made
        print("Z"+str(count-1))
    for i in range(len(Tree.nodeUnderCut)):
        print("Z"+str(i)," = ",end = " ")
        printTree(Tree.nodeUnderCut[i])
        print()
        print(Tree.nodeUnderCut[i].subTreeSequence)
    print(var)
    
    
    
