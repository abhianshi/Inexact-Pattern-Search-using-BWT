class LongestCommonPrefix:
    def characterComparison(self, s1, s2):
        i = 0
        end = min(len(s1), len(s2))
        while(i < end and s1[i] == s2[i]):
            i += 1
        return i


    # s is the String, SA is the suffix Array and R is the inverse of the SA
    def LongestCommonPrefix(self, s, SA, R):
        m = len(s)
        LCP = [0 for i in range(0, m)]

        # First comparison
        LCP[R[0]] = self.characterComparison(s[0:m], s[SA[R[0]+1]:m])
        l = LCP[R[0]]

        for i in range(1,m-1):
            if(l == 0 and (R[i]+1) < m):
                LCP[R[i]] = self.characterComparison(s[i:m],s[SA[R[i]+1]:m])
                l = LCP[R[i]]
            else:
                LCP[R[i]] = l-1
                l = max(l-1,0)
                if(i+l < m and R[i]+1 < m and SA[R[i]+1]+l < m):
                    LCP[R[i]] += self.characterComparison(s[i+l:m],s[SA[R[i]+1]+l:m])
                    l = LCP[R[i]]

        print("Longest Common Prefix",LCP)
        print()

        return LCP
