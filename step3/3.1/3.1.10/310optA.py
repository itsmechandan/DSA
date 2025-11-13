def missingnumber(n,arr):
    sum = (n*(n+1))/2
    s2=0
    for i in arr:
        s2=s2+i
    return sum-s2
n = 5
arr=[1,2,4,5]
print(missingnumber(5,arr))
