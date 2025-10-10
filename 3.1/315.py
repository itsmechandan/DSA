# Left Rotate array by one place- Easy most optimal solution

def left_rotate_by_one(arr):
  if not arr:
    return
  first_element = arr[0]
  for i in range(1,len(arr)):
    arr[i-1] = arr[i]
  arr[-1] = first_element

# Example usage:
my_array = [1, 2, 3, 4, 5]
print("Original array:", my_array)
left_rotate_by_one(my_array)
print("Array after left rotation:", my_array)