class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        print(len(prices))
        arr = [0] * len(prices)
        for i in range(1, len(prices)):
            print("i = ", i)
            if(prices[i]> prices[i-1]):
                for j in range(0, i):
                    print("j = ", j)
                    if(prices[i] > prices[j]):
                        value = prices[i] - prices[j]
                        arr[i] = max(value, arr[i])
        print(arr)

obj = Solution()
obj.maxProfit(