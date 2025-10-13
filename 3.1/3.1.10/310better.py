# Concept of hashing
def findmissing(n,arr):
    hash = [0]*(n+1)
    for i in hash:
        hash[arr[i]] = 1
    for i in range(1,n+1):
        if hash[i]==0:
            return i 
n=5
arr=[1,2,4,5]
print(findmissing(n,arr))