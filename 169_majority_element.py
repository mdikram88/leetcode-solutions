'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.'''

'''Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109'''

def majorityElement(nums):
    nums.sort()
    mid = len(nums) // 2
    return nums[mid]
  
nums=[0,1,2,2,2,3,3,3,3, 3,3,0,4]

n = majorityElement(nums)
print(n)