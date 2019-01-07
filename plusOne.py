import collections
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if (len(digits) == 0):
            return [1]
        elif (digits[-1] == 9):
            return self.plusOne(disgits[:-1]) + [0]
        else:
            digits[-1] += 1
            return digits
        
abc = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
data = abc.plusOne(nums1)
print(data)