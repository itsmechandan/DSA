def missingnumber(n,arr):
    for i in range(1,n+1):
        flag = 0
        for j in range(n-1):
            if arr[j]==i:
                flag = 1
                break
        if flag == 0:
            return i
        
n = 5
arr=[1,2,4,5]
print(missingnumber(5,arr))