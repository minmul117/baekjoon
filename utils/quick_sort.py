import random

def quicksort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)
        quicksort(nums, low, p - 1)
        quicksort(nums, p + 1, high)

def partition(nums, low, high):
    pivot = nums[high]
    j = low
    for i in range(low, high, 1):
        if nums[i] < pivot:
            nums[low], nums[i] = nums[i], nums[low]
            j += 1
    nums[j], nums[high] = nums[high], nums[j]
    return j

a = [3, 4, 1, 2, 9, 5, 0, 22, 15]
quicksort(a, 0, len(a) - 1)
print(a)