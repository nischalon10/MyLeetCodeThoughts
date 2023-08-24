class Solution:
    def isPalindrome(self, s: str) -> bool:
        fwd = ''.join(c for c in s.lower() if c.isalnum())
        bck = fwd[::-1]
        return fwd == bck