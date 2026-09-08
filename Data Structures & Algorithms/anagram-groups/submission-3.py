class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in range(len(strs)):
            sorted_curr =  "".join(sorted(strs[i]))
            if sorted_curr in ans:
                ans[sorted_curr].append(strs[i])
            else:
                ans[sorted_curr] = [strs[i]]

        ans_list = []

        return list(ans.values())
        #     ans_list.append(v)
        # return ans_list