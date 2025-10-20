def brute(arr):
    n=len(arr)
    pos=[]
    neg=[]
    for i in range(n):
        if arr[i]>0:
            pos.append(arr[i])
        else: 
            neg.append(arr[i])
    p=len(pos)
    x=len(neg)

    if p==x:
        for i in range(p):
            arr[2*i]=pos[i]
        for i in range(x):
            arr[2*i+1]=neg[i]
    
    if p>x:
        for i in range(x):
            arr[2*i]=pos[i]
        for i in range(x):
            arr[2*i+1]=neg[i]
    
    if p<x:
        for i in range(p):
            arr[2*i]=pos[i]
        for i in range(p):
            arr[2*i+1]=neg[i]

    return arr

arr=[1,2,-4,-5,3,4]
arr2=[1,2,-3,-1,-2,3]
arr3=[1,2,-4,-3,-5,-6]
print(f" brute force: {brute(arr)}")
print(f" brute force: {brute(arr2)}")
print(f" brute force: {brute(arr3)}")

