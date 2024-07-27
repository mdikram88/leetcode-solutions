'''Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.'''

'''Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100'''

def removeElement(nums, val):

  ind = 0
  for i in range(len(nums)):
    if nums[i] != val:
      nums[ind] = nums[i]
      ind += 1
      
  return ind


nums=[0,1,2,2,3,0,4,2]
val = 2

n = removeElement(nums, val)
print(nums[:n])