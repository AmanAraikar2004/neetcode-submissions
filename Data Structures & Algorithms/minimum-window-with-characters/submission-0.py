from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()
        left, right = 0, 0
        have = 0
        required = len(need)
        best_length = float("inf")
        best_left = 0
        best_right = 0
        while right < len(s):
            window[s[right]] += 1
            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1
            right += 1
            while have == required:
                if right - left < best_length:
                    best_length = right - left
                    best_left = left
                    best_right = right

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        return s[best_left: best_right]