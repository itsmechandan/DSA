def rearrange_brute(arr):
    n=len(arr)
    pos=[]
    neg=[]
    for i in range(n):
        if arr[i]>0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    for i in range(len(pos)):
        arr[2*i]=pos[i]

    for i in range(len(neg)):
        arr[2*i+1]=neg[i]
    return arr

def optimal(arr):
    n=len(arr)
    p= 0
    n= 1
    for i in range(n):
        if arr[i]>0:
            arr[p]=arr[i]
            p=p+2
        if arr[i]<0:
            arr[n]=arr[i]
            n=n+2
    return arr

arr=[1,2,-3,-1,-2,3]
print(f"brute force: {rearrange_brute(arr)}")
print(f"optimal:{optimal(arr)}")

