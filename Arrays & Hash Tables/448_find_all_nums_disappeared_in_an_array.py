class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type : List[int]
        :rtype: List[int]
        """

        for num in nums:  
            idx = abs(num) - 1 
            if nums[idx] > 0:
                nums[idx] = -num[idx]


        res = [] 
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)

        return res 

                
