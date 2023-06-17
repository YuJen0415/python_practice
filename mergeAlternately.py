word1 = "abcd"
word2 = "pq"

l1 = len(word1)
l2 = len(word2)
word3 = ""
# python can use max() to check which number is bigger
for i in range(max(l1, l2)):
    if i < l1:
        word3 += word1[i]
    
    if i < l2:
        word3 += word2[i]

print(word3)

# 1768. Merge Strings Alternately
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

# Find the max length of the two string and put each letter into word3