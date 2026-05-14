class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = []
        for idx in range(len(nums)-1):
            for idx_two in range(idx+1,len(nums)):
                if (nums[idx] + nums[idx_two]) == target:
                    sol.append(idx)
                    sol.append(idx_two)
        return sol