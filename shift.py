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


def shiftHeavy(superRoot,root,var):
    if root.left == None or root.right == None:
        return
    if returnK(root.left.subTreeSequence,var) < returnK(root.right.subTreeSequence,var):
        temp = root.left
        root.left = root.right
        root.right = temp
        updateSubSequence(superRoot,root)
    shiftHeavy(superRoot,root.left,var)
    shiftHeavy(superRoot,root.right,var)
    