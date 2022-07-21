
def printTree(root, filePointer):
    if root == None:
        return
    filePointer.write("(") 
    printTree(root.left,filePointer)
    if root.notOp == "!":
        filePointer.write("!")
    filePointer.write (root.variable)
    printTree(root.right,filePointer)
    filePointer.write(")")

def verilogWriter(lutNo,eqnNo,root):
    fileName = "fileVerilog" + str(eqnNo)+".v"
    fileWithOptimizedLut = "lut.txt"
    file = open(fileName,"w")
    fileOne = open(fileWithOptimizedLut,"a")
    fileOne.write(str(lutNo))
    fileOne.write("\n")
    file.write("module Equation(A,B,C,D,E,F,G,H,out);\n")
    file.write("    input A,B,C,D,E,F,G,H;\n")
    file.write("    output out;\n")
    file.write("    assign out = ")
    printTree(root,file)
    file.write(";\n")
    file.write("end module")
    


    
