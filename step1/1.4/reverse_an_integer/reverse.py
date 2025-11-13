def reverse_integer(x: int) -> int:
    rev = 0
    sign = -1 if x < 0 else 1
    x = abs(x)

    while x != 0:
        rev = rev * 10 + x % 10
        x //= 10

    rev *= sign

    # Check 32-bit overflow
    if rev < -2**31 or rev > 2**31 - 1:
        return 0

    return rev

if __name__ == "__main__":
    num = int(input("Enter an integer: "))
    print("Reversed integer:", reverse_integer(num))