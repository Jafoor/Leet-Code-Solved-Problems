"""
This is same as middle school math quiz.

Let's say that 'a' is moving right, and 'b' is moving down.

If you want to find the number of unique path in 5 x 7 grid, (need to move right 6 times and move down 4 times)
it is same as calculate the number of permutation of 'aaaaaabbbb' (6*'a' and 4*'b')

Formula is 10!/(6!*4!)

So, if general formula for m x n grid,

((m-1)+(n-1))! / ((m-1)!*(n-1)!)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def fact(nn):
            r = 1
            for i in range(r,nn+1):
                r *= i
            return r
        return(fact(m-1+n-1)//fact(n-1)//fact(m-1))