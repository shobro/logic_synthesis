
global minLevel 
global maxLevel
global size
global var 
import random
class node:
    def __init__(self, variable = None, notOp = None,label = None,parent = None):
        self.right = None
        self.left = None
        self.variable = variable                #initializes a node
        self.notOp  = notOp
        self.parent = parent
        self.label =  [False,False,False,False,False,False,False,False] 
        self.subTreeSequence = []

def generateTree(root,level):
    if level > maxLevel+1:
        root.left = None
        root.right = None
        return root
    
    root.variable,root.notOp = fitOperator(level)
    for i in range(size):
        if root.variable == var[i]:
            root.subTreeSequence.append(var[i])
            root.label[i] = True
            root.left = None
            root.right = None
            return root
    level = level+1
    
    root.left = node(parent = root)
    root.left = generateTree(root.left,level)
    root.right = node(parent = root)
    root.right = generateTree(root.right,level)
    root.label = unioni(root.right.label,root.left.label)
    root.subTreeSequence = root.left.subTreeSequence.copy()
    root.subTreeSequence.extend(root.right.subTreeSequence)
    return root



def unioni(A,B):
    C = []
    for i in range(len(A)):
        if (A[i] == True) or (B[i] == True):
            C.append(True)
        else:
            C.append(False)
    return C



def fitOperator(level):
    opProb = random.randint(1,5)#change this 
    if ((level <= maxLevel) and (opProb >=1) and (opProb<=2)) or level < minLevel:         
        prob = random.randint(0,2)        
        if (prob == 0):
            return '|',None
        elif prob ==1:
            return '|',None
        elif prob == 2:
            return '&',None
    else :
        prob = random.randint(0,7)
        if prob >= 0 and prob <= 3:
            return var[prob],'!'
        else:
            return var[prob],None
    return None,None



minLevel = 4
maxLevel  = 6
size = 8
var = ["A","B","C","D","E","F","G","H"]