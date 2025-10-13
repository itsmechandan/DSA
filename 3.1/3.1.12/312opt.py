# concept of xor
def appeareoncexor(arr):
    n = len(arr)
    xorr=0
    for i in range(n):
        xorr = xorr^arr[i]
    return xorr
arr = [1,1,2,3,3,4,4]
print(appeareoncexor(arr))