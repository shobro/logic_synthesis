#does the cut in the graph
from shift import *
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

def returnK(arr,var):
    count = 0
    for i in range(len(var)):
        if arr.count(var[i]) > 0:
            count = count+1
    return count

def updateSubSequence(superRoot,root):  #updates subsequence after each swap
    if  superRoot.left == None or superRoot.right == None  :
        return 
    if (superRoot.left == root or superRoot.right == root):
        superRoot.subTreeSequence = []
        superRoot.subTreeSequence = superRoot.left.subTreeSequence.copy()
        superRoot.subTreeSequence.extend(superRoot.right.subTreeSequence)  
        return 
    updateSubSequence(superRoot.left,root)
    updateSubSequence(superRoot.right,root)
    superRoot.subTreeSequence = []
    superRoot.subTreeSequence = superRoot.left.subTreeSequence.copy()
    superRoot.subTreeSequence.extend(superRoot.right.subTreeSequence)
    return  

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

def checkParent(root,currLen,k,var):
    if root.parent == None or root == None:
        return 0
    if (returnK(root.parent.subTreeSequence,var)>k):
        return 0
    if returnK(root.parent.subTreeSequence,var)>currLen:
        flag = checkParent(root.parent,returnK(root.parent.subTreeSequence,var),k,var)
        return 1
    flag = checkParent(root.parent,returnK(root.parent.subTreeSequence,var),k,var)
    return flag


def cut(superRoot,root,k,nodesUnderCut,count,var):  #count tells us no of luts
    if root == None:
        return nodesUnderCut,count,var,0
    if returnK(root.subTreeSequence,var) <=k and (checkParent(root,returnK(root.subTreeSequence,var),k,var) == 0):
        #print(len(root.subTreeSequence))
        nodesUnderCut.append(root)
        variableName = "Z" + str(count)
        newVariable = node(variable = variableName,parent = root.parent)
        newSubTreeSequence = []
        newSubTreeSequence.append(variableName)
        var.append(variableName)
        if root.parent == None:
            return nodesUnderCut,count+1,var,1
        
        if root.parent.left == root:
            newSubTreeSequence.extend(root.parent.right.subTreeSequence)
            root.parent.subTreeSequence = []
            root.parent.subTreeSequence = newSubTreeSequence.copy()
            newVariable.subTreeSequence = [variableName]
            root.parent.left = newVariable
            updateSubSequence(superRoot,root.parent)
            shiftHeavy(superRoot,superRoot,var)
            printTree(superRoot)
            print()
            return nodesUnderCut,count+1,var,1

        if root.parent.right == root:
            root.parent.subTreeSequence = root.parent.left.subTreeSequence.copy()
            root.parent.subTreeSequence.extend(newSubTreeSequence)
            newVariable.subTreeSequence = [variableName]
            root.parent.right = newVariable
            updateSubSequence(superRoot,root.parent)
            shiftHeavy(superRoot,superRoot,var)
            printTree(superRoot)
            print()
            return nodesUnderCut,count+1,var,1    
    nodesUnderCut,count,var,flag = cut(superRoot,root.left,k,nodesUnderCut,count,var)
    if flag == 0:
        nodesUnderCut,count,var,flag = cut(superRoot,root.right,k,nodesUnderCut,count,var)
    return nodesUnderCut,count,var,flag
    
