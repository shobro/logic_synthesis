from driver import *

def otherDriver(root,superRoot):
    if root == None or root.left == None or root.right == None:
        return
    driver(root,superRoot)
    otherDriver(root.left,superRoot)
    otherDriver(root.right,superRoot)
    return
