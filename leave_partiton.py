def leaves_of_partition(li,li_leaves,root): #finds leaves in the cluster
    if root == None:
        return
    if root not in li:
        li_leaves.append(root)
        return

    leaves_of_partition(li, li_leaves, root.left)
    leaves_of_partition(li, li_leaves, root.right)