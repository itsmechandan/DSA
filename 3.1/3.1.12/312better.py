# Looks like hashmap lets see
def hashingappearence(arr):

    n = len(arr)
    hash = [0]*n
    for i in range(n):
        hash[arr[i]]+=1
    m = len(hash)
    for i in range(m):
        if hash[i]==1:
            return i 
        
def dictionaryapperance(arr2):
    frequency_map={}
    for element in arr2:
        frequency_map[element]=frequency_map.get(element,0)+1
    for key,value in frequency_map.items():
        if value==1:
            return key
        
def findmaximumelement(arr):
    n=len(arr)
    max = 0
    for i in range(n):
        if( arr[i]>max):
            max=arr[i]
    return max

def hashingstriver(arr):
    n = len(arr)
    m = findmaximumelement(arr)+1
    hash = [0]*m
    for i in range(n):
        hash[arr[i]]+=1
    for i in range(m):
        if hash[i]==1:
            return i
arr = [4,1,2,1,2]
print(hashingappearence(arr))
# over here concept of hashing doesnt work cause [0]*n does not apply to all the arrays ( eg: [33,1,2,1,2]) index error would occur
arr2=[33,1,2,1,2]
print(dictionaryapperance(arr2))
# or you could simply just use hashing by defining the size of array as the maximum element +1 
print(hashingstriver(arr2))

