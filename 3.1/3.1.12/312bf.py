def onceapperancebruteforce(arr):
    n = len(arr)
    for i in range(n):
        num = arr[i]
        count = 0
        for j in range(n):
            if arr[j]==num:
                count +=1
        if (count ==1):
            return num
arr = [1,1,2,3,3,4,4]
print(onceapperancebruteforce(arr))