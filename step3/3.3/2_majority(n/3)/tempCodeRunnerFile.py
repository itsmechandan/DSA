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
        
def majorityElement(self, nums):
        
        n = len(nums)
        cnt1 = 0
        element1 = 0
        cnt2 = 0
        element2 = 0
        for i in range(n):
            if cnt1 == 0 and element2 != nums[i]:
                element1 = nums[i]
                cnt1 = 1
            elif cnt2 == 0 and element1 != nums[i]:
                element2 = nums[i]
                cnt2 = 1
            elif nums[i] == element1:
                cnt1 += 1
            elif nums[i] == element2:
                cnt2 += 2
            else:
                cnt1 -= 1
                cnt2 -= 2
        cnt1_ = 0
        cnt2_ = 0
        for i in range(n):
            if nums[i] == element1:
                cnt1_ += 1
            if nums[i] == element2:
                cnt2_ += 1

        ls = []
        mini = int(n/3)+1
        if cnt1_ >= mini:
            ls.append(element1)
        if cnt2_ >= mini:
            ls.append(element2)
        
        return ls
arr = [3,1,3]
arr2 = [3,1,3]
arr3 = [1,1,1,1,2,2,2]
print(f"brute force: {majority_3_bruteforce(arr)}")
print(f"brute force: {anotherbruteforce(arr2)}")
print(f"Optimal: f{majorityElement(arr3)}")
