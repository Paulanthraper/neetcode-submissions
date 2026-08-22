class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        copy = nums[:]   # make a shallow copy
        for i in nums:
            copy.remove(i)
            if i in copy:
                return True
        return False



            
        