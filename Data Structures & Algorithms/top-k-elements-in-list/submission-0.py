class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        noof = {}
        for num in nums:
            if num in noof:
                noof[num] = noof.get(num,0) + 1
            else:
                noof[num] = 1
        list1 = []
        while(k):
            res = max(noof, key=noof.get)
            list1.append(res)
            noof.pop(res)
            k-=1

        return list1
        