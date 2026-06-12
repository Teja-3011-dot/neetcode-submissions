class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=len(nums)
        a=len(set(nums))
        res=s-a
        if res>0:
            return True
        return False
