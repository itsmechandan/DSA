def reverse_subarray(arr, start, end):
    """
    Helper function to reverse a portion of the array in-place.
    The reversal happens between indices 'start' and 'end' (inclusive).
    """
    while start < end:
        # Swap the elements
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def leftRotate_optimal(arr, d):
    """
    Left-rotates an array (list) by 'd' steps using the Reversal Algorithm.

    Time Complexity: O(N)
    Space Complexity: O(1) (Auxiliary)

    Args:
        arr (list): The array to be rotated.
        d (int): The number of steps to rotate left.
    """
    n = len(arr)

    # Normalize 'd' to be within the array bounds
    d = d % n
    if d == 0 or n <= 1:
        return arr

    # Step 1: Reverse the first 'd' elements (0 to d-1)
    # The pseudo code was: reverse(0, d)
    reverse_subarray(arr, 0, d - 1)
    # Example: [1, 2, 3, 4, 5, 6, 7], d=3 -> [3, 2, 1, 4, 5, 6, 7]

    # Step 2: Reverse the remaining 'n-d' elements (d to n-1)
    # The pseudo code was: reverse(d, n)
    reverse_subarray(arr, d, n - 1)
    # Example: [3, 2, 1, 4, 5, 6, 7] -> [3, 2, 1, 7, 6, 5, 4]

    # Step 3: Reverse the whole array (0 to n-1)
    reverse_subarray(arr, 0, n - 1)
    # Example: [3, 2, 1, 7, 6, 5, 4] -> [4, 5, 6, 7, 1, 2, 3]

    return arr

# --- Example Usage ---
my_array = [1, 2, 3, 4, 5, 6, 7]
steps = 3
print(f"Original Array: {my_array}")

# We use a copy since the function modifies the list in-place
rotated_array = leftRotate_optimal(my_array.copy(), steps)
print(f"Array after {steps} left rotations (Reversal Algorithm): {rotated_array}")