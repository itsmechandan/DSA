# arr1 and arr2 are sorted and we have to find the intersection of both of them. So a corresponding value of arr1 should be 
# present in arr2
def intersection(a,b):
    m=len(a)
    n=len(b)
    vis=n*[0]
    ans = list()
    for i in range(m):
        for j in range(n):
            if a[i]==b[j] and vis[j]==0:
                ans.append(a[i])
                vis[j]=1
                break
            if b[j]>a[i]:
                break
    return ans

arr1 = [1,2,2,3,3,4,5,6]
arr2=[2,3,3,5,6,6,7]
print(intersection(arr1,arr2))

