"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""

### O(n^2)
def threeSum(nums):
    result = []
    prevValue = set()
    for i, n in enumerate(nums):
        if n not in prevValue:
            sollTwoSum = 0 - n
            newList = nums.copy()
            newList.pop(i)
            resultTwoSum = twoSum(newList, sollTwoSum)
            for r in resultTwoSum:
                if r[0] not in prevValue and r[1] not in prevValue:
                    r.append(n)
                    result.append(r)
            prevValue.add(n)
    return result

### O(n)
def twoSum(nums, target: int):
    result = []
    prevMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap and n not in prevMap and n != diff:
            result.append([diff, n])
        elif diff in prevMap and n == diff:
            if [diff, n] not in result:
                result.append([diff, n])
        prevMap[n] = i
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #answer1 = threeSum([-1,0,1,2,-1,-4])
    #print(answer1)
    #answer2 = threeSum([0,1,1])
    #print(answer2)
    #answer3 = threeSum([0,0,0])
    #print(answer3)
    answer4 = threeSum([0,0,0,0])
    print(answer4)
