def returnK(arr,var):
    count = 0
    for i in range(len(var)):
        if arr.count(var[i]) > 0:
            count = count+1
    return count

def returnY(root):
    

