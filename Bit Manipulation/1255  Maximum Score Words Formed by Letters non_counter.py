def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def letterScore(c):
            return score[ord(c) - ord('a')]
       
        def getCountLetters(lst):
            counter = [0 for _ in range(26)]
            for c in lst:
                counter[ord(c) - ord('a')] += 1
            return counter
       
        def substract(count1, count2): # returns a pair Boolean (whether count2 is included in count 1), counter of the remaining of count1 after removing count2 occ
            for i in range(26):
                if count1[i] < count2[i]:
                    return False, count1
                count1[i] -= count2[i]    
            return True, count1
       
        def helper(i, remaining, scoreSoFar):
            if not remaining or i == len(words):
                return scoreSoFar
       
        # choices
            # 1. skip words[i]
            res = helper(i + 1, remaining, scoreSoFar)
           
            # 2. take words[i] if possible
            cw = getCountLetters(words[i])
            canBeTaken, remainingLetters = substract(remaining.copy(), cw)
            if canBeTaken:
                res = max(res, helper(i + 1, remainingLetters, scoreSoFar + sum(map(letterScore, words[i]))))
            return res
       
        return helper(0, getCountLetters(letters), 0)