class BurrowsWheelerTransform:

    def BurrowsWheelerTransform(self, s, SA):
        m = len(s)
        BWT = [0 for i in range(0, m)]
        BWT[0] = s[m-2]
        for i in range(1,m):
            BWT[i] = s[SA[i]-1]

        print("Burrows Wheeler Transform",BWT)
        print()

        return BWT


    def Occ(self, tree, i, c):
        return tree.Rank(c,i)


    def BackwardSearch(self, tree, P, BWT, C):
        i = len(P) - 1
        sp = 1
        ep = len(BWT)

        while(sp <= ep and i >= 0):
            c = P[i]
            sp = C[c] + self.Occ(tree, sp - 1 , c) + 1
            ep = C[c] + self.Occ(tree, ep, c)
            i -= 1
            # print(sp, ep)
        if(ep < sp):
            return [-1,-1]
        else:
            return [sp,ep]


    def Exrecur(self,W, i, k, l, C, tree1):
        if i < 0:
            return [k, l]
        if k <= l:
            # print(k,l)
            k = C[W[i]] + self.Occ(tree1, k-1, W[i]) + 1
            l = C[W[i]] + self.Occ(tree1, l, W[i])
        return self.Exrecur(W, i-1, k, l, C, tree1)


    def InexRecur(self,W, i, z, k, l, C, tree1, Σ, I):

        if z < 0:
            return {}
        if i < 0:
            return {(k, l)}

        I = I.union(self.InexRecur(W, i-1, z - 1, k, l, C, tree1, Σ, I))
        K = k
        L = l
        for char in Σ:
            k = C[char] + self.Occ(tree1, K-1, char) + 1
            l = C[char] + self.Occ(tree1, L, char)
            if (k <= l):
                I = I.union(self.InexRecur(W, i, z - 1, k, l, C, tree1, Σ, I))
                if char == W[i]:
                    I = I.union(self.InexRecur(W, i-1, z, k, l, C, tree1, Σ, I))
                else:
                    I = I.union(self.InexRecur(W, i-1, z-1, k, l, C, tree1, Σ, I))

        return I


    def InexRecurwithD(self,W, i, z, k, l, C, tree1, Σ, I, D):
        if z < D[i]:
            return {}
        if i < 0:
            return {(k, l)}

        I = I.union(self.InexRecurwithD(W, i-1, z - 1, k, l, C, tree1, Σ, I, D))
        K = k
        L = l
        for char in Σ:
            k = C[char] + self.Occ(tree1, K-1, char) + 1
            l = C[char] + self.Occ(tree1, L, char)
            if (k <= l):
                I = I.union(self.InexRecurwithD(W, i, z - 1, k, l, C, tree1, Σ, I, D))
                if char == W[i]:
                    I = I.union(self.InexRecurwithD(W, i-1, z, k, l, C, tree1, Σ, I, D))
                else:
                    I = I.union(self.InexRecurwithD(W, i-1, z-1, k, l, C, tree1, Σ, I, D))

        return I

    def calculateDwithreverse(self,s,W,C,tree):
        k = 1
        l = len(s) - 1
        z = 0
        D = []
        for i in range(0, len(W)):
            k = C[W[i]] + self.Occ(tree, k-1, W[i]) + 1
            l = C[W[i]] + self.Occ(tree, l, W[i])
            if(k > l):
                k = 1
                l = len(s) - 1
                z += 1
            D.append(z)
        return D

    def calculateD(self,s,W):
        z = 0
        j = 0
        D = []
        for i in range(0, len(W)):
            if(W[j:i+1] not in s):
                z += 1
                j = i + 1
            D.append(z)
        return D


    def inexactSearchwithoutD(self,I,s,W,C,tree1,z, Σ):
        print("Exact search with recursive Search", self.Exrecur(W, len(W)-1, 1, len(s), C, tree1))
        print()
        I = set([])
        I = self.InexRecur(W, len(W)-1, z, 1, len(s), C, tree1, Σ, I)
        return I

    def inexactSearch(self,I,s,W,C,tree1,z, Σ):
        D = self.calculateD(s,W)
        print("D",D)
        print()
        I = self.InexRecurwithD(W, len(W)-1, z, 1, len(s), C, tree1, Σ, I, D)
        return I

    def inexactSearchwithreverse(self,I,s,W,C,tree1,tree2,z, Σ):
        D = self.calculateDwithreverse(s,W,C,tree2)
        print("D", D)
        print()
        I = self.InexRecurwithD(W, len(W)-1, z, 1, len(s), C, tree1, Σ, I, D)
        return I
