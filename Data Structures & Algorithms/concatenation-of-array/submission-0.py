class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans1 = []
        ans2 = []
        for i in range(len(nums)):
            ans1.append(nums[i])
            ans2.append(nums[i])
        ans =  ans1 + ans2
        return ans
        

        