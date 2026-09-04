class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        po = []
        ne = []
        res = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                po.append(nums[i])
            else:
                ne.append(nums[i])
        
        for a,b in zip(po,ne):
           res.append(a)
           res.append(b)
        return res