class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        heap = []
        for r in range(len(nums)):
            heapq.heappush(heap, [-nums[r], r])
            l = r - k + 1
            while heap and heap[0][1] < l:
                heapq.heappop(heap)
            if l >= 0:
                result.append(-heap[0][0])
        return result
        