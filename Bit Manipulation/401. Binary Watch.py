class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        
        result = []
        for hour in range(12):
            for minuite in range(60):
                if bin(hour).count('1') + bin(minuite).count('1') == num:
                    result.append('{:d}:{:02d}'.format(hour,minuite))
        return result