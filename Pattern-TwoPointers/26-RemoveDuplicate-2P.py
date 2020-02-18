class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None: return 0
        p = 1
        while(p<len(nums)):
            if (nums[p-1] == nums[p]):
                nums.remove(nums[p])
                p-=1
            p+=1
        return len(nums)