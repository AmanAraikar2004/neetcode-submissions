class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        l = sorted(list(s))
        print(l)
        count = 0
        d = {}
        n = len(l) - 1
        if len(nums) == 0:
            return 0
        else:
            d[count] = [l[0]]
        for i in range(n):
            if l[i] + 1 == l[i + 1]:
                d[count].append(l[i+1])
            else:
                count += 1
                d[count] = [l[i + 1]]
        longest = max(d.values(), key=len)
        return len(longest)