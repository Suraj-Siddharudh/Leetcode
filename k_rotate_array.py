class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """
        print(k% len(nums))
        for iter in range(k % len(nums)):
            nums.insert(0, nums.pop())
        """
        # assert k >= 0
        """
        if len(nums) != 0: 
            
            k = k % len(nums)
            
            nums[:] = reversed(nums)
            print(nums)
            nums[:k] = reversed(nums[:k])
            print(nums)
            nums[k:] = reversed(nums[k:])
        """
        if k != 0:
            l = len(nums)
            k = k % l
            print(nums[l-k:])
            print(nums[:l-k])
            nums[:] = nums[l-k:] + nums[:l-k]
        print(nums)


obj = Solution()
obj.rotate([1,2,3,5,6,8,-1], 31)