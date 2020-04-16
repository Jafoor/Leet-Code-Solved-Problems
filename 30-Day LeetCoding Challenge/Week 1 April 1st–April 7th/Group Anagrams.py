class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solved_ans= {}
        for i in range(0, len(strs)):
            if str(sorted(strs[i])) in solved_ans:
                solved_ans[str(sorted(strs[i]))].append(strs[i])
            else:
                solved_ans[str(sorted(strs[i]))] = [strs[i]]
        return list(solved_ans.values())
        