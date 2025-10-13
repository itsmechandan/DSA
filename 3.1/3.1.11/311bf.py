def consecutivezeroes(arr):
    maxcount=0
    count = 0
    n = len(arr)
    for i in range(n):
        if arr[i]==1:
            count =count+1
            if(count>maxcount):
                maxcount=count
        if arr[i]==0:
            count = 0
    return maxcount
arr = [1,1,0,1,1,1,1,0,1]
print(consecutivezeroes(arr))