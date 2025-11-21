"""
Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Sample Input: [1, 2, 3, 3]
Sample Output: true

Sample Input: [1, 2, 3, 4]
Sample Output: false

Sample Input: [1, 2, 3, 1]
Sample Output: true
"""

def main():
    print("Contains Duplicate")
    input = [1, 2, 3, 3]
    print(containsDuplicate(input))


def containsDuplicate(nums:list[int]) -> bool:
    refTable = {}
    for num in nums:
        if num in refTable:
            return True
        else:
            refTable[num] = True
    return False

if __name__ == "__main__":
    main()