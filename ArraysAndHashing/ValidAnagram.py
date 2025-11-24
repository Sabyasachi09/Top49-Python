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

from collections import Counter


def main():
    print("Valid Anagram")
    s = "anagram"
    t = "nagaram"
    print(validAnagramSolutionOne(s, t))
    print(validAnagramSolutionTwo(s, t))
    print(validAnagramSolutionThree(s, t))

def validAnagramSolutionOne(s, t) -> bool:
    if len(s) != len(t):
        return False
    
    countS = {}
    countT = {}
    # add letter and their count in two different dictionary/map from string s and t
    for letter in range(len(s)):
        countS[s[letter]] = 1 + countS.get(s[letter], 0)
        countT[t[letter]] = 1 + countT.get(t[letter], 0)
    
    # Compare letter count in both dictionary/map, return false is mismatch
    for count in countS:
        if countS.get(count) != countT.get(count, 0):
            return False
    return True

def validAnagramSolutionTwo(s, t) -> bool:
    """
    Counter() for efficiently counting hashable objects is the Counter class 
    from the collections module. It is a specialized dictionary subclass designed for this purpose.
    It provides an optimized way to count the occurrences of elements in an iterable 
    (like lists, strings, tuples) or from a mapping (dictionary). 
    """
    return Counter(s) == Counter(t)

def validAnagramSolutionThree(s, t) -> bool:
    return sorted(s) == sorted(t)

if __name__ == "__main__":
    main()