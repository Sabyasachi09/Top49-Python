"""
Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
*   Anagram: An anagram is a word or phrase formed by rearranging the letters of a 
    different word or phrase, using all the original letters exactly once.

Sample Input: s = "anagram", t = "nagaram"
Sample Output: true

Sample Input: s = "rat", t = "car"
Sample Output: false
"""

def main():
    print("Valid Anagram")
    s = "anagram"
    t = "nagaram"
    print(validAnagramSolutionOne(s, t))

def validAnagramSolutionOne(s, t) -> bool:
    if len(s) != len(t):
        return False
    
    refTableS = {}
    refTableT = {}
    # add letter and their count in two different dictionary/map from string s and t
    for letter in range(len(s)):
        letterCountInS = refTableS.get(s[letter], 0) +1
        refTableS[s[letter]] = letterCountInS
        letterCountInT = refTableT.get(t[letter], 0) +1
        refTableT[t[letter]] = letterCountInT
    
    # Compare letter count in both dictionary/map, return false is mismatch
    for letter in s:
        if refTableS.get(letter) != refTableT.get(letter):
            return False
    return True

if __name__ == "__main__":
    main()