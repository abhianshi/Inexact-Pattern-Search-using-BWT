import SuffixArray
import Wavelet
import LongestCommonPrefix
import BurrowsWheelerTransform
import MergeIntervals
import timeit


s = "MISSISSIPPI"
P = "IPPI"

s = "GOOGOL"
P = "GOL"

s = "IamAbhianshuSingla"
P = "Abhi"

s = "PANAMABANANAS"
P = "ANA"

s = "TTAACGTTTATTACGTTTAAGTTTAACCTT"
P = "AACG"

s = "A book is both a usually portable physical object and the body of immaterial representations or intellectual object whose material signs—written or drawn lines or other two-dimensional media—the physical object contains or houses. As a physical object, a book is a stack of usually rectangular pages (made of papyrus, parchment, vellum, or paper) oriented with one longer side (either left or right, depending on the direction in which one reads a script) tied, sewn, or otherwise fixed together and then bound to the flexible spine of a protective cover of heavier, relatively inflexible material so that, when the opened front cover has received a massy enough stack of sheets, the book can lie flat.[1] The technical term for this physical arrangement is codex (in the plural, codices). In the history of hand-held physical supports for extended written compositions or records, the codex replaces its immediate predecessor, the scroll. As an intellectual object, a book is prototypically a composition of such great length that it takes a considerable investment of time to compose and a still considerable, though not so extensive, investment of time to read. This sense of book has a restricted and an unrestricted sense. "
P = "book"

s = "GOOGOL"
P = "GOL"

s = ''.join(e for e in s if e.isalpha())
# s = s.lower()
s += '$'

print("Original String",s)
print()

sa = SuffixArray.SuffixArray()
SA, C = sa.createArray(s)
R = sa.Inverse(SA)

lcp = LongestCommonPrefix.LongestCommonPrefix()
LCP = lcp.LongestCommonPrefix(s,SA,R)

bwt = BurrowsWheelerTransform.BurrowsWheelerTransform()
BWT = bwt.BurrowsWheelerTransform(s, SA)


Σ = list(set(BWT))
w = Wavelet.Wavelet()
tree1 = w.ConstructNode(''.join(BWT),Σ)
# print(tree1.S)
# print(tree1.Bitmap)
# print(tree1.LeftNode.S)
# print(tree1.LeftNode.Bitmap)
# print(tree1.RightNode.S)
# print(tree1.RightNode.Bitmap)
# print(tree1.LeftNode.LeftNode.S)
# print(tree1.LeftNode.LeftNode.Bitmap)
# print(tree1.LeftNode.RightNode.S)
# print(tree1.LeftNode.RightNode.Bitmap)
# print(tree1.RightNode.LeftNode.S)
# print(tree1.RightNode.LeftNode.Bitmap)
# print(tree1.RightNode.RightNode.S)
# print(tree1.RightNode.RightNode.Bitmap)

[sp,ep] = bwt.BackwardSearch(tree1, P, BWT, C)
print("Backward Search", sp,ep)
print()

if(sp != -1):
    print("In original string, pattern is at position ", end = " ")
    for i in range(sp-1,ep):
        print(SA[i]+1, end = " ")
else:
    print("No exact matching of string ", P, "in", s)
print()
print()

z = 1
I = set([])
mergeI = MergeIntervals.MergeIntervals()

start = timeit.default_timer()
I = bwt.inexactSearchwithoutD(I,s,P,C,tree1,z,Σ)
stop = timeit.default_timer()
I = mergeI.merge(I)
print("Without D", I)
print()
print('Time: ', stop - start, 'seconds')
print()

I = set([])
start = timeit.default_timer()
I = bwt.inexactSearch(I,s,P,C,tree1,z,Σ)
stop = timeit.default_timer()
I = mergeI.merge(I)
print("With D", I)
print()
print('Time: ', stop - start, 'seconds')
print()
print("Length of String", len(s))
print()

print("In original string, approximate pattern search is at position ",SA[sp-1]-z+1, end = " ")
for i in I:
    sp = i[0]
    ep = i[1]
    for i in range(sp-1,ep):
        print(SA[i]+1, end = " ")

print()
print()

# print("Reverse the String and compute BWT on the reverse String")
# s_ = s[len(s)-2::-1]
# s_ += '$'
# print("Inverse String", s_)
# print()
#
# SA_, C = sa.createArray(s_)
# R_ = sa.Inverse(SA_)
# # LCP_ = lcp.LongestCommonPrefix(s_,SA_,R_)
#
# BWT_ = bwt.BurrowsWheelerTransform(s_, SA_)
# tree2 = w.ConstructNode(''.join(BWT_),Σ)
#
# [sp_,ep_] = bwt.BackwardSearch(tree2, P, BWT_, C)
# I = set([])
# I = bwt.inexactSearchwithreverse(I,s,P,C,tree1, tree2,z,Σ)
# I = mergeI.merge(I)
# print("With reverse string", I)
# print()
