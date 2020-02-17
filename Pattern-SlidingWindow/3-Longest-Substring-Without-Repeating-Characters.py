class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        winStart = 0
        k=0
        usedChar = {}
        if s is None: return 0
        for winEnd in range(len(s)):
            newChar = s[winEnd]
            if newChar in usedChar:
                winStart = max(winStart, usedChar[newChar] + 1)
            usedChar[s[winEnd]] = winEnd
            k = max(k, winEnd-winStart + 1)
        return k