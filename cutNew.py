
def returnX(arr,var):
    count = 0
    for i in range(len(var)):
        if arr.count(var[i]) > 0:
            count = count+1
    return count


def returnY(superArray,array,var):
    superRootX = returnX(superArray,var)    #uses A uNion B =A + B - A intersection B Rule 
    rootX = returnX(array,var)
    count = 0
    for i in range(len(var)):
        if (superArray.count(var[i]) - array.count(var[i])) > 0:
            count = count + 1
    Y =  superRootX - rootX + count 
    return Y
    


def cutNew(superRoot,root,k,var,Y):
    if root == None:
        return Y
    if returnX(root.subTreeSequence,var)<= k and returnX(root.subTreeSequence,var) > 1 and returnY(superRoot.subTreeSequence,root.subTreeSequence,var) < Y :
        Y = returnY(superRoot.subTreeSequence,root.subTreeSequence,var)
    
    Y = cutNew(superRoot,root.left,k,var,Y)
    Y = cutNew(superRoot,root.right,k,var,Y)
    return Y


    