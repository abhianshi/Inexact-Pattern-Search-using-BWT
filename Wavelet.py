import math

# Wavelet Tree
class Wavelet:

    # Initialization
    def __init__(self):
        self.S = ""
        self.Σ = []
        self.LeftNode = None
        self.RightNode = None
        self.Bitmap =[]

    # Tree Construction
    def ConstructNode(self, S, Σ):
        # String
        self.S = S

        # Unique characters in String S
        self.Σ = Σ

        # Temporary fields for left and right subsequences
        Sleft = []
        Sright = []

        # Return if the subsequence contains only one type of character
        if(len(Σ) == 1 or len(S) == 1):
            return self

        # Sort the unique characters
        Σ.sort()

        # Get the character where splitting is to be done
        splitChar = Σ[math.ceil(len(Σ) / 2) - 1]

        # Save the bitmap for this sequence
        for i in range(0,len(S)):
            if(S[i] <= splitChar):
                Sleft.append(S[i])
                self.Bitmap.append(0)
            else:
                Sright.append(S[i])
                self.Bitmap.append(1)

        # Left and Right child of this sequence
        self.LeftNode = Wavelet().ConstructNode(''.join(Sleft), list(set(Sleft)))
        self.RightNode = Wavelet().ConstructNode(''.join(Sright), list(set(Sright)))

        return self

    # Check if the sequence is at tree's leaf
    def IsLeaf(self):
        return (self.LeftNode == None and self.RightNode == None)


    # Compute the rank of character c in the sequence[1:p]
    def Rank(self,c, p):

        # Return p if it is a leaf node
        if (self.IsLeaf()):
            return p

        # Extract the bit of the character c in the sequence
        if(c <= self.Σ[math.ceil(len(self.Σ) / 2) - 1]):
            CharBit = 0
        else:
            CharBit = 1

        # Count the number of occurences of bit representing the character
        o = 0
        for i in range(0,p):
            if(self.Bitmap[i] == CharBit):
                o += 1

        # Go further down the tree to compute the number of occurences of character
        if(CharBit == 1):
            if(self.RightNode == None):
                return o
            rank = self.RightNode.Rank(c, o)
        else:
            if(self.LeftNode == None):
                return o
            rank = self.LeftNode.Rank(c, o)

        return rank
