from cutNew import * #to calculate Y  

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


def clust(superRoot,root,var,k):
    if (root == None or root.left == None or root.right == None) or returnX(root.subTreeSequence,var) < k:
        return
    clust(superRoot,root.left,var,k)
    clust(superRoot,root.right,var,k)
    if root.variable == root.left.variable:
        #printTree(superRoot)
        #print("hell1")
        YInitialSecond =  returnY(superRoot.subTreeSequence,root.left.subTreeSequence,var)
        XInitialSecond = returnX(root.left.subTreeSequence,var)
        newArrayOne = root.left.left.subTreeSequence.copy()
        newArrayOne.extend(root.right.subTreeSequence)
        XFinalSecond = returnX(newArrayOne,var)
        YFinalSecond = returnY(superRoot.subTreeSequence,newArrayOne,var)
        
        if (YInitialSecond > YFinalSecond and XInitialSecond >= XFinalSecond) or XInitialSecond >= XFinalSecond:

            temp = root.right
            root.right = root.left.right
            root.left.right = temp

            root.right.parent = root
            root.left.right.parent = root.left   #fixing parents

            root.left.subTreeSequence = []
            root.left.subTreeSequence = root.left.left.subTreeSequence.copy()
            root.left.subTreeSequence.extend(root.left.right.subTreeSequence)
            root.subTreeSequence = []
            root.subTreeSequence = root.left.subTreeSequence.copy()
            root.subTreeSequence.extend(root.right.subTreeSequence)
            updateSubSequence(superRoot,root)
            #printTree(superRoot)
            
            #print("hell2")
        
        newArrayOne = []
        newArrayOne = root.right.subTreeSequence.copy()
        newArrayOne.extend(root.left.right.subTreeSequence)
        YFinalSecond = returnY(superRoot.subTreeSequence,newArrayOne,var)
        XFinalSecond = returnX(newArrayOne,var)
        
        if (YInitialSecond > YFinalSecond and XInitialSecond >= XFinalSecond) or XInitialSecond > XFinalSecond:
            temp = root.right
            root.right = root.left.left
            root.left.left = temp
            
            root.right.parent = root
            root.left.left.parent = root.left #fixing parents

            root.left.subTreeSequence = []
            root.left.subTreeSequence = root.left.left.subTreeSequence.copy()
            root.left.subTreeSequence.extend(root.left.right.subTreeSequence)
            root.subTreeSequence = []
            root.subTreeSequence = root.left.subTreeSequence.copy()
            root.subTreeSequence.extend(root.right.subTreeSequence)
            updateSubSequence(superRoot,root)
            #printTree(superRoot)
            #print("hell3")

    if root.variable == root.right.variable:
        #printTree(superRoot)
        #print("hell4")
        XInitial = returnX(root.right.subTreeSequence,var)
        YInitial = returnY(superRoot.subTreeSequence,root.right.subTreeSequence,var)
        newArrayOne = root.right.left.subTreeSequence.copy()
        newArrayOne.extend(root.left.subTreeSequence)
        XFinal = returnX(newArrayOne,var)
        YFinal = returnY(superRoot.subTreeSequence,newArrayOne,var)
        
        if (YInitial > YFinal and XInitial >= XFinal) or XInitial > XFinal:
            temp = root.left
            root.left = root.right.right
            root.right.right = temp

            root.left.parent = root
            root.right.right.parent = root.right

            root.right.subTreeSequence = []
            root.right.subTreeSequence = root.right.left.subTreeSequence.copy()
            root.right.subTreeSequence.extend(root.right.right.subTreeSequence)
            root.subTreeSequence = []
            root.subTreeSequence = root.left.subTreeSequence.copy()
            root.subTreeSequence.extend(root.right.subTreeSequence)
            updateSubSequence(superRoot,root)
            #printTree(superRoot)
            #print("hell5")
        
        XInitial = returnX(root.right.subTreeSequence,var)
        YInitial = returnY(superRoot.subTreeSequence,root.right.subTreeSequence,var)
        newArrayOne = []
        newArrayOne = root.left.subTreeSequence.copy()
        newArrayOne.extend(root.right.right.subTreeSequence)
        
        XFinal = returnX(newArrayOne,var)
        YFinal = returnY(superRoot.subTreeSequence,newArrayOne,var)

        if (YInitial> YFinal and XInitial >= XFinal) or (XInitial > XFinal):
            temp = root.left
            root.left = root.right.left
            root.right.left = temp

            root.left.parent = root
            root.right.left.parent = root.right

            root.right.subTreeSequence = []
            root.right.subTreeSequence = root.right.left.subTreeSequence.copy()
            root.right.subTreeSequence.extend(root.right.right.subTreeSequence)
            root.subTreeSequence = []
            root.subTreeSequence = root.left.subTreeSequence.copy()
            root.subTreeSequence.extend(root.right.subTreeSequence)
            updateSubSequence(superRoot,root)
            #printTree(superRoot)
            #print("hell6")

    return


        








