import collections
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        data = collections.Counter(nums1)
        for elem in nums2:
            count = data[elem]
            if count > 0:
                result.append(elem)
                data[elem] = count -1
        return result
        
abc = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
data = abc.intersect(nums1, nums2)
print(data)