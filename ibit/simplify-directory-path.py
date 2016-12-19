class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        path = A.split('/')
        stack = ['']
        for dir in path:
            if not dir or dir == ".":
                continue
            elif dir == "..":
                stack.pop()
            else:
                stack.append(dir)
        return '/'.join(stack)
