from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : 
            return False 
        freq_s = Counter(s)
        freq_t = Counter(t)
        for ch in freq_s : 
            if ch not in freq_t : 
                return False 
            if freq_s[ch] != freq_t[ch] : 
                return False 
        return True 
        