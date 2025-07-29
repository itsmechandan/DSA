def countdigits(n):

    count = 0
    while(n>0):
        n = n//10
        count = count +1
    return count
n = int(input("Value enter please"))
print("Number of digits",countdigits(n))
