class Solution:
    def KMPsearch(self, string, pattern):
        lps = self.createLPS(pattern)
        i = 0 # index in string
        j = 0 # index in pattern

        while(i < len(string)):
            if(string[i] == pattern[j]):
                i += 1
                j += 1
            else:
                if(j == 0):
                    i += 1
                else:
                    j = lps[j-1]
            
            if(j == len(pattern)):
                return True
        return False
        
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

    def changeChar(self, i, string, new_char):
        string = list(string)
        string[i] = new_char
        return "".join(string)

    def traverseAllPossibleStrings(self, i, s1, s2, evil):
        if(i >= n):
            return 0
        if(self.KMPsearch(s1, evil)):
            return 0
        
        s = s1
        int1 = ord(s1[i])
        int2 = ord(s2[i])

        for char_int in range(int1, int2 + 1):
            s = self.changeChar(i, s, chr(char_int))
            self.traverseAllPossibleStrings(i+1, s, s2, evil)
            print(s)
        print("done")
            
    def findGoodStrings(self, n, s1, s2, evil):
        self.traverseAllPossibleStrings(0, s1, s2, evil)

sol = Solution()

s1 = "helloa"
s2 = "helloz"
n = len(s1)
evil = "hello"
sol.findGoodStrings(n, s1, s2, evil)