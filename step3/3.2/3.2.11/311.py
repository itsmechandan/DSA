# Set matrix to Zero (3.2.11)

def convertRow(m,n,arr,i):
    for j in range(m):
        if arr[i][j]!=0:
            arr[i][j]=-1

def convertCol(m,n,arr,j):
    for i in range(n):
        if arr[i][j]!=0:
            arr[i][j]=-1

def BruteForce(arr):
    n = len(arr)
    m = len(arr[0])
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                convertRow(m,n,arr,i)
                convertCol(m,n,arr,j)
    for i in range(n):
        for j in range(m):
            if arr[i][j]==-1:
                arr[i][j]=0
    return arr

def Better(arr):
    n = len(arr)
    m = len(arr[0])
    row = [0]*n
    col = [0]*m
    
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                row[i]=1
                col[j]=1
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                arr[i][j]=0

    return arr

def Optimal(arr):
    n = len(arr)
    m = len(arr[0])
    colx = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                arr[i][0]=0
                if j!=0:
                    arr[0][j]=0
                else:
                    colx=0
    for i in range(1,n):
        for j in range(1,m):
            if arr[0][j]==0 or arr[i][0]==0:
                arr[i][j]=0

    if arr[0][0]==0:
        for j in range(m):
            arr[0][j]=0

    if colx == 0:
        for i in range(n):
            arr[i][0]=0

    return arr

arr1 = [[1,1,1,1],[1,0,1,1],[1,1,0,1],[0,1,1,1]]
arr2 = [[1,1,1,1],[1,0,1,1],[1,1,0,1],[0,1,1,1]]
arr3 = [[1,1,1,1],[1,0,1,1],[1,1,0,1],[0,1,1,1]]
print(f"Brute Force Approach: {BruteForce(arr1)}")
print(f"Better Solution:{Better(arr2)} ")
print(f"optimal solution:{Optimal(arr3)}")
