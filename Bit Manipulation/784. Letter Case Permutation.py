class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        #using backtracking
        
        def backtrack(sub = "", i=0):
            if len(sub) == len(S):
                result.append(sub)
            else:
                if S[i].isalpha():
                    backtrack(sub + S[i].swapcase(), i+1)
                backtrack(sub+S[i], i+1)
        
        result = []
        backtrack()
        return result