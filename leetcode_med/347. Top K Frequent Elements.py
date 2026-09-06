import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freq_map = {} 

        for num in nums: 
            if num not in freq_map:
                freq_map[num] = 1

            else:
                 freq_map[num] += 1


        heap = []

        for num,count in freq_map.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)


        return [num for count, num in heap]







                        
 


