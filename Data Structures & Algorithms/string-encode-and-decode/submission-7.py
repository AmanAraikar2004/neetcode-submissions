import re

class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""
        for s in strs:
            r = r + "@" + str(len(s)) + "$" + s
        return r

    def decode(self, s: str) -> List[str]:
        return re.split(r"\@[0-9]+\$", s)[1:]
