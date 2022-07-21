def return_lut_no(lines,found):
    flag = 0
    no= ""
    j = 0
    for i in lines:
        if i.isnumeric() == True:
            no = no+i
            flag = 1
        elif flag == 1 and i.isnumeric() == False:
            break 
    return int(no)


def file_analyzer(n):
    for i in range(n):
        fileName = "resultFile" + str(i) + ".v"
        file = open("fileName","r")
        lut = []
        for lines in file:
            if lines.find("assign") != -1:
                lut.append(return_lut_no(lines,lines.find("assign")))
        return lut[len(lut)-1] - lut[1] + 2
