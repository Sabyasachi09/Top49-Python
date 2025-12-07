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
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    target = 10
    print("Array: %r | target: %d" %(array, target))
    solutionOne = twoSumSolutionOne(array, target)
    solutionTwo = twoSumSolutionTwo(array, target)
    printResult(solutionOne, target, "One")
    printResult(solutionTwo, target, "Two")

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

# This solution uses two pointer approach on a sorted array
# Time Complexity: O(nlog(n)) + O(n) = O(nlog(n))
def twoSumSolutionTwo(array: list[int], target: int):
    sortedArray = sorted(array)
    lp = 0
    rp = len(sortedArray)-1
    while(lp < rp):
        currentSum = array[lp] + array[rp]
        if currentSum == target:
            return [lp, rp]
        elif currentSum > target:
            rp -= 1
        else:
            lp += 1
    return [] 

if __name__ == "__main__":
    main()