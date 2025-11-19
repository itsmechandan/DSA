def bruteforce(arr):
    n = len(arr)
    st = set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):

                    if arr[i]+arr[j]+arr[k]+arr[l] == 0:
                        temp = [arr[i],arr[j],arr[k],arr[l]]
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
            for k in range(j+1,n):
                res = -(arr[i]+arr[j]+arr[k])
                if res in hashset:
                    temp = [arr[i],arr[j],arr[k],res]
                    temp.sort()
                    st.add(tuple(temp))
                hashset.add(arr[k])
    ans = list(st)
    return ans
def Optimal(nums):
    nums.sort()
    n = len(nums)
    ans = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            
            k = j + 1
            l = n - 1
            
            while k < l:
                s = nums[i] + nums[j] + nums[k] + nums[l]
                
                if s == 0:
                    ans.append([nums[i], nums[j], nums[k], nums[l]])

                    k += 1
                    l -= 1

                    # skip duplicates for k
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1

                    # skip duplicates for l
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1

                elif s < 0:
                    k += 1
                else:
                    l -= 1
    
    return ans

                    
arr = [1,0,-1,0,-2,2]
print(f"brute force: {bruteforce(arr)}")
arr2 = [1,0,-1,0,-2,2]
print(f"Better: {Better(arr2)}")
arr3 = [1,0,-1,0,-2,2]
print(f"Optima: {Optimal(arr3)}")