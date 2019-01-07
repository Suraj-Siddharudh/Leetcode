import collections
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        print(nums)
        print(nums.index(0))
        while True:
            try:
                ind = nums.index(0)
                # print(sum(nums[ind:])
            except ValueError:
                break
            if (sum(nums[ind:]) != 0):
                nums.remove(0)
                nums.append(0)
            else:
                break
        return

        
abc = Solution()
nums1 = [1,2,0,0,0]
nums2 = [2,2]
data = abc.moveZeroes(nums1)
print(data)
print(nums1)