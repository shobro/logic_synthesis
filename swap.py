
def findSwappableNodes(superRoot,root,sequence,k):
    if root == None or root.left == None or root.right == None:
        return
    findSwappableNodes(superRoot,root.left,sequence,k)
    findSwappableNodes(superRoot,root.right,sequence,k)
    root = positionChanger(superRoot,root,sequence)

def positionChanger(superRoot,root,sequence):
    flag = evaluator(root.left.subTreeSequence,root.right.subTreeSequence,sequence)     #changes the position with the help of evaluator function
    if flag == 1:
        temp = root.left
        root.left = root.right
        root.right = temp
        root.subTreeSequence = []
        root.subTreeSequence = root.left.subTreeSequence.copy()
        root.subTreeSequence.extend(root.right.subTreeSequence)
        updateSubSequence(superRoot,root)

    return root


def evaluator(subTreeSequenceOne,subTreeSequenceTwo,sequence):   #tells which node should be in which position
    posOne = sequence.index(subTreeSequenceOne[len(subTreeSequenceOne)-1])
    posTwo = sequence.index(subTreeSequenceTwo[0])
    if posOne <= posTwo:
        return 0  #left node should be first
    else:
        return 1 #right node should be first


def updateSubSequence(superRoot,root):  #updates subsequence after each swap
    if superRoot.left == None or superRoot.right == None:
        return 
    if (superRoot.left == root or superRoot.right == root):
        superRoot.subTreeSequence = None
        superRoot.subTreeSequence = superRoot.left.subTreeSequence.copy()
        superRoot.subTreeSequence.extend(superRoot.right.subTreeSequence)  
        return 
    
    updateSubSequence(superRoot.left,root)
    updateSubSequence(superRoot.right,root)
    superRoot.subTreeSequence = []
    superRoot.subTreeSequence = superRoot.left.subTreeSequence.copy()
    superRoot.subTreeSequence.extend(superRoot.right.subTreeSequence)
    return   
