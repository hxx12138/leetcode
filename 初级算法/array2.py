# 自己做法
class Solution:
    def maxProfit(self, prices):
        i = 0 
        ans = 0
        while i <len(prices)-1:
            while i <len(prices)-1 and prices[i+1]>prices[i]:
                ans += prices[i+1] - prices[i]
                i += 1
            else:
                i += 1
        return ans

s = Solution()
#prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]
ans = s.maxProfit(prices)
print(ans)
                