def chandan(a):
    n = len(a)
    x= []
    for i in range(n):
        if i==n-1:
            x.append(a[i])
            break
        j=1+1
        while j<n:
            if j ==n-1 & a[i]>a[j]:
                x.append(a[i])
                break
            if a[j]>a[i]:
                break
            else:
                j=j+1
    return x

def optimal(a):
    n= len(a)
    leader=[]
    maxi=-1
    for i in range(n-1,-1,-1):
        if a[i]>maxi:
            leader.append(a[i])
            maxi = a[i]

    return leader
arr = [10,22,12,3,0,6]
print(f"chandan's solution: {chandan(arr)}")
print(f"optimal solution: {optimal(arr)}")
