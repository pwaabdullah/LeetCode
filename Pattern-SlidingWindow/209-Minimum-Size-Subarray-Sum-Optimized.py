class Solution(object):
    def minSubArrayLen(self, s, arr):
        winStart,winEnd, winSum = 0,0,0
        k = float("inf")
        for winEnd in range(len(arr)):
            winSum+=arr[winEnd]
            while(winSum>=s):
                k = min(k, winEnd-winStart+1)
                winSum-=arr[winStart]
                winStart+=1
        if k == float("inf"): return 0
        else: return k