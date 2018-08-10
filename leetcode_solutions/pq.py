from queue import PriorityQueue
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        q = PriorityQueue()
        for i in nums:
            q.put(i)
            if q.qsize()>k:
                q.get()
        return q.get()

sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 2))
