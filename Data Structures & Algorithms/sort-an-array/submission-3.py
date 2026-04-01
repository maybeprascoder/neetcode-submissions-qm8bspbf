class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def partition(l, h):
            mid = (l + h) // 2
            nums[l], nums[mid] = nums[mid], nums[l]

            pivot = nums[l]   # __define-ocg__
            i = l
            j = h

            while i < j:
                while i <= h - 1 and nums[i] <= pivot:
                    i += 1
                while j >= l + 1 and nums[j] > pivot:
                    j -= 1

                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]

            nums[l], nums[j] = nums[j], nums[l]
            return j

        def Quicksort(l, h):
            if l < h:
                p = partition(l, h)
                Quicksort(l, p - 1)
                Quicksort(p + 1, h)

        Quicksort(0, len(nums) - 1)
        return nums