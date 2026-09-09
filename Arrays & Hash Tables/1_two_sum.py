class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        
        ids_map = {}

        for i, num1 in enumerate(nums):
            num2 = target - num1 

            if num2 in ids_map:
                return [ids_map[num1] ,i]

            else:
                ids_map[num1] = i