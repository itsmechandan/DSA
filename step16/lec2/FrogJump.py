"""
Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair.
 At a time the frog can climb either one or two steps. A height[N] array is also given. 
 Whenever the frog jumps from a stair i to stair j, the energy consumed in the jump is 
 abs(height[i]- height[j]), where abs() means the absolute difference.
 We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1.

"""


class solution(object):
    def minEnergy(self,arr):
        self.arr = arr
        n = len(arr)
        self.dp = [-1]*n
        return self.cost(n-1)
    def cost(self,index):
        if index == 0:
            return 0
        if self.dp[index] != -1:
            return self.dp[index]
        cost1 = self.cost(index-1) + abs(self.arr[index] - self.arr[index-1])
        cost2 = float('inf')
        if index > 1:
            cost2 = self.cost(index-2)+ abs(self.arr[index]-self.arr[index-2])
        self.dp[index] = min(cost1,cost2)
        return self.dp[index]
    

def Tabulation(arr):
    n = len(arr)
    dp = [0]*n
    dp[0] = 0
    for i in range(1,n):
        left = dp[i-1] + abs(arr[i] - arr[i-1])
        right = float('inf')
        if i>1:
            right = dp[i-2]+ abs(arr[i]-arr[i-2])
        dp[i] = min(left,right)
    return dp[-1]

def SpaceOptimization(arr):
    n= len(arr)
    prev = 0
    prev2 = 0
    for i in range(1,n):
        left = prev + abs(arr[i] - arr[i-1])
        right = float('inf')
        if i>1:
            right = prev2 + abs(arr[i]- arr[i-2])
        curi = min(left,right)
        prev2 = prev
        prev = curi
    return prev

        
arr =[30,10,60,10,60,50]
obj = solution()
print(f"minimum Energy Using Meomiation: {obj.minEnergy(arr)}")

arr2 =[30,10,60,10,60,50]
print(f"Minimum Energy using Tabulation:{Tabulation(arr2)}")

arr3 =[30,10,60,10,60,50]
print(f"After space Optimization in Tabulation: {SpaceOptimization(arr3)}")



