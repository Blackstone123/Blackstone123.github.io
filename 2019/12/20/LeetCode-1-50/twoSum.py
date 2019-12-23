from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            delta = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == delta:
                    return [i, j]

    def towSum(self, nums: List[int], target: int) -> List[int]:
        prev_dic = {}
        for index, item in enumerate(nums):
            if target - item in prev_dic:
                return [index, prev_dic[target-item]]
            prev_dic[item] = index
    


def main():
    solution = Solution()
    nums = [3, 3]
    target = 6
    result = solution.twoSum(nums, target)
    print(result)


if __name__ == '__main__':
    main()