def bruteforce(arr):
    n = len(arr)
    st = set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k] == 0:
                    temp = [arr[i],arr[j],arr[k]]
                    temp.sort()
                    st.add(tuple(temp)) # set doesn't take in mutable things like list, so had to convert to tuple first.
    ans = [list(i) for i in st]
    return ans

def Better(arr):
    n = len(arr)
    st = set()
    for i in range(n):
        hashset = set()
        for j in range(i+1,n):
            res = -(arr[i]+arr[j])
            if res in hashset:
                temp = [arr[i],arr[j],res]
                temp.sort()
                st.add(tuple(temp))
            hashset.add(arr[j])
    ans = list(st)
    return ans

def Optimal(nums):
    nums.sort()                     # <-- IMPORTANT
    n = len(nums)
    ls = []
        
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
            
        j = i + 1
        k = n - 1
            
        while j < k:
            s = nums[i] + nums[j] + nums[k]
                
            if s < 0:
               
               j += 1
            elif s > 0:
                k -= 1
            else:
                ls.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                    
                    # skip duplicates for j
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                    # skip duplicates for k
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
        
    return ls
        



arr1 = [-1, 0, 1, 2, -1, -4] 
print(f"brute force: {bruteforce(arr1)}")
arr2 = [-1, 0, 1, 2, -1, -4] 
print(f"better method: {Better(arr2)}")
arr3 = [-1, 0, 1, 2, -1, -4] 
print(f"optimal method: {Optimal(arr3)}")