class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = sorted(nums)
        for i in range(0,len(ans)-1):
            if ans[i] == ans[i+1]:
                return True
        return False
        