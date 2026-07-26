class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def solve(i, path, curr_sum):

            if curr_sum == target:
                ans.append(path.copy())

                return

            if i >= len(nums) or curr_sum>target:
                return
            
            new_path = path.copy()
            new_path.append(nums[i])
            solve(i, new_path, curr_sum+nums[i])
            solve(i+1, path, curr_sum)

        
        solve(0, [], 0)
        return ans
