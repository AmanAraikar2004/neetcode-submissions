class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        l = 0
        result.append(-heap[0][0])
        for r in range(k, len(nums)):
            heapq.heappush(heap, (-nums[r], r))
            l += 1
            while heap[0][1] < l:
                heapq.heappop(heap)
            result.append(-heap[0][0])
        return result
        