from functools import lru_cache 

class Solution:
    # LPS (longest prefix-suffix) creates and array
    # that keeps track of the longest proper prefix which is also suffix
    # in the string
    def createLPS(self, pattern):
        m = len(pattern)
        lps = [ 0 for _ in range(m)]
        i = 0
        j = 1
        while j < m:
            if(pattern[i] == pattern[j]):
                i += 1
                lps[j] = i
                j += 1
            else:
                if(i == 0):
                    lps[j] = 0
                    j += 1
                else:
                    i = lps[i - 1]
        return lps

    # def kmp(l, c):
    #        while l and evil[l] != c: l = f[l-1]
    #        if evil[l] == c : l += 1
    #        return l
    #    
    #    f = [0] * len(evil) 
    #    for i in range(1, len(evil)):
    #        f[i] = kmp(f[i-1], evil[i])
        
    def findGoodStrings(self, n, s1, s2, evil):
        lps = self.createLPS(evil)
        print("done")

        # DP using Digit DP
        # i is the current index of the string we're building
        # evilLen is the current length of matched with evil in a substring
        # f1 = the word we are building has already become bigger than s1? [0 = no, 1 = yes]
        # f2 = the word we are building has already become smaller than s2? [0 = no, 1 = yes]
        @lru_cache(None)
        def dp(i, evilLen, f1, f2):
            if(evilLen == len(evil)):
                return 0
            if(i == n):
                return 1
            start = 'a' if f1 else s1[i]
            finish = 'z' if f2 else s2[i]
            ans = 0
            for c_int in range(ord(start), ord(finish)+1):
                c = chr(c_int)
                new_f1 = f1 or c_int > ord(s1[i])
                new_f2 = f2 or c_int < ord(s2[i])

                # KMP Substring Search
                j = evilLen
                while(j != 0 and evil[j] != c):
                    j = lps[j-1]
                if(evil[j] == c):
                    j += 1
                
                ans += dp(i+1, j, new_f1, new_f2)
                ans %= (10**9 + 7)
            return ans

        return dp(0, 0, False, False) 

sol = Solution()

s1 = "pzdanyao"
s2 = "wgpmtywi"
n = len(s1)
evil = "sdka"

