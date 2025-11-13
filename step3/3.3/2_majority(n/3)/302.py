from collections import Counter
def majority_3_bruteforce(arr):
    n = len(arr)
    counts = Counter(arr)
    for num,counts in counts.items():
        if counts > n/3:
            return num
        
def anotherbruteforce(arr):
    n = len(arr)
    hashmap = {}
    for i in range(n):
        if arr[i] in hashmap:
            hashmap[arr[i]] += 1
        else:
            hashmap[arr[i]]=  1
    for num,count in hashmap.items():
        if count > n /3:
            return num
arr = [3,1,3]
arr2 = [3,1,3]
print(f"brute force: {majority_3_bruteforce(arr)}")
print(f"brute force: {anotherbruteforce(arr2)}")
