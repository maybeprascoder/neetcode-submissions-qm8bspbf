class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort
        noof = {}
        for num in nums:
            noof[num] = noof.get(num,0) + 1
        list1 = []
        buckets = [[] for _ in range(len(nums)+1)]
        for num,freq in noof.items():
            buckets[freq].append(num)
        
        for freq in range(len(buckets)-1,0,-1):
            for num in buckets[freq]:
                list1.append(num)
                k-=1
                if k==0:
                    return list1

        return list1

        