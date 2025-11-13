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
    hashmap={}
    for i in range(n):
        req=target-arr[i]
        if req in hashmap:
            return i, hashmap[req]
        else:
            hashmap[arr[i]]=i 
    return {-1,-1}

def twosum_optimal(arr, target):
    n = len(arr)
    nums = [(nums,i)for i,nums in enumerate(arr)]
    nums.sort() # O(N log N)
    l = 0
    r = n - 1
    
    while l < r:
        current_sum = nums[l][0] + nums[r][0]
        
        if current_sum < target:
            l += 1 
        elif current_sum > target:
            r -= 1 
        else: 
    
            return nums[l][1], nums[r][1] 
            
    return -1, -1 


arr=[2,6,5,8,11]
target=14
print(f"Brute force solution {twosum_bruteforce(arr,target)}")
print(f"Hash Map solution {twosum_Hashmap(arr,target)}")
print(f"optimal solution {twosum_optimal(arr,target)}")
target2=15
print(f"Brute force solution {twosum_bruteforce(arr,target2)}")
print(f"Hash Map solution {twosum_Hashmap(arr,target2)}")