class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        smaller = float("-inf")
        count = 0
        nums = sorted(nums)
        longest = 1

        for i in range(len(nums)):

            if (nums[i]-1 == smaller):
                count+=1
                smaller = nums[i]
            elif (nums[i] != smaller):
                count = 1
                smaller = nums[i]
            longest = max(longest,count)
        return longest




        