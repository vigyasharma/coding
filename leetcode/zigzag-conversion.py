class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        p = ["" for i in xrange(numRows)]
        i = 0
        jump = 1
        for c in s:
            p[i] += c
            jump = 1 if i==0 else jump
            jump = -1 if i==numRows-1 else jump
            i = i + jump
        
        return ''.join(p)

if __name__ == '__main__':
    ob = Solution()
    x = ob.convert("PAYPALISHIRING", 3)
    print x