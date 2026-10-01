import re

class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""
        for s in strs:
            r += f"{s}|-|"
        return r

    def decode(self, s: str) -> List[str]:
        return re.split(r"\|-\|", s)[:-1]
