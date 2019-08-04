# Merge sort Implementation
# Average, worst case time complexity is O(nlogn)
# Merge sort is stable sort
from collections import deque

def merge_sort(nums):
    # length 1 이하는 sort된 것으로 가정한다.
    if len(nums) <= 1:
        return nums
    
    mid = int(len(nums) / 2)
    left = merge_sort(nums[0:mid])
    right = merge_sort(nums[mid:len(nums)])

    return merge(left, right)

def merge(left, right):
    results = []
    left = deque(left)
    right = deque(right)
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            results.append(left.popleft())
        else:
            results.append(right.popleft())

    for i in left:
        results.append(i)
    for i in right:
        results.append(i)
    return results

numbers = [110, 2, 1, 4, 5, 10, 8, -1]
merge_results = merge_sort(numbers)
print(merge_results)