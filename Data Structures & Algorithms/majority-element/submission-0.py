class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] = count.get(nums[i],0) + 1
            else:
                count[nums[i]] = 0
        res = max(count, key=count.get)
        return res
        