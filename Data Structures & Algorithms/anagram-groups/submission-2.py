class Solution:

    def is_anagram(self, s1,s2):
        if len(s1)!= len(s2):
            return False 
        arr = [0]*26
        for i in range(len(s1)):
            arr[ord('a')-ord(s1[i])]+=1
            arr[ord('a')-ord(s2[i])]-=1
        
        for num in arr:
            if num!=0:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = {}

        for i in range(len(strs)):
            sorted_curr =  "".join(sorted(strs[i]))
            if sorted_curr in ans:
                ans[sorted_curr].append(strs[i])
            else:
                ans[sorted_curr] = [strs[i]]

        ans_list = []

        for k,v in ans.items():
            ans_list.append(v)
        return ans_list
        # already_processed = set()
        # ans = []
        # for i in range(len(strs)):
        #     if i in already_processed:
        #         continue
        #     ans.append([strs[i]])
        #     already_processed.add(i)
        #     for j in range(i+1, len(strs)):
        #         if j not in already_processed and self.is_anagram(strs[i],strs[j]):
        #             ans[-1].append(strs[j])
        #             already_processed.add(j)
        # return ans