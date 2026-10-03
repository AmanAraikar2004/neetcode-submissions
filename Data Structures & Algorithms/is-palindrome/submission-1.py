import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]", '', s)
        print(s)
        k = s.lower()
        print(k)
        print(k[::-1])
        if k[::-1] == k:
            return True
        return False