class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        def solve(i, curr_sum):
            if curr_sum == target:
                ans.append(path.copy())
                return

            if i == len(nums) or curr_sum>target:
                return
            
            path.append(nums[i])
            solve(i, curr_sum+nums[i])

            path.pop()
            solve(i+1 , curr_sum)

        solve(0, 0)
        return ans
