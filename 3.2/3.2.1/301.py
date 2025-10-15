# 2 SUM PROBLEM
def twosum_bruteforce(arr,target):
    n=len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return i,j
    return {-1,-1}

def twosum_Hashmap(arr,target):
    n=len(arr)
    hashmap={0:-1}
    for i in range(n):
        req=target-arr[i]
        if req in hashmap:
            return i, hashmap[req]
        else:
            hashmap[arr[i]]=i 
    return {-1,-1}

def twosum_optimal(arr, target):
    # This version correctly implements the two-pointer logic 
    # but still returns indices of the *sorted* array.
    n = len(arr)
    sort = sorted(arr) # O(N log N)
    l = 0
    r = n - 1
    
    while l < r:
        current_sum = sort[l] + sort[r]
        
        if current_sum < target:
            l += 1 # Move left pointer right to increase sum
        elif current_sum > target:
            r -= 1 # Move right pointer left to decrease sum
        else: # current_sum == target
            # Found the pair in the sorted array
            return l, r # Still returns indices in the *sorted* array
            
    return -1, -1 # Correctly returns a tuple for "not found"


arr=[2,6,5,8,11]
target=14
print(f"Brute force solution {twosum_bruteforce(arr,target)}")
print(f"Hash Map solution {twosum_Hashmap(arr,target)}")
print(f"optimal solution {twosum_optimal(arr,target)}")
target2=15
print(f"Brute force solution {twosum_bruteforce(arr,target2)}")
print(f"Hash Map solution {twosum_Hashmap(arr,target2)}")