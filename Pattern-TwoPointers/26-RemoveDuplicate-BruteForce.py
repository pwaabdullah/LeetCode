class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None: return 0
        limit = len(nums)
        for i in range(limit-1):
            j = i+1
            while(j<limit):
                if (nums[i] == nums[j]):
                    nums.remove(nums[j])
                    limit = len(nums)
                    j-=1
                j+=1
        return limit