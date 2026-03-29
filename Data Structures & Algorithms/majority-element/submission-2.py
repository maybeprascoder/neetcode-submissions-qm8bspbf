class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 2 pointer approach
        n = len(nums)
        nums =  sorted(nums)
        return nums[len(nums)//2]
            
                

        