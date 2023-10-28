# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def twoSum(nums, target: int):
    # Use a breakpoint in the code line below to debug your script.
    nums_sort = nums.copy()
    nums_sort.sort()
    i, j = 0, len(nums) - 1
    summe = nums_sort[i] + nums_sort[j]
    while summe != target:
        if summe > target:
            j = j - 1
        else:
            i = i + 1
        summe = nums_sort[i] + nums_sort[j]
    print(i,j)
    i_origin = nums.index(nums_sort[i])
    j_origin = 0
    for j_o in range(len(nums)):
        if nums[j_o] == nums_sort[j]:
            if j_o != i_origin:
                j_origin = j_o
                break
    return [i_origin, j_origin]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    answer = twoSum([3,3], 6)
    print(answer)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
