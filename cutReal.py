from cutNew import *

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


def cutReal(superRoot,root,k,var,Y,count,nodesUnderCut):
    if root == None:    
        return nodesUnderCut,count,var,0
    if (returnX(root.subTreeSequence,var) <= k and returnX(root.subTreeSequence,var) > 1 and returnY(superRoot.subTreeSequence,root.subTreeSequence,var) == Y) :
        nodesUnderCut.append(root) 
        variableName = "Z" + str(count)
        newVariable = node(variable = variableName,parent = root.parent)
        newVariable.subTreeSequence.append(variableName)
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
            return nodesUnderCut,count+1,var,1
        
        
        
        if root.parent.right == root:
            root.parent.subTreeSequence = root.parent.left.subTreeSequence.copy()
            root.parent.subTreeSequence.extend(newSubTreeSequence)
            newVariable.subTreeSequence = [variableName]
            root.parent.right = newVariable
            updateSubSequence(superRoot,root.parent)
            return nodesUnderCut,count+1,var,1
    flag = 0
    nodesUnderCut,count,var,flag = cutReal(superRoot,root.left,k,var,Y,count,nodesUnderCut)
    if flag == 0:
        nodesUnderCut,count,var,flag = cutReal(superRoot,root.right,k,var,Y,count,nodesUnderCut)
    return nodesUnderCut,count,var,flag