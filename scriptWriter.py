def scriptWriter(n):
    for i in range(n):
        file = open("script.scr","a")
        fileRead = "fileVerilog" + str(i) + ".v"
        string = "read "+fileRead+"\n"
        file.write(string)
        string = "if -K 3\n"
        fileWrite = "write resultFile" + str(i) + ".v\n"
        file.write(fileWrite)