"""
Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
AKA: Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

Sample Input: ["eat","tea","tan","ate","nat","bat"]
Sample Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanition:
    Word There is no string in the list that can be rearranged to form "bat".
    The string "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The string "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Sample Input: ["act","pots","tops","cat","stop","hat"]
Sample Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Sample Input: [""]
Sample Output: [[""]]

Sample Input: ["a"]
Sample Output: [["a"]]

"""

def main():
    input = ["act","pots","tops","cat","stop","hat"]
    # input = ["","b"]
    print(groupAnagramsSolution(input))

def groupAnagramsSolution(strs: list[str]) -> list[list[str]]:
    groupedAnagrams = []
    anagrams = {}
    for word in range(len(strs)):
        sortedString = "".join(sorted(strs[word]))
        if sortedString in anagrams:
            anagrams[sortedString].append(word)
        else:
            anagrams[sortedString] = [word]
    for val in anagrams.values():
        anagramsList = []
        for indicies in val:
            anagramsList.append(strs[indicies])
        groupedAnagrams.append(anagramsList)
    return groupedAnagrams

if __name__ == "__main__":
    main()