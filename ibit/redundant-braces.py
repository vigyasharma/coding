class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        s = []
        for c in braces:
            if c != ')':
                s.append(c)
            else:
                while(s and s[-1] != '('):
                    s.pop()
                s.pop()