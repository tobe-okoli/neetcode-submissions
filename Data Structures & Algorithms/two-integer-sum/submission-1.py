class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff: int = target - nums[i]
            for j in range(len(nums)):
                if nums[j] == diff and j!= i:
                    numbers = [i, j]
                    return numbers
                
            

        