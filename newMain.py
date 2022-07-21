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
from cutReal import *
from generateTree import *
from cutNew import *
from clust import *
from driver import *
from otherDriver import *
from verilogWriter import *
from file_analyzer import *
from scriptWriter import *

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

var = ['A','B','C','D','E','F','G','H']
minLevel = 2
maxLevel = 4
size =8

def checkParent(root):
    if root.left == None or root.right == None:
        return 
    if root.left.parent == root.right.parent:
        print(end = "") 
    else:
        print("yes",root.left.subTreeSequence," ",root.right.subTreeSequence," ",root.subTreeSequence," ",root.left.parent.subTreeSequence," ",root.right.parent.subTreeSequence)
        return
    
    checkParent(root.left)
    checkParent(root.right) 
    

def printSequence(root): #prints sequence of leaf nodes under a node
    if root == None:
        return
    print(root.subTreeSequence)
    printSequence(root.left)
    printSequence(root.right)


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

n = 10
for j in range(n):
    root = node()
    level = 0
    root = generateTree(root,level)
    printTree(root)
    print()
    rootNew = copy.deepcopy(root)
    otherDriver(rootNew,rootNew)
    print("final")
    printTree(rootNew)
    checkParent(rootNew)

    k = 3
    count = 0
    nodesUnderCut = []
    flag = 0                # just a return to make sure a cut has happend
    Y = 1500
               #just a comman practice to use a large no to find min Y
    '''Y = cutNew(root,root,k,var,Y)
    nodesUnderCut,count,var,flag = cutReal(root,root,k,var,Y,count,nodesUnderCut)
    Tree = tree() 
    while root != nodesUnderCut[len(nodesUnderCut)-1]:
        Y = 1500    
        Y = cutNew(root,root,k,var,Y)
        nodesUnderCut,count,var,flag = cutReal(root,root,k,var,Y,count,nodesUnderCut)
    
    if root != nodesUnderCut[len(nodesUnderCut)-1]:
        printTree(root)
        print()
    else:
        print("finalLut : ",end = " ") # in case one lut is made
        print("Z"+str(count-1))
    for i in range(len(nodesUnderCut)):
        print("Z"+str(i)," = ",end = " ")
        printTree(nodesUnderCut[i])
        print()'''
    var = ['A','B','C','D','E','F','G','H']
    Y = 1500
    flag = 0
    count = 0
    nodesUnderCut = []
    clust(rootNew,rootNew,var,k)       
    Y = cutNew(rootNew,rootNew,k,var,Y)
    print(Y)
    nodesUnderCut,count,var,flag = cutReal(rootNew,rootNew,k,var,Y,count,nodesUnderCut)
    while rootNew != nodesUnderCut[len(nodesUnderCut)-1]:
        Y = 1500  
        clust(rootNew,rootNew,var,k)    
        Y = cutNew(rootNew,rootNew,k,var,Y)
        nodesUnderCut,count,var,flag = cutReal(rootNew,rootNew,k,var,Y,count,nodesUnderCut)
    
    if rootNew != nodesUnderCut[len(nodesUnderCut)-1]:
        printTree(rootNew)
        print()
    else:
        print("finalLut : ",end = " ") # in case one lut is made
        print("Z"+str(count-1))
    for i in range(len(nodesUnderCut)):
        print("Z"+str(i)," = ",end = " ")
        printTree(nodesUnderCut[i])
        print()
        print(nodesUnderCut[i].subTreeSequence)  

    verilogWriter(len(nodesUnderCut),j,root)
scriptWriter(n)     
