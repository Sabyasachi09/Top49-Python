"""
Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice. You can return the answer in any order.

Sample Input:
    array: [2, 7, 11, 15] | target = 9
Sample Output: [0, 1]

Sample Input:
    array: [3, 2, 4] | target = 6
Sample Output: [1, 2]
"""

def main():
    print("Two Sum")
    array = [2, 7, 11, 15]
    target = 9
    print("Array: %r | target: %d" %(array, target))
    solutionOne = twoSumSolutionOne(array, target)
    printResult(solutionOne, target, "One")

def printResult(result: list[int], target, solution):
    if result:
        print("Using solution %s: %r indicies sum up to %d" %(solution, result, target))
    else:
        print("Using solution %s: no two numbers sum up to %d" %(solution, target))

# This solution uses brute force appraoch
# Time Complexity: O(n) * O(n) = O(n^2)
def twoSumSolutionOne(array: list[int], target: int):
    for lp in range(len(array)):
        for rp in range(len(array)):
            if array[lp] + array[rp] == target:
                return [lp, rp]
    return []

if __name__ == "__main__":
    main()