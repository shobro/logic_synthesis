def findCluster(superRoot,root,sequence): #superroot is just the top most node
    if root == None or root.left == None or root.right == None:
        return
    findCluster(superRoot,root.left,sequence)
    findCluster(superRoot,root.right,sequence)
    if root.variable == root.left.variable:   #clusterFound
        root,root.left = changePosition(root,root.left,sequence)
        updateSubSequence(superRoot,root)

    elif root.variable == root.right.variable:
        root,root.right = changePosition(root,root.right,sequence) 
        updateSubSequence(superRoot,root)
    return root



def evaluate(subTreeSequenceOne,subTreeSequenceTwo,subTreeSequenceThree,sequence):
    posOne = sequence.index(subTreeSequenceOne[0])
    posTwo = sequence.index(subTreeSequenceTwo[0])
    posThree = sequence.index(subTreeSequenceThree[0])
    arr = []
    arr.append(posOne)
    arr.append(posTwo)
    arr.append(posThree)
    arr.sort()
    if arr[0] == posOne:
        if arr[1] == posTwo:
            return 0         #mean order is same
        else :
            return 1
                     #means posOne,posThree, posTwo  
    if arr[0] == posTwo:
        if arr[1] == posOne:
            return 2
        else :
            return 3
    if arr[0] == posThree:
        if arr[1] == posOne:
            return 4
        else:
            return 5



def updateSubSequence(superRoot,root):  #updates subsequence after each swap
    if superRoot.left == None or superRoot.right == None:
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

