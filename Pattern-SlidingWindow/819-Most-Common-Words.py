class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banSet = set(banned) # banned words
        words = paragraph.split() # split word
        cnt = dict([])
        maxCnt = 0
        res = ""
        for w in words:
            w = w.lower()
            if w[-1].isalpha() == False:
                w = w[:-1]
            if w not in banSet: # count word not in the banSet
                if cnt.has_key(w) == True:    
                    cnt[w] += 1
                else:
                    cnt[w] = 1
                if maxCnt < cnt[w]: # find max count word
                    maxCnt = cnt[w]
                    res = w 
        return res