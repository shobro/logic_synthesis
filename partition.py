def nodes_of_partition(root, op, li):  #find cluster of comman operators

    if root == None or root.left == None or root.right == None:
        return
    if root.variable != root.left.variable and root.right.variable != root.variable:
        return     #if cluster is not being formed
    
    
    if root.variable == root.left.variable:
        li.append(root.left)
        nodes_of_partition(root.left,op,li) #if cluster go deep to find more cluster
    if root.variable == root.right.variable:
        li.append(root.right)
        nodes_of_partition(root.right,op,li)