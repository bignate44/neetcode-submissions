class Solution:
    def isPalindrome(self, s: str) -> bool:
        newSTR = ""

        for c in s:
            if c.isalnum():
                newSTR += c.lower()
        return newSTR == newSTR[::-1]

        

        