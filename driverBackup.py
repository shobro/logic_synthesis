from cutReal import updateSubSequence
from partition import nodes_of_partition
from leave_partiton import leaves_of_partition


global var

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

def isParent(leave,leftChild,root):         #checks if the leave's parent is root.left to find out partition len 
    if leave.parent == root:
        return 0
    if leave.parent == leftChild:
        return 1
    return isParent(leave.parent,leftChild,root)

def order(li_leaves,partitionLen):
    mat_var = []
    for i in range(len(var)):
        mat_leave_col = []
        for j in range(len(li_leaves)):
            if var[i] in li_leaves[j].subTreeSequence:
                mat_leave_col.append(1)
            else:
                mat_leave_col.append(0)
        mat_var.append(mat_leave_col)
    
    comman_mat = []
    for i in range(len(li_leaves)):
        comman_mat_col = []
        for j in range(len(li_leaves)):
            if i == j:
                comman_mat_col.append(-1)
            elif i > j:
                comman_mat_col.append(-1)
            else:
                commanEle = 0
                for k in range(len(var)):
                    if mat_var[k][i] == 1 and mat_var[k][j] == 1:
                        commanEle = commanEle+1
                comman_mat_col.append(commanEle)
        comman_mat.append(comman_mat_col)
    
    
    newLeaves = []
    skip = 0
    for i in range(partitionLen):
        if skip == 1:
            skip =0
            continue
        longestLen = -1
        for j in range(len(comman_mat)):
            for k in range(j,len(comman_mat)):
                if longestLen < comman_mat[j][k]:
                    longestLen = comman_mat[j][k]
        for k in range(len(comman_mat)):
            try:
                if comman_mat[k].index(longestLen) >=0:
                    if partitionLen - len(newLeaves) >= 2 and (li_leaves[k] not in newLeaves) and (li_leaves[comman_mat[k].index(longestLen)] not in newLeaves):       
                        newLeaves.append(li_leaves[k])
                        newLeaves.append(li_leaves[comman_mat[k].index(longestLen)])
                        comman_mat[k][comman_mat[k].index(longestLen)] = -1                        
                        skip = 1
                        break
                    elif li_leaves[k] in newLeaves and (li_leaves[comman_mat[k].index(longestLen)] not in newLeaves):
                        newLeaves.append(li_leaves[comman_mat[k].index(longestLen)])                        
                        comman_mat[k][comman_mat[k].index(longestLen)] = -1
                        skip = 1
                        break
                    elif li_leaves[comman_mat[k].index(longestLen)] in newLeaves and (li_leaves[k] not in newLeaves):
                        newLeaves.append(li_leaves[k])
                        
                        comman_mat[k][comman_mat[k].index(longestLen)] = -1
                        skip = 1
                        break
                    elif partitionLen - len(newLeaves) == 1 and (li_leaves[k] not in newLeaves) and (li_leaves[comman_mat[k].index(longestLen)] not in newLeaves):
                        newLeaves.append(li_leaves[k])
                        comman_mat[k][comman_mat[k].index(longestLen)] = -1
                        
                        skip = 1
                        break
            except:
                print(end = "")
    
    while(partitionLen != len(newLeaves)):
        longestLen = -1
        for j in range(len(comman_mat)):
            for k in range(j,len(comman_mat)):
                if longestLen < comman_mat[j][k]:
                    longestLen = comman_mat[j][k]
        for k in range(len(comman_mat)):
            try:
                if comman_mat[k].index(longestLen) >=0:
                    if partitionLen - len(newLeaves) >= 2 and (li_leaves[k] not in newLeaves) and (li_leaves[comman_mat[k].index(longestLen)] not in newLeaves):       
                        newLeaves.append(li_leaves[k])
                        newLeaves.append(li_leaves[comman_mat[k].index(longestLen)])
                        comman_mat[k][comman_mat[k].index(longestLen)] = -1
                        
                        break
                    elif li_leaves[k] in newLeaves and (li_leaves[comman_mat[k].index(longestLen)] not in newLeaves):
                        newLeaves.append(li_leaves[comman_mat[k].index(longestLen)])
                        comman_mat[k][comman_mat[k].index(longestLen)] = -1
                                               
                        break
                        
                    elif li_leaves[comman_mat[k].index(longestLen)] in newLeaves and (li_leaves[k] not in newLeaves):
                        newLeaves.append(li_leaves[k])
                        comman_mat[k][comman_mat[k].index(longestLen)] = -1
                        
                        break
                    elif (partitionLen - len(newLeaves)) == 1 and (li_leaves[k] not in newLeaves) and (li_leaves[comman_mat[k].index(longestLen)] not in newLeaves):
                        newLeaves.append(li_leaves[k])
                        comman_mat[k][comman_mat[k].index(longestLen)] = -1
                        break

            except:
                print(end = "")
    return newLeaves

        
        
        
        