def changePosition(nodeOne,nodeTwo,sequence):   #only for clusters 
    if nodeOne.left == nodeTwo: #if cluster node and its left child
        flag = evaluate(nodeTwo.left.subTreeSequence,nodeTwo.right.subTreeSequence,nodeOne.right.subTreeSequence,sequence)
        if flag == 0:
            return nodeOne,nodeTwo
        elif flag == 1:
            temp = nodeOne.right
            nodeTwo.right = nodeOne.right
            nodeOne.right = temp
            nodeTwo.subTreeSequence = []
            nodeTwo.subTreeSequence = nodeTwo.left.subTreeSequence.copy()
            nodeTwo.subTreeSequence.extend(nodeTwo.right.subTreeSequence)
            nodeOne.subTreeSequence = []
            nodeOne.subTreeSequence = nodeOne.left.subTreeSequence.copy()
            nodeOne.subTreeSequence.extend(nodeOne.right.subTreeSequence)
            return nodeOne,nodeTwo
        elif flag == 2:
            temp2 = nodeTwo.left
            nodeTwo.left = nodeTwo.right
            nodeTwo.right = temp2
            nodeTwo.subTreeSequence = []
            nodeTwo.subTreeSequence = nodeTwo.left.subTreeSequence.copy()
            nodeTwo.subTreeSequence.extend(nodeTwo.right.subTreeSequence)
            nodeOne.subTreeSequence = []
            nodeOne.subTreeSequence = nodeOne.left.subTreeSequence.copy()
            nodeOne.subTreeSequence.extend(nodeOne.right.subTreeSequence)
        elif flag == 3:
            temp1 = nodeOne.right
            temp2 = nodeTwo.left
            nodeTwo.left = nodeTwo.right
            nodeOne.right = temp2
            nodeTwo.right = temp1
            nodeTwo.subTreeSequence = []
            nodeTwo.subTreeSequence = nodeTwo.left.subTreeSequence.copy()
            nodeTwo.subTreeSequence.extend(nodeTwo.right.subTreeSequence)
            nodeOne.subTreeSequence = []
            nodeOne.subTreeSequence = nodeOne.left.subTreeSequence.copy()
            nodeOne.subTreeSequence.extend(nodeOne.right.subTreeSequence)
        elif flag == 4:
            temp1 = nodeOne.right
            temp2 = nodeTwo.left
            temp3 = nodeTwo.right
            nodeTwo.left = temp1
            nodeTwo.right = temp2
            nodeOne.right = temp3
            nodeTwo.subTreeSequence = []
            nodeTwo.subTreeSequence = nodeTwo.left.subTreeSequence.copy()
            nodeTwo.subTreeSequence.extend(nodeTwo.right.subTreeSequence)
            nodeOne.subTreeSequence = []
            nodeOne.subTreeSequence = nodeOne.left.subTreeSequence.copy()
            nodeOne.subTreeSequence.extend(nodeOne.right.subTreeSequence)
        else:
            temp1 = nodeTwo.left
            #temp2 = nodeTwo.right
            temp3 = nodeOne.right
            nodeTwo.left = temp3
            nodeOne.right = temp1
            nodeTwo.subTreeSequence = []
            nodeTwo.subTreeSequence = nodeTwo.left.subTreeSequence.copy()
            nodeTwo.subTreeSequence.extend(nodeTwo.right.subTreeSequence)
            nodeOne.subTreeSequence = []
            nodeOne.subTreeSequence = nodeOne.left.subTreeSequence.copy()
            nodeOne.subTreeSequence.extend(nodeOne.right.subTreeSequence)

    elif nodeOne.right == nodeTwo:
        flag = evaluate(nodeOne.left.subTreeSequence,nodeTwo.left.subTreeSequence,nodeTwo.right.subTreeSequence,sequence)
        if flag == 0:
            return nodeOne,nodeTwo
        elif flag == 1:
            temp = nodeTwo.right
            nodeTwo.right = nodeTwo.left
            nodeTwo.left = temp
            nodeTwo.subTreeSequence = []
            nodeTwo.subTreeSequence = nodeTwo.left.subTreeSequence.copy()
            nodeTwo.subTreeSequence.extend(nodeTwo.right.subTreeSequence)
            nodeOne.subTreeSequence = []
            nodeOne.subTreeSequence = nodeOne.left.subTreeSequence.copy()
            nodeOne.subTreeSequence.extend(nodeOne.right.subTreeSequence)
        elif flag == 2:
            temp = nodeOne.left
            nodeOne.left = nodeTwo.left
            nodeTwo.left = temp
            nodeTwo.subTreeSequence = []
            nodeTwo.subTreeSequence = nodeTwo.left.subTreeSequence.copy()
            nodeTwo.subTreeSequence.extend(nodeTwo.right.subTreeSequence)
            nodeOne.subTreeSequence = []
            nodeOne.subTreeSequence = nodeOne.left.subTreeSequence.copy()
            nodeOne.subTreeSequence.extend(nodeOne.right.subTreeSequence)
        elif flag == 3:
            temp1 = nodeOne.left
            temp2 = nodeTwo.left
            temp3 = nodeTwo.right
            nodeOne.left = temp2
            nodeTwo.left = temp3
            nodeTwo.right = temp1
            nodeTwo.subTreeSequence = []
            nodeTwo.subTreeSequence = nodeTwo.left.subTreeSequence.copy()
            nodeTwo.subTreeSequence.extend(nodeTwo.right.subTreeSequence)
            nodeOne.subTreeSequence = []
            nodeOne.subTreeSequence = nodeOne.left.subTreeSequence.copy()
            nodeOne.subTreeSequence.extend(nodeOne.right.subTreeSequence)
        elif flag == 4:
            temp1 = nodeOne.left
            temp2 = nodeTwo.left
            temp3 = nodeTwo.right
            nodeOne.left = temp3
            nodeTwo.left = temp1
            nodeTwo.right = temp2
            nodeTwo.subTreeSequence = []
            nodeTwo.subTreeSequence = nodeTwo.left.subTreeSequence.copy()
            nodeTwo.subTreeSequence.extend(nodeTwo.right.subTreeSequence)
            nodeOne.subTreeSequence = []
            nodeOne.subTreeSequence = nodeOne.left.subTreeSequence.copy()
            nodeOne.subTreeSequence.extend(nodeOne.right.subTreeSequence)
        elif flag == 5:
            temp1 = nodeOne.left
            #temp2 = nodeTwo.left
            temp3 = nodeTwo.right
            nodeOne.left = temp3
            nodeTwo.right = temp1
            nodeTwo.subTreeSequence = []
            nodeTwo.subTreeSequence = nodeTwo.left.subTreeSequence.copy()
            nodeTwo.subTreeSequence.extend(nodeTwo.right.subTreeSequence)
            nodeOne.subTreeSequence = []
            nodeOne.subTreeSequence = nodeOne.left.subTreeSequence.copy()
            nodeOne.subTreeSequence.extend(nodeOne.right.subTreeSequence)
    return nodeOne,nodeTwo


