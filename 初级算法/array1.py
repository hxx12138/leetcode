# 删除有序数组中存在的重复值
def remove(List):
    count = 0
    i = 0
    while i < len(List)-1:
        i -= count
        count = 0
        while i+1<len(List) and len(List)!=1 and List[i+1] == List[i]:
            List.pop(i)
            count += 1
        i += 1

# 题解 双指针法
class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow


nums = [0,0,1,1,1,2,2,3,3,4]
print(nums)
#remove(nums)  # 自己做法
s = Solution()
s.removeDuplicates(nums) # 题解做法
print(nums)