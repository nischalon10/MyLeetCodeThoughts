class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dist = []
        for i in nums:
            if i in dist:
                return True
            dist += [i]
        return False
            
            