def move_zeros(nums):
    return sorted(nums, key=lambda x: x == 0)

# Test cases
nums1 = [0, 1, 0, 3, 12]
result = move_zeros(nums1)
print(result)  # Output: [1, 3, 12, 0, 0]

nums2 = [0, 0, 1, 0, 2, 3]
result = move_zeros(nums2)
print(result)  # Output: [1, 2, 3, 0, 0, 0]
