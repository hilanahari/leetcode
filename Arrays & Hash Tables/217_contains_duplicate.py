class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        seen_nums = set()

        for num in nums:
            if num in seen_nums:
                return True
            else:
                seen_nums.add(num)

        return False

        

        