def driver(root):
    li = [root]
    nodes_of_partition(root,root.variable,li)
    partition_len_left = 0
    partition_len_right = 0
    li_leaves = []
    if len(li) > 1:
        leaves_of_partition(li, li_leaves, root)
        for i in li_leaves:
            partition_len_left = partition_len_left + isParent(i,root.left,root)
            partition_len_right = partition_len_right + isParent(i, root.right, root)
    if partition_len_right == 0:
        partition_len_right = 1
    if partition_len_left == 0:
        partition_len_left = 1
    print("before")
    for i in li_leaves:
        printTree(i)
        print()
    newLeaves = order(li_leaves,(partition_len_left if (partition_len_left>partition_len_right) else partition_len_right))
    print("after")
    for i in newLeaves:
        #printTree(i)
        print(i.subTreeSequence)
    count = 0
    for i in newLeaves:                                
        pos = li_leaves[count]              
        if i != pos:                               
            if (pos.parent.left) == pos:
                temp = pos
                pos.parent.left = i                   
                if i.parent.left == i:
                    i.parent.left = temp
                    temp.parent = i.parent#fixing parent

                elif i.parent.right == i:
                    i.parent.right = temp
                    i.parent.right.parent = i.parent#fixing parent
                        
                    
                pos.parent.left.parent = pos.parent#fixing parent
                pos.parent.subTreeSequence = []
                pos.parent.subTreeSequence = pos.parent.left.subTreeSequence.copy()
                pos.parent.subTreeSequence.extend(pos.parent.right.subTreeSequence)

                i.parent.subTreeSequence = []
                i.parent.subTreeSequence = i.parent.left.subTreeSequence.copy()
                i.parent.subTreeSequence.extend(i.parent.right.subTreeSequence)
                updateSubSequence(root,i)
                updateSubSequence(root,pos)
                
            elif pos.parent.right == pos:
                    
                temp = pos
                pos.parent.right = i
                if i.parent.left == i:
                    i.parent.left = temp
                    i.parent.left.parent = i.parent
                elif i.parent.right == i:
                    i.parent.right = temp
                    i.parent.right.parent = i.parent

                    
                pos.parent.right.parent = pos.parent
                pos.parent.subTreeSequence = []
                pos.parent.subTreeSequence = pos.parent.left.subTreeSequence.copy()
                pos.parent.subTreeSequence.extend(pos.parent.right.subTreeSequence)


                i.parent.subTreeSequence = []
                i.parent.subTreeSequence = i.parent.left.subTreeSequence.copy()
                i.parent.subTreeSequence.extend(i.parent.right.subTreeSequence)
                updateSubSequence(root,i)
                updateSubSequence(root,pos)   
            
        num = -1
        for k in range(len(li_leaves)):
            if li_leaves[k] == i:
                num = k
                break 
        if num == -1:
            print("tell me")
        li_leaves[num] = pos
        li_leaves[count] = i
        count = count + 1

    """i = newLeaves[0]
    pos = li_leaves[0]
    if i != pos:
        if (pos.parent.left) == pos:
            temp = pos
            pos.parent.left = i                   
            if i.parent.left == i:
                i.parent.left = temp
                temp.parent = i.parent#fixing parent

            elif i.parent.right == i:
                i.parent.right = temp
                i.parent.right.parent = i.parent#fixing parent
                        
                    
            pos.parent.left.parent = pos.parent#fixing parent
            pos.parent.subTreeSequence = []
            pos.parent.subTreeSequence = pos.parent.left.subTreeSequence.copy()
            pos.parent.subTreeSequence.extend(pos.parent.right.subTreeSequence)

            i.parent.subTreeSequence = []
            i.parent.subTreeSequence = i.parent.left.subTreeSequence.copy()
            i.parent.subTreeSequence.extend(i.parent.right.subTreeSequence)
            updateSubSequence(root,i)
            updateSubSequence(root,pos)
                
        elif pos.parent.right == pos:
                    
            temp = pos
            pos.parent.right = i
            if i.parent.left == i:
                i.parent.left = temp
                i.parent.left.parent = i.parent
            elif i.parent.right == i:
                i.parent.right = temp
                i.parent.right.parent = i.parent

                    
            pos.parent.right.parent = pos.parent
            pos.parent.subTreeSequence = []
            pos.parent.subTreeSequence = pos.parent.left.subTreeSequence.copy()
            pos.parent.extend(pos.parent.right.subTreeSequence)


            i.parent.subTreeSequence = []
            i.parent.subTreeSequence = i.parent.left.subTreeSequence.copy()
            i.parent.subTreeSeqeuence.extend(pos.parent.right.subTreeSequence)
            updateSubSequence(root,i)
            updateSubSequence(root,pos)"""
        

    
var = ['A','B','C','D','E','F','G','H']